---
title: "LLM Wiki — Andrej Karpathy"
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author:
  - Andrej Karpathy
published: 2026-04-04
created: 2026-04-07
description: "Karpathy's LLM Wiki pattern: persistent compounding knowledge base vs RAG. Three layers (Raw/Wiki/Schema), three operations (Ingest/Query/Lint). 5,000+ stars in 48 hours. Open source."
tags:
  - research
  - ai-agents
  - knowledge-management
  - markdown-knowledge-base
---

# LLM Wiki

By Andrej Karpathy. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Created April 4, 2026. 5,000+ stars in 48 hours.

## The Core Idea

Most people's experience with LLMs and documents is RAG: upload files, LLM retrieves relevant chunks at query time, generates an answer. The LLM rediscovers knowledge from scratch on every question. Nothing accumulates. Ask a subtle question requiring synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time.

**LLM Wiki is different.** Instead of retrieving from raw documents at query time, the LLM incrementally builds and maintains a **persistent wiki** — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting contradictions, strengthening or challenging the evolving synthesis. The knowledge is compiled once and kept current, not re-derived on every query.

**Key difference: the wiki is a persistent, compounding artifact.** Cross-references are already there. Contradictions have been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## Three-Layer Architecture

### Raw Sources

Your curated collection of source documents — articles, papers, images, data files. These are **immutable** — the LLM reads from them but never modifies them. This is the source of truth.

### The Wiki

A directory of LLM-generated markdown files — summaries, entity pages, concept pages, comparisons, overviews, synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent.

### The Schema

A document (e.g. CLAUDE.md for Claude Code, AGENTS.md for Codex) that tells the LLM how the wiki is structured, what conventions to follow, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it makes the LLM a disciplined wiki maintainer rather than a generic chatbot.

## Three Operations

### Ingest

Drop a new source into the raw collection, tell the LLM to process it. The LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. **A single source might touch 10–15 wiki pages simultaneously.**

### Query

Ask questions against the wiki. The LLM searches for relevant pages, reads them, synthesizes an answer with citations. Answers can take different forms — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas.

**Good answers can be filed back into the wiki as new pages.** A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

### Lint

Periodically ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, important concepts lacking their own page, missing cross-references, data gaps that could be filled with a web search.

## Indexing and Logging

Two special files help navigate the wiki as it grows:

**index.md** — content-oriented catalog of everything in the wiki. Each page listed with a link, one-line summary, and optional metadata. Organized by category (entities, concepts, sources). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. Works surprisingly well at moderate scale (~100 sources, hundreds of pages) and avoids embedding-based RAG infrastructure.

**log.md** — chronological append-only record of what happened and when: ingests, queries, lint passes. If each entry starts with a consistent prefix (e.g. `## [2026-04-02] ingest | Article Title`), the log becomes parseable with simple unix tools: `grep "^## \[" log.md | tail -5` gives the last 5 entries.

## Use Cases

- **Personal**: tracking goals, health, psychology — filing journal entries, articles, podcast notes, building a structured picture of yourself over time
- **Research**: going deep on a topic over weeks or months — reading papers, building a comprehensive wiki with an evolving thesis
- **Reading a book**: filing each chapter, building pages for characters, themes, plot threads — by the end you have a rich companion wiki
- **Business/team**: internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, customer calls
- **Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives**

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. **LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.** The wiki stays maintained because the cost of maintenance is near zero.

The human's job: curate sources, direct the analysis, ask good questions, think about what it all means. The LLM's job: everything else.

Related to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became. The part he couldn't solve was who does the maintenance. The LLM handles that.

## Optional Tools

- **Obsidian Web Clipper**: browser extension converting web articles to markdown
- **qmd**: local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. Has both CLI and MCP server.
- **Marp**: markdown-based slide deck format (Obsidian plugin available)
- **Dataview**: Obsidian plugin running queries over page frontmatter
- **Obsidian graph view**: best way to see the shape of the wiki
- **Download images locally**: set attachment folder to `raw/assets/`, bind hotkey for "Download attachments for current file"

## Community Implementations (from gist comments)

- **llm-wiki-kit** (iamsashank09): MCP server giving agents tools to autonomously ingest, write, search, and lint their own persistent knowledge base
- **omega-memory**: local semantic search over markdown — vector embeddings + FTS5 + cross-encoder reranking, 95.4% on LongMemEval at 50ms retrieval
- **claude-playbook-plugin** (horiacristescu): coding harness with user intent tracking, agent knowledge management, agent work tracking
- **LLM-wiki** (Ss1024sS): bootstrap generates 27 files, 5 platform configs auto-generated (Claude Code, Codex, Cursor, Windsurf, ChatGPT), YAML frontmatter with provenance, content hash staleness detection
- **sp-context** (qiuyanxin): Git repo + CLI implementation, `sp doctor` = lint, `sp push` = ingest, `sp search → sp get` = query, ~90 tokens/session
- **sage-wiki** (xoai): built-in web UI with article rendering, knowledge graph visualization, streaming Q&A
- **agentic-wiki-builder** (ap0phasi): git branches and merges for every ingestion, enabling provenance tracing of which raw info an agent was looking at when it made an update
