---
title: "Long-Context LLM"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# Long-Context LLM

Long-context LLMs handle extended input sequences (100K+ tokens). KV cache becomes the dominant memory bottleneck at scale.

## Key Methods

- [[kvquant]] — 10 million context on 8-GPU (NeurIPS 2024)
- [[bitdecoding]] — Tensor core optimization for long-context (2025)

## Challenge

Memory for KV cache scales O(n²) with sequence length, making long contexts prohibitively expensive without compression.
