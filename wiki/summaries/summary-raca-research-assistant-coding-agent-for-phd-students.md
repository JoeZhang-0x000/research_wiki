---
title: "Summary — RACA: Research Assistant Coding Agent for Ph.D. Students"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/RACA Research Assistant Coding Agent for Ph.D. Students.md
links:
  - https://x.com/ZayneSprague/status/2041162383691800673
tags:
  - ai-agents
  - research
  - coding-agents
  - claude-code
---

# Summary — RACA: Research Assistant Coding Agent for Ph.D. Students

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog                           |
| Author(s)    | @ZayneSprague                 |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/RACA Research Assistant Coding Agent for Ph.D. Students.md` |

## Main Idea

RACA 是一个 Claude Code harness，帮助 PhD 学生把"设计实验 → 检查 → 运行 → 验证 → 回顾结果"的全流程串成在一个 Claude Code session 里完成。通过 SSH 连接 HPC/Slurm 集群，HuggingFace Spaces 做可视化，研究者只说话不写代码。核心洞察：AI agent 时代"知识重于代码"——与其写库，不如写 reference guide 让 LLM 按需读取。

## Key Details

**RACA 工作流**：设计 → sanity-check → 运行 → 验证 → 回顾结果

**核心组件**：
- Slurm 管理工具：Claude Code 通过 SSH 与集群交互
- 可视化网站：HuggingFace Spaces 托管
- Skills 和 rules：实验控制的 pipeline
- Red-teaming：实验设计后运行问题检查

**关键设计——Canary Job**：快速任务（<2小时）测试实验端到端，队列更快，失败迭代更快

**知识 > 代码的思维转变**：与其写库（共享代码、版本控制），不如写 reference guide（plain text 参考文档，LLM 按需读取）

## Results / Evidence

- 管理约 3x 更多并行研究线程
- Countdown 实验：从设计到可视化，一个下午完成

## Limitations

- Rules 是建议而非硬约束，Claude 不总是遵循
- Canary job 不 catch 所有 bug（如 reward hack）
- 研究没有完全自动化

## Links to Concepts

- [[agent-harness]] — RACA 是一个 Claude Code harness
- [[coding-agents]] — 用于 coding agent 场景

## Links to Topics

- [[ai-agents]] — AI agent 在科研场景的应用

## Quotes Worth Preserving

> "We aren't sharing code anymore with Claude Code. We are sharing intermediate representations of code in plain English that Claude Code, and any agent that comes after, will compile into actual code."

> "The fix is not more code. It's clear documentation, referenced when needed."

## Key Details

**RACA 工作流**：设计 → sanity-check → 运行 → 验证 → 回顾结果

**核心组件**：
- Slurm 管理工具：Claude Code 通过 SSH 与集群交互
- 可视化网站：HuggingFace Spaces 托管
- Skills 和 rules：实验控制的 pipeline
- Red-teaming：实验设计后运行问题检查

**关键设计——Canary Job**：快速任务（<2小时）测试实验端到端，队列更快，失败迭代更快

**知识 > 代码的思维转变**：与其写库（共享代码、版本控制），不如写 reference guide（plain text 参考文档，LLM 按需读取）

## Method / Approach

RACA 期望的结构：
- Workspace: `~/Research/` 包含所有项目、笔记、工具、仓库
- `notes/experiments/` 存放实验计划、时间线、artifact 注册表
- `.claude/rules/` 定义实验设计的 pipeline rules

**关键工具**：Superpowers（让 Claude 更主动问澄清问题）、Agent-Deck（编排多 session）

## Results / Evidence

- 管理约 3x 更多并行研究线程
- Countdown 实验：从设计到可视化，一个下午完成

## Limitations
What does the source acknowledge as limitations?
What limitations does the source NOT acknowledge but you observe?
-->

## Links to Concepts

- [[agent-harness]] — RACA 是一个 Claude Code harness
- [[coding-agents]] — 用于 coding agent 场景

## Links to Topics

- [[ai-agents]] — AI agent 在科研场景的应用

## Quotes Worth Preserving

> "We aren't sharing code anymore with Claude Code. We are sharing intermediate representations of code in plain English that Claude Code, and any agent that comes after, will compile into actual code."

> "The fix is not more code. It's clear documentation, referenced when needed."
