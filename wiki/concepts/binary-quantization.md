---
title: "Binary Quantization"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# Binary Quantization

Binary quantization reduces weights to 1-bit (binary: {0,1} or {-1,+1}). The most aggressive form of quantization, trading significant accuracy for extreme compression.

## Key Methods

- [[stbllm]] — Structured binary with N:M sparsity (2024)
- [[summary-binary-weight-activation-llm-ptq-2025]] — Binary weights AND activations (2025)

## Note

Binary is often combined with structured sparsity (N:M) to improve accuracy while maintaining extreme compression.
