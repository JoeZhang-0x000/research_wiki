---
title: "Summary — STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/stbllm-structured-binary-2024.md
links:
  - https://arxiv.org/abs/2408.01803
tags: [1-bit, binary, structured-sparsity, n-m-sparsity, quantization]
---

# Summary — STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Peijie Dong, Lujun Li, Dayou Du, et al. |
| Year         | 2024                           |
| Venue        | arXiv (2408.01803)             |
| Raw file     | `raw/stbllm-structured-binary-2024.md` |

## Main Idea

STBLLM combines **N:M structured sparsity** with **binarization** to achieve "sub-1-bit" LLM compression. Uses a novel Standardized Importance (SI) metric to guide layer-wise sparsity allocation.

## Key Observation

Some weights in binarized LLMs can be randomly flipped without significant degradation — suggesting potential for further compression beyond binary.

## Key Methods

1. **Standardized Importance (SI) metric**: considers weight magnitude AND input feature norm to assess importance
2. **Layer-wise N:M sparsity**: different layers get different N:M ratios
3. **Fine-grained grouping**: different quantization for sparse/intermediate/dense regions
4. **Custom CUDA kernel**: hardware support for structural binarization

## Results / Evidence

- Evaluated on LLaMA-1/2/3, OPT, Mistral
- Outperforms other compressed binarization methods
- [UNVERIFIED] Specific numbers

## Limitations

- Complexity of combined sparsity + binarization
- [UNVERIFIED] Accuracy vs ternary methods like BitNet b1.58

## Links to Concepts

- [[binary-quantization]] — core methodology
- [[structured-sparsity]] — N:M sparsity component

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
