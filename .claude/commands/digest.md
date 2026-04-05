Compile new raw files into the wiki.

Usage: /digest

## Steps

1. Run `python skills/ingest.py --new`
2. If there are no new files, stop
3. For each new file:
   - read `raw/<filename>`
   - create a summary stub with `python skills/stub.py summary "<filename>"`
   - fill the summary using `schemas/summary.md`
   - create or update related concept and topic pages as needed
4. Update `wiki/index.md`
5. Run `python skills/lint.py`
6. Commit the resulting `raw/` and `wiki/` changes
