---
title: "WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More"
authors: ["Yuxuan Yue", "Zhihang Yuan", "Haojie Duanmu", "Sifan Zhou", "Jianlong Wu", "Liqiang Nie"]
year: 2024
arxiv: "2402.12065"
url: "https://arxiv.org/abs/2402.12065"
venue: arXiv
tags: [llm, quantization, kv-cache, weight-only]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

WKVQuant is a PTQ framework for quantizing both **weights and KV cache** of LLMs. Claims to be the first work to exclusively quantize weight and KV cache together.

## Key Methods

1. **Past-only quantization**: Improves attention computation by quantizing only past tokens' KV cache
2. **Two-dimensional quantization strategy**: Handles KV cache distribution more effectively
3. **Cross-block reconstruction regularization**: Optimizes quantization parameters across blocks

## Key Claims

- Achieves memory savings comparable to weight-activation quantization
- Approaches performance of weight-only quantization
- Balances efficiency and accuracy by targeting both weights and KV cache

## Context

This is a concurrent work to KIVI — both address KV cache quantization around the same time (early 2024). WKVQuant additionally includes weight quantization.

## Notes

The paper claims to be the "first work to exclusively quantize weight and Key/Value cache for large language models" — a similar claim to KIVI's per-channel/per-token asymmetry, though WKVQuant takes a different approach.
