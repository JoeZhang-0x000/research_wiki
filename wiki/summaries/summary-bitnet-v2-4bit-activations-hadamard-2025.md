---
title: "Summary — BitNet v2: Native 4-bit Activations with Hadamard Transformation for 1-bit LLMs"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/bitnet-v2-4bit-activations-hadamard-2025.md
links:
  - https://arxiv.org/abs/2504.18415
tags: [1-bit-llm, bitnet, hadamard, activation-quantization, 4bit-activation]
---

# Summary — BitNet v2: Native 4-bit Activations with Hadamard Transformation for 1-bit LLMs

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Hongyu Wang, Shuming Ma, Furu Wei |
| Year         | 2025                           |
| Venue        | arXiv (2504.18415)             |
| Raw file     | `raw/bitnet-v2-4bit-activations-hadamard-2025.md` |

## Main Idea

BitNet v2 enables **native 4-bit activation quantization** for 1-bit LLMs (like BitNet b1.58) by applying an **online Hadamard transformation** that smooths activation distributions before quantization.

## Key Details

- BitNet b1.58 uses ternary weights (-1, 0, +1) but 8-bit activations
- Activation outliers prevent lower-bit quantization
- H-BitLinear: applies Hadamard transformation to smooth distributions
- Transforms sharp/outlier-heavy distributions to Gaussian-like

## Method / Approach

1. **H-BitLinear module**: online Hadamard transformation applied before activation quantization
2. Transformation is mathematically equivalent — output unchanged, but quantization-friendly
3. Can be trained from scratch with 4-bit activations

## Results / Evidence

- BitNet v2 (8-bit activations) matches BitNet b1.58 performance
- Native 4-bit activation training: minimal performance degradation
- Memory footprint and compute cost significantly reduced

## Limitations

- "Work in progress" — not peer-reviewed
- [UNVERIFIED] Actual speedup numbers
- Hadamard transformation adds computational overhead

## Links to Concepts

- [[1-bit-llm]] — BitNet b1.58 context
- [[hadamard-transformation]] — key technique
- [[activation-quantization]] — target

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
