---
title: "BitDecoding: Unlocking Tensor Cores for Long-Context LLMs Decoding with Low-Bit KV Cache"
source: "https://arxiv.org/abs/2503.18773"
author:
  - "Dayou Du"
  - "Mao Yang"
  - "Ting Cao"
  - "Shijie Cao"
  - "Luo Mai"
  - "Jianyi Cheng"
published: 2025-03-24
created: 2026-04-05
description: "BitDecoding: 首个结合 CUDA core 和 Tensor Core 实现低比特 KV Cache 高效解码的系统，Blackwell 上平均 7.5x 加速"
tags:
  - "papers"
  - "kv-cache"
  - "quantization"
  - "tensor-core"
---

# BitDecoding: Unlocking Tensor Cores for Long-Context LLMs Decoding with Low-Bit KV Cache

**Authors**: Dayou Du, Mao Yang, Ting Cao, Shijie Cao, Luo Mai, Jianyi Cheng  
**arXiv**: 2503.18773

## Abstract

The growth of long-context Large Language Models (LLMs) significantly increases memory and bandwidth pressure during autoregressive decoding due to the expanding Key-Value (KV) cache. While accuracy-preserving KV-cache quantization (e.g., 4-bit or 2-bit) reduces memory footprint, existing systems decode inefficiently by relying solely on CUDA cores, underutilizing Tensor Cores—the dominant compute resource on GPUs.

We present **BitDecoding**, the first inference system to efficiently decode low-bit KV caches by cooperatively leveraging CUDA cores and Tensor Cores. BitDecoding smartly induces Tensor-Core-friendly layouts, introduces warp-level dequantization parallelism, and provides unified system support through query transformation, high-performance tensor- and channel-wise quantization, and a software-pipelined dequantization kernel enabling mixed-precision execution. Architecture-aware optimizations further leverage Hopper's warpgroup tensor instructions and Blackwell's NVFP4 (MXFP4) tensor formats.

## Key Results

- **Average 7.5x decoding speedup** over FP16 FlashDecoding-v2
- **Up to 8.6x on Blackwell with NVFP4**
- **Up to 4.3x over state-of-the-art approaches**
- **LLaMA-3.1-8B with 128K context**: 3x reduction in single-batch decoding latency

## Key Contributions

1. **Tensor-Core-friendly layouts** for low-bit KV cache
2. **Warp-level dequantization parallelism**
3. **Query transformation + high-performance tensor/channel-wise quantization**
4. **Software-pipelined dequantization kernel** for mixed-precision execution
5. **Hopper/Blackwell architecture optimizations** (warpgroup tensor instructions, NVFP4)

## Source

https://arxiv.org/abs/2503.18773
