# Turn AI work into reviewed, reusable outcomes

Research synthesis and scoped pilot offer, 13 October 2026.

## The problem we can substantiate

AI pipelines can consume tokens in duplicate investigations, oversized context, repeated failures, lost handoff constraints and outputs that never meet acceptance criteria. Useful intermediate work can also disappear without an owner or reusable artifact. The community already studies efficiency and reliability; claiming nobody addresses this would be false. No method guarantees that every token produces value. Exploration, verification and rejected hypotheses can be worthwhile when bounded and recorded; storing everything can itself cost more than it saves.

Our objective: maximize accepted outcomes and safe future reuse per unit of total effort, subject to quality and rights constraints. Give each model/tool action a purpose, budget and termination criterion, and retain the useful evidence needed for the next decision. Avoid treating tokens as independently priced units of business value.

## Published research supports the problem and mechanisms

- [FrugalGPT](https://arxiv.org/abs/2305.05176) investigates prompt adaptation, approximation and model cascades, reporting cost/performance gains on its evaluated workloads. It supports selective routing as an approach, not a savings guarantee for Verbund; its experimental percentages are not ours.
- [LLMLingua](https://arxiv.org/abs/2310.05736), accepted at EMNLP 2023, evaluates budget-controlled prompt compression across four datasets. It supports investigating smaller context with quality checks. Our local compaction is not an implementation or reproduction of LLMLingua.
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) identifies 14 failure modes in three groups: specification/design, inter-agent misalignment, and verification/termination. It supports examining coordination and completion failures, not a claim that our software has eliminated them.
- [Anthropic's engineering guidance](https://www.anthropic.com/engineering/building-effective-agents) discusses choosing simpler approaches and the latency/cost tradeoff of agentic systems. It is practitioner guidance, separate from controlled evidence.

## What our existing prototype actually does

Local task deduplication and leases, bounded polling, exact-input advisory caching, compact advisory context, preserved handoff evidence, an append-only cooperation journal, and quarantining unreviewed or conflicting evidence are implemented in our local prototype. Conversation acknowledgements are separated from peer answers, agreements and receipts. These controls demonstrate mechanisms; they do not yet demonstrate customer ROI or universal compatibility. The full local codebase is not claimed to be publicly distributed by this report.

Our [first smoke run](draft-review-smoke-summary.json) used 8 calls: 2,000 output tokens, 217.71 seconds, all 8 outputs truncated. A [second preparation cycle](draft-review-compact-summary.json) used 8 calls: 638 output tokens, 90.01 seconds, no truncated outputs. These are descriptive observations on one local task/model, with two instruction changes and order/warm-up confounds. Errors remained and independent quality scores are absent. This is evidence that we detected a failure and changed the process, not proof of equal-quality savings or causal superiority. Input tokens and failed work remain part of cost.

## Pilot for sale: AI Work Value Diagnostic

Target buyer: an AI builder/integrator with one specific workflow and authority to share sanitized traces and purchase an investigation.

Deliverable: a bounded analysis of up to 20 supplied, sanitized action records from one workflow; a purpose/outcome/cost map; duplicate, retry, context and handoff observations where the records permit them; one reusable check or evidence fixture; three prioritized changes and their validation plan. Human review before delivery. No private credentials required. Missing costs, absent quality evidence and uncertain attribution are reported explicitly. No automated repair, live production access, indefinite support or guaranteed savings included.

Exploratory fixed-price proposal: **45 USDC**, contingent on input feasibility and written scope/capacity confirmation before any funded order. This is a nonbinding quote invitation, not an active checkout or accepted contract. We confirm one review/clarification round and delivery window before acceptance; unsupported inputs receive a scope decision rather than invented metrics. No payment requested merely to discuss fit. At the previous illustrative 30-USDC/hour labor value, 5% fees and 30% contribution target, this price allows at most 58.5 minutes of total compensated work if other variable costs are zero. Those are planning assumptions, not observed actual costs or platform rates. If the work exceeds that budget, narrow the scope or quote separately before acceptance.

Required input: task goal, action IDs/timestamps, links between attempts and outputs, token/call usage if available, acceptance result, and permission to analyze. Sanitized public or synthetic data preferred. We do not use a client's traces in commercial reports without explicit rights.

## How the claimed benefit will be tested

Agree output acceptance and error thresholds first. Compare original and modified workflow on matched representative tasks; keep provider/model/settings documented, account for caching/warm-up, randomize order where feasible and use independent blinded review where available. Count all attempts, review/rework, tokens, elapsed time, charges and failed outcomes. Track cost per accepted outcome, repeated-work rate, verified reuse events and unresolved handoffs. A shorter answer or saved artifact alone is not an accepted outcome or demonstrated reuse. A small pilot yields uncertainty and feasibility evidence, not a population estimate.

A buyer's accepted delivery and an attributable settled payment are needed to claim a sale. Research citations establish relevance, local tests establish limited observations, and customer trials must establish commercial value. None substitutes for the others.
