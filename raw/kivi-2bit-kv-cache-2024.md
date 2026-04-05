---
title: "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache"
authors: ["Zirui Liu", "Jiayi Yuan", "Hongye Jin", "Shaochen Zhong", "Zhaozhuo Xu", "Vladimir Braverman", "Beidi Chen", "Xia Hu"]
year: 2024
arxiv: "2402.02750"
url: "https://arxiv.org/abs/2402.02750"
venue: ICML 2024
tags: [llm, quantization, kv-cache, 2bit]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

KIVI is a **tuning-free 2bit KV cache quantization** algorithm. Key finding: Key cache should be quantized per-channel, while Value cache should be quantized per-token.

## Key Analysis: KV Cache Distribution

The paper conducts a comprehensive study of element distribution in KV cache:
- **Key cache**: elements along channel dimension should be grouped together for quantization
- **Value cache**: elements along token dimension should be grouped together

## Key Methods

1. **Per-channel Key quantization**: Group elements along channel dimension
2. **Per-token Value quantization**: Group elements along token dimension
3. **Tuning-free**: No hyperparameters to tune for different models

## Key Results

- **2.6x less peak memory** (including model weights)
- **4x larger batch size** enabled
- **2.35x - 3.47x throughput improvement** on real LLM inference workloads
- Works for Llama, Falcon, and Mistral models

## Code

https://github.com/jy-yuan/KIVI
