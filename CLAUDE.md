# Claude Code Instructions — knowledge-wiki-starter

LLM-native markdown knowledge base starter.

---

## Directories

| Directory | Purpose | Git |
|-----------|---------|-----|
| `raw/` | Source materials | tracked |
| `wiki/` | Compiled knowledge pages | tracked |
| `output/` | Ephemeral scratch | gitignored |
| `skills/` | Executable local logic | tracked |
| `schemas/` | Page templates | tracked |
| `.claude/commands/` | Slash command wrappers | tracked |

## Skills

Check `skills/` before implementing anything:

```bash
ls skills/
python skills/<name>.py --help
```

Core workflows:
- `ingest.py`
- `digest.py`
- `evidence.py`
- `lint.py`
- `reorganize.py`
- `stub.py`

## Output vs Wiki — Hard Boundary

| User intent | Destination |
|-------------|-------------|
| Generate a report or exploratory analysis | `output/` |
| Ask a grounded question | conversation only |
| Compile new raw sources | `wiki/` |
| Repair or restructure existing knowledge pages | `wiki/` |

Do not write generated reports directly into `wiki/`.

## Query Policy

- Run `python skills/evidence.py "<question>" --json` first
- Use the evidence bundle as the factual base
- Cite substantive claims with `[S1]`, `[S2]`, ...
- If coverage is `not-covered`, stop instead of answering from priors

## Analysis Policy

- Build from the wiki evidence bundle
- Write one grounded output file to `output/`
- Ask before distilling analysis back into `wiki/`

## Provenance

- `sources:` tracks raw files or URLs
- `links:` tracks canonical external references
- `[UNVERIFIED]` marks unresolved claims

## Git

```bash
git add wiki/ raw/
git commit -m "digest: <scope>"

git add wiki/
git commit -m "distill: <scope>"

git add skills/ .claude/commands/
git commit -m "skill: add <name>"
```

Run `python skills/lint.py` before pushing.
