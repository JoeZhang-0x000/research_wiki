# AGENTS.md — raw/

## Role

`raw/` is the **immutable source-of-truth**. Files here are primary inputs: papers, notes, transcripts, web captures.

---

## Rules

1. **Never edit an existing file.** Once added, it is frozen.
2. **Never delete files.** Even if superseded.
3. **Never add sidecar or metadata files here.** Ingestion state is tracked structurally — a file is "compiled" if any `wiki/summaries/` page lists it in `sources:`. No extra files needed.

---

## Allowed

- Adding new files (any format: `.md`, `.txt`, `.pdf`, `.html`)
- Creating subdirectories for organization (`raw/hpc/`, `raw/agents/`, etc.)

---

## Ingestion State

Detected automatically by `python skills/ingest.py`:

- **new** — no `wiki/summaries/` page has this file in its `sources:` field
- **compiled** — at least one summary page references it

No sidecar files. No registry. State is in the wiki itself.

---

## File Naming

Obsidian Clipper files land with their own names — leave them as-is.
For manually added files, use descriptive names:

| Example |
|---------|
| `paper_megatron-lm-2021.md` |
| `note_nvlink-bandwidth.md` |
| `talk_sc24-moe-routing.md` |
