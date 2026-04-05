---
title: "KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization"
authors: ["Coleman Hooper", "Sehoon Kim", "Hiva Mohammadzadeh", "Michael W. Mahoney", "Yakun Sophia Shao", "Kurt Keutzer", "Amir Gholami"]
year: 2024
arxiv: "2401.18079"
url: "https://arxiv.org/abs/2401.18079"
venue: NeurIPS 2024
tags: [llm, quantization, kv-cache, long-context]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

KVQuant addresses the memory bottleneck of **long-context LLM inference** by quantizing KV cache activations. It enables up to **10 million context length** on an 8-GPU system.

## Key Methods

1. **Per-Channel Key Quantization**: Adjusts the quantization dimension for Key activations to better match their distribution
2. **Pre-RoPE Key Quantization**: Quantizes Key activations before rotary positional embedding to mitigate its impact
3. **Non-Uniform KV Cache Quantization**: Derives per-layer sensitivity-weighted non-uniform datatypes
4. **Per-Vector Dense-and-Sparse Quantization**: Isolates outliers separately for each vector to minimize quantization range skew

## Key Findings

- Achieves **< 0.1 perplexity degradation** with 3-bit quantization on Wikitext-2 and C4
- LLaMA-7B with **1 million context** on a single A100-80GB
- **10 million context** on 8-GPU system
- Up to **~1.7x speedup** via custom CUDA kernels

## Comparison to Prior Work

Outperforms existing KV cache quantization approaches by addressing outlier sensitivity through the four novel methods above.

## Hardware

Custom CUDA kernels developed for efficient low-bit KV cache operations.
