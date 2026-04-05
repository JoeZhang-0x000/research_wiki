---
title: "LLM Serving"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# LLM Serving

LLM serving refers to deploying quantized models for inference in production. Key challenge is batching efficiency and throughput optimization.

## Key Methods

- [[qserv]] — W4A8KV4 system: 3x dollar cost reduction (2024)
- [[atom]] — W4A4 serving: 7.7x throughput vs FP16 (2023)
- [[flexq]] — INT6 for serving via co-design (2025)

## Key Metrics

- **Throughput** (tokens/s) — primary for batch serving
- **Latency** (time to first token) — critical for interactive use
- **Memory utilization** — GPU VRAM efficiency
