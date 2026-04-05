---
title: "Summary — Channel-Wise Mixed-Precision Quantization for Large Language Models"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/channel-wise-mixed-precision-quantization-2024.md
links:
  - https://arxiv.org/abs/2410.13056
tags: [mixed-precision, channel-wise, weight-only, quantization]
---

# Summary — Channel-Wise Mixed-Precision Quantization for Large Language Models

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Zihan Chen, Bike Xie, Jundong Li, Cong Shen |
| Year         | 2024                           |
| Venue        | arXiv (2410.13056)             |
| Raw file     | `raw/channel-wise-mixed-precision-quantization-2024.md` |

## Main Idea

CMPQ (Channel-Wise Mixed-Precision Quantization) allocates quantization precision **per weight channel** based on activation distributions, enabling adaptation to any bit-width constraint including fractional bits.

## The Problem

Existing weight-only quantization methods focus on integer-bit quantization, limiting adaptability to fractional-bit scenarios and preventing full utilization of available storage.

## Key Methods

1. **Channel-wise precision allocation**: different precision for different weight channels
2. **Non-uniform quantization**: adapts to actual weight distributions
3. **Two outlier extraction techniques**: preserve critical information by separating outliers

## Results / Evidence

- Works for both integer-bit and fractional-bit quantization
- Enhances performance in integer-bit tasks
- **Significant gains with modest memory overhead**
- [UNVERIFIED] Specific benchmark numbers

## Limitations

- [UNVERIFIED] Computational overhead of per-channel optimization
- [UNVERIFIED] Generalization across model architectures

## Links to Concepts

- [[mixed-precision-quantization]] — core methodology
- [[channel-wise-quantization]] — precision allocation strategy

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
