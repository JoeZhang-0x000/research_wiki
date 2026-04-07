---
title: "Summary — Feynman: Open Source AI Research Agent"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Thread by @aigleeson.md
links:
  - https://x.com/aigleeson/status/2041073339616387468
tags:
  - ai-agents
  - research
  - multi-agent
---

# Summary — Feynman: Open Source AI Research Agent

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog/tweet thread              |
| Author(s)    | @aigleeson                    |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/Thread by @aigleeson.md` |

## Main Idea

Feynman 是一个开源 AI 研究 agent，多 agent 系统。输入一个主题，搜索论文、综合发现、验证每个声明、输出一份有引用的研究简报。MIT 协议。

## Key Details

**四个 Agent**：
- Researcher：从论文、仓库、文档和网页提取证据
- Reviewer：运行模拟同行评审，带 severity 分级反馈
- Writer：从研究笔记起草论文风格输出
- Verifier：检查每个引用，杀死死链接

**额外能力**：本地/云 GPU 复现实验、论文 vs codebase 审计、周期性研究监控

**争议**：Ian Smith 指出 `curl -fsSL https://feynman.is/install | bash` 不是真正的开源

## Limitations

产品介绍 thread，信息有限。安装方式有安全争议。无独立验证。

## Links to Topics

- [[ai-agents]] — AI 研究 agent

## Quotes Worth Preserving

> "autonomous + verified is the solved half. the unsolved half is compound learning - making run 10 sharper than run 1 by carrying keywords forward."
