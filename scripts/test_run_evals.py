import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EvalRunnerTests(unittest.TestCase):
    def test_documented_only_runner_checks_rubric_without_claiming_a_host_run(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "run_evals.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("DOCUMENTED_ONLY", result.stdout)
        self.assertIn("rubric", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
