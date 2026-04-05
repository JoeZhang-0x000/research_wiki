---
title: "LLM Quantization"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# LLM Quantization

LLM quantization reduces the precision of model weights, activations, and KV cache to decrease memory footprint and accelerate inference. Methods range from 8-bit (near-lossless) to 1-bit (aggressive compression).

## Categories

- [[weight-only-quantization]] — quantize weights only, activations stay fp16
- [[weight-activation-quantization]] — quantize both weights and activations
- [[kv-cache-quantization]] — quantize the key-value cache for long-context
- [[binary-quantization]] — extreme 1-2 bit quantization

## Precision Levels

| Precision | Typical Use Case | Accuracy Impact |
|-----------|-----------------|----------------|
| INT8 | Near-lossless, widely deployed | Minimal |
| INT4 | Moderate compression, good accuracy | Low |
| INT2-3 | Aggressive, emerging | Moderate |
| 1-bit (binary/ternary) | Extreme compression, research | Significant |

## Key Methods

- [[gptq]] — Hessian-based weight-only quantization (2022, ICLR 2023)
- [[smoothquant]] — W8A8 via outlier migration (2022, ICML 2023)
- [[kvquant]] — 3-bit KV cache, 10M context (NeurIPS 2024)
- [[kivi]] — 2-bit KV cache, per-channel/per-token asymmetry (ICML 2024)
- [[qserv]] — W4A8KV4 system co-design for serving (2024)
- [[bitnet]] — 1-bit weights, ternary (-1, 0, +1)

## Related Concepts

- [[scaling-laws]] — Compression scaling laws unify sparsity and quantization
- [[mixed-precision-quantization]] — Different precision per layer/channel
- [[outlier-migration]] — SmoothQuant's key technique
