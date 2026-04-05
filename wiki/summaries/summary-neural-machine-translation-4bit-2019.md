---
title: "Summary — Neural Machine Translation with 4-Bit Precision and Beyond"
type: summary
status: draft
created: 2026-04-05
updated: 2026-04-05
sources:
  - raw/neural-machine-translation-4bit-2019.md
links:
  - https://arxiv.org/abs/1909.06091
tags: [nmt, 4bit, transformer, rnn, log-quantization, error-feedback]
---

# Summary — Neural Machine Translation with 4-Bit Precision and Beyond

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Alham Fikri Aji, Kenneth Heafield |
| Year         | 2019                           |
| Venue        | arXiv/WMT                      |
| Raw file     | `raw/neural-machine-translation-4bit-2019.md` |

## Main Idea

Early work (2019) on quantizing NMT models to 4-bit using **logarithmic quantization** and **error-feedback** during retraining. Found RNNs more robust to quantization than Transformers.

## Key Methods

1. **Logarithmic quantization**: better than fixed-point for near-zero parameters (most weights)
2. **Bias terms left uncompressed**: not amenable to log quantization (tiny fraction of model)
3. **Error-feedback**: stale gradients from compressed model preserved during retraining

## Results / Evidence

- Transformer and RNN NMT models: **4-bit without noticeable quality degradation**
- Can compress to **binary precision** with lower quality
- **RNN more robust** to quantization than Transformer

## Historical Context

2019 predates LLM era — foundational work establishing that deep networks survive aggressive quantization. Many ideas (log quantization, error feedback) reappear in later LLM quantization work.

## Limitations

- NMT, not LLM (but ideas transfer)
- Pre-LLM scale models
- [UNVERIFIED] Specific benchmark numbers

## Links to Concepts

- [[log-quantization]] — key technique
- [[error-feedback]] — training mechanism

## Links to Topics

- [[llm-quantization]]

## Quotes Worth Preserving

None yet — abstract-level information only.
