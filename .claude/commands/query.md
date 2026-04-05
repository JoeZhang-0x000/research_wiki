Answer a question using only wiki-backed evidence. No files written.

Usage: /query <question>

## Steps

1. Run `python skills/evidence.py "<question>" --json`
2. If coverage is `not-covered`, stop and say the wiki does not cover the question well enough
3. Read the cited pages in bundle order, prioritizing summaries
4. Answer inline with citations such as `[S1]`
5. Note relevant gaps or unresolved claims
6. Ask whether to fill those gaps
