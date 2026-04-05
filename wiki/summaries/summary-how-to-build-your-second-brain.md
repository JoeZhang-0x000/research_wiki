---
title: "Summary — How to Build Your Second Brain"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/How to Build Your Second Brain.md
links:
  - https://x.com/NickSpisak_/status/2040448463540830705
tags: [second-brain, personal-knowledge-base, llm, workflow]
---

# Summary — How to Build Your Second Brain

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog/tweet-thread              |
| Author(s)    | @NickSpisak_                  |
| Year         | 2026                           |
| Venue        | X/Twitter                     |
| Raw file     | `raw/How to Build Your Second Brain.md` |

## Main Idea

A practitioner guide to building a personal wiki knowledge base using LLMs, inspired by Karpathy's approach: three folders (raw/, wiki/, outputs/) + one schema file + AI compilation.

## Key Details

### Folder Structure
- `raw/` — unorganized source material (articles, notes, screenshots, bookmarks)
- `wiki/` — AI-compiled organized knowledge
- `outputs/` — AI-generated answers, reports, research

### Schema File (CLAUDE.md/AGENTS.md)
Tells the AI the rules: folder semantics, wiki conventions, linking format, topics to focus on.

### Core Principle
> "Don't organize it. Don't rename anything. Don't clean it up. That's the AI's job."

### Health Check (Monthly)
- Flag contradictions between articles
- Find topics mentioned but never explained
- List claims without sources in raw/
- Suggest articles to fill gaps

### Warning: Error Compounding
> "When outputs get filed back, errors compound too." [@HFloyd]

Periodic health checks prevent AI-generated errors from accumulating.

## Tools Mentioned

- **agent-browser** (Vercel Labs): AI-controlled browser CLI, 82% fewer tokens than Playwright MCP
- **Claude Code / Cursor**: AI coding tools that maintain the wiki
- **Obsidian**: Optional viewer (not required — flat files work)

## Relationship to This Wiki

This approach is exactly the design of `research_wiki/`:
- `raw/` = source materials
- `wiki/` = compiled knowledge
- `output/` = ephemeral scratch

The schema in `AGENTS.md` and `skills/` directory implement the automated compilation workflow described here.

## Quotes Worth Preserving

> "A folder of text files and a schema file is the entire product."

> "Obsidian with 47 plugins is the Notion trap all over again. You spend more time configuring the tool than using the knowledge base."

> "41K people bookmarked Karpathy's post. The difference between bookmarking it and benefiting from it is one weekend of setup."
