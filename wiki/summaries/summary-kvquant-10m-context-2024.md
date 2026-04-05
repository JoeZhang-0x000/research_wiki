---
title: "Summary — KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/kvquant-10m-context-2024.md
links:
  - https://arxiv.org/abs/2401.18079
tags: [kv-cache, long-context, 3bit, neurips-2024]
---

# Summary — KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Coleman Hooper, Sehoon Kim, Hiva Mohammadzadeh, Michael W. Mahoney, Yakun Sophia Shao, Kurt Keutzer, Amir Gholami |
| Year         | 2024                           |
| Venue        | NeurIPS 2024                   |
| Raw file     | `raw/kvquant-10m-context-2024.md` |

## Main Idea

KVQuant enables **10 million context length** LLM inference through aggressive KV cache quantization, achieving < 0.1 perplexity degradation with 3-bit KV cache via four novel techniques.

## Key Details

1. **Per-Channel Key Quantization**: quantize Key along channel dimension (not standard per-token)
2. **Pre-RoPE Key Quantization**: quantize Key before rotary positional embedding
3. **Non-Uniform KV Cache Quantization**: sensitivity-weighted per-layer datatypes
4. **Per-Vector Dense-and-Sparse**: isolate outliers per vector, minimize quantization range skew

## Results / Evidence

- **< 0.1 perplexity degradation** with 3-bit quantization on Wikitext-2 and C4
- LLaMA-7B with **1 million context** on single A100-80GB
- **10 million context** on 8-GPU system
- Up to **~1.7x speedup** via custom CUDA kernels

## Method / Approach

Four key innovations that address different aspects of KV cache quantization error, targeting the specific distribution characteristics of attention keys vs values.

## Limitations

- Hardware-specific CUDA kernels required
- Per-channel Key quantization may not generalize to all architectures [UNVERIFIED]

## Links to Concepts

- [[kv-cache]] — target of compression
- [[long-context]] — target use case

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
