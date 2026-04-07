---
title: "Thread by xiao_zcloak — Agent Trust Protocol ATP zCloak"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Thread by @xiao_zcloak.md
links:
  - https://x.com/xiao_zcloak/status/2041030845910421917
tags: [ai-agents, security, agent-trust-protocol]
---

# Summary — Thread by xiao_zcloak — Agent Trust Protocol ATP zCloak

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | note                           |
| Author(s)    | xiao_zcloak (via zCloak.AI)   |
| Year         | 2026                           |
| Venue        | x.com thread                   |
| Raw file     | `raw/Thread by @xiao_zcloak.md` |

## Main Idea

Google DeepMind's report (502 participants, 23 attack methods, GPT-4o/Claude/Gemini tested) found that hidden instructions in web pages succeed against AI agents 86% of the time. The core vulnerability: LLMs cannot distinguish user instructions from web content once both are in the context window. zCloak's proposed solution is ATP (Agent Trust Protocol) — HTTPS-equivalent for AI agents, adding cryptographic identity (BIP-340 Schnorr signatures), signed messaging, and tamper-evident memory ledgers.

## Key Details

- **Prompt injection success rate**: 86% when instructions are hidden in web pages (invisible to humans, visible to agents). No malware, no password cracking — just HTML with white-on-white text.
- **Attack propagation in multi-agent chains**: Agent A fetches data, Agent B processes, Agent C acts — a single poisoned source propagates without suspicion through the entire chain. No agent questions another's data.
- **Persistence**: DeepMind found that just 0.1% (1 in 1000) polluted documents can permanently rewrite an agent's knowledge base with 80%+ probability.
- **Why filtering doesn't work**: Attackers hide instructions in image pixels, PDF metadata, calendar invites. Each mitigation creates a new hiding spot. The fundamental problem is that LLMs treat all text in context equally — there is no notion of "principal" or "source of instructions."
- **OpenAI's own admission**: Prompt injection likely cannot be fully solved at the model level (December 2025 statement).
- **ATP's three-layer solution**:
  1. **Identity layer**: Every agent has a BIP-340 Schnorr signature AI-ID. Agent B can verify a message actually came from Agent A, not an impersonator.
  2. **Message layer**: Agents communicate via zMail — every message signed and verifiable, like an HTTPS channel for agent-to-agent communication.
  3. **Memory/Action layer**: Every memory entry carries a signature and timestamp, stored in an immutable ledger. Actions (API calls, data transfers) require the agent's own AI-ID signature and are checked against user-defined permission policies in a Trust Portal.
- **Verification cost**: Near-zero. Signature verification is computationally cheap compared to LLM inference — agents can verify hundreds of signed messages for the cost of reading one tweet.
- **When signature verification applies**: (1) At ingestion — data entering context window is verified for signature and content integrity; (2) Before execution — any consequential action (sending data, API calls) requires signing and permission check; (3) Between agents — every cross-agent message is signed.
- **HTTPS analogy**: HTTPS didn't make websites honest — it let your browser verify identity. ATP doesn't make the information environment safe — it lets agents distinguish signed/verified information from unsigned/unverified, and act accordingly.
- **zCloak's ATP repo**: github.com/zCloak-Network/ATP

## Method / Approach (if applicable)

Analytical framing: draws parallel between current agent security and pre-HTTPS internet. Argues that like HTTPS adoption (forced by browsers marking HTTP as "insecure"), agent platform adoption of ATP will require either regulatory/platform pressure, user demand, or a major incident (e.g., a 2010 Flash Crash-scale event caused by agent poisoning).

## Results / Evidence

- Google DeepMind report: 502 participants, 23 attack types, 86% prompt injection success rate [UNVERIFIED — from tweet, not the original report]
- DeepMind scenario: 1,000 AI trading agents simultaneously reading the same fabricated financial report — each independently concludes the same wrong thing, with no capacity to question the source.
- Memory pollution: 0.1% polluted data → 80%+ probability of permanent knowledge base corruption [UNVERIFIED]

## Limitations

- ATP is a proposed protocol from zCloak — not deployed, not battle-tested.
- The Google DeepMind report statistics (86%, 0.1%/80%) are cited from a tweet summarizing the report, not from the original paper.
- No implementation details, benchmarks, or adversarial evaluation of ATP itself.
- zCloak is a company promoting this protocol — conflict of interest not addressed.
- The HTTPS analogy may be imperfect: HTTPS secures a channel between two endpoints; ATP needs to secure an information environment with multiple principals, memories, and actions.

## Links to Concepts

- [[agent-harness]] — ATP is a security layer within the agent harness; it addresses the trust problem in harness design
- [[sandbox-isolation]] — ATP addresses a complementary threat model: even isolated agents can be manipulated via prompt injection

## Links to Topics

- [[ai-agents]] — primary topic

## Quotes Worth Preserving

> 在网页里多写几行白色的字，人眼看不见，你的 AI 助手看见了，还当圣旨。86% 的概率乖乖照做。

> 大语言模型的脑子里，压根分不清谁跟它说话。用户给它的指令，恶意网页里藏的文字，进了上下文窗口之后享受同等待遇。

> HTTPS 是一把锁。ATP 是一把锁加一本护照加一本账本。锁管通道安全，护照管你是谁，账本管你干了什么。

> 攻击者不需要攻破模型。他只需要污染模型吃进去的数据。脑子可能很聪明，但眼睛是瞎的。
