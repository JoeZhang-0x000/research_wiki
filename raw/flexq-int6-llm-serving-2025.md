---
title: "FlexQ: Efficient Post-training INT6 Quantization for LLM Serving"
source: "https://arxiv.org/abs/2508.04405"
author:
  - "Hao Zhang"
  - "Hao Chen"
  - "Xin He"
  - "Kai Sheng"
  - "Aining Jia"
  - "Weifeng Bu"
  - "Yushu Cai"
published: 2025-08-06
created: 2026-04-05
description: "FlexQ: INT6 权重量化 + 算法-系统协同设计，W6A6/W6A8 高性能 GPU kernel，推理加速 1.33x"
tags:
  - "papers"
  - "weight-quantization"
  - "int6"
  - "llm-serving"
---

# FlexQ: Efficient Post-training INT6 Quantization for LLM Serving

**Authors**: Hao Zhang, Hao Chen, Xin He, Kai Sheng, Aining Jia, Weifeng Bu, Yushu Cai  
**arXiv**: 2508.04405

## Abstract

Large Language Models (LLMs) demonstrate exceptional performance but entail significant memory and computational costs, restricting their practical deployment. While existing INT4/INT8 quantization reduces these costs, they often degrade accuracy or lack optimal efficiency. **INT6 quantization offers a superior trade-off** between model accuracy and inference efficiency, but lacks hardware support in modern GPUs, forcing emulation via higher-precision arithmetic units that limit acceleration.

We propose **FlexQ**, a novel post-training INT6 quantization framework combining algorithmic innovation with system-level optimizations:

1. **Uniform 6-bit weight quantization** across all layers
2. **Adaptive retention of 8-bit activations** in layers identified through layer-wise sensitivity analysis
3. **Specialized high-performance GPU kernel** supporting W6A6 and W6A8 matrix multiplication via Binary Tensor Core (BTC) equivalents

## Key Results

- **Near-FP16 accuracy**: perplexity increase of no more than 0.1 on WikiText2 (LLaMA family)
- **1.39x speedup** over ABQ-LLM on LLaMA-2-70B linear layers
- **1.33x end-to-end inference acceleration** over SmoothQuant
- **1.21x memory savings** over SmoothQuant

## Source

https://arxiv.org/abs/2508.04405
