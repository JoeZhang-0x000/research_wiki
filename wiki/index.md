---
title: Knowledge Base Index
type: index
updated: 2026-04-04
---

# Research Wiki — Index

Knowledge base covering: **High-Performance Computing**, **AI Infrastructure**, **AI Agents**

---

## Topics

| Topic | Description | Status |
|-------|-------------|--------|
| [[gpu-memory-optimization]] | Techniques for reducing GPU memory usage and improving bandwidth utilization | draft |

---

## Concepts

This section collects the atomic knowledge units that topic and summary pages build on.

### AI Infra / HPC

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[flash-attention]] | IO-aware tiled attention that avoids materializing the N×N attention matrix | stable |
| [[hbm-bandwidth]] | GPU HBM data transfer rate — primary bottleneck for memory-bound kernels | draft |

### Candidate Future Pages

The following concepts are useful follow-up pages for expanding the wiki:

- `online-softmax` — linked from [[flash-attention]]
- `sparse-attention` — linked from [[flash-attention]]
- `collective-communication` — linked from [[gpu-memory-optimization]]
- `transformer-training-infrastructure` — linked from [[flash-attention]]
- `roofline-model` — linked from [[hbm-bandwidth]]

---

## Summaries

| Summary | Source | Topic |
|---------|--------|-------|
| [[summary-flashattention2]] | FlashAttention-2 paper (Dao, ICLR 2024) | [[gpu-memory-optimization]] |

---

## How to Navigate

- Start from a **topic** page for a broad overview of an area
- Drill into **concept** pages for precise definitions and mechanistic explanations
- Read **summary** pages for per-paper notes with results and limitations
- Use Obsidian's graph view to see link clusters

---

## Recently Updated

- 2024-01-15 — [[flash-attention]] created (stable)
- 2024-01-15 — [[hbm-bandwidth]] created (draft)
- 2024-01-15 — [[gpu-memory-optimization]] created (draft)
- 2024-01-15 — [[summary-flashattention2]] created (stable)
