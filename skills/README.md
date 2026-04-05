# Skills

Shared capability library for this knowledge-base scaffold.

```bash
python skills/<name>.py --help
```

## Built-in Skills

| Script | Description |
|--------|-------------|
| `backfill_provenance.py` | Repair stale `raw/` references and missing summary links |
| `digest.py` | Preview or create summary stubs for new raw files |
| `evidence.py` | Build grounded evidence bundles from `wiki/` and `raw/` |
| `ingest.py` | Find raw files not yet referenced by summary pages |
| `rename.py` | Slugify raw filenames based on frontmatter title |
| `search.py` | Keyword search across wiki pages |
| `lint.py` | Structural checks for links, frontmatter, provenance, and unresolved markers |
| `stub.py` | Create a blank wiki page from a schema template |
| `reorganize.py` | Detect and fix graph issues such as broken links and likely duplicates |

## Adding a Skill

1. Create `skills/<name>.py`
2. Add a row to the table above
3. Optionally add `.claude/commands/<name>.md`
4. Confirm the script runs with `--help`

Template:

```python
#!/usr/bin/env python3
"""
<name>.py — <one-line description>

Inputs:  ...
Outputs: stdout only (or writes to a specific location)
Deps:    ...
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="...")
    parser.parse_args()

if __name__ == "__main__":
    main()
```

## Suggested Extensions

- A fetcher for external sources
- A domain-specific normalizer for raw files
- Project-specific lint rules
- A richer distillation workflow for topic and concept pages
