---
title: "Weight-Only Quantization"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# Weight-Only Quantization

Weight-only quantization reduces the precision of model weights while keeping activations in fp16/bf16. Simpler than weight-activation quantization, often sufficient for memory-bound inference.

## Key Methods

- [[gptq]] — Hessian-based, 175B in 4 GPU hours (ICLR 2023)
- [[finequant]] — Adaptive fine-grained granularity (2023)
- [[daq]] — Density-aware post-training (2024)

## Tradeoffs

Weight-only quantization reduces memory by ~2x (fp16 → int8) or ~4x (fp16 → int4) but doesn't reduce compute bandwidth proportionally since activations remain full precision.
