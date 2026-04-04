Detect and fix Obsidian graph health issues: broken links, orphans, likely duplicates.

Usage: /reorganize

## Steps

1. Run: `python skills/reorganize.py`
   - Shows all broken [[links]] with fuzzy-matched fix candidates
   - Shows orphan pages (not linked from anywhere)
   - Shows likely duplicate pages (high name similarity)

2. Review the report with the user.

3. For **unambiguous broken links** (one clear candidate):
   Run: `python skills/reorganize.py --fix`
   This auto-applies single-candidate fixes in-place.

4. For **ambiguous broken links** (multiple candidates or no match):
   Ask the user which target is correct.
   Then manually edit the page to fix the link.
   Or: if the target page doesn't exist at all, ask if you should create a stub:
   `python skills/stub.py concept "<name>"`

5. For **orphan pages**:
   Read the orphan page, identify which existing page(s) should link to it,
   add the `[[link]]` there. Always update `wiki/index.md` too.

6. For **likely duplicates**:
   Read both pages. Ask the user: merge into one, or add cross-links?
   If merge: keep the richer page, redirect the other with `status: deprecated`
   and a "Superseded by [[PageName]]" line.

7. Run: `python skills/lint.py` to confirm clean.

8. Commit:
   ```bash
   git add wiki/
   git commit -m "reorganize: fix broken links and graph gaps"
   git push
   ```
