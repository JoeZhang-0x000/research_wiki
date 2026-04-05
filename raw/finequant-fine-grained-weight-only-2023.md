---
title: "FineQuant: Unlocking Efficiency with Fine-Grained Weight-Only Quantization for LLMs"
authors: ["Young Jin Kim", "Rawn Henry", "Raffy Fahim", "Hany Hassan Awadalla"]
year: 2023
arxiv: "2308.09723"
url: "https://arxiv.org/abs/2308.09723"
venue: arXiv
tags: [llm, quantization, weight-only, fine-grained]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

FineQuant introduces a simple heuristic approach for **fine-grained weight-only quantization** that adapts the granularity of quantization per model. Applicable to both MoE and dense models without fine-tuning.

## Key Approach

1. **Analyze challenges** of LLM weight-only quantization
2. **Heuristic approach** to find optimal quantization granularity adaptively
3. **On-the-fly dequantization** in GPU GEMM operations

## Key Innovation: Fine-Grained Granularity

Unlike previous methods that use fixed quantization granularity (e.g., per-tensor or per-channel), FineQuant finds the optimal granularity **per model** using a heuristic approach.

## Key Results

- Tested on **OPT-175B** and internal MoE models
- **Up to 3.65x higher throughput** on the same number of GPUs
- Minimal accuracy loss
- Supports int8 and int4 weights with fp16/bf16 activations

## Notes

Authors are from Meta AI — similar research group that produced LLaMA models. Fine-tuning-free approach makes it practical for deployment.
