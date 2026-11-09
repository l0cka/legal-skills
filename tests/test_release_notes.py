"""Controls for the release-notes extractor used by the release workflow."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import release_notes  # noqa: E402

SAMPLE = """# Changelog

## Unreleased

- Pending work for 1.2.0.

## 2026-11-09 - 1.1.0: first tag

### Changed

- One thing.

## 2026-08-26 - Earlier

- Old thing.
"""


class ReleaseNotesTests(unittest.TestCase):
    def test_extracts_only_the_named_section(self) -> None:
        title, body = release_notes.section_for(SAMPLE, "1.1.0")
        self.assertEqual(title, "2026-11-09 - 1.1.0: first tag")
        self.assertEqual(body, "### Changed\n\n- One thing.\n")

    def test_unreleased_version_has_no_section(self) -> None:
        self.assertIsNone(release_notes.section_for(SAMPLE, "1.2.0"))

    def test_version_is_not_matched_as_a_prefix(self) -> None:
        self.assertIsNone(release_notes.section_for(SAMPLE.replace("1.1.0:", "1.1.01:"), "1.1.0"))

    def test_last_section_runs_to_end_of_file(self) -> None:
        text = "## 2026-01-01 - 2.0.0\n\n- Only thing.\n"
        self.assertEqual(release_notes.section_for(text, "2.0.0")[1], "- Only thing.\n")

    def test_changelog_has_a_section_for_a_tagged_version(self) -> None:
        text = release_notes.CHANGELOG.read_text(encoding="utf-8")
        self.assertIsNotNone(release_notes.section_for(text, "1.1.0"))


if __name__ == "__main__":
    unittest.main()
