import unittest
from async_job_guard import next_action
class GuardTests(unittest.TestCase):
    def test_timeout_is_not_resubmission(self):
        for state in ('timeout','unknown','submitting'):
            self.assertEqual(next_action({'state':state}),'reconcile_existing_request_do_not_resubmit')
    def test_submission_requires_approval(self):
        self.assertEqual(next_action({'state':'not_submitted'}),'manual_review')
        self.assertEqual(next_action({'state':'not_submitted','approved':True}),'submit_once_with_stable_id')
    def test_artifact_must_be_verified(self):
        self.assertEqual(next_action({'state':'complete'}),'verify_artifact')
        self.assertEqual(next_action({'state':'complete','artifact_verified':True}),'reuse_verified_result')
    def test_confirmed_failure_does_not_auto_spend(self):
        self.assertEqual(next_action({'state':'failed_confirmed'}),'review_failure_and_budget_before_new_attempt')
if __name__=='__main__':unittest.main()
