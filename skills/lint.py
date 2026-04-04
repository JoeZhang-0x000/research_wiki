#!/usr/bin/env python3
"""
lint.py — Structural health check for wiki/.

Checks:
  1. Broken [[links]] — referenced pages that don't exist
  2. Orphan pages — not linked from anywhere
  3. Missing frontmatter fields (title, type, status, sources)
  4. [UNVERIFIED] claims in stable pages

Usage:
    python skills/lint.py
    python skills/lint.py --strict    # exit 1 if issues found
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"
REQUIRED = ["title", "type", "status", "sources"]
EXEMPT = {"index", "AGENTS"}


def wiki_pages() -> list[Path]:
    return [p for p in sorted(WIKI_DIR.rglob("*.md")) if p.name != "AGENTS.md"]


def page_map(pages: list[Path]) -> dict[str, Path]:
    return {p.stem: p for p in pages}


def links_in(text: str) -> list[str]:
    return re.findall(r"\[\[([^\]]+)\]\]", text)


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


def main():
    parser = argparse.ArgumentParser(description="Wiki structural linter")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    pages = wiki_pages()
    pmap = page_map(pages)
    issues = 0

    # Build link graph
    outgoing: dict[str, list[str]] = {}
    incoming: dict[str, set[str]] = {p.stem: set() for p in pages}
    for page in pages:
        links = links_in(page.read_text())
        outgoing[page.stem] = links
        for lnk in links:
            incoming.setdefault(lnk, set()).add(page.stem)

    print("# Wiki Lint\n")

    # 1. Broken links
    broken = [(src, lnk) for src, links in outgoing.items() for lnk in links if lnk not in pmap]
    if broken:
        print(f"## Broken links ({len(broken)})")
        for src, lnk in broken:
            print(f"  {src} → [[{lnk}]]")
        print()
        issues += len(broken)
    else:
        print("## Broken links: none\n")

    # 2. Orphans
    orphans = [p for p in pages if p.stem not in EXEMPT and not incoming.get(p.stem)]
    if orphans:
        print(f"## Orphan pages ({len(orphans)})")
        for p in orphans:
            print(f"  {p.relative_to(ROOT)}")
        print()
        issues += len(orphans)
    else:
        print("## Orphan pages: none\n")

    # 3. Missing frontmatter
    fm_issues = []
    for page in pages:
        if page.stem in ("index",):
            continue
        fm = frontmatter(page.read_text())
        missing = [f for f in REQUIRED if f not in fm]
        if missing:
            fm_issues.append((page, missing))
    if fm_issues:
        print(f"## Missing frontmatter ({len(fm_issues)} pages)")
        for page, missing in fm_issues:
            print(f"  {page.relative_to(ROOT)} — missing: {', '.join(missing)}")
        print()
        issues += len(fm_issues)
    else:
        print("## Missing frontmatter: none\n")

    # 4. [UNVERIFIED] in stable pages
    unverified = []
    for page in pages:
        text = page.read_text()
        if frontmatter(text).get("status") == "stable" and "[UNVERIFIED]" in text:
            unverified.append((page, text.count("[UNVERIFIED]")))
    if unverified:
        print(f"## [UNVERIFIED] in stable pages ({len(unverified)} pages)")
        for page, n in unverified:
            print(f"  {page.relative_to(ROOT)} — {n} claim(s)")
        print()
        issues += len(unverified)
    else:
        print("## [UNVERIFIED] in stable pages: none\n")

    print(f"---\nTotal issues: {issues}")
    if args.strict and issues > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
