---
title: "KV Cache Quantization"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# KV Cache Quantization

KV cache quantization compresses the key-value cache that stores attention keys and values during autoregressive decoding. Critical for long-context scenarios where KV cache dominates memory.

## Key Methods

- [[kvquant]] — 3-bit KV cache, 10M context length (NeurIPS 2024)
- [[kivi]] — 2-bit KV cache, per-channel Key + per-token Value (ICML 2024)
- [[wkvquant]] — Joint weight + KV cache quantization (2024)
- [[hcattention]] — Extreme compression via heterogeneous attention (2025)
- [[kvmix]] — Gradient-based layer importance mixed-precision (2025)
- [[bitdecoding]] — Tensor core optimization for low-bit KV cache (2025)

## Key Insights

- Key and Value caches have different optimal quantization granularities
- Per-channel for Key, per-token for Value (KIVI)
- Pre-RoPE Key quantization improves accuracy (KVQuant)
- Long-context scenarios benefit most from KV cache compression
