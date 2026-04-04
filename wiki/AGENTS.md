# AGENTS.md — wiki/

## Role of This Directory

`wiki/` is the **compiled, structured knowledge base**. All content here is derived from `raw/` and shaped by agent processing.

---

## Page Types

| Type      | Location           | Schema             | One file per...              |
|-----------|--------------------|--------------------|------------------------------|
| concept   | `wiki/concepts/`   | `schemas/concept.md` | One atomic concept or term |
| topic     | `wiki/topics/`     | `schemas/topic.md`   | One research area/subfield |
| summary   | `wiki/summaries/`  | `schemas/summary.md` | One source document/paper  |

---

## Schema Requirements

Every page **must** begin with YAML frontmatter:

```yaml
---
title: <page title>
type: concept | topic | summary
status: draft | stable | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - raw/<filename> or https://...
tags: [tag1, tag2]
---
```

Pages missing frontmatter will be flagged by `lint.py` as malformed.

---

## Linking Rules

- Use `[[PageName]]` syntax for all internal links (Obsidian-compatible)
- `PageName` must match the filename without `.md` extension (case-sensitive)
- Every new page must be linked from at least one existing page or `wiki/index.md`
- Do not use bare URLs for internal references — always use `[[links]]`
- External URLs are allowed inline in `Sources` sections

---

## Update Rules

1. **Additive by default**: add new sections, update existing sections, never delete content
2. **Preserve all `[[links]]`**: if you remove a sentence containing a link, move the link elsewhere on the page
3. **Bump `updated` date** in frontmatter whenever content changes
4. **Status promotion**: `draft` → `stable` only when all `[UNVERIFIED]` markers are resolved and at least one source is confirmed
5. **Deprecation**: set `status: deprecated` and add a `Superseded By` section pointing to the replacement page

---

## Index Maintenance

`wiki/index.md` is the entry point for human readers and agents.
- All concept pages must appear in at least one index section
- Topic pages must appear in the top-level topic list
- Summary pages are listed under their corresponding topic or concept

---

## Directory Layout

```
wiki/
  index.md              Master index — keep up to date
  concepts/             Atomic knowledge units
    flash-attention.md
    collective-communication.md
    ...
  topics/               Broader topic pages
    gpu-memory-optimization.md
    ...
  summaries/            Per-source summaries
    summary-flashattention2-paper.md
    ...
```
