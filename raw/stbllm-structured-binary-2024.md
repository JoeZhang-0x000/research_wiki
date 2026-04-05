---
title: "STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs"
authors: ["Peijie Dong", "Lujun Li", "Dayou Du", "Yuhan Chen", "Zhenheng Tang", "Qiang Wang", "Wei Xue", "Wenhan Luo", "Xiaowen Chu"]
year: 2024
arxiv: "2408.01803"
url: "https://arxiv.org/abs/2408.01803"
venue: arXiv
tags: [llm, quantization, 1-bit, binary, structured-sparsity]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

STBLLM is the first **structural binarization method** for LLM compression to less than 1-bit precision. It combines N:M sparsity with structured binarization to break the 1-bit barrier.

## Key Observation

Some weights in binarized LLMs can be **randomly flipped** without significant performance degradation, suggesting potential for further compression.

## Key Methods

1. **Standardized Importance (SI) metric**: Considers weight magnitude and input feature norm to assess weight significance more accurately
2. **Layer-wise N:M sparsity**: Different layers can have different N:M ratios, balancing compression and accuracy
3. **Fine-grained grouping**: Apply distinct quantization schemes to sparse, intermediate, and dense regions
4. **Custom CUDA kernel**: Supports structural binarization efficiently

## Key Findings

- Evaluated on LLaMA-1/2/3, OPT family, and Mistral
- Outperforms other compressed binarization LLM methods
- Significantly reduces memory requirements

## Notes

Combines ideas from pruning (N:M sparsity) with quantization (binarization) for synergistic compression.
