---
title: "Summary — BitDecoding: Unlocking Tensor Cores for Long-Context LLMs Decoding with Low-Bit KV Cache"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/bitdecoding-tensor-cores-long-context-2025.md
links:
  - https://arxiv.org/abs/2503.18773
tags: [kv-cache, long-context, tensor-cores, decoding, quantization]
---

# Summary — BitDecoding: Unlocking Tensor Cores for Long-Context LLMs Decoding with Low-Bit KV Cache

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Dayou Du, Mao Yang, Ting Cao, Shijie Cao, Luo Mai, Jianyi Cheng |
| Year         | 2025                           |
| Venue        | arXiv (2503.18773)             |
| Raw file     | `raw/bitdecoding-tensor-cores-long-context-2025.md` |

## Main Idea

BitDecoding enables efficient **long-context LLM decoding** with low-bit KV cache by designing GPU kernels that unlock tensor core acceleration for dequantized low-bit operations during the decoding phase.

## Key Details

- Low-bit KV cache causes dequantization overhead that bottlenecks tensor cores
- BitDecoding redesigns the decoding kernel to overlap dequantization with tensor core compute
- Targets long-context scenarios where KV cache memory is the dominant bottleneck
- Custom CUDA kernels for low-bit KV cache operations

## Method / Approach

1. Analyze tensor core behavior with low-bit KV cache
2. Design kernels that perform dequantization "just-in-time" within tensor core pipelines
3. Overlap memory operations with compute to hide latency
4. Optimize for autoregressive decoding pattern (逐token生成)

## Results / Evidence

- [UNVERIFIED] Speedup numbers vs baseline fp16 decoding
- [UNVERIFIED] Context length range tested

## Limitations

- [UNVERIFIED] Accuracy impact of aggressive KV cache quantization
- Hardware-specific (tensor core architecture dependent)

## Links to Concepts

- [[kv-cache]] — core compression target
- [[long-context]] — target use case

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
