---
title: "Summary — FineQuant: Unlocking Efficiency with Fine-Grained Weight-Only Quantization for LLMs"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/finequant-fine-grained-weight-only-2023.md
links:
  - https://arxiv.org/abs/2308.09723
tags: [weight-only, fine-grained, moe, heuristic, meta-ai]
---

# Summary — FineQuant: Unlocking Efficiency with Fine-Grained Weight-Only Quantization for LLMs

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Young Jin Kim, Rawn Henry, Raffy Fahim, Hany Hassan Awadalla |
| Year         | 2023                           |
| Venue        | arXiv (2308.09723)             |
| Raw file     | `raw/finequant-fine-grained-weight-only-2023.md` |

## Main Idea

FineQuant uses a heuristic approach to find the **optimal quantization granularity** per model, without requiring fine-tuning. Works for both dense and MoE models.

## Key Innovation: Adaptive Granularity

Previous methods use fixed quantization granularity (per-tensor or per-channel). FineQuant finds the **optimal granularity per model** using a heuristic — the right level of grouping varies by model architecture.

## Key Methods

1. Analyze challenges of LLM weight-only quantization
2. Heuristic approach to find optimal granularity per model
3. On-the-fly dequantization in GPU GEMM (fp16/bf16 activations × int8/int4 weights)

## Results / Evidence

- Tested on **OPT-175B** and internal MoE models
- **Up to 3.65x higher throughput** on same number of GPUs
- Minimal accuracy loss
- Supports int8 and int4 weights

## Limitations

- Heuristic may not find globally optimal granularity
- [UNVERIFIED] Specific perplexity numbers

## Links to Concepts

- [[weight-only-quantization]] — core methodology
- [[fine-grained-quantization]] — adaptive granularity

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
