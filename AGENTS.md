# AGENTS.md — research_wiki

This file is read by all AI coding agents (Claude Code, OpenAI Codex, Gemini CLI, etc.)

---

## Mission

Convert raw AI research materials into a structured, evolving markdown knowledge base.
Domains: **High-Performance Computing (HPC)**, **AI Infrastructure**, **AI Agents**.

```
raw/  →  /digest  →  wiki/  →  /query (inline)
                       ↑              ↓ user approves
                    /distill      /analyze → output/
```

---

## Directory Semantics

```
raw/          Source materials. Append-only. Never edit existing files. Fully tracked in git.
wiki/         Compiled knowledge. Evolve via rules. Tracked in git.
  concepts/   Atomic knowledge units
  topics/     Broader topic overviews
  summaries/  Per-source summaries — ingestion state lives here
output/       Ephemeral scratch. Gitignored. Never commit.
skills/       All executable logic. Check here first.
schemas/      Markdown templates. Stable contracts.
.claude/commands/  Slash commands. Wrap skills/.
```

---

## Skills — Check Before Implementing

```bash
ls skills/
python skills/<name>.py --help
```

| Skill | Purpose |
|-------|---------|
| `skills/ingest.py` | Find raw/ files not yet referenced by wiki/summaries/ |
| `skills/search.py` | Keyword search across wiki/ — stdout only |
| `skills/lint.py` | Structural checks: broken links, orphans, missing frontmatter |
| `skills/stub.py` | Create a blank wiki page from a schema template |

To add a skill: create `skills/<name>.py`, add to `skills/README.md`.

---

## Ingestion State

A raw file is **compiled** when any `wiki/summaries/` page lists it in `sources:`.
No sidecar files. No registry. State is implicit in the wiki.

---

## Allowed

- `raw/`: append files only
- `wiki/`: create/update pages per schemas — **with user approval after any analysis**
- `output/`: write freely, never commit
- `skills/`: add skills, never remove without checking dependents
- Always update `wiki/index.md` when adding a page

## Forbidden

- Editing existing files in `raw/`
- Deleting wiki pages — use `status: deprecated`
- Inventing facts — use `[UNVERIFIED]`
- Adding sidecar/meta files to `raw/`
- Writing to `wiki/` without explicit user approval after analysis or query
- Committing `output/`

---

## Wiki Page Rules

1. Every page conforms to its schema in `schemas/`
2. Required frontmatter: `title`, `type`, `status`, `sources`, `links`
3. Internal links: `[[PageName]]` syntax
4. No orphans — every new page linked from at least one other or `wiki/index.md`
5. `status`: `draft` | `stable` | `deprecated`

---

## Provenance

- `sources:` lists raw files or URLs this page was compiled from
- `links:` lists original web URLs (Obsidian Clipper)
- Uncertain claims: `[UNVERIFIED]` — must be resolved before `status: stable`

---

## Git Conventions

```bash
# After digest
git add wiki/ raw/
git commit -m "digest: <titles>"
git push

# After filling wiki gaps
git add wiki/
git commit -m "distill: <what was filled>"
git push

# After adding a skill
git add skills/ .claude/commands/
git commit -m "skill: add <name>"
git push
```

Run `python skills/lint.py` before every push. Do not push with lint errors.
Do not bundle wiki changes with skill changes.
