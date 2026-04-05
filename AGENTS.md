# AGENTS.md — knowledge-wiki-starter

This file is read by coding agents working in this repository.

---

## Mission

Convert raw source materials into a structured, evolving markdown knowledge base.

```text
raw/  ->  /digest  ->  wiki/  ->  /query
                       ^
                    /distill
```

## Directory Semantics

```text
raw/          Source materials. Append-only.
wiki/         Compiled knowledge.
  concepts/   Atomic knowledge units
  topics/     Broader topic overviews
  summaries/  Per-source summaries
output/       Ephemeral scratch. Gitignored. Never commit.
skills/       Executable local logic. Check here first.
schemas/      Markdown templates and contracts.
.claude/commands/  Agent command wrappers.
```

## Skills — Check Before Implementing

```bash
ls skills/
python skills/<name>.py --help
```

## Output vs Wiki — Hard Boundary

| User intent | Destination |
|-------------|-------------|
| User asks for generated content, research notes, or a report | `output/` |
| User asks a grounded question against existing knowledge | conversation only |
| New source ingestion | `wiki/` via `/digest` |
| Structural cleanup or provenance repair | `wiki/` via `/distill` or maintenance workflows |

`wiki/` is for compiled knowledge, not ad hoc generated prose.

## Grounded Generation Policy

- Query and analysis work must be grounded in `wiki/`
- Run `python skills/evidence.py "<question>" --json` before answering grounded questions
- Every substantive claim should cite evidence ids such as `[S1]`
- If the wiki does not cover the question well enough, say so explicitly instead of filling gaps from model priors

## Allowed

- Add new files to `raw/`
- Create or update `wiki/` pages through the structured workflow
- Write freely to `output/`
- Add new skills under `skills/`
- Update `wiki/index.md` whenever you add durable pages

## Forbidden

- Deleting durable wiki knowledge without replacing it with a deprecation path
- Inventing facts without marking them `[UNVERIFIED]`
- Adding sidecar state files for ingestion status
- Committing `output/`
- Writing generated report content directly into `wiki/` just because the user asked for prose

## Wiki Page Rules

1. Every durable page should follow a schema in `schemas/`
2. Required frontmatter for knowledge pages: `title`, `type`, `status`, `sources`, `links`
3. Internal links use `[[PageName]]` syntax
4. New pages must be linked from another page or `wiki/index.md`
5. `status` values are `draft`, `stable`, or `deprecated`

## Provenance

- `sources:` lists raw files or URLs the page was derived from
- `links:` lists canonical external URLs when available
- Uncertain claims use `[UNVERIFIED]`

## Git Conventions

```bash
git add wiki/ raw/
git commit -m "digest: <scope>"

git add wiki/
git commit -m "distill: <scope>"

git add skills/ .claude/commands/
git commit -m "skill: add <name>"
```

Run `python skills/lint.py` before pushing.
