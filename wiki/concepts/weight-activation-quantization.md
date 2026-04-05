---
title: "Weight-Activation Quantization"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# Weight-Activation Quantization

Weight-activation quantization reduces precision of both weights AND activations, enabling the most aggressive compression. Requires careful handling of activation outliers.

## Key Methods

- [[smoothquant]] — W8A8 via outlier migration (ICML 2023)
- [[atom]] — W4A4 for serving (2023)

## The Outlier Problem

Activation tensors in LLMs have extreme outliers in specific channels, making uniform quantization ineffective. [[smoothquant]] solves this by migrating difficulty from activations to weights.
