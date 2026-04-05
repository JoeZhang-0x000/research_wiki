---
title: "Summary — WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/wkvquant-weight-kv-cache-2024.md
links:
  - https://arxiv.org/abs/2402.12065
tags: [weight-only, kv-cache, post-training, quantization]
---

# Summary — WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Yuxuan Yue, Zhihang Yuan, Haojie Duanmu, Sifan Zhou, Jianlong Wu, Liqiang Nie |
| Year         | 2024                           |
| Venue        | arXiv (2402.12065)             |
| Raw file     | `raw/wkvquant-weight-kv-cache-2024.md` |

## Main Idea

WKVQuant is a PTQ framework for quantizing **both weights and KV cache**. Claims to be the first work exclusively targeting weight + KV cache together (not weight-activation or weight-only).

## Key Methods

1. **Past-only quantization**: improves attention by quantizing only past tokens' KV cache (not current token)
2. **Two-dimensional quantization strategy**: handles KV cache distribution more effectively than uniform approaches
3. **Cross-block reconstruction regularization**: optimizes quantization parameters across blocks

## Key Claims

- Memory savings comparable to weight-activation quantization
- Performance approaching weight-only quantization
- Balances efficiency and accuracy by targeting both weights and KV cache

## Context

Concurrent work with KIVI (early 2024) — both address KV cache quantization, but WKVQuant additionally includes weight quantization.

## Limitations

- [UNVERIFIED] Specific benchmark numbers
- [UNVERIFIED] Comparison fairness against KIVI

## Links to Concepts

- [[kv-cache]] — target of compression
- [[weight-only-quantization]] — weight quantization component

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
