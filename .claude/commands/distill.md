Fill structural or provenance gaps in the wiki. User approval required before writing.

Usage: /distill [topic]

## Steps

1. Run `python skills/lint.py`
2. Read the affected pages
3. Show the user what will change
4. After approval, fill the gaps:
   - broken links
   - orphan pages
   - missing provenance
   - unresolved `[UNVERIFIED]` markers that can be checked from sources
5. Re-run `python skills/lint.py`
6. Commit the resulting `wiki/` changes
