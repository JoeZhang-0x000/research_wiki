---
title: "Summary — Compression Scaling Laws: Unifying Sparsity and Quantization"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/compression-scaling-laws-unifying-2025.md
links:
  - https://arxiv.org/abs/2502.16440
tags: [scaling-laws, quantization, sparsity, unified-theory]
---

# Summary — Compression Scaling Laws: Unifying Sparsity and Quantization

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Elias Frantar, Utku Evci, Wonpyo Park, Neil Houlsby, Dan Alistarh |
| Year         | 2025                           |
| Venue        | arXiv (2502.16440)             |
| Raw file     | `raw/compression-scaling-laws-unifying-2025.md` |

## Main Idea

This paper establishes a **unified scaling law framework** for compression methods (sparsity and quantization), showing they can be described by the same mathematical framework and compared systematically.

## Key Findings

1. **Weight sparsity** acts as a constant multiplier on model size in scaling laws (prior work)
2. **Weight-only quantization** achieves strong parameter efficiency multipliers
3. **Full quantization** (weights + activations) shows diminishing returns at lower bitwidths

## Theoretical Contribution

Different compression techniques can be compared under a common framework:
- Sparsity = constant multiplier on effective model size
- Quantization = similar but with diminishing returns at extremes
- Enables principled combination of methods

## Implications

- Predict effective model capacity at different compression ratios
- Guide selection between sparsity vs quantization for a given budget
- Systematic comparison of compression methods

## Limitations

- [UNVERIFIED] Specific mathematical form of the unified law
- [UNVERIFIED] Empirical validation across model sizes

## Links to Concepts

- [[scaling-laws]] — theoretical framing
- [[quantization]] — one of the compression methods studied

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
