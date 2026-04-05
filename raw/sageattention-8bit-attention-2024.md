---
title: "SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration"
source: "https://arxiv.org/abs/2410.02367"
author:
  - "Jintao Zhang"
  - "Jia Wei"
  - "Pengle Zhang"
  - "Jun Zhu"
  - "Jianfei Chen"
published: 2024-10-03
created: 2026-04-05
description: "SageAttention: 8-bit 注意力量化，比 FlashAttention2 快 2.1x，比 xformers 快 2.7x，精度接近 FlashAttention3"
tags:
  - "papers"
  - "attention"
  - "quantization"
  - "inference-acceleration"
---

# SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration

**Authors**: Jintao Zhang, Jia Wei, Pengle Zhang, Jun Zhu, Jianfei Chen  
**Venue**: ICLR 2025  
**arXiv**: 2410.02367

## Abstract

The transformer architecture predominates across various models. As the heart of the transformer, attention has a computational complexity of O(N²), compared to O(N) for linear transformations. When handling large sequence lengths, attention becomes the primary time-consuming component.

Although quantization has proven to be an effective method for accelerating model inference, existing quantization methods primarily focus on optimizing the linear layer. In response, we first analyze the feasibility of quantization in attention detailedly. Following that, we propose **SageAttention**, a highly efficient and accurate quantization method for attention.

## Key Results

- **OPS outperforms FlashAttention2 by ~2.1x**
- **OPS outperforms xformers by ~2.7x**
- **Superior accuracy performance over FlashAttention3**
- **Almost no end-to-end metrics loss** across diverse models (language, image generation, video generation)

## Method

- Analyzes feasibility of quantization in attention
- Proposes 8-bit attention quantization that preserves accuracy
- Plug-and-play: can be integrated without model fine-tuning

## Source

https://arxiv.org/abs/2410.02367
