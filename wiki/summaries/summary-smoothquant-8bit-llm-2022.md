---
title: "Summary — SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/smoothquant-8bit-llm-2022.md
links:
  - https://arxiv.org/abs/2211.10438
tags: [w8a8, post-training, weight-activation, icml-2023, mit-han-lab]
---

# Summary — SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, Song Han |
| Year         | 2022                           |
| Venue        | ICML 2023                      |
| Raw file     | `raw/smoothquant-8bit-llm-2022.md` |

## Main Idea

SmoothQuant enables **INT8 quantization of both weights and activations** (W8A8) for LLMs by migrating quantization difficulty from activations (hard to quantize due to outliers) to weights (easy to quantize) via a mathematically equivalent transformation.

## Core Insight

- Weights are easy to quantize (uniform distribution)
- Activations are hard (have outlier channels)
- Solution: smooth the activation outliers mathematically, pushing difficulty to weights

## Method

1. For each channel, compute a smoothing factor
2. Divide activation by smoothing factor (reduces outlier magnitude)
3. Multiply weight by same factor (maintains mathematical equivalence)
4. Quantize the smoothed activation and adjusted weights at INT8
5. Output remains unchanged

## Results / Evidence

- **1.56x speedup**, **2x memory reduction**
- Works on: OPT, BLOOM, GLM, MT-NLG, Llama-1/2, Falcon, Mistral, Mixtral
- Enables **530B model on single node**
- Negligible accuracy loss

## Code

https://github.com/mit-han-lab/smoothquant

## Historical Significance

One of the first works (2022) showing that LLM quantization beyond weights was practical. Many subsequent works build on the insight of migrating difficulty between weights and activations.

## Limitations

- 8-bit may not be aggressive enough for largest models
- Mathematical equivalence holds only for inference, not training

## Links to Concepts

- [[weight-activation-quantization]] — both quantized
- [[outlier-migration]] — core technique

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
