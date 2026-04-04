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

Built-in: `ingest.py`, `search.py`, `lint.py`, `stub.py`, `reorganize.py`

---

## Output vs Wiki — Hard Boundary

This is the most important rule. When deciding where to write:

| User intent | Destination | Examples |
|-------------|-------------|---------|
| "Generate / write me a report on X" | `output/` | research reports, analysis, summaries on demand |
| "Analyze X" | `output/` | `/analyze` results |
| "What does the wiki say about X" | conversation only | `/query` answers |
| New raw source was ingested | `wiki/summaries/` + `wiki/concepts/` | via `/digest` only |
| Filling a gap found by lint | `wiki/` | via `/distill` only |

**If the user asks you to generate, research, or produce content → `output/`, never `wiki/`.**
**`wiki/` is only modified through the structured pipeline: `/digest` or `/distill`.**

No exceptions. Even if the output looks like a concept page — if the user requested it, it goes to `output/`.

---

## Command → Destination Map

| Command | Writes to |
|---------|-----------|
| `/digest` | `wiki/` (summaries + concepts from raw/) |
| `/distill` | `wiki/` (fill lint-detected gaps, with user approval) |
| `/analyze` | `output/` (one analysis file) |
| `/query` | conversation only |
| `/reorganize` | `wiki/` in-place (fix broken links only) |

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
