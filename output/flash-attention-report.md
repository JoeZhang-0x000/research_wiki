# Query Report: flash attention

**Query**: `flash attention`  
**Generated**: 2026-04-04 14:01  
**Pages searched**: 4  
**Pages with matches**: 4

---

## Results (4 pages)

### [[flash-attention]]

**File**: `wiki/concepts/flash-attention.md`  
**Type**: concept  **Status**: stable

**Matching lines** (11 hits):

- Line 2: `title: Flash Attention`
- Line 8: `- raw/paper_flashattention2-2023.md`
- Line 13: `# Flash Attention`
- Line 17: `Flash Attention is a family of IO-aware exact attention algorithms that compute the standard scaled dot-product attentio`
- Line 21: `Transformer self-attention has O(N²) memory and compute complexity with respect to sequence length. For long sequences, `
- Line 25: `Flash Attention splits Q, K, and V into tiles that fit in SRAM. For each tile:`
- Line 33: `**FlashAttention-2 improvements** over v1:`
- Line 44: `- **Throughput (A100)**: FlashAttention-2 achieves ~73% of A100 theoretical FLOP/s on forward pass; naive PyTorch reache`
- Line 58: `- [[summary-flashattention2]] — primary source`
- Line 59: `- `raw/paper_flashattention2-2023.md` — full extracted notes`
- ... and 1 more matches

### [[summary-flashattention2]]

**File**: `wiki/summaries/summary-flashattention2.md`  
**Type**: summary  **Status**: stable

**Matching lines** (8 hits):

- Line 2: `title: Summary — FlashAttention-2 (Dao, 2023)`
- Line 8: `- raw/paper_flashattention2-2023.md`
- Line 13: `# Summary — FlashAttention-2 (Dao, 2023)`
- Line 23: `| Raw file    | `raw/paper_flashattention2-2023.md`                |`
- Line 27: `FlashAttention-2 achieves ~2× speedup over FlashAttention-1 by reducing non-matmul FLOPs and improving parallelism acros`
- Line 41: `The kernel is a fused CUDA/Triton implementation. Key algorithmic move: instead of storing the softmax denominator per r`
- Line 60: `- [[flash-attention]] — this paper is the primary source for the concept page`
- Line 61: `- [[hbm-bandwidth]] — the IO-bound analysis underpins why FlashAttention works`

### [[gpu-memory-optimization]]

**File**: `wiki/topics/gpu-memory-optimization.md`  
**Type**: topic  **Status**: draft

**Matching lines** (7 hits):

- Line 8: `- raw/paper_flashattention2-2023.md`
- Line 33: `Avoid writing intermediate tensors to HBM by computing within SRAM tiles. The canonical example is [[flash-attention]], `
- Line 42: `At inference, techniques like grouped-query attention (GQA) and multi-query attention (MQA) reduce the KV cache size by `
- Line 51: `| FlashAttention      | 2022 | IO-aware tiled attention, O(N) memory        |`
- Line 52: `| FlashAttention-2    | 2023 | 2× speedup, better parallelism               |`
- Line 53: `| FlashAttention-3    | 2024 | Hopper async pipeline support [UNVERIFIED]   |`
- Line 60: `- Dao et al. (2022) — "FlashAttention" — [[summary-flashattention2]] — foundational IO-aware attention`

### [[hbm-bandwidth]]

**File**: `wiki/concepts/hbm-bandwidth.md`  
**Type**: concept  **Status**: draft

**Matching lines** (5 hits):

- Line 8: `- raw/paper_flashattention2-2023.md`
- Line 20: `Many deep learning operations — including attention, layer normalization, and elementwise ops — are memory-bound: they s`
- Line 27: `- SRAM (shared memory / L2 cache) bandwidth is ~10-20× higher than HBM bandwidth, which is the motivation for tiling tec`
- Line 31: `- Used in: [[flash-attention]], [[gpu-memory-optimization]]`
- Line 36: `- `raw/paper_flashattention2-2023.md` — IO-bound analysis section`

---

## Distillation Prompt

After reviewing these results, if new reusable knowledge was found, run:
```bash
python agent/distill.py output/<this-report-filename>
```
to extract insights back into wiki/.