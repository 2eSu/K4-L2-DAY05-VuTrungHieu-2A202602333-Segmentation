"""Structural checks for the learner-facing Day 5 repository."""

import html.parser
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {
    "easy_semantic": 3,
    "medium_instance": 3,
    "hard_panoptic": 2,
    "cp1_holes": 1,
    "cp2_slice": 1,
    "cp5_occlusion": 1,
    "cp3_thin": 1,
    "cp4_curb": 1,
    "cp6_coverage": 1,
}


class LocalReferences(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                if not value.startswith(("#", "http:", "https:")):
                    self.references.append(value.split("#", 1)[0])


class ReleaseContract(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / "data" / "manifest.json").read_text())

    def test_starter_tasks_and_weights_are_preserved(self):
        tasks = self.manifest["tasks"]
        self.assertEqual(set(tasks), set(EXPECTED_COUNTS))
        self.assertEqual(sum(info["weight"] for info in tasks.values()), 100)
        self.assertEqual(tasks["easy_semantic"]["weight"], 20)
        self.assertEqual(tasks["medium_instance"]["weight"], 32)
        self.assertEqual(tasks["hard_panoptic"]["weight"], 30)

    def test_images_and_classes_are_present(self):
        for name, count in EXPECTED_COUNTS.items():
            base = ROOT / "data" / self.manifest["tasks"][name]["path"]
            self.assertEqual(len(list((base / "images").glob("*.jpg"))), count, name)
            self.assertTrue((base / "classes.json").is_file(), name)

    def test_no_reference_answers_are_shipped(self):
        self.assertFalse(list(ROOT.rglob("groundtruth")))
        self.assertFalse(list(ROOT.rglob("instances-golden.json")))

    def test_html_local_assets_exist(self):
        parser = LocalReferences()
        parser.feed((ROOT / "lab-guide.html").read_text())
        self.assertTrue(parser.references)
        for reference in parser.references:
            self.assertTrue((ROOT / reference).is_file(), reference)

    def test_report_uses_same_score_weights(self):
        report = (ROOT / "reports" / "REPORT_TEMPLATE.md").read_text()
        for row in ("| easy_semantic |", "| medium_instance |", "| hard_panoptic |"):
            self.assertIn(row, report)
        self.assertIn("**100**", report)


if __name__ == "__main__":
    unittest.main()
