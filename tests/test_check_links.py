"""URL extraction rules for scripts/check_links.py (no network)."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_links", ROOT / "scripts" / "check_links.py")
assert SPEC and SPEC.loader
check_links = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_links)


class CollectTests(unittest.TestCase):
    def test_extraction_keeps_commas_and_skips_placeholders(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "plugins").mkdir()
            (root / "plugins" / "note.md").write_text(
                "See <https://example.test> and "
                "https://www.oaic.gov.au/news/x,-y-finds. "
                "Template https://www.legislation.gov.au/{title_id} and "
                "(https://www.hcourt.gov.au/cases/1).\n",
                encoding="utf-8",
            )
            (root / "plugins" / "skip.txt").write_text("https://ignored.example.com\n", encoding="utf-8")
            found = check_links.collect(root)
        self.assertEqual(
            set(found),
            {"https://www.oaic.gov.au/news/x,-y-finds", "https://www.hcourt.gov.au/cases/1"},
        )


if __name__ == "__main__":
    unittest.main()
