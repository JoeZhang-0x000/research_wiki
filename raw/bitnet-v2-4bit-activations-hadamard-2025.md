---
title: "BitNet v2: Native 4-bit Activations with Hadamard Transformation for 1-bit LLMs"
authors: ["Hongyu Wang", "Shuming Ma", "Furu Wei"]
year: 2025
arxiv: "2504.18415"
url: "https://arxiv.org/abs/2504.18415"
venue: arXiv
tags: [llm, quantization, 1-bit, activation-quantization, hadamard]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

BitNet v2 enables **native 4-bit activation quantization** for 1-bit LLMs. The core challenge is **activation outliers** — extreme values that prevent low-bit representation.

## Key Innovation: H-BitLinear

The paper proposes **H-BitLinear**, a module that applies an **online Hadamard transformation** before activation quantization. This transforms sharp, outlier-heavy distributions into more Gaussian-like forms suitable for low-bit representation.

## Key Findings

- BitNet v2 trained from scratch with **8-bit activations** matches BitNet b1.58 performance
- When trained with **native 4-bit activations**, performance degradation is minimal
- Significantly reduces memory footprint and computational cost for batched inference

## Background

BitNet b1.58 uses ternary weights (-1, 0, +1) with 8-bit activations. The key limitation is that activation outliers make it difficult to quantize activations below 8 bits.

## Architecture

The Hadamard transformation is applied online (not pre-computed) to preserve the quantization-friendly distribution while maintaining the original model behavior.

## Notes

- "Work in progress" — published as arXiv paper, not yet peer-reviewed
