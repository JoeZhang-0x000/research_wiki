Run the wiki linter and fix issues.

Usage: /lint

## Steps

1. Run `python skills/lint.py`

2. For each issue type found:
   - **Broken links** → offer to create stub pages with `python skills/stub.py`
   - **Orphan pages** → offer to add to `wiki/index.md`
   - **Missing frontmatter** → add required fields
   - **[UNVERIFIED] in stable** → attempt to resolve from `raw/` sources

3. Re-run `python skills/lint.py` to confirm clean.
