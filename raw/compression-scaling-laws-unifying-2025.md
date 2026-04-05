---
title: "Compression Scaling Laws: Unifying Sparsity and Quantization"
authors: ["Elias Frantar", "Utku Evci", "Wonpyo Park", "Neil Houlsby", "Dan Alistarh"]
year: 2025
arxiv: "2502.16440"
url: "https://arxiv.org/abs/2502.16440"
venue: arXiv
tags: [llm, quantization, sparsity, scaling-laws]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

Investigates how different compression techniques (weight/activation quantization, weight sparsity) affect LLM scaling laws during pretraining. Establishes a **unified scaling law framework** for compression methods.

## Key Findings

1. **Weight sparsity** acts as a **constant multiplier on model size** in scaling laws (prior work)
2. **Weight-only quantization** also achieves strong parameter efficiency multipliers
3. **Full quantization** (weights + activations) shows **diminishing returns** at lower bitwidths

## Theoretical Contribution

Demonstrates that sparsity and quantization can be unified under a common scaling law framework, enabling principled comparison and combination of compression methods.

## Implications

- Different compression techniques can be systematically compared using the same framework
- Provides guidance on how to combine sparsity and quantization optimally
- Helps predict the effective model capacity at different compression ratios

## Notes

- Builds on prior work showing sparsity scaling behavior
- Elias Frantar is also the author of GPTQ
