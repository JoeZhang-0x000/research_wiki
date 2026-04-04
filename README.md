# research_wiki

An LLM-native knowledge compilation system for AI research.

Covers: **High-Performance Computing**, **AI Infrastructure**, **AI Agents**

---

## How It Works

```
raw/  →  /digest  →  wiki/  →  /query (inline answer)
                       ↑              ↓ (if gaps found, user approves)
                    /distill   /analyze (first-principles report)
```

- **`raw/`** — source materials (tracked in git)
- **`wiki/`** — compiled, structured knowledge (tracked in git)
- **`output/`** — ephemeral scratch space, gitignored

---

## Directory Structure

```
raw/          Source materials — append-only, fully tracked
wiki/
  concepts/   Atomic concept pages
  topics/     Broad topic overview pages
  summaries/  Per-paper / per-source summary pages
  index.md    Master navigation index
output/       Ephemeral scratch (gitignored)
agent/        Pipeline scripts
skills/       Reusable skill scripts
schemas/      Page templates (concept / topic / summary)
.claude/commands/  Claude Code slash commands
```

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/digest` | Detect new files in `raw/`, compile into wiki, lint, commit, push |
| `/query <question>` | Answer inline from wiki — no output file generated |
| `/analyze <topic>` | Five-pass first-principles analysis → writes to `output/` |
| `/distill [topic]` | Scan wiki for gaps (broken links, stubs), fill them — user approves before commit |
| `/lint` | Run linter, surface and fix issues |
| `/ingest <file>` | Manually ingest a single file |
| `/add-skill <name>` | Add a new skill to `skills/` |

---

## Typical Workflow

```bash
# Drop source files into raw/
cp ~/Downloads/paper_xyz.pdf raw/

# Compile into wiki (one command)
# /digest

# Ask a question
# /query how does X work?

# Deep analysis
# /analyze X

# Fill wiki gaps
# /distill
```

After `/digest` or `/distill`, changes are committed and pushed automatically (with user approval).

---

## Pipeline Scripts (low-level)

```bash
python agent/ingest.py           # scan raw/, report status
python agent/compile.py          # check what needs compiling
python agent/query.py "term"     # keyword search across wiki/
python agent/distill.py          # surface gaps from lint output
python agent/lint.py             # check orphans, broken links, missing frontmatter
```

---

## Skills

Reusable scripts in `skills/`. See `skills/README.md`.

Add via `/add-skill <name> <description>`.

---

## Opening in Obsidian

Open repo root as a vault. All `[[links]]` are Obsidian-compatible.
Recommended plugins: Dataview, Obsidian Git.

---

## Notes

- `output/` is gitignored — analysis reports and query scratch are local only
- All wiki pages have YAML frontmatter with a `links:` field for original URLs (Obsidian Clipper)
- Agent rules: `AGENTS.md` (root / raw/ / wiki/) and `CLAUDE.md`
