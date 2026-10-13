from __future__ import annotations

import re
import unittest
from pathlib import Path

from test_plugin_structure import CONTRACT_HEADINGS, DRAFT, READY

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-commercial-drafting"


class AustralianCommercialDraftingTests(unittest.TestCase):
    def test_each_skill_has_eval_coverage(self) -> None:
        skills = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        prompts = [path.read_text(encoding="utf-8") for path in (PLUGIN / "evals").glob("*/prompt.md")]
        covered = {
            name
            for name in skills
            if any(re.search(rf"(?m)^name: {re.escape(name)} ", prompt) for prompt in prompts)
        }
        self.assertEqual(covered, skills)

    def test_result_contracts_match_document_family(self) -> None:
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            vocabulary = DRAFT if path.parent.name.startswith("draft-") else READY
            with self.subTest(skill=path.parent.name):
                text = " ".join(path.read_text(encoding="utf-8").split())
                for required in (*CONTRACT_HEADINGS, *vocabulary):
                    self.assertIn(required, text)

    def test_all_local_document_links_resolve(self) -> None:
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                with self.subTest(document=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).resolve().is_file())


if __name__ == "__main__":
    unittest.main()
