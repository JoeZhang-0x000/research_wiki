# README.agent.md

Quickstart for coding agents working in this repository.

`AGENTS.md` is the authoritative policy file. This document is a shorter operational guide.

## Objective

Turn files in `raw/` into grounded, traceable knowledge in `wiki/`, and keep generated scratch work in `output/`.

## Mental Model

```text
raw/        source inputs
wiki/       durable compiled knowledge
output/     disposable generated work
skills/     local automation
schemas/    content contracts
```

## First Commands

```bash
python skills/ingest.py
python skills/digest.py --list
python skills/lint.py
python skills/evidence.py "<question>" --json
```

## Write Boundaries

- User-requested reports, analyses, and exploratory writing go to `output/`
- Durable knowledge compilation goes to `wiki/`
- Grounded Q&A stays in the conversation unless the user explicitly approves wiki changes

## Grounding Rules

- Use `python skills/evidence.py "<question>" --json` before grounded answers
- Treat `wiki/summaries/` as the primary evidence layer
- Cite evidence ids like `[S1]`
- If coverage is insufficient, stop instead of filling gaps from priors

## Durable Page Rules

- Use schemas from `schemas/`
- Keep `sources:` and `links:` traceable
- Use `[[PageName]]` internal links
- Update `wiki/index.md` when adding durable pages

## Common Tasks

### Ingest new material

1. Check `python skills/ingest.py --new`
2. Create summary pages
3. Create or update related concept/topic pages
4. Run `python skills/lint.py`

### Answer a grounded question

1. Build an evidence bundle
2. Read cited pages, prioritizing summaries
3. Answer with citations
4. Report gaps explicitly

### Repair wiki structure

1. Run `python skills/lint.py`
2. Fix links, provenance, orphan pages, or unresolved markers
3. Re-run lint before finishing

## Before Committing

```bash
python skills/lint.py
```

If you are changing workflow behavior, also run the relevant script entrypoints directly.
