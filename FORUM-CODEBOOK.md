# Forum reconnaissance: agent communication and coordination

Exploratory reading notes, 13 October 2026. These are hypotheses and community claims, not representative findings or independently reproduced results.

## Sample and provenance
Four Moltbook searches returned 20 distinct posts from 14 profile names. Six posts came from one profile and two from another. Profiles are not verified independent operators. Four targeted full-text records were saved privately; three short posts were read in full and the long resource-isolation essay was examined through selected sections. Also read selected Reddit threads and A2A GitHub discussion #2022. Search snippets are leads, not full-text evidence. Relative dates in web renderings varied from search metadata, so no trend-by-day estimate is made.

| Theme | What the sampled texts discuss | What to test in our verbund |
|---|---|---|
| Lost constraints | A result arrives without why alternatives were rejected; downstream work repeats a known mistake. | Preserve constraints, rejected options and unresolved questions; measure downstream correctness. |
| Coordination expense | Repeated context, delegation and retries can dominate useful execution. | Record root-task and per-handoff tokens/bytes, retries, abandoned branches and cost per accepted output. |
| Contract disagreement | Some posters prefer strict schema checkpoints; another reports more resilience with Markdown. | Compare typed contract and plain-language handoff under the same task, source and failure conditions. |
| Silent failures | Healthy individual steps can hide an unacknowledged or lost transition. | Persist actual states and one accountable owner; treat absent acknowledgement as unknown delivery and reconcile before retry. |
| Work versus payment | Signed receipts and success messages do not alone establish accepted work or settlement. | Separate provenance, reproduced output, buyer acceptance and verified payment. |
| Shared resources | Resource-isolation essays warn about noisy neighbours and shared failure domains. | Measure queue and contention; sharing infrastructure must not silently share credentials, unlimited quotas or authority. |

## Evidence anchors
- [Reddit: coordination costs](https://www.reddit.com/r/AI_Agents/comments/1w9u6us/how_much_do_multiagent_systems_cost_agent/): repeated context and compression/retry trade-offs; several comments also advertise products. Numerical savings and pricing are unverified claims here.
- [Reddit: Markdown handoffs](https://www.reddit.com/r/AI_Agents/comments/1rjsdt1/the_hardest_part_of_multiagent_setups_isnt_the/): a poster reports preferring plain-text intermediate documents. This conflicts with universal claims for stricter JSON, and motivates a comparison rather than a conclusion.
- [Reddit: production choices](https://www.reddit.com/r/AI_Agents/comments/1x2qpdj/multiagent_in_production_what_does_it_look_like/): builders ask when code-controlled flows, reviews and tracing justify decomposition. Available comments are sparse, not a consensus.
- [Moltbook: orchestration audit](https://www.moltbook.com/post/b3f0d0cc-1f99-45b9-96df-c1f13eb26877): the author describes orchestration/rework expense and suggests simple tasks need less coordination. The reported percentages and single-agent comparison are self-report, with no inspected raw traces.
- [Moltbook: handoff observability](https://www.moltbook.com/post/d4f63bbc-e1e9-4cee-a047-db0862fc99a5): checkpoint, dependency and rollback proposals. We do not adopt automatic rollback for uncertain external writes; a missing acknowledgement requires reconciliation.
- [Moltbook: receipt RFC](https://www.moltbook.com/post/edf981cd-29f9-468e-9ce5-262768771f13): proposed signed envelopes, revocation and execution receipts. A self-signed log may still contain a false claim; provenance is not independent truth or payment.
- [Moltbook: resource isolation](https://www.moltbook.com/post/58f70c4b-b812-4040-9184-ea36efc5286f): selected sections describe contention and quotas, with broad implementation claims. We did not inspect a deployed system or telemetry.
- [A2A GitHub discussion #2022](https://github.com/a2aproject/A2A/discussions/2022): participants distinguish task lifecycle, artifacts, progress and application payloads. It is an unanswered community discussion, not a normative specification; verify version-specific requirements against the official protocol.

## Language to test
Concrete task terms in the sample include handoff, constraints, checkpoint, schema, retry, trace, token budget, receipt and acceptance. This is qualitative observation, not a measured term-frequency result. Prefer a specific offer such as "check one failed handoff and produce a reproducible repair plan"; test comprehension rather than assuming the name Verbund explains it.

## Interpretation and next research
Similar infrastructure and handoff ideas already exist in these discussions. Our proposed contribution needs to be demonstrated through common provenance from contact to accepted delivery to later knowledge reuse, with costs and failures included. A keyword hit, upvote, post count or vendor claim is not market demand. Silence still has unknown cause without delivery/read evidence or a counterpart explanation.

Next additions to the study: plain-language-versus-typed handoff control, full-run coordination accounting, uncertain-delivery reconciliation fixtures, and independent output grading. No new model performance run occurred during this forum reading. Community excerpts and private traces are not included in commercial editions; reuse and editorial scope require review.
