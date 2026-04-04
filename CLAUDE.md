# Claude Code Instructions — research_wiki

LLM-native knowledge compilation system for AI research (HPC, AI Infra, Agents).

---

## Directories

| Directory | Purpose | Git |
|-----------|---------|-----|
| `raw/` | Source materials — append-only, never edit | tracked |
| `wiki/` | Compiled knowledge pages | tracked |
| `output/` | Ephemeral scratch — never commit | gitignored |
| `skills/` | All executable logic — check here first | tracked |
| `schemas/` | Page templates — stable | tracked |
| `.claude/commands/` | Slash commands | tracked |

---

## Skills

Before implementing anything, check `skills/`:

```bash
ls skills/
python skills/<name>.py --help
```

Built-in: `ingest.py`, `search.py`, `lint.py`, `stub.py`

---

## Core Rule: Ask Before Touching Wiki

After any analysis, query, or `/analyze` report — **always ask the user** before modifying wiki pages.

Exception: `/digest` is an explicit ingest command and implies consent.

---

## Query Policy

`/query` → read wiki → answer in conversation → note gaps → ask user.
Never write to `output/` for a query.

## Analysis Policy

`/analyze` → five passes → write ONE file to `output/` → tell user key findings → ask before touching wiki.

## Distillation Policy

`/distill` → run `python skills/lint.py` → show user what will change → get approval → write wiki → commit.

---

## Ingestion State

A raw file is **compiled** when a `wiki/summaries/` page lists it in `sources:`.
No sidecar files. State is in the wiki.

---

## Provenance

- `sources:` — raw files or URLs this page was compiled from
- `links:` — original web URLs (Obsidian Clipper) for clickable references
- `[UNVERIFIED]` — uncertain claims; must resolve before `status: stable`

---

## Git

```bash
git add wiki/ raw/ && git commit -m "digest: <titles>" && git push
git add wiki/    && git commit -m "distill: <topic>"  && git push
git add skills/  && git commit -m "skill: add <name>" && git push
```

Run `python skills/lint.py` before every push.
