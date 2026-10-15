import unittest
import collaboration_pilot as pilot

class PilotTests(unittest.TestCase):
    def test_comment_fix_does_not_imply_contract_correctness(self):
        baseline=pilot.invariants('baseline');partial=pilot.invariants('comment_only_fix')
        self.assertFalse(baseline['comment_round_half_up'])
        self.assertTrue(partial['comment_round_half_up'])
        self.assertFalse(partial['held_out_none_passthrough'])
        self.assertTrue(all(pilot.invariants('complete').values()))
    def test_missing_content_blocks_and_complete_mapping_needs_review(self):
        r=pilot.demo()
        self.assertFalse(r['handoff_incomplete']['experiment_allowed'])
        self.assertIn('acceptance',r['handoff_incomplete']['missing_fact_mappings'])
        self.assertTrue(r['handoff_complete_unreviewed']['ready_for_semantic_review'])
        self.assertFalse(r['handoff_complete_unreviewed']['experiment_allowed'])
        self.assertFalse(r['handoff_complete_unreviewed']['semantic_equivalence_verified_by_code'])

if __name__=='__main__':unittest.main()
