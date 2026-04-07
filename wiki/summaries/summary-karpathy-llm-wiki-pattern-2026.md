---
title: "Karpathy LLM Wiki Pattern"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Andrej Karpathy LLM Wiki Gist 2026-04-04.md
links:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
tags: [ai-agents, knowledge-management, markdown-knowledge-base, obsidian]
---

# Summary — Karpathy LLM Wiki Pattern

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog / pattern description      |
| Author(s)    | Andrej Karpathy                |
| Year         | 2026                           |
| Venue        | GitHub Gist                   |
| Raw file     | `raw/Andrej Karpathy LLM Wiki Gist 2026-04-04.md` |

## Main Idea

Karpathy's LLM Wiki is a knowledge management pattern where an LLM incrementally builds and maintains a persistent, compounding wiki from raw sources — instead of re-deriving knowledge on every query like RAG. The key shift: **compile once, keep current**. The wiki is a persistent artifact that grows richer with every source ingested and every question answered.

## Key Details

- **Three-layer architecture**: (1) Raw sources — immutable input corpus (articles, papers, images); (2) Wiki — LLM-generated markdown files (summaries, entity pages, concept pages) that the LLM owns and maintains; (3) Schema — CLAUDE.md/AGENTS.md telling the LLM how to structure, ingest, query, and lint the wiki
- **Ingest operation**: Drop source into raw, LLM reads it, writes a summary page, updates index, updates 10–15 relevant entity/concept pages simultaneously, appends log entry. Cross-references built automatically. Contradictions flagged.
- **Query operation**: LLM searches wiki pages (reads index.md first), synthesizes answer with citations. Good answers filed back into wiki as new pages — explorations compound just like ingested sources.
- **Lint operation**: LLM health-checks wiki — finds contradictions, stale claims, orphan pages, missing cross-references, data gaps. Keeps wiki healthy as it grows.
- **Two indexing files**: `index.md` (content catalog, organized by category — sufficient at ~100 sources without vector search); `log.md` (append-only chronological record, parseable with `grep "^## \[" log.md | tail -5`)
- **Why it works**: Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored, don't forget cross-reference updates, can touch 15 files in one pass. Maintenance cost near zero.
- **Context**: Related to Vannevar Bush's Memex (1945) — Bush's unfulfilled vision of a personal, curated knowledge store with associative trails. The part he couldn't solve was who does the maintenance. LLM handles that.
- **Community responses**: Multiple implementations emerged within days of posting — MCP servers, Obsidian plugins, bootstrap generators, semantic search layers (OMEGA: 95.4% on LongMemEval at 50ms), git-based provenance trackers
- **Scale note**: At moderate scale (~100 sources, hundreds of pages), index.md is sufficient without vector search. Scale limitations acknowledged but not precisely quantified.

## Method / Approach

Pattern description / workflow design. Not a research paper — an idea file designed to be copy-pasted into an LLM Agent (Claude Code, OpenAI Codex, OpenCode, etc.) so the agent can build out the specifics collaboratively. The gist is intentionally abstract about implementation details.

## Results / Evidence

- 5,000+ stars on the gist in 48 hours (self-reported by author)
- Multiple independent implementations appeared within days (llm-wiki-kit, OMEGA, claude-playbook-plugin, LLM-wiki by Ss1024sS, sp-context, sage-wiki, agentic-wiki-builder)
- Working scale cited: ~100 sources, ~400K words without needing vector search (from prior April 3 thread)

## Limitations

- Pattern description, not empirical evaluation — no benchmarks comparing LLM Wiki to RAG on equivalent tasks
- Scale ceiling not precisely defined — index.md works at ~100 sources but exact threshold where vector search becomes necessary is unspecified
- "Every good answer filed back as a page" is a rule, not an automated mechanism — depends on human discipline
- Open questions on formation: which insights deserve a wiki page vs. disappear into chat history? No automatic feedback loop
- Many community implementations but no consensus on which tooling stack is optimal

## Links to Concepts

- [[markdown-knowledge-base]] — this is the canonical formalization of the pattern previously described in the April 3 thread; LLM Wiki = markdown knowledge base with compounding writes
- [[persistent-agent-memory]] — the wiki serves as durable cross-session memory for agents; LLM Wiki is the concrete instantiation
- [[openclaw]] — OpenClaw's MEMORY.md and .openclaw/ directory for persistent context is described by commentors as a similar pattern
- OMEGA (community implementation, not yet in wiki) — vector embeddings + FTS5 + cross-encoder reranking for the retrieval scale problem; 95.4% on LongMemEval at 50ms retrieval

## Links to Topics

- [[markdown-knowledge-bases]] — primary topic
- [[agent-memory-systems]] — the wiki functions as a persistent memory layer

## Quotes Worth Preserving

> The key difference: the wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read.

> You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

> The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.
