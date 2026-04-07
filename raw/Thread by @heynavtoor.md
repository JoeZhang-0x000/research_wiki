---
title: "Thread by @heynavtoor"
source: "https://x.com/heynavtoor/status/2041140052949090417"
author:
  - "[[@heynavtoor]]"
published: 2026-04-06
created: 2026-04-07
description: "Andrej Karpathy thinks RAG is broken. He published the replacement 2 days ago. 5,000 stars in 48 hours. It's called LLM Wiki. A pattern wh"
tags:
  - "clippings"
---
**Nav Toor** @heynavtoor [2026-04-06](https://x.com/heynavtoor/status/2041140052949090417)

🚨 Andrej Karpathy thinks RAG is broken. He published the replacement 2 days ago. 5,000 stars in 48 hours.

It's called LLM Wiki.

A pattern where your AI doesn't retrieve information from scratch every time. It builds and maintains a persistent, compounding knowledge base. Automatically.

RAG re-discovers knowledge on every question. LLM Wiki compiles it once and keeps it current.

Here's the difference:

RAG: You ask a question. AI searches your documents. Finds fragments. Pieces them together. Forgets everything. Starts over next time.

LLM Wiki: You add a source. AI reads it, extracts key information, updates entity pages, revises topic summaries, flags contradictions, strengthens the synthesis. The knowledge compounds. Every source makes the wiki smarter. Permanently.

Here's how it works:

→ Drop a source into your raw collection. Article, paper, transcript, notes.

→ AI reads it, writes a summary, updates the index

→ Updates every relevant entity and concept page across the wiki

→ One source can touch 10 to 15 wiki pages simultaneously

→ Cross-references are built automatically

→ Contradictions between sources get flagged

→ Ask questions against the wiki. Good answers get filed back as new pages.

→ Your explorations compound in the knowledge base. Nothing disappears into chat history.

Here's the wildest part:

Karpathy's use case examples:

→ Personal: track goals, health, psychology. File journal entries and articles. Build a structured picture of yourself over time.

→ Research: read papers for months. Build a comprehensive wiki with an evolving thesis.

→ Reading a book: build a fan wiki as you read. Characters, themes, plot threads. All cross-referenced.

→ Business: feed it Slack threads, meeting transcripts, customer calls. The wiki stays current because the AI does the maintenance nobody wants to do.

Think of it like this: Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase. You never write the wiki yourself. You source, explore, and ask questions. The AI does all the grunt work.

NotebookLM, ChatGPT file uploads, and most RAG systems re-derive knowledge on every query. This compiles it once and builds on it forever.

5,000+ stars. 1,294 forks. Published by Andrej Karpathy. 2 days ago.

100% Open Source.

![Image](https://pbs.twimg.com/media/HFOWD5QbYAAzGVp?format=jpg&name=large)

---

**Nav Toor** @heynavtoor [2026-04-06](https://x.com/heynavtoor/status/2041140065016201685)

Link:

---

**TravelerOfCode** @TravelerOfCode [2026-04-07](https://x.com/TravelerOfCode/status/2041360559560589800)

5k stars in 48h is wild. gonna go check this out tonight

---

**Nav Toor** @heynavtoor [2026-04-07](https://x.com/heynavtoor/status/2041424142264918255)

let me know what you think after trying it

---

**Nika Karliuchenko** @nikaukraine [2026-04-07](https://x.com/nikaukraine/status/2041367478001909776)

Genuinely interesting pattern. My instinct is that RAG and LLM Wiki might just be solving different things: RAG for “find the relevant piece and answer,” LLM Wiki for “synthesize everything I know over time.” Thoughts?

---

**Nav Toor** @heynavtoor [2026-04-07](https://x.com/heynavtoor/status/2041425057734623495)

that's a smart take, they might work best together rather than one replacing the other

---

**JFMorro** @AlpenglowAgents [2026-04-06](https://x.com/AlpenglowAgents/status/2041168671054118956)

Still RAG, just better sorted. He isnt close, and he cant do what I can do.

---

**Nav Toor** @heynavtoor [2026-04-07](https://x.com/heynavtoor/status/2041424308770320648)

it builds on RAG concepts for sure but the compounding part is what makes it feel different in practice