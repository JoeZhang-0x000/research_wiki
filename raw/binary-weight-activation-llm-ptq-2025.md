---
title: "Achieving Binary Weight and Activation for LLMs using Post-Training Quantization"
source: "https://arxiv.org/abs/2504.05352"
author:
  - "Yi Yang"
  - "Ruiqi Wang"
  - "Chuang Wang"
  - "Xu-Yao Zhang"
  - "Siqing Song"
published: 2025-04-07
created: 2026-04-05
description: "W(1+1)A(1*4) 二值化 PTQ，权重 1bit + 细粒度分组，激活 1bit + 通道扩展，超 SOTA W2A4"
tags:
  - "papers"
  - "binary-quantization"
  - "post-training"
  - "weight-activation"
---

# Achieving Binary Weight and Activation for LLMs using Post-Training Quantization

**Authors**: Yi Yang, Ruiqi Wang, Chuang Wang, Xu-Yao Zhang, Siqing Song  
**arXiv**: 2504.05352

## Abstract

Quantizing large language models (LLMs) to 1-bit precision significantly reduces computational costs, but existing quantization techniques suffer from noticeable performance degradation when using weight and activation precisions below 4 bits (W4A4).

We propose a post-training quantization framework with **W(1+1)A(1*4) configuration**:
- **Weights**: quantized to 1 bit with an additional 1 bit for fine-grain grouping
- **Activations**: quantized to 1 bit with a 4-fold increase in the number of channels

## Key Innovations

**Weight quantization:**
- Hessian-aware fine-grained grouping
- EM-based quantization scheme

**Activation quantization:**
- Decompose INT4-quantized activations into 4*INT1 format equivalently
- Smooth scaling factors based on quantization errors

## Key Results

- Surpasses SOTA LLM quantization baselines on **W2A4** across multiple tasks
- Pushes boundaries toward fully binarized models

## Source

https://arxiv.org/abs/2504.05352
