---
title: "Neural Machine Translation with 4-Bit Precision and Beyond"
authors: ["Alham Fikri Aji", "Kenneth Heafield"]
year: 2019
arxiv: "1909.06091"
url: "https://arxiv.org/abs/1909.06091"
venue: arXiv/WMT
tags: [nmt, quantization, 4bit, transformer, rnn]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

Early work (2019) on quantizing NMT models to 4-bit precision. Uses **logarithmic quantization** for weights and an **error-feedback mechanism** during retraining to preserve compressed models.

## Key Methods

1. **Logarithmic quantization**: Better than fixed-point for parameters near zero (most neural network weights)
2. **Bias terms left uncompressed**: Found bias terms are not amenable to log quantization (but comprise tiny fraction of model)
3. **Error-feedback**: During retraining, stale gradients from compressed model are preserved

## Key Results

- Transformer and RNN NMT models can be compressed to **4-bit precision** without noticeable quality degradation
- Can compress to **binary precision** with lower quality
- RNN architecture more robust to quantization than Transformer

## Historical Context

This is a 2019 paper — predates the LLM era by several years. However, it establishes foundational ideas (log quantization, error feedback) that later appear in LLM quantization work. It is the oldest paper in this collection.

## Notes

While not an LLM paper per se, it provides early evidence that deep networks can survive aggressive quantization, which later proved true for LLMs.
