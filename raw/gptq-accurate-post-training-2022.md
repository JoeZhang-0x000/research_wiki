---
title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
authors: ["Elias Frantar", "Saleh Ashkboos", "Torsten Hoefler", "Dan Alistarh"]
year: 2022
arxiv: "2210.17323"
url: "https://arxiv.org/abs/2210.17323"
venue: ICLR 2023
tags: [llm, quantization, post-training, weight-only, 4bit]
type: paper
status: draft
sources: []
links: []
---

## Paper Overview

GPTQ is a **one-shot weight quantization** method using approximate second-order information. It can quantize **175B parameter models** in ~4 GPU hours to 3-4 bits with negligible accuracy loss.

## Key Method

Uses **approximate second-order information** (Hessian-based) to select quantization parameters that minimize reconstruction error. This is a classic approach from the quantization literature adapted for LLMs.

## Key Results

- Quantize **175B model in ~4 GPU hours**
- Reduce to **3 or 4 bits per weight**
- Negligible accuracy degradation
- **2-bit and ternary** quantization also possible (with some accuracy loss)

## Speedup

- **3.25x** speedup on NVIDIA A100
- **4.5x** speedup on NVIDIA A6000 (cost-effective GPU)

## Historical Significance

GPTQ (2022) was one of the first practical methods for quantizing large models (100B+) to 4 bits. It enabled running 175B models on a single GPU for the first time. The method inspired many follow-ups and is still widely used as a baseline.

## Code

https://github.com/IST-DASLab/gptq
