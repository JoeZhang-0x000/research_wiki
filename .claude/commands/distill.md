Scan wiki for structural gaps and fill them. User approves before commit.

Usage: /distill [topic]

## Steps

1. Run `python skills/lint.py` to surface issues.

2. Read the affected pages.

3. **Show the user** what you plan to write or change before doing it.

4. After approval, fill the gaps:
   - Broken links → create pages with `python skills/stub.py <type> <name>`, then fill content
   - `[UNVERIFIED]` in stable pages → check `raw/` sources, resolve or mark "disputed"
   - Orphans → link from an appropriate page or `wiki/index.md`

5. Run `python skills/lint.py` again to confirm clean.

6. Commit:
```bash
git add wiki/
git commit -m "distill: <what was filled>"
git push
```
