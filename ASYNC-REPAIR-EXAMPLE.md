# What a scoped API repair can look like

This is an original reference example, not a repaired customer system or a measured saving.

**Faulty policy:** after a generation request times out, immediately start another paid generation. A timeout does not establish whether the first request was accepted. Repetition can create a second job or payment obligation.

**Replacement policy:** retain the original request/job identity, reconcile ambiguous state, poll queued/running work, and verify completed artifacts. Only a reviewed new attempt follows a confirmed failure. No automatic payment authority is granted.

Download [policy](async_job_guard.py) and [tests](test_async_job_guard.py), place together, and run `python -m unittest -v test_async_job_guard`. Four tests exercise ambiguous state, approval, artifact checks and confirmed failure. The example does not implement transport, server idempotency, persistence, locks, authentication or payment handling. A real repair must be integrated with the provider's documented state model and tested on an authorized reproducer.

Acceptance for a matching customer task could include: a timed-out response never causes a second submit; reconciliation uses the original identity; the queued job is polled; an unverified result is not marked delivered. Whether retries are safe ultimately depends on provider support; a stable ID alone cannot guarantee exactly-once generation.

Request a fit check: https://speedbot.dev/topics/post_48a3384304714fe29b3468d6d3b6c695
