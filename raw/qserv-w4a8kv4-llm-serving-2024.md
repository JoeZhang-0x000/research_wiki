---
title: "QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving"
authors: ["Yujun Lin", "Haotian Tang", "Shang Yang", "Zhekai Zhang", "Guangxuan Xiao", "Chuang Gan", "Song Han"]
year: 2024
arxiv: "2405.04532"
url: "https://arxiv.org/abs/2405.04532"
venue: arXiv
tags: [llm, quantization, serving, w4a8, kv-cache, system-co-design]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

QServe is a **W4A8KV4 quantization** system (4-bit weight, 8-bit activation, 4-bit KV cache) with system-algorithm co-design for efficient LLM serving. It targets **cloud-based, large-batch serving** — not just edge inference.

## The Problem

Existing INT4 quantization methods only accelerate **low-batch, edge LLM inference**. For cloud serving with large batches, dequantization overhead (20-90%) negates the gains from lower precision.

## Key Insight

LLM serving efficiency is critically influenced by operations on **low-throughput CUDA cores**. The dequantization step is the bottleneck.

## Key Contributions

### Algorithm: QoQ (Quattuor-Octo-Quattuor = 4-8-4)
1. **Progressive quantization**: Reduces dequantization overhead in W4A8 GEMM
2. **SmoothAttention**: Mitigates accuracy degradation from 4-bit KV quantization

### System: QServe
1. **Compute-aware weight reordering**: Reduces dequantization latency
2. **Register-level parallelism**: Exploits parallelism during dequantization
3. **Fused attention**: Makes attention memory-bound to harness KV4 quantization gains

## Results

- Llama-3-8B: **1.2x** throughput on A100, **1.4x** on L40S (vs TensorRT-LLM)
- Qwen1.5-72B: **2.4x** on A100, **3.5x** on L40S
- L40S + QServe > A100 + TensorRT-LLM in throughput
- **3x dollar cost reduction** for LLM serving

## Code

https://github.com/mit-han-lab/omniserve
