---
title: "1-bit AI Infra: Part 1.1, Fast and Lossless BitNet b1.58 Inference on CPUs"
authors: ["Jinheng Wang", "Hansong Zhou", "Ting Song", "Shaoguang Mao", "Shuming Ma", "Hongyu Wang", "Yan Xia", "Furu Wei"]
year: 2024
arxiv: "2410.16144"
url: "https://arxiv.org/abs/2410.16144"
venue: arXiv
tags: [llm, quantization, 1-bit, bitnet, cpu-inference]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

This paper introduces **bitnet.cpp**, a tailored software stack for fast, lossless inference of ternary BitNet b1.58 LLMs on CPUs. It enables 1-bit LLM deployment across a broad range of devices.

## BitNet b1.58 Background

BitNet b1.58 uses ternary weights (-1, 0, +1) with 8-bit activations, representing a significant step toward 1-bit model inference.

## Key Contributions: bitnet.cpp

A set of optimized CPU kernels specifically designed for 1-bit LLM inference:

### Performance Results

| Platform | Speedup Range |
|----------|---------------|
| x86 CPUs | **2.37x - 6.17x** |
| ARM CPUs | **1.37x - 5.07x** |

Across various model sizes.

## Implications

- Enables local LLM deployment on consumer CPUs
- Significant energy efficiency gains (1-bit = fewer arithmetic operations)
- Makes 1-bit models practical beyond specialized hardware

## Code

https://github.com/microsoft/BitNet
