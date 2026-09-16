"""A learner checkout must never emit a grade without protected references."""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HAS_SCORING_DEPS = all(importlib.util.find_spec(name) for name in ("numpy", "PIL", "pycocotools"))


@unittest.skipUnless(HAS_SCORING_DEPS, "Install optional scoring dependencies from requirements.txt")
class ScoringReferenceGate(unittest.TestCase):
    def test_one_task_refuses_to_score_without_reference(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scoring" / "score.py"), "easy_semantic", "missing.zip"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Protected reference missing", result.stderr)
        self.assertNotIn("points:", result.stdout)

    def test_scorecard_does_not_write_zero_grade_without_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            submissions = base / "submissions"
            submissions.mkdir()
            (submissions / "easy_semantic.zip").touch()
            output = base / "reports"
            result = subprocess.run(
                [sys.executable, str(ROOT / "scoring" / "scorecard.py"),
                 "--dir", str(submissions), "--out", str(output)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Protected reference missing", result.stderr)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
