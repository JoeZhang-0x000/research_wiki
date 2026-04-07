---
title: Agent Trust Protocol
type: concept
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Thread by @xiao_zcloak.md
links:
  - https://x.com/xiao_zcloak/status/2041030845910421917
  - https://github.com/zCloak-Network/ATP
tags: [ai-agents, security, protocol, cryptographic-identity]
---

# Agent Trust Protocol (ATP)

## Definition

Agent Trust Protocol (ATP) is a proposed cryptographic trust infrastructure for AI agents — analogous to HTTPS for the web — that adds identity verification, message signing, and tamper-evident memory ledgers so agents can distinguish legitimate instructions from injected malicious content.

## Why It Matters

Current agents treat all text in their context window equally — user instructions and web content carry the same weight. This allows prompt injection attacks (86% success rate per DeepMind report) to redirect agent behavior. ATP solves this not by making models smarter, but by making the information environment accountable: every piece of data, message, and memory carries a cryptographic proof of origin.

## How It Works

ATP operates at four layers:

1. **Identity layer**: Every agent has a BIP-340 Schnorr signature AI-ID — a cryptographic identity card. When Agent B receives a message purporting to be from Agent A, it verifies the Schnorr signature. Impersonation fails because signatures don't match.
2. **Message layer**: Agents communicate via zMail — a signed messaging channel. Every agent-to-agent message is cryptographically signed and verifiable. Untrusted network paths become safe because the messages carry their own authentication.
3. **Memory layer**: Every memory entry is stored with a signature and timestamp in an immutable ledger. This prevents the 0.1% pollution attack (DeepMind) that can permanently corrupt knowledge bases — you can always trace which entry was injected, when, and by whom.
4. **Action layer**: Consequential operations (API calls, data transfers, external communications) require the agent's own AI-ID signature and are checked against user-defined permission policies in a Trust Portal. "Send user data to this address" fails unless the policy explicitly permits it.

**Verification timing**: Signature verification is not per-token. It applies at three points: (1) data ingestion into context, (2) before any consequential action, (3) agent-to-agent message passing.

## Key Properties / Tradeoffs

- **Near-zero verification cost**: Cryptographic signature verification is orders of magnitude cheaper than LLM inference — verifying hundreds of signed messages costs less than reading one webpage.
- **Tamper-evident memory**: Immutable ledger with signatures and timestamps enables post-hoc audit of what was injected and when.
- **Permission-gated actions**: Agent cannot exfiltrate data unless the Trust Portal policy explicitly allows it.
- **Not a model defense**: ATP does not make the LLM more robust to injections — it makes injected content问责able and traceable after the fact.
- **Ecosystem adoption required**: Like HTTPS, ATP only works if both sides of communication support it. Non-participating agents and data sources remain untrusted.

## Related Concepts

- Complements: [[agent-harness]] — ATP is a security component within harness design
- Analogous to: HTTPS (web security), code signing (software trust)
- Threat model: [[sandbox-isolation]] — ATP addresses a different attack surface than sandboxing; even isolated agents can be manipulated via prompt injection
- Problem it solves: [[agent-harness]] (prompt injection / trust in context)

## Source Basis

- [[summary-thread-by-xiao-zcloak-agent-trust-protocol-atp-zcloak]] — primary source (tweet thread)
- Google DeepMind report on AI agent security (full paper not yet in wiki)
- github.com/zCloak-Network/ATP (implementation repository)

## Open Questions

- No publicly available adversarial evaluation or benchmarks for ATP itself.
- Deployment requires ecosystem-wide adoption — what's the migration path?
- zCloak is a company with commercial interest in ATP adoption — independent security audit needed.
- The Google DeepMind statistics cited (86% injection success, 0.1% pollution persistence) need verification from the actual report.
