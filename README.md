# knowledge-wiki-starter

LLM-native markdown knowledge base starter.

This repository is a clean scaffold for building a grounded, file-native knowledge system with `raw/`, `wiki/`, `output/`, and small local automation in `skills/`.

## Who This Is For

- Humans: use this as a starter for a markdown-first knowledge base
- Agents: use the repo workflow and local scripts to ingest, compile, search, and verify knowledge

## Read This First

- Human guide: `README.md`
- Agent quickstart: `README.agent.md`
- Agent hard rules: `AGENTS.md`

## Core Flow

```text
raw/  ->  /digest  ->  wiki/
                      ->  /query     answer inline
                      ->  /analyze   grounded report -> output/
                      ->  /distill   fill structural gaps
```

## Repository Layout

- `raw/` stores source material
- `wiki/` stores compiled knowledge pages
- `output/` stores scratch output and should not be committed
- `skills/` stores executable local workflows
- `schemas/` stores stable page templates
- `.claude/commands/` stores command wrappers for agent workflows

## Getting Started

1. Add source files to `raw/`
2. Run `python skills/ingest.py --new`
3. Preview summary naming with `python skills/digest.py --list`
4. Build or update `wiki/` pages through the structured workflow
5. Run `python skills/lint.py` before committing

## Useful Commands

```bash
python skills/ingest.py
python skills/digest.py --list
python skills/stub.py concept "example-concept"
python skills/search.py "example term"
python skills/evidence.py "example question" --json
python skills/lint.py
```

## Customize It

- Edit `schemas/concept.md`, `schemas/topic.md`, and `schemas/summary.md`
- Edit `AGENTS.md` to match your project rules
- Adjust `.claude/commands/` for your preferred workflows
- Extend `skills/` with domain-specific automation

## Notes

- `wiki/` is for durable compiled knowledge, not ad hoc reports
- `output/` is disposable scratch space
- Obsidian-style `[[links]]` are supported throughout the wiki
