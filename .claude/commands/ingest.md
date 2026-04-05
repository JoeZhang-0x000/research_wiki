Inspect ingestion state for `raw/`.

Usage: /ingest [filepath]

## Steps

1. If no filepath is given, run `python skills/ingest.py` and report the status
2. If a filepath is given and it is outside `raw/`, move or copy it into `raw/` after user approval
3. Run `python skills/ingest.py --new`
4. Ask whether to compile the new source now via `/digest`
