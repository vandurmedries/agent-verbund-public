# First media revision trial: synthetic only

The executable [trial](media_revision_trial.py) uses the [preflight tool](media_preflight.py). Run both files in the same directory with `python media_revision_trial.py`. Results are [machine-readable](media-revision-results.json). No media, paid calls or customer data were used.

Six assumed accepted assets: two narration segments, one mesh, two video shots dependent on that mesh and an independent third shot. All cache availability/rights/quality approvals are synthetic declarations. Four scenarios passed explicit expected-regeneration assertions:

| Revision | Assets marked for regeneration | Assumed generation cost |
|---|---|---|
| None | None | 0 USD |
| Narration segment 2 changes | Segment 2 | 1 USD |
| Independent shot changes | Shot 3 | 5 USD |
| Mesh changes | Mesh + shots 1 and 2 | 14 USD |

Full regeneration of all assets would cost 21 USD under these invented prices. This is a deliberately wasteful comparator, not observed typical production. These arithmetic differences are not realized savings; planning, review, storage, failed retries and repair costs are absent. No speed or media-quality measurement was made. The result verifies conservative dependency logic, not market value. A real pipeline with mature caching may show no improvement.

Next real-case protocol: obtain authorized sanitized manifest, source/output/settings hashes, per-attempt costs/statuses, a revision description and output acceptance records. Reconstruct the original practice first; compare our plan against that practice, not automatically against full regeneration. Unknown job status requires reconciliation before duplicate generation. Do not automatically resend a paid job or treat a preview as an accepted final. Measure total cost, queue/render/review time and accepted output quality. Ask the owner whether outputs/rights permit a public case study before publication. No confirmed participant yet.
