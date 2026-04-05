---
title: "DAQ: Density-Aware Post-Training Weight-Only Quantization For LLMs"
authors: ["Ling Chen", "Yingsong Luo"]
year: 2024
arxiv: "2410.12187"
url: "https://arxiv.org/abs/2410.12187"
venue: arXiv
tags: [llm, quantization, weight-only, post-training]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

DAQ (Density-Aware Post-Training Weight-Only Quantization) addresses the challenge of quantizing LLM weights by centering the quantization dynamic range around high-density weight regions.

## Two-Stage Approach

### Stage 1: Density-Centric Alignment
- Identifies the **center of high-density weights**
- Centers the dynamic range on this point
- Aligns high-density weight regions with floating-point high-precision regions

### Stage 2: Learnable Dynamic Range Adjustment
- Optimizes quantization parameters (scale and zero-point)
- Based on the **impact of weights on model output**
- Learns to preserve the most important weight distributions

## Key Findings

- Consistently outperforms best baseline methods
- **Perplexity loss reduced by 22.8%** on LLaMA (average)
- **Perplexity loss reduced by 19.6%** on LLaMA-2 (average)

## Code

https://github.com/LuoYingSong/DAQ
