---
title: "Summary — GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/gptq-accurate-post-training-2022.md
links:
  - https://arxiv.org/abs/2210.17323
tags: [weight-only, post-training, hessian, 4bit, iclr-2023]
---

# Summary — GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh |
| Year         | 2022                           |
| Venue        | ICLR 2023                      |
| Raw file     | `raw/gptq-accurate-post-training-2022.md` |

## Main Idea

GPTQ is a **one-shot weight quantization** method using approximate second-order information (Hessian-based) that can quantize **175B parameter models in ~4 GPU hours** to 3-4 bits with negligible accuracy loss.

## Key Method

Uses **approximate second-order information** to select quantization parameters that minimize reconstruction error:
1. Compute approximate Hessian of the loss with respect to weights
2. Select quantization levels that minimize weighted reconstruction error
3. Process weights in groups for efficiency

## Results / Evidence

- **175B model in ~4 GPU hours** to 3-4 bits
- Negligible accuracy degradation vs uncompressed baseline
- 2-bit and ternary quantization also possible (with more accuracy loss)
- **3.25x speedup** on NVIDIA A100
- **4.5x speedup** on NVIDIA A6000

## Historical Significance

One of the first practical methods for quantizing large models (100B+) to 4 bits. First to enable 175B models on a single GPU. Still widely used as baseline.

## Code

https://github.com/IST-DASLab/gptq

## Limitations

- Weight-only (activations still in fp16)
- 2-bit accuracy degradation is significant

## Links to Concepts

- [[weight-only-quantization]] — core methodology
- [[hessian-based-quantization]] — second-order approach

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
