#!/usr/bin/env python3
"""
reorganize.py — Detect and fix Obsidian graph health issues in wiki/.

Obsidian renders [[links]] as graph edges. Broken links = broken graph.
This script goes beyond lint: it actively proposes fixes.

Checks and fixes:
  1. Broken [[links]] — fuzzy-match against existing pages to find likely targets
  2. Case/slug mismatches — e.g. [[FlashAttention]] → [[flash-attention]]
  3. Orphan pages — suggest which existing pages should link to them
  4. Duplicate pages — detect pages that likely cover the same concept

Usage:
    python skills/reorganize.py              # show all issues + proposed fixes
    python skills/reorganize.py --dry-run    # same, explicit flag
    python skills/reorganize.py --fix        # apply all unambiguous fixes in-place
    python skills/reorganize.py --fix --confirm  # apply fixes one by one with prompts
"""

import argparse
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher, get_close_matches

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"
SKIP = {"AGENTS.md"}


# ── helpers ────────────────────────────────────────────────────────────────────

def wiki_pages() -> list[Path]:
    return [p for p in sorted(WIKI_DIR.rglob("*.md")) if p.name not in SKIP]


def page_map(pages: list[Path]) -> dict[str, Path]:
    """stem → path"""
    return {p.stem: p for p in pages}


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")


def links_in(text: str) -> list[tuple[int, str]]:
    """Return (line_number, link_target) for every [[link]] in text."""
    results = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\[\[([^\]]+)\]\]", line):
            results.append((i, m.group(1)))
    return results


def frontmatter(text: str) -> dict[str, str]:
    fields = {}
    in_fm = False
    for line in text.splitlines():
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            break
        if in_fm and ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip()
    return fields


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


# ── analysis ───────────────────────────────────────────────────────────────────

def find_broken_links(pages: list[Path], pmap: dict[str, Path]) \
        -> list[tuple[Path, int, str, list[str]]]:
    """
    Returns: [(page, line_no, broken_link, [candidate_fixes])]
    """
    broken = []
    stems = list(pmap.keys())
    for page in pages:
        text = page.read_text()
        for lineno, link in links_in(text):
            if link in pmap:
                continue  # fine
            # fuzzy match — higher cutoff for short names to avoid false positives
            slug_link = slugify(link)
            cutoff = 0.72
            candidates = get_close_matches(slug_link, stems, n=3, cutoff=cutoff)
            # also try exact slug match (handles CamelCase → kebab-case)
            if slug_link in pmap and slug_link not in candidates:
                candidates.insert(0, slug_link)
            broken.append((page, lineno, link, candidates))
    return broken


def find_orphans(pages: list[Path], pmap: dict[str, Path]) -> list[Path]:
    """Pages not linked from any other page (excluding index)."""
    EXEMPT = {"index", "AGENTS"}
    incoming: dict[str, set[str]] = {p.stem: set() for p in pages}
    for page in pages:
        for _, link in links_in(page.read_text()):
            incoming.setdefault(link, set()).add(page.stem)
    return [p for p in pages
            if p.stem not in EXEMPT and not incoming.get(p.stem)]


def find_duplicate_candidates(pages: list[Path]) -> list[tuple[Path, Path, float]]:
    """Detect pairs of pages that likely cover the same concept (high title similarity)."""
    pairs = []
    stems = [(p, slugify(p.stem)) for p in pages if p.stem not in ("index",)]
    for i in range(len(stems)):
        for j in range(i + 1, len(stems)):
            pa, sa = stems[i]
            pb, sb = stems[j]
            score = similarity(sa, sb)
            if score > 0.82:
                pairs.append((pa, pb, score))
    return sorted(pairs, key=lambda x: -x[2])


# ── fix application ─────────────────────────────────────────────────────────────

def apply_fix(page: Path, old_link: str, new_link: str, dry_run: bool) -> bool:
    """Replace [[old_link]] with [[new_link]] in page. Returns True if changed."""
    text = page.read_text()
    new_text = re.sub(
        r"\[\[" + re.escape(old_link) + r"\]\]",
        f"[[{new_link}]]",
        text
    )
    if new_text == text:
        return False
    if not dry_run:
        page.write_text(new_text)
    return True


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Obsidian wiki graph health checker")
    parser.add_argument("--fix", action="store_true",
                        help="Apply unambiguous fixes (single candidate) in-place")
    parser.add_argument("--confirm", action="store_true",
                        help="With --fix: prompt before each change")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Show proposed fixes without writing (default)")
    args = parser.parse_args()

    # --fix overrides dry-run
    dry_run = not args.fix

    pages = wiki_pages()
    pmap = page_map(pages)

    total_issues = 0
    auto_fixes = 0
    ambiguous = 0

    # ── 1. Broken links ──────────────────────────────────────────────────────
    broken = find_broken_links(pages, pmap)
    print(f"# Wiki Reorganization Report\n")
    print(f"## Broken [[links]] ({len(broken)})\n")

    for page, lineno, link, candidates in broken:
        rel = page.relative_to(ROOT)
        total_issues += 1

        if not candidates:
            print(f"  {rel}:{lineno}  [[{link}]]  → no match found  ⚠ manual fix needed")
            ambiguous += 1
        elif len(candidates) == 1:
            fix = candidates[0]
            status = "FIXED" if args.fix else "would fix"
            if args.fix:
                if args.confirm:
                    resp = input(f"  Fix [[{link}]] → [[{fix}]] in {rel}? [y/N] ")
                    if resp.lower() != "y":
                        print(f"  skipped")
                        continue
                apply_fix(page, link, fix, dry_run=False)
                auto_fixes += 1
            print(f"  {rel}:{lineno}  [[{link}]]  → [[{fix}]]  ({status})")
        else:
            cands_str = ", ".join(f"[[{c}]]" for c in candidates)
            print(f"  {rel}:{lineno}  [[{link}]]  → ambiguous: {cands_str}  ⚠ pick one manually")
            ambiguous += 1

    if not broken:
        print("  none\n")
    else:
        print()

    # ── 2. Orphan pages ──────────────────────────────────────────────────────
    orphans = find_orphans(pages, pmap)
    print(f"## Orphan pages ({len(orphans)})\n")

    for page in orphans:
        total_issues += 1
        fm = frontmatter(page.read_text())
        tags = fm.get("tags", "")
        print(f"  {page.relative_to(ROOT)}  tags: {tags}")
        print(f"    → Add a [[{page.stem}]] link from wiki/index.md or a related page")

    if not orphans:
        print("  none\n")
    else:
        print()

    # ── 3. Likely duplicates ─────────────────────────────────────────────────
    dupes = find_duplicate_candidates(pages)
    print(f"## Likely duplicate pages ({len(dupes)})\n")

    for pa, pb, score in dupes:
        total_issues += 1
        print(f"  [[{pa.stem}]]  ≈  [[{pb.stem}]]  (similarity {score:.0%})")
        print(f"    → Consider merging or adding a cross-link")

    if not dupes:
        print("  none\n")
    else:
        print()

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"---")
    print(f"Total issues: {total_issues}")
    if args.fix:
        print(f"Auto-fixed: {auto_fixes}  |  Needs manual attention: {ambiguous}")
        if auto_fixes > 0:
            print(f"\nRun `python skills/lint.py` to verify, then commit.")
    else:
        print(f"Run with --fix to auto-apply unambiguous fixes.")
        print(f"Run `python skills/lint.py` for a full structural check.")

    if total_issues > 0 and not args.fix:
        sys.exit(1)


if __name__ == "__main__":
    main()
