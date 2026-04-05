---
title: "Summary — HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/hcattention-extreme-kv-cache-compression-2025.md
links:
  - https://arxiv.org/abs/2507.19823
tags: [kv-cache, attention, compression, extreme, heterogeneous]
---

# Summary — HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Yifan Yang, Xianbiao Qi, Rong Xiao, Xiaotian Yu, Dongquan Yang |
| Year         | 2025                           |
| Venue        | arXiv (2507.19823)             |
| Raw file     | `raw/hcattention-extreme-kv-cache-compression-2025.md` |

## Main Idea

HCAttention applies **extreme compression** to the KV cache by using heterogeneous computing — different precision/compression for different parts of the attention computation based on their sensitivity.

## Key Details

- "Extreme" suggests very aggressive compression (possibly < 2-bit)
- Heterogeneous: mix of compression strategies
- Different attention heads or layers get different treatments
- [UNVERIFIED] Specific mechanism for determining heterogeneity

## Method / Approach

[UNVERIFIED] Technical approach. Likely analyzes per-head/per-layer sensitivity and allocates compression budget accordingly.

## Results / Evidence

- [UNVERIFIED] Compression ratio achieved
- [UNVERIFIED] Quality retention on benchmarks

## Limitations

- Extreme compression likely sacrifices more accuracy
- [UNVERIFIED] Applicability to diverse model architectures

## Links to Concepts

- [[kv-cache]] — target compression
- [[mixed-precision-quantization]] — related methodology

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
