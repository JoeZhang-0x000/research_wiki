Run the wiki linter and fix issues.

Usage: /lint

## Steps

1. Run `python skills/lint.py`
2. Review each issue type
3. Offer targeted fixes for:
   - broken links
   - orphan pages
   - missing frontmatter
   - unresolved `[UNVERIFIED]` markers in stable pages
   - provenance drift
4. Re-run `python skills/lint.py` to confirm clean output
