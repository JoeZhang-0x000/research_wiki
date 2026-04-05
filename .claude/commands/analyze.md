Write a grounded analysis from existing wiki evidence.

Usage: /analyze <topic>

## Steps

1. Run `python skills/evidence.py "<topic>" --json`
2. If coverage is `not-covered`, stop and tell the user the wiki does not support a grounded analysis yet
3. Read the cited pages, prioritizing `summary` pages
4. Write one grounded report to `output/analysis-<topic-slug>-<YYYY-MM-DD>.md`
5. Cite substantive claims with evidence ids such as `[S1]`
6. Ask before distilling anything back into `wiki/`
