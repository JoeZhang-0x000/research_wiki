---
title: "Thread by @deedydas"
source: "https://x.com/deedydas/status/2041189706910875869"
author:
  - "[[@deedydas]]"
published: 2026-04-07
created: 2026-04-07
description: "Meta Harnesses is Autoresearch on steroids. Something I've been exploring recently is to get long running agents to hill climb on a verifia"
tags:
  - "clippings"
---
**Deedy** @deedydas [2026-04-06](https://x.com/deedydas/status/2041189706910875869)

Meta Harnesses is Autoresearch on steroids.

Something I've been exploring recently is to get long running agents to hill climb on a verifiable task to continuously improve without my intervention. Karpathy's Autoresearch did this pretty well on specific tasks, but this weekend I tried Meta Harnesses which moves one level of abstraction up.

What does Meta Harness do?

Autoresearch can be used in harness like Claude Code / Codex to generate experiments to try, evaluate results, and continue looping. Meta Harness generates a harness itself that optimizes on a task or a set of task. Here, we define a harness as "a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic". The idea is that LLMs are very powerful today, but to harness \[pun intended\] their power, you need to give it the right prompts and context. Meta Harnesses automates coming up with the right prompts and the right way to retrieve context to solve a problem.

Where did this idea come from?

This is from a paper from Stanford and the author of DSPy written last week. The paper shows fantastic performance on 3 tasks: text classification, math reasoning (IMO level problems) and coding (Terminal Bench 2.0), far outperforming traditional harnesses. The discovered harnesses are interesting: math for example, splits up the logic into different categories (Combinatorics, Geometry, Number Theory, Algebra) and prompts and looks at the context differently. The coding harness, amongst other things, pre-processes the tools available in the environment to save exploratory turns.

When should you use and not use it?

Meta Harnesses seem pretty useful for tackling a specific but wide set of problems where the result is verifiable. In contrast, when I tried it on a specific task like Chess, it arbitrarily divides the problem into separate tasks - opening, mid game, end game, and creates different approaches for each. This "works" but isn't really clean because we believe there should be one approach that does all three. It does far better on things like examinations (JEE, Gaokao) where it splits problems into categories and tackles each category with different strategies.

This paper covers a pretty light version of what a harness means. In the future, we can split up tasks into harnesses that have access to specific kinds of data, specific toolchains and various models to get even better results.

Overall, pretty cool applied AI approach to hillclimb a verifiable task in a specific domain with variety within the problem space.

![Image](https://pbs.twimg.com/media/HFPDOKNboAEgr9m?format=jpg&name=large)

---

**Deedy** @deedydas [2026-04-06](https://x.com/deedydas/status/2041189719250522192)

Paper: https://alphaxiv.org/abs/2603.28052

Demo:

---

**Chahid Chirchi** @CChirchi [2026-04-06](https://x.com/CChirchi/status/2041200794314141957)

that's wild, autoresearch on steroids? def trying it out this weekend

---

**AIHacksByMK** @AIHacksByMK [2026-04-06](https://x.com/AIHacksByMK/status/2041230463885512813)

How did you handle the potential for Meta Harnesses to overfit to the specific tasks or datasets it was trained on, and did you observe any signs of overfitting in your experiments.

---

**HOL** @HashgraphOnline

DON'T MISS: Claim 10 FREE HOL Points Before They're Gone!

Instant – no fees and it only takes 30 seconds.

Thousands are applying right now... don't lose your shot at the agentic future.

Tap image to claim + enter 10,000 HOL giveaway.

Limited – act fast ↓

---

**Tech With Matteo** @TechWithMatteo [2026-04-06](https://x.com/TechWithMatteo/status/2041200619436835041)

the idea of letting agents self-optimize on verifiable tasks is something i been thinking about too, the math split into categories part is really clever and something i wouldnt have thought to do manually

---

**Henry Lu** @HenryL\_AI [2026-04-06](https://x.com/HenryL_AI/status/2041226183468265602)

Thanks for sharing @deedydas , and we have just open-sourced integration for Meta-Harness in A-EVOLVE, so now you can use it (and other self-evolving/auto-harness algorithm for all other use-cases), happy to share more about it if interested

> 2026-04-04
> 
> 🚀 Major update: Meta-Harness integration (new evolution algorithm) is now complete! You can run Meta-Harness on all environments in A-Evolve.
> 
> We added Meta-Harness as a new pluggable evolution algorithm inside A-Evolve (just like PyTorch adding a new CNN).
> 
> Ran it on MCP-Atlas x.com/HenryL\_AI/stat…
> 
> ![Image](https://pbs.twimg.com/media/HFBPdDebcAAG7bh?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/HFBPkyObgAEh_vB?format=jpg&name=large)