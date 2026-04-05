# knowledge-wiki-starter

LLM-native markdown knowledge base starter.

This repository is a clean scaffold for building a grounded, file-native knowledge system with `raw/`, `wiki/`, and small local automation in `skills/`.

---

## How It Works

```text
raw/  ->  /digest  ->  wiki/
                      ->  /query     answer inline
                      ->  /analyze   grounded report -> output/
                      ->  /distill   fill structural gaps
```

- `raw/` stores source material
- `wiki/` stores compiled knowledge pages
- `output/` stores ephemeral generated work and is never committed
- `skills/` stores executable local workflows
- `schemas/` stores stable page templates

Ingestion state is structural: a raw file is considered compiled when a `wiki/summaries/` page references it in `sources:`.

## Getting Started

1. Drop source files into `raw/`
2. Run `python skills/ingest.py --new` to see what is not yet compiled
3. Run `python skills/digest.py --list` to preview summary file names
4. Create or update wiki pages with the schema-backed workflow
5. Run `python skills/lint.py` before committing

Useful commands:

```bash
python skills/ingest.py
python skills/digest.py --list
python skills/stub.py concept "example-concept"
python skills/search.py "example term"
python skills/evidence.py "example question" --json
python skills/lint.py
```

## Grounded Answers

- Build an evidence bundle before answering questions or writing analyses
- Treat `wiki/summaries/` as the primary evidence layer
- Cite evidence ids such as `[S1]` for substantive claims
- If the wiki does not cover a question well enough, stop and report the gap

## Customization

- Edit `AGENTS.md` to set project rules
- Edit `schemas/concept.md`, `schemas/topic.md`, and `schemas/summary.md` to match your knowledge model
- Adjust `.claude/commands/` if you want different agent workflows
- Extend `skills/` with repo-specific ingestion, linting, or provenance tools

## Notes

- `output/` is scratch space and should stay untracked
- `wiki/` is intended to evolve through the structured pipeline, not ad hoc report generation
- Obsidian-style `[[links]]` are supported throughout the wiki
