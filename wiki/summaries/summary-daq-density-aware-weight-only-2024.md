---
title: "Summary — DAQ: Density-Aware Post-Training Weight-Only Quantization For LLMs"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/daq-density-aware-weight-only-2024.md
links:
  - https://arxiv.org/abs/2410.12187
tags: [weight-only, post-training, density-aware, quantization]
---

# Summary — DAQ: Density-Aware Post-Training Weight-Only Quantization For LLMs

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Ling Chen, Yingsong Luo |
| Year         | 2024                           |
| Venue        | arXiv (2410.12187)             |
| Raw file     | `raw/daq-density-aware-weight-only-2024.md` |

## Main Idea

DAQ (Density-Aware Post-Training Weight-Only Quantization) centers the quantization dynamic range around high-density weight regions, identifying the center of high-density weights and aligning them with floating-point precision.

## Two-Stage Approach

### Stage 1: Density-Centric Alignment
- Identifies center of high-density weights
- Centers dynamic range on this point
- Aligns high-density regions with fp precision

### Stage 2: Learnable Dynamic Range Adjustment
- Optimizes scale and zero-point based on weight impact on model output
- Learns to preserve most important distributions

## Results / Evidence

- Outperforms best baseline methods consistently
- **Perplexity loss reduced by 22.8%** on LLaMA (average)
- **Perplexity loss reduced by 19.6%** on LLaMA-2 (average)

## Code

https://github.com/LuoYingSong/DAQ

## Limitations

- [UNVERIFIED] Specific quantization bit-widths tested
- [UNVERIFIED] Whether it combines well with KV cache quantization

## Links to Concepts

- [[weight-only-quantization]] — methodology
- [[post-training-quantization]] — approach

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
