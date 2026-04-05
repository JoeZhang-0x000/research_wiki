---
title: "Outlier Migration"
type: concept
status: draft
created: 2026-04-05
updated: 2026-04-05
sources: []
links: []
---

# Outlier Migration

Outlier migration is [[smoothquant]]'s key technique: mathematically transform activation outliers to weights before quantization, then reverse after. This migrates quantization difficulty from hard-to-quantize activations to easy-to-quantize weights.
