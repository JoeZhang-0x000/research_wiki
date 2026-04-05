# AGENTS.md — wiki/

## Role of This Directory

`wiki/` is the compiled knowledge base.

## Page Types

| Type | Location | Schema |
|------|----------|--------|
| concept | `wiki/concepts/` | `schemas/concept.md` |
| topic | `wiki/topics/` | `schemas/topic.md` |
| summary | `wiki/summaries/` | `schemas/summary.md` |

## Schema Requirements

Durable pages should begin with YAML frontmatter containing:

```yaml
---
title: <page title>
type: concept | topic | summary
status: draft | stable | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - raw/<filename> or https://...
links:
  - https://...
tags: []
---
```

## Linking Rules

- Use `[[PageName]]` for internal links
- New pages must be linked from another page or `wiki/index.md`
- Keep provenance traceable through summaries or raw sources

## Update Rules

1. Additive by default
2. Bump `updated` when content changes
3. Promote `draft` to `stable` only after resolving `[UNVERIFIED]`
4. Deprecate with `status: deprecated` instead of silent deletion

## Index Maintenance

`wiki/index.md` is the entry point for humans and agents.
Keep it current whenever durable pages are added or reorganized.
