import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_comparative_trials.py"


class ComparativeTrialsTests(unittest.TestCase):
    def valid_results(self) -> dict:
        criteria = ["preserves the existing behavior", "runs the focused check"]
        return {
            "schemaVersion": 1,
            "task": {"id": "local-contract-change", "successCriteria": criteria},
            "variants": [
                {
                    "id": "no-skill",
                    "taskId": "local-contract-change",
                    "status": "PASS",
                    "observationSource": "HOST_OBSERVED",
                    "elapsedSeconds": 91,
                    "reworkCount": 2,
                    "verifiedCriteria": criteria,
                },
                {
                    "id": "short-prompt",
                    "taskId": "local-contract-change",
                    "status": "PASS",
                    "observationSource": "HOST_OBSERVED",
                    "elapsedSeconds": 74,
                    "reworkCount": 1,
                    "verifiedCriteria": criteria,
                },
                {
                    "id": "ai-first",
                    "taskId": "local-contract-change",
                    "status": "PASS",
                    "observationSource": "HOST_OBSERVED",
                    "elapsedSeconds": 88,
                    "reworkCount": 0,
                    "verifiedCriteria": criteria,
                },
            ],
        }

    def run_check(self, results: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.json"
            path.write_text(json.dumps(results), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), "--results", str(path)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_complete_same_task_trial_produces_a_comparable_summary(self):
        result = self.run_check(self.valid_results())
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("VALID: comparable trial record", result.stdout)
        self.assertIn("ai-first", result.stdout)

    def test_missing_variant_cannot_be_called_a_three_way_comparison(self):
        results = self.valid_results()
        results["variants"].pop()
        result = self.run_check(results)
        self.assertEqual(1, result.returncode)
        self.assertIn("missing required variants: ai-first", result.stdout)

    def test_completed_variant_requires_observed_evidence(self):
        results = self.valid_results()
        results["variants"][0]["observationSource"] = "DOCUMENTED_ONLY"
        result = self.run_check(results)
        self.assertEqual(1, result.returncode)
        self.assertIn("no-skill: completed status requires HOST_OBSERVED or HUMAN_OBSERVED", result.stdout)

    def test_variant_task_id_must_match_the_shared_task(self):
        results = self.valid_results()
        results["variants"][1]["taskId"] = "different-task"
        result = self.run_check(results)
        self.assertEqual(1, result.returncode)
        self.assertIn("short-prompt: taskId must match task.id", result.stdout)

    def test_completed_variant_cannot_pad_verified_criteria_with_duplicates(self):
        results = self.valid_results()
        results["variants"][0]["verifiedCriteria"] = [
            *results["variants"][0]["verifiedCriteria"],
            "preserves the existing behavior",
        ]
        result = self.run_check(results)
        self.assertEqual(1, result.returncode)
        self.assertIn("no-skill: verifiedCriteria must match task.successCriteria", result.stdout)


if __name__ == "__main__":
    unittest.main()
