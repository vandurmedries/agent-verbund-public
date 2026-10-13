"""Reference policy only: no API calls, payments or jobs are executed."""
def next_action(record):
    if not isinstance(record,dict):raise ValueError('Object required')
    state=record.get('state')
    if state=='not_submitted' and record.get('approved') is True:
        return 'submit_once_with_stable_id'
    if state in ('submitting','timeout','unknown'):
        return 'reconcile_existing_request_do_not_resubmit'
    if state in ('queued','running'):
        return 'poll_existing_job'
    if state=='complete' and record.get('artifact_verified') is True:
        return 'reuse_verified_result'
    if state=='complete':return 'verify_artifact'
    if state=='failed_confirmed':return 'review_failure_and_budget_before_new_attempt'
    return 'manual_review'
