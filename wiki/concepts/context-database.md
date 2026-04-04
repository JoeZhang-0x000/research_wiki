---
title: Context Database
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/volcengineOpenViking OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradig.md
links: []
tags: [ai-agents, context, storage]
---

# Context Database

## Definition

A context database is a store designed around the needs of agent context rather than only around generic document retrieval, often unifying memories, resources, and skill-related artifacts in one system.

## Why It Matters

Agent runtimes need more than top-k chunk lookup. The context database framing treats context as a managed substrate with structure, retrieval logic, and observability.

## How It Works

In the OpenViking framing, context is written into a hierarchical store, transformed across levels, and later retrieved through directory-like exploration rather than only flat similarity search.

## Key Properties / Tradeoffs

- **Structure**: richer than a plain vector database.
- **Agent fit**: better aligned with browseable, multi-type context.
- **Complexity**: requires stronger policies for organization and retrieval.

## Related Concepts

- Realized through: [[filesystem-paradigm]], [[three-tier-context]]
- Supports: [[context-engineering]], [[memory-management]]

## Source Basis

- [[summary-openviking]]

## Open Questions

- When does a context database outperform simpler document-plus-search approaches?

