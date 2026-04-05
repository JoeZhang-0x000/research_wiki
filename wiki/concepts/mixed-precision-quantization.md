---
title: "Mixed-Precision Quantization"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# Mixed-Precision Quantization

Mixed-precision quantization assigns different bit-widths to different layers or channels based on their sensitivity to quantization error.

## Key Methods

- [[kvtuner]] — Auto-tuning per-layer precision for KV cache (2025)
- [[kvmix]] — Gradient-based layer importance for KV cache (2025)
- [[cmpq]] — Channel-wise mixed-precision for weights (2024)

## Key Insight

Not all layers are equally important. More important layers get higher precision, less important layers get lower precision, optimizing the total memory-accuracy tradeoff.
