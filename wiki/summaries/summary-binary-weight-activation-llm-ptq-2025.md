---
title: "Summary — Achieving Binary Weight and Activation for LLMs using Post-Training Quantization"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/binary-weight-activation-llm-ptq-2025.md
links:
  - https://arxiv.org/abs/2504.05352
tags: [quantization, binary, post-training, weight-activation]
---

# Summary — Achieving Binary Weight and Activation for LLMs using Post-Training Quantization

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Yi Yang, Ruiqi Wang, Chuang Wang, Xu-Yao Zhang, Siqing Song |
| Year         | 2025                           |
| Venue        | arXiv (2504.05352)             |
| Raw file     | `raw/binary-weight-activation-llm-ptq-2025.md` |

## Main Idea

This paper pushes LLM quantization to the extreme: **binary weights AND binary activations** (1-bit each) using post-training quantization, achieving the most aggressive compression possible.

## Key Details

- Binary weight: each parameter is either -1 or +1 (or 0/1)
- Binary activation: activations also reduced to 1-bit
- Post-training: no fine-tuning needed
- Extreme compression ratio vs fp16

## Method / Approach

[UNVERIFIED] Technical approach for maintaining accuracy with binary weight + activation. Likely involves:
- Special handling of the binarization process
- Error feedback mechanisms
- Straight-through estimators or similar

## Results / Evidence

- [UNVERIFIED] Perplexity or task accuracy vs fp16 baseline
- [UNVERIFIED] Model sizes tested

## Limitations

- Binary quantization typically causes significant accuracy degradation
- [UNVERIFIED] Whether results are competitive with higher-bit methods

## Links to Concepts

- [[quantization]] — core methodology
- [[binary-quantization]] — extreme case

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
