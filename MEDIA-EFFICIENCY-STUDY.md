# Faster, cheaper AI media production: exploratory study and working prototype

13 October 2026. Target: small studios, creators and agencies making recurring videos, voiceovers or 3D assets. The need is a hypothesis supported by cost mechanisms and research, not validated demand for our product.

## What the evidence supports

| Medium | Evidence | Practical hypothesis | Boundary |
|---|---|---|---|
| Video | [TeaCache, CVPR 2025](https://arxiv.org/abs/2411.19108) studies inference caching and reports model-specific acceleration | Where model internals are accessible, test caching; with closed APIs, reduce unnecessary generated seconds and repeat attempts | We did not install TeaCache or reproduce its benchmark; cannot modify a vendor's closed inference |
| Audio | [Pruned step sampling](https://arxiv.org/abs/2505.19931) evaluates acceleration of flow-matching TTS; [F5-TTS](https://github.com/SWivid/F5-TTS) documents runtime options | Compare local inference on available hardware; segment approved scripts and rerender changed segments only | Hardware, language, prosody and voice rights affect feasibility; code and weight licenses differ |
| 3D | [Stable Fast 3D](https://github.com/Stability-AI/stable-fast-3d) reconstructs textured meshes from single images | Compare reconstruction against iterative generation where the brief permits; reuse a base mesh and material variants | Not equivalent to animation-ready topology, CAD accuracy or every text-to-3D task; manual repair can dominate cost |

[Runway API pricing](https://docs.dev.runwayml.com/guides/pricing/) uses model-specific credits, including generated-video seconds. [ElevenLabs pricing](https://elevenlabs.io/pricing) varies by plan/product/model and usage unit. Hence avoid unnecessary duration/characters and count failed attempts. Do not equate credits across vendors or quote one universal audio rate. Hardware, queues, review and subscriptions belong in total cost; API charges alone are insufficient.

Commercial use needs the exact weight/license and source asset rights checked: F5-TTS's repository distinguishes code from pretrained models; [Stability's license](https://stability.ai/license) has eligibility conditions. No model weights were downloaded, model installed, voice cloned or paid generation started in this study.

## Workflow interventions to test

1. Approve script, pronunciation, storyboard and technical brief before costly final output.
2. Split work into shots, speech segments, meshes and materials; retain inputs/settings/accepted outputs. Only changed components and their dependents need review or regeneration.
3. Use previews before finals when available. Count the extra preview cost: preview-first may cost more when a direct final already succeeds.
4. Decide whether each scene needs generative video, motion graphics or an existing approved asset. Different methods have different creative capabilities; substitution must satisfy the brief, not merely lower the bill.
5. Bound variants/retries and inspect failure reasons. Batch independent work only within provider quotas and local VRAM limits. Measure wall time separately from GPU time and cost.

## Product created: Media Production Preflight v0.1

A dependency-free, offline Python CLI checks a production manifest before generation. It handles video/audio/3D assets; requires approved brief and confirmed rights; identifies exact-spec accepted cache candidates; blocks dependencies when upstream work is blocked; invalidates downstream reuse when an upstream asset must regenerate; orders work; reports known planned costs and unknown costs separately; rejects cycles and mixed currencies. It neither uploads inputs nor spends credits.

Download [media_preflight.py](media_preflight.py) and [media-example.json](media-example.json). Run `python media_preflight.py media-example.json`. See [synthetic example result](media-example-result.json): one audio reuse candidate, one planned video generation, one blocked unapproved 3D asset. Prices are invented demonstration inputs, not provider quotes or actual savings. Source input hashes, settings, model version and output acceptance must be supplied correctly. The tool trusts operator declarations; it does not inspect media quality, verify licenses, scan files or orchestrate vendor renders. If upstream outputs change, recompute downstream input hashes and rerun.

Six focused tests passed: exact cache versus voice changes, unaccepted output rejection, rights/dependency blocking, cycle/currency rejection, unknown-cost handling, and downstream invalidation. This is functional prototype evidence, not a video/audio/3D performance benchmark.

## Validation protocol and business case

First recruit 5–10 producers with repeated work and documented costs. Ask last delivery, number of rejected attempts, changes after approval, cache practices, review burden and budget authority. Request public/synthetic plans or authorized sanitized logs. Interested peers are not purchase commitments.

Pilot design: same approved brief and acceptance rubric, original pipeline versus planned selective generation/reuse. Use several distinct briefs per medium; randomize execution order when possible, keep settings/provider/hardware logged, score output blind where feasible. Include preview/final attempts, manual review, repair, storage, orchestration, queue delays, refunds and licenses. Primary metrics: total cost and elapsed time per accepted deliverable, accepted quality and first-pass acceptance. Reuse counts alone do not establish savings. Track continuity/brand adherence for video, intelligibility/prosody for audio, and topology/material/usability for 3D. Establish quality tolerances before results; report failures and uncertainty. No experiments on generated media have yet been run.

Break-even: saved repeat-generation and repair cost must exceed added planning/review/storage costs plus service price. A customer who rarely revises may not benefit. Proposed paid pilot: **45 USDC** to analyze one sanitized production manifest, up to 20 assets, deliver its preflight result, review three improvement candidates and a measurement plan. Feasibility, total workload, capacity, one clarification round and delivery window require agreement before funding. No implementation, media generation, model installation or savings guarantee included. If the cost floor cannot support the scope, narrow or requote before acceptance. Public tool available without a fee; commercial value must come from reviewed application to the buyer's workflow. No live checkout or confirmed sale implied.
