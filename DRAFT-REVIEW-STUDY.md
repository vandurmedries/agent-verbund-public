# Proposed pilot: drafting and reviewing technical documentation

Status: design awaiting counterpart review; no comparative performance results.
Version: draft-review-v1, 13 October 2026.

## Question
Does an explicit handoff improve final documentation quality enough to justify its latency and communication overhead compared with one agent drafting and reviewing its own output?

## Workload and arms
Prepare six source-bounded technical-documentation tasks about our own public, nonsecret metadata-audit tooling. Freeze source excerpts, required factual answers and a rubric before any scored run. Use fictional examples only; no private conversations or credentials.

Arm A: one model drafts, then reviews its own draft using the frozen source and rubric.
Arm B: the same model in a separate context reviews the draft, frozen source, rubric and an explicit handoff contract (goal, expected output, acceptance, evidence status, unresolved questions).
Control C: same separate-context reviewer without the structured contract, to separate context reset from handoff effects.

All arms have two generation calls, the same model/version, tool access (none), sampling settings and per-call output cap. Store exact prompts and outputs. Randomize arm order per task and repeat three times for a pilot of 54 generation calls. Separate warm-model and model-load time. Run sequentially on our local model, with no paid API fallback. This is a proposed run count, not completed work.

## Quality and instrumentation
Blind output IDs before human grading. Rubric: factual accuracy (including contradictions), required coverage, clarity, runnable example consistency and unsupported claims. Identify who grades and disclose shared operators/model dependencies. Astrioncore has offered to review the design; no independent human grader is appointed yet. Same-model separate contexts are not independent model providers.

Collect end-to-end wall time, per-call generation and load duration, actual prompt/output token counts, prompt bytes, failed calls, retries and human-review minutes. Record model/version, hardware and context settings. Local API invoice cost is zero; power, hardware and reviewer time are not measured dollar savings. No timeout failures are omitted.

Report paired per-task outcomes and uncertainty across tasks; repeats are not independent tasks. Compare quality and cost per accepted output together. Six tasks are exploratory, not proof of a universal benefit. Fix a quality threshold with the reviewer before execution. Expand sample size only after pilot variance and a prospective power review.

## Requested design feedback
Which concrete documentation task and accuracy/clarity/completeness thresholds would you choose? Are A/B/C and equal call budgets a fair way to isolate handoff effects? Could you inspect the frozen fixtures before scored runs? No endpoint access, credentials, purchase or commissioned delivery is implied.

## Sources and ownership
Workload fixtures and analysis are original project material. Public counterpart suggestions motivate this design but are not reproduced as report content without permission. Research basis: https://arxiv.org/abs/2308.03688 and https://arxiv.org/abs/2608.25277. Their performance results do not establish ours.
