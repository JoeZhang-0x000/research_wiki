Detect new files in raw/, compile them into wiki pages, lint, commit, push.

Usage: /digest

## Steps

### 1. Detect new files
Run: `python skills/ingest.py --new`

If output says 0 new → tell the user "Nothing new to digest." and stop.

### 2. For each new file:

a. **Read the file** at `raw/<filename>`.

b. **Create a summary page** in `wiki/summaries/` using `schemas/summary.md`.
   - Use `python skills/stub.py summary "<filename>"` to create the file.
   - Fill in ALL sections. No placeholders.
   - Set `sources: raw/<filename>` and `links:` to the original URL if present in the file.
   - Use `[[PageName]]` links to related concepts and topics.

c. **Create or update concept pages** for new concepts introduced.
   - Use `python skills/stub.py concept "<name>"` for new pages.
   - If the concept already exists in wiki/, update it instead.
   - Mark uncertain claims `[UNVERIFIED]`.

d. **Update existing topic pages** if this source adds to a known area.

### 3. Update the index
Add all new pages to `wiki/index.md`.

### 4. Lint
Run: `python skills/lint.py`
Fix all issues before continuing.

### 5. Commit and push
```bash
git add wiki/ raw/
git commit -m "digest: <comma-separated source titles>"
git push
```
