---
title: "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"
authors: ["Guangxuan Xiao", "Ji Lin", "Mickael Seznec", "Hao Wu", "Julien Demouth", "Song Han"]
year: 2022
arxiv: "2211.10438"
url: "https://arxiv.org/abs/2211.10438"
venue: ICML 2023
tags: [llm, quantization, post-training, w8a8, weight-activation]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

SmoothQuant enables **INT8 quantization of both weights and activations** (W8A8) for LLMs without accuracy loss. It migrates quantization difficulty from activations (hard to quantize) to weights (easy to quantize) via a mathematically equivalent transformation.

## Core Insight

- Weights are **easy to quantize** (relatively uniform distribution)
- Activations are **hard to quantize** (have outlier values in specific channels)

Solution: **Smooth** the activation outliers by migrating difficulty to weights.

## Method: SmoothQuant

Mathematically equivalent transformation that:
1. Divides activation by a per-channel smoothing factor
2. Multiplies weight by the same factor
3. The quantization difficulty migrates from activations to weights
4. The output remains mathematically identical

## Key Results

- **1.56x speedup** and **2x memory reduction** for LLMs
- Works on: OPT, BLOOM, GLM, MT-NLG, Llama-1/2, Falcon, Mistral, Mixtral
- Enables serving **530B LLM within a single node**
- Negligible loss in accuracy

## Code

https://github.com/mit-han-lab/smoothquant

## Historical Significance

SmoothQuant (2022) was one of the first major works showing that LLM quantization beyond just weights was practical. Many subsequent works (QServe, etc.) build on this insight.
