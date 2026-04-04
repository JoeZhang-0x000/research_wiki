Answer a question using the wiki knowledge base. Answer inline — no files written.

Usage: /query <question>

## Steps

1. Run `python skills/search.py "<question>"` to find relevant pages.

2. Read each matching page with the Read tool.

3. Answer directly in the conversation. No output files.

4. After answering, note any gaps:
   - Broken `[[links]]` pointing to non-existent pages
   - `[UNVERIFIED]` claims relevant to the question
   - Topics that seem thin given what was asked

5. Ask the user: "Should I fill in any of these gaps?"
   If yes → create/update wiki pages, run `python skills/lint.py`, commit.
   If no → done.
