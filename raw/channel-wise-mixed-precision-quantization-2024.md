---
title: "Channel-Wise Mixed-Precision Quantization for Large Language Models"
authors: ["Zihan Chen", "Bike Xie", "Jundong Li", "Cong Shen"]
year: 2024
arxiv: "2410.13056"
url: "https://arxiv.org/abs/2410.13056"
venue: arXiv
tags: [llm, quantization, weight-only, mixed-precision, channel-wise]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

CMPQ (Channel-Wise Mixed-Precision Quantization) allocates quantization precision per weight channel based on activation distributions. It adapts to any bit-width constraint, including fractional bits.

## The Problem

Existing weight-only quantization methods focus on **integer-bit quantization**, limiting adaptability to fractional-bit scenarios and preventing full utilization of available storage on edge devices.

## Key Methods

1. **Channel-wise precision allocation**: Different precision for different weight channels
2. **Non-uniform quantization**: Adapts to the actual weight distribution
3. **Two outlier extraction techniques**: Preserve critical information by separating outliers from quantized values

## Key Findings

- Works for both **integer-bit** and **fractional-bit** quantization
- Enhances performance in integer-bit tasks
- Achieves significant gains with **modest memory overhead**
- Adaptive to diverse device capabilities

## Approach

The method assigns precision levels based on activation distributions, identifying which channels need higher precision to preserve model performance.
