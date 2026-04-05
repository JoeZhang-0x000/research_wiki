Detect and fix wiki graph health issues.

Usage: /reorganize

## Steps

1. Run `python skills/reorganize.py`
2. Review broken links, orphans, and likely duplicates
3. Apply unambiguous fixes with `python skills/reorganize.py --fix`
4. For ambiguous cases, ask the user before editing
5. Update `wiki/index.md` where needed
6. Run `python skills/lint.py`
7. Commit the resulting `wiki/` changes
