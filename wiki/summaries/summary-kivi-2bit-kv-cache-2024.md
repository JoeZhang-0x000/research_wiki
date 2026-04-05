---
title: "Summary — KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/kivi-2bit-kv-cache-2024.md
links:
  - https://arxiv.org/abs/2402.02750
tags: [kv-cache, 2bit, per-channel, per-token, icml-2024]
---

# Summary — KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, Xia Hu |
| Year         | 2024                           |
| Venue        | ICML 2024                      |
| Raw file     | `raw/kivi-2bit-kv-cache-2024.md` |

## Main Idea

KIVI is a **tuning-free 2-bit KV cache quantization** algorithm based on a key insight: **Key cache should be quantized per-channel** (group along channel dimension), while **Value cache should be quantized per-token** (group along token dimension).

## Key Analysis: KV Cache Distribution

The paper studies element distribution in KV cache:
- **Key cache**: channel dimension grouping is better (per-channel)
- **Value cache**: token dimension grouping is better (per-token)

This asymmetry is because Key and Value have different statistical properties in attention.

## Key Methods

1. **Per-channel Key quantization**: groups elements along channel dimension
2. **Per-token Value quantization**: groups elements along token dimension
3. **Tuning-free**: no hyperparameters to tune per model

## Results / Evidence

- **2.6x less peak memory** (including model weights)
- **4x larger batch size** enabled
- **2.35x - 3.47x throughput improvement** on real LLM inference workloads
- Works for Llama, Falcon, and Mistral

## Code

https://github.com/jy-yuan/KIVI

## Limitations

- 2-bit may not be optimal for all models
- [UNVERIFIED] Perplexity impact numbers

## Links to Concepts

- [[kv-cache]] — target of compression
- [[asymmetric-quantization]] — Key vs Value treated differently

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
