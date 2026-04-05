---
title: "Summary — FlexQ: Efficient Post-training INT6 Quantization for LLM Serving via Algorithm-System Co-Design"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/flexq-int6-llm-serving-2025.md
links:
  - https://arxiv.org/abs/2508.04405
tags: [quantization, int6, serving, co-design, post-training]
---

# Summary — FlexQ: Efficient Post-training INT6 Quantization for LLM Serving via Algorithm-System Co-Design

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Hao Zhang, Hao Chen, Xin He, Kai Sheng, Aining Jia, Weifeng Bu, Yushu Cai |
| Year         | 2025                           |
| Venue        | arXiv (2508.04405)             |
| Raw file     | `raw/flexq-int6-llm-serving-2025.md` |

## Main Idea

FlexQ achieves **INT6 weight quantization** for LLM serving through algorithm-system co-design, addressing the accuracy challenge of 6-bit quantization with system-level optimizations that make INT6 practical.

## Key Details

- INT6 (6-bit) quantization: between INT8 (too wasteful) and INT4 (too aggressive for most layers)
- Algorithm-system co-design: quantization algorithm designed together with serving system
- Post-training: no fine-tuning required
- Targets LLM serving场景 (cloud deployment)

## Method / Approach

[UNVERIFIED] Specific approach — likely involves per-channel or per-group quantization with calibration dataset.

## Results / Evidence

- [UNVERIFIED] Throughput improvements vs INT8 serving
- [UNVERIFIED] Accuracy保持在可接受范围内

## Limitations

- INT6 accuracy on large models [UNVERIFIED]
- Hardware support for INT6 [UNVERIFIED]

## Links to Concepts

- [[quantization]] — core methodology
- [[llm-serving]] — target use case

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
