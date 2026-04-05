---
title: "1-bit LLM (BitNet)"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# 1-bit LLM (BitNet)

1-bit LLMs use ternary ({ -1, 0, +1 }) or binary weights, dramatically reducing memory and compute. BitNet b1.58 is the reference implementation.

## BitNet Family

- **BitNet b1.58** — Ternary weights, 8-bit activations (2024)
- **BitNet v2** — 4-bit native activations via Hadamard transform (2025)
- **bitnet.cpp** — Fast CPU inference for BitNet b1.58 (2024)

## Tradeoffs

1-bit weights reduce memory ~16x vs fp16 but require specialized kernels for efficient inference. Accuracy remains competitive with fp16 baselines for many tasks.
