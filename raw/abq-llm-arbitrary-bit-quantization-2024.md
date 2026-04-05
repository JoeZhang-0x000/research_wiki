---
title: "ABQ-LLM: Arbitrary-Bit Quantized Inference Acceleration for Large Language Models"
source: "https://arxiv.org/abs/2408.08554"
author:
  - "Hong Liu"
  - "Shu Yang"
  - "Xiaojian Wang"
  - "Songwei Liu"
  - "Yusheng Xie"
  - "Chao Zeng"
  - "Xing Mei"
  - "Fangmin Chen"
  - "Miao Wei"
published: 2024-08-16
created: 2026-04-05
description: "ABQ-LLM: 任意比特量化，利用 BTC 克服 GPU INT4/INT8 限制，W2*A8 在 LLaMA-7B 上比 AffineQuant 快 2.17 perplexity"
tags:
  - "papers"
  - "weight-quantization"
  - "arbitrary-bit"
  - "llm-inference"
---

# ABQ-LLM: Arbitrary-Bit Quantized Inference Acceleration for Large Language Models

**Authors**: Hong Liu, Shu Yang, Xiaojian Wang, Songwei Liu, Yusheng Xie, Chao Zeng, Xing Mei, Fangmin Chen, Miao Wei  
**Venue**: AAAI 2025  
**arXiv**: 2408.08554

## Abstract

Large Language Models (LLMs) have revolutionized natural language processing tasks. However, their practical application is constrained by substantial memory and computational demands. Post-training quantization (PTQ) is considered an effective method to accelerate LLM inference.

Despite its growing popularity, PTQ deployment faces two major challenges:
1. Low-bit quantization leads to performance degradation
2. Restricted by limited integer computing unit type on GPUs, quantized matrix operations with different precisions cannot be effectively accelerated

We introduce **ABQ-LLM**, a novel arbitrary-bit quantization algorithm and inference framework enabling efficient arbitrary-precision quantized inference on GPU.

## Key Innovations

1. **Distribution correction method** for transformer blocks to mitigate distribution differences from full quantization of weights and activations
2. **Bit balance strategy** to counteract asymmetric distribution issues at very low bit-widths (e.g., 2-bit)
3. **Innovative quantization acceleration framework** based on BTC (Binary TensorCore) equivalents

## Key Results

- **W2*A8 on LLaMA-7B**: WikiText2 perplexity 7.59 (2.17↓ vs AffineQuant)
- **1.6x acceleration improvement** over SmoothQuant
- **2.7x memory compression gain** over SmoothQuant

## Source

https://arxiv.org/abs/2408.08554
