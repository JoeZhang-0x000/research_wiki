---
title: "Summary — QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/qserv-w4a8kv4-llm-serving-2024.md
links:
  - https://arxiv.org/abs/2405.04532
tags: [quantization, w4a8, kv-cache, serving, system-co-design, mit-han-lab]
---

# Summary — QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Yujun Lin, Haotian Tang, Shang Yang, Zhekai Zhang, Guangxuan Xiao, Chuang Gan, Song Han |
| Year         | 2024                           |
| Venue        | arXiv (2405.04532)             |
| Raw file     | `raw/qserv-w4a8kv4-llm-serving-2024.md` |

## Main Idea

QServe is a **W4A8KV4 quantization** system (4-bit weight, 8-bit activation, 4-bit KV cache) with algorithm-system co-design for **cloud-based large-batch LLM serving**. Solves the dequantization overhead problem that plagues existing INT4 methods.

## The Problem

Existing INT4 quantization only accelerates **edge, low-batch** scenarios. For cloud serving (large batch), dequantization overhead is 20-90%, negating INT4 benefits.

## Key Insight

LLM serving efficiency is bottlenecked by low-throughput CUDA cores during dequantization.

## Key Methods

### QoQ Algorithm (Quattuor-Octo-Quattuor = 4-8-4):
1. **Progressive quantization**: reduces dequantization overhead in W4A8 GEMM
2. **SmoothAttention**: mitigates accuracy loss from 4-bit KV quantization

### QServe System:
1. **Compute-aware weight reordering**: reduces dequantization latency
2. **Register-level parallelism**: exploits parallelism during dequantization
3. **Fused attention**: makes attention memory-bound to leverage KV4 gains

## Results / Evidence

| Model | GPU | Speedup vs TensorRT-LLM |
|-------|-----|------------------------|
| Llama-3-8B | A100 | 1.2x |
| Llama-3-8B | L40S | 1.4x |
| Qwen1.5-72B | A100 | 2.4x |
| Qwen1.5-72B | L40S | 3.5x |

- L40S + QServe > A100 + TensorRT-LLM in throughput
- **3x dollar cost reduction** for LLM serving

## Code

https://github.com/mit-han-lab/omniserve

## Limitations

- Requires custom kernels (not universally available)
- [UNVERIFIED] Accuracy degradation numbers

## Links to Concepts

- [[quantization]] — core methodology
- [[llm-serving]] — target use case

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
