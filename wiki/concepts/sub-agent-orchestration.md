---
title: Sub-Agent Orchestration
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bytedancedeer-flow An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minute.md
  - raw/code-yeongyuoh-my-openagent omo; the best agent harness - previously oh-my-opencode.md
links: []
tags: [ai-agents, orchestration, delegation]
---

# Sub-Agent Orchestration

## Definition

Sub-agent orchestration is the control pattern where a lead agent delegates bounded work to additional agents with narrower context, roles, or permissions.

## Why It Matters

Long-horizon tasks often exceed what one flat prompt can manage cleanly. Delegation lets systems parallelize work, specialize reasoning, and keep local context smaller.

## How It Works

An orchestrator plans the task, spawns one or more workers or specialists, gathers their outputs, and decides whether to continue, re-route, or finalize.

## Key Properties / Tradeoffs

- **Parallelism**: can speed up multi-part tasks.
- **Specialization**: lets different agents carry different prompts or tools.
- **Coordination cost**: merging results and avoiding duplicated work is hard.

## Related Concepts

- Used by: [[superagent-harness]], [[discipline-agents]]
- Often depends on: [[sandbox-isolation]]

## Source Basis

- [[summary-deer-flow]]
- [[summary-oh-my-openagent]]

## Open Questions

- What contract between orchestrator and worker is enough to prevent wasted work?

