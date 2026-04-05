---
title: "KVTuner: Sensitivity-Aware Layer-wise Mixed Precision KV Cache Quantization"
source: "https://arxiv.org/abs/2502.04420"
author:
  - "Yiming Li"
  - "Sinno Jialin Pan"
  - "Hui-Ling Zhen"
  - "Mingxuan Yuan"
  - "Wulong Liu"
  - "Xing Li"
  - "Yiwu Yao"
  - "Zeyu Xing"
  - "Linping Qu"
published: 2025-02-06
created: 2026-04-05
description: "KVTuner: 层敏感度感知的混合精度 KV Cache 量化，Llama-3.1-8B 近乎无损 3.25bit，推理吞吐提升 21.25%"
tags:
  - "papers"
  - "kv-cache"
  - "quantization"
  - "mixed-precision"
---

# KVTuner: Sensitivity-Aware Layer-wise Mixed Precision KV Cache Quantization

**Authors**: Yiming Li, Sinno Jialin Pan, Hui-Ling Zhen, Mingxuan Yuan, Wulong Liu, Xing Li, Yiwu Yao, Zeyu Xing, Linping Qu  
**Venue**: ICML 2025  
**arXiv**: 2502.04420

## Abstract

KV cache quantization can improve LLM inference throughput and latency in long contexts and large batch-size scenarios while preserving LLMs effectiveness. However, current methods have three unsolved issues:

1. Overlooking layer-wise sensitivity to KV cache quantization
2. High overhead of online fine-grained decision-making
3. Low flexibility to different LLMs and constraints

We theoretically analyze the inherent correlation of layer-wise transformer attention patterns to KV cache quantization errors and study why key cache is generally more important than value cache for quantization error reduction.

We propose **KVTuner**, a framework to adaptively search for optimal hardware-friendly layer-wise KV quantization precision pairs for coarse-grained KV cache with multi-objective optimization, and directly utilize offline searched configurations during online inference.

To reduce the computational cost of offline calibration, we utilize intra-layer KV precision pair pruning and inter-layer clustering to reduce the search space.

## Key Results

- **Nearly lossless 3.25-bit mixed precision KV cache** for Llama-3.1-8B-Instruct
- **4.0-bit for sensitive models** like Qwen2.5-7B-Instruct on math reasoning tasks
- **21.25% inference throughput improvement** over KIVI-KV8 quantization across various context lengths

## Source

https://arxiv.org/abs/2502.04420
