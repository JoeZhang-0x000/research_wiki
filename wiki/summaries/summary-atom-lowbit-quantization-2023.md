---
title: "Summary — Atom: Low-bit Quantization for Efficient and Accurate LLM Serving"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/atom-lowbit-quantization-2023.md
links:
  - https://arxiv.org/abs/2310.19102
tags: [w4a4, low-bit, serving, mixed-precision]
---

# Summary — Atom: Low-bit Quantization for Efficient and Accurate LLM Serving

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Yilong Zhao, Chien-Yu Lin, Kan Zhu, Zihao Ye, Lequn Chen, Size Zheng, Luis Ceze, Arvind Krishnamurthy, Tianqi Chen, Baris Kasikci |
| Year         | 2024                           |
| Venue        | arXiv (2310.19102)             |
| Raw file     | `raw/atom-lowbit-quantization-2023.md` |

## Main Idea

Atom achieves **W4A4 quantization** (4-bit weight, 4-bit activation) for LLM serving, achieving up to **7.7x throughput improvement** over FP16 and 2.5x over INT8 by exploiting hardware 4-bit integer operators.

## The Problem

INT8 quantization can't fully leverage modern GPU 4-bit integer operators — hardware has evolved but software hasn't caught up.

## Key Approach

1. **Novel mixed-precision**: different precision for different layers/channels based on sensitivity
2. **Fine-grained quantization**: sub-channel level granularity
3. **Low-bit operators**: exploit GPU 4-bit integer support directly

## Results / Evidence

- **7.7x throughput improvement** vs FP16
- **2.5x throughput improvement** vs INT8
- Same latency target
- Negligible accuracy loss

## Limitations

- [UNVERIFIED] Per-layer or per-channel sensitivity analysis overhead
- [UNVERIFIED] Hardware requirements (which GPUs support 4-bit integer ops?)

## Links to Concepts

- [[low-bit-quantization]] — core methodology
- [[llm-serving]] — target use case

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
