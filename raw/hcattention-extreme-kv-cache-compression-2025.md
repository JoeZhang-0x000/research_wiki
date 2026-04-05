---
title: "HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing"
source: "https://arxiv.org/abs/2507.19823"
author:
  - "Yifan Yang"
  - "Xianbiao Qi"
  - "Rong Xiao"
  - "Xiaotian Yu"
  - "Dongquan Yang"
published: 2025-07-26
created: 2026-04-05
description: "HCAttention: 极端 KV Cache 压缩（12.5% 显存），Key 量化 + Value offload + 动态驱逐，Llama-3-8B 单卡 A100 处理 4M tokens"
tags:
  - "papers"
  - "kv-cache"
  - "compression"
  - "heterogeneous-computing"
---

# HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing

**Authors**: Yifan Yang, Xianbiao Qi, Rong Xiao, Xiaotian Yu, Dongquan Yang  
**arXiv**: 2507.19823

## Abstract

Processing long-context inputs with large language models presents a significant challenge due to the enormous memory requirements of the Key-Value (KV) cache during inference. Existing KV cache compression methods exhibit noticeable performance degradation when memory is reduced by more than 85%. Additionally, strategies that leverage GPU-CPU collaboration for approximate attention remain underexplored.

We propose **HCAttention**, a heterogeneous attention computation framework that integrates:
- **Key quantization**
- **Value offloading**
- **Dynamic KV eviction**

The method is compatible with existing transformer architectures and does not require model fine-tuning.

## Key Results

- **Preserves accuracy** of full-attention model while shrinking KV cache to **25% of original size**
- **State-of-the-art at 12.5% cache**: competitive accuracy
- **First to extend Llama-3-8B to process 4 million tokens on a single A100 80GB GPU**

## Source

https://arxiv.org/abs/2507.19823
