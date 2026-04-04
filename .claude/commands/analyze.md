First-principles analysis. Reasons from irreducible constraints to necessary conclusions.

Usage: /analyze <topic>

---

## What "first principles" means here

First principles are constraints you cannot argue with:
physical laws, information-theoretic limits, logical necessity.

Everything else is a response — either *forced* (no alternative given the constraint)
or *chosen* (one of many valid responses). The analysis distinguishes these.

Numbers are not conclusions. The question is always:
*why must this be, given what cannot be otherwise?*

---

## Step 0: Gather

Run: `python skills/search.py "<topic>"`
Read every matching page and every page they link to.

For each page, extract from frontmatter:
- `links:` — original URLs (Obsidian Clipper source)
- `sources:` — raw files or URLs this page was compiled from

Build a reference list. You will cite these throughout as `([source](url))`.
If a source has no URL, cite as `(raw/filename)`.

---

## Pass 1 — The irreducible constraint

What physical or mathematical law makes this problem hard in a way no engineering escapes?
State the fundamental tension: the two things you cannot simultaneously have, and why.

*One paragraph. No hedging. No solution names.*

---

## Pass 2 — Forced vs. chosen

For each major design decision:
- **Forced** — any valid solution must do this because the constraint leaves no room
- **Chosen** — this did X; Y was also possible; the difference is the assumption that X's case dominates

`[forced/chosen] <decision> — <one-sentence reason> ([source](url))`

---

## Pass 3 — What moved

Every choice that solves Pass 1's constraint moves cost somewhere else.

`Solved <X> by moving cost to <Y>` — one line each, with source link.
Then: what new assumption is now load-bearing? One line each.

---

## Pass 4 — Adversarial

Strongest case that the approach is right for narrower reasons than claimed,
or that Pass 1's framing is wrong.

Three questions only:
1. Is Pass 1's constraint actually the binding one, or is there a prior?
2. Does the dominant-case assumption in Pass 2 hold in practice?
3. What is the real ceiling — the structural reason improvement terminates?

*Three answers, three sentences max each.*

---

## Pass 5 — Synthesis

What is actually true, in plain reasoning chains.
Resolve contradictions between passes explicitly.
Prose, not bullets. Every sentence answers "why must this be?" not "what did we observe?"

End with one sentence:
**The one thing that, if it changed, would make this approach obsolete:** (the condition, not a technology name)

---

## Output format

Write to: `output/analysis-<topic-slug>-<YYYY-MM-DD>.md`

```markdown
---
title: Analysis — <topic>
date: YYYY-MM-DD
sources: [list of wiki pages read]
---

## TL;DR
<2-3 sentences. What is essentially true after all five passes. Written last.>

---

## Pass 1 — The irreducible constraint
...

## Pass 2 — Forced vs. chosen
...

## Pass 3 — What moved
...

## Pass 4 — Adversarial
...

## Pass 5 — Synthesis
...

---

## References
<!-- All links: fields collected in Step 0. Only include URLs, not raw/ paths. -->
- [<page title or domain>](<url>) — [[PageName]]
```

After writing, tell the user:
- The finding in Pass 5 most absent from the wiki's framing
- The Pass 4 challenge hardest to rebut

Then ask: "Should I distill any of this into wiki pages?"
Do NOT touch wiki/ until the user says yes.
