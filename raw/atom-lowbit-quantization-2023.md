---
title: "Atom: Low-bit Quantization for Efficient and Accurate LLM Serving"
authors: ["Yilong Zhao", "Chien-Yu Lin", "Kan Zhu", "Zihao Ye", "Lequn Chen", "Size Zheng", "Luis Ceze", "Arvind Krishnamurthy", "Tianqi Chen", "Baris Kasikci"]
year: 2024
arxiv: "2310.19102"
url: "https://arxiv.org/abs/2310.19102"
venue: arXiv
tags: [llm, quantization, low-bit, serving, w4a4]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

Atom enables **W4A4 quantization** (4-bit weight, 4-bit activation) for LLM serving, achieving up to **7.7x throughput improvement** over FP16 and 2.5x over INT8.

## The Problem

Existing INT8 quantization can't fully leverage modern GPU capabilities (4-bit integer operators). Result: sub-optimal hardware utilization.

## Key Approach

1. **Novel mixed-precision quantization**: Different precision for different layers/channels based on sensitivity
2. **Fine-grained quantization**: Granularity at sub-channel level
3. **Low-bit operators**: Fully exploit GPU 4-bit integer support

## Key Results

- **7.7x throughput improvement** vs FP16
- **2.5x throughput improvement** vs INT8
- Same latency target, negligible accuracy loss
- Significant memory reduction from low-bit quantization

## Notes

Atom targets the serving scenario where batching is used — different from training-time or offline compression. The throughput numbers are end-to-end token/s improvements.
