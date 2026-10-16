from __future__ import annotations

import unittest

from test_plugin_structure import AREAS, skill_text

AREA = "cognitive-sparring"
REQUIRED = (
    "Jurisdiction is lawyer-supplied.",
    "qualified lawyer",
    "cannot tell from the supplied record",
    "sparring-contract.md",
)


class CognitiveSparringTests(unittest.TestCase):
    def test_each_skill_keeps_jurisdiction_with_the_lawyer(self) -> None:
        skills = AREAS[AREA]["skills"]
        self.assertEqual(len(skills), 12)
        for skill in sorted(skills):
            with self.subTest(skill=skill):
                text = skill_text(skill)
                for needle in REQUIRED:
                    self.assertIn(needle, text)
                self.assertNotIn("Australia", text)
                self.assertNotIn("Australian", text)


if __name__ == "__main__":
    unittest.main()
