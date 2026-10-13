from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-consumer-competition"
LINK_PATTERNS = (
    r'\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))',
    r'^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|([^\s]+))',
    r'(?:href|src)\s*=\s*[\"\']([^\"\']+)[\"\']',
)
OFFICIAL_PREFIXES = (
    "https://www.legislation.gov.au/",
    "https://www.accc.gov.au/",
    "https://www.productsafety.gov.au/",
    "https://ministers.treasury.gov.au/",
)


def cross_plugin_links(text: str, source: Path) -> list[str]:
    violations = []
    for pattern in LINK_PATTERNS:
        for match in re.finditer(pattern, text, re.MULTILINE | re.IGNORECASE):
            target = next(group for group in match.groups() if group is not None)
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"} or parsed.netloc:
                continue
            if not parsed.path:
                continue
            destination = (source.parent / unquote(parsed.path)).resolve()
            if destination.is_relative_to(ROOT / "plugins") and not destination.is_relative_to(PLUGIN):
                violations.append(target)
    return violations


class ConsumerCompetitionContractTests(unittest.TestCase):
    def test_each_skill_has_an_eval_and_lawyer_gate(self) -> None:
        prompts = [path.read_text() for path in (PLUGIN / "evals").glob("*/prompt.md")]
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                self.assertTrue(any(f"Use {path.parent.name}." in text for text in prompts))
                self.assertIn("qualified lawyer", path.read_text())
        self.assertTrue(any("happy-path" in text for text in prompts))

    def test_watch_register_has_controlled_states_and_official_sources(self) -> None:
        register_path = PLUGIN / "skills/track-accc-developments/references/watch-register.json"
        register = json.loads(register_path.read_text())
        self.assertEqual(register["as_at"], "2026-10-13")
        items = register["watch_items"]
        self.assertEqual(len({item["id"] for item in items}), len(items))
        self.assertEqual(len({item["expected_trigger"] for item in items}), len(items))
        for item in items:
            with self.subTest(item=item["id"]):
                self.assertTrue(item["status_at_snapshot"])
                self.assertTrue(item["expected_trigger"])
                self.assertTrue(item["primary_sources"])
                for source in item["primary_sources"]:
                    self.assertTrue(source.startswith(OFFICIAL_PREFIXES))
        general = next(item for item in items if item["id"] == "general-safety")
        self.assertIn("compilation 167", general["status_at_snapshot"])
        self.assertTrue(any("treasury.gov.au" in source for source in general["primary_sources"]))
        forms = next(item for item in items if item["id"] == "merger-forms")
        self.assertIn("UNCONFIRMED", forms["status_at_snapshot"])
        self.assertIn("https://www.legislation.gov.au/F2025L01604/latest", forms["primary_sources"])
        future = next(item for item in items if item["id"] == "utpa-2026")
        self.assertIn("not yet in force", future["status_at_snapshot"])

    def test_dependencies_name_existing_skills_and_do_not_link_across_plugins(self) -> None:
        catalog = json.loads((PLUGIN / "catalog.json").read_text())
        self.assertEqual(set(catalog["handsOffTo"]), {
            "australian-commercial-drafting",
            "australian-employment-fair-work",
            "australian-privacy-cybersecurity",
        })
        for path in PLUGIN.rglob("*.md"):
            with self.subTest(path=path):
                self.assertEqual(cross_plugin_links(path.read_text(), path), [])

    def test_link_check_resolves_targets_and_handles_multiple_syntaxes(self) -> None:
        source = PLUGIN / "README.md"
        other = "../australian-commercial-drafting/README.md"
        examples = (
            f"[other]({other})",
            f"[other](<{other}>)",
            f"[other]: {other}#scope",
            f'<a href="{other}">other</a>',
            "[other](%2e%2e/australian-commercial-drafting/README.md)",
            f"[other]({ROOT / 'plugins/australian-commercial-drafting/README.md'})",
            "[other](../legal-workflow-router/references/skill-map.md)",
        )
        for text in examples:
            with self.subTest(text=text):
                self.assertEqual(len(cross_plugin_links(text, source)), 1)
        allowed = "\n".join((
            "[local](references/merger-pathways.md)",
            "[local](../australian-consumer-competition/CONTEXT.md#scope)",
            "[anchor](#scope)",
            "[official](https://www.legislation.gov.au/C2004A00109/latest/text)",
        ))
        self.assertEqual(cross_plugin_links(allowed, source), [])


if __name__ == "__main__":
    unittest.main()
