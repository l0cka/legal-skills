from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import zipfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ai_tool_bundle", ROOT / "scripts" / "ai_tool_bundle.py")
assert SPEC and SPEC.loader
bundle = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = bundle
SPEC.loader.exec_module(bundle)

EXCLUDED_PREFIXES = ("evals/", "benchmarks/", "tests/", "scripts/", "plugins/", ".claude-plugin/")


class BundleContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.files = bundle.build_files()

    def test_repository_passes_every_bundle_check(self) -> None:
        self.assertEqual(bundle.validate_all(), [])

    def test_contains_the_documented_entries(self) -> None:
        for name in ("ROUTER.md", "catalog.json", "PRIVACY.md", "LICENSE", "VERSION", "reference/firm/README.md"):
            self.assertIn(name, self.files)
        self.assertIn(bundle.plugin_version(), self.files["VERSION"].decode())

    def test_excludes_code_evals_and_manifests(self) -> None:
        for name in self.files:
            self.assertFalse(name.startswith(EXCLUDED_PREFIXES), name)
            self.assertNotIn("/scripts/", name)
            self.assertNotIn("/agents/", name)
            self.assertFalse(name.endswith((".py", ".yaml")), name)
            self.assertNotIn("plugin.json", name)

    def test_router_lists_every_skill_once(self) -> None:
        router = self.files["ROUTER.md"].decode()
        catalog = bundle.load_catalog()
        for area in catalog["areas"]:
            for skill in area["skills"]:
                self.assertEqual(router.count(f"(skills/{skill}/SKILL.md)"), 1, skill)
                self.assertIn(f"skills/{skill}/SKILL.md", self.files)

    def test_firm_slot_ships_no_firm_material(self) -> None:
        firm = [n for n in self.files if n.startswith("reference/")]
        self.assertEqual(firm, ["reference/firm/README.md"])

    def test_every_script_backed_skill_has_its_section(self) -> None:
        skills = bundle.script_backed_skills()
        self.assertGreaterEqual(len(skills), 7)
        for skill in skills:
            text = self.files[f"skills/{skill}/SKILL.md"].decode()
            self.assertIn(bundle.SECTION_HEADING, text, skill)

    def test_deadline_skills_keep_their_gates_in_the_bundle(self) -> None:
        for skill in ("compute-procedural-deadlines", "map-tribunal-review-deadlines"):
            text = self.files[f"skills/{skill}/SKILL.md"].decode()
            self.assertIn("deadline-profile-schema.md", text, skill)
            self.assertIn("litigation-deadlines-source-and-control-method.md", text, skill)
            self.assertIn("binding deadline", text, skill)

    def test_fingerprint_is_never_computed_in_the_bundle(self) -> None:
        text = self.files["skills/verify-deadline-basis/SKILL.md"].decode()
        self.assertNotIn("Compute a fingerprint", text)
        self.assertIn("fingerprint not computed", text)

    def test_every_area_bundle_passes_its_checks(self) -> None:
        for area in bundle.load_catalog()["areas"]:
            files = bundle.build_files(area["id"])
            self.assertEqual(bundle.check_files(files), [], area["id"])
            self.assertIn("ROUTER.md", files)

    def test_area_bundle_unlinks_other_area_skills_and_keeps_text(self) -> None:
        files = bundle.build_files("estate-planning")
        text = files["references/employment-extension-sources.md"].decode()
        self.assertNotIn("track-fair-work-developments/references/watch-register.json)", text)
        self.assertIn("watch-register.json", self.files["references/employment-extension-sources.md"].decode())
        self.assertNotIn("route-legal-fact-pattern", files["ROUTER.md"].decode())

    def test_validator_gates_survive_in_the_bundle(self) -> None:
        text = self.files["skills/triage-legal-enquiry/references/triage-protocol.md"].decode()
        self.assertIn("`--require-approved` validation;", text)
        section = self.files["skills/configure-legal-triage/SKILL.md"].decode().split(bundle.SECTION_HEADING)[1]
        self.assertIn("Never report\n   `VALIDATED APPROVED PROFILE`", section)
        self.assertIn("review date", section)

    def test_no_instruction_to_compute_a_hash_or_fingerprint_survives(self) -> None:
        for name, data in self.files.items():
            if not name.endswith(".md") or name in bundle.HASH_FACT_FILES:
                continue
            in_section = False
            for line in data.decode().splitlines():
                if line.startswith(bundle.SECTION_HEADING):
                    in_section = True
                elif line.startswith("## "):
                    in_section = False
                if bundle.HASH_WORDS.search(line) and not in_section:
                    self.assertTrue(
                        any(phrase in line for phrase in bundle.HASH_ALLOWED), f"{name}: {line.strip()}"
                    )

    def test_zip_is_rooted_and_uses_fixed_times(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = bundle.build(Path(tmp), None, "t")
            with zipfile.ZipFile(path) as archive:
                infos = archive.infolist()
                self.assertTrue(all(i.filename.startswith("legal-skills/") for i in infos))
                self.assertTrue(all(i.date_time == bundle.FIXED_TIME for i in infos))
                self.assertEqual([i.filename for i in infos], sorted(i.filename for i in infos))


class DeterminismTests(unittest.TestCase):
    def build_from_copy(self, tmp: Path, name: str, mtime: int, reverse: bool) -> bytes:
        plugin = tmp / name / "plugin"
        shutil.copytree(bundle.PLUGIN, plugin, ignore=shutil.ignore_patterns("evals", "__pycache__"))
        for path in plugin.rglob("*"):
            os.utime(path, (mtime, mtime))
        with mock.patch.object(bundle, "PLUGIN", plugin), mock.patch.object(bundle, "TEMPLATES", plugin / "ai-tool"):
            files = bundle.build_files(None, "t")
        if reverse:
            files = dict(reversed(list(files.items())))
        out = tmp / name / "out.zip"
        bundle.write_zip(files, out)
        return out.read_bytes()

    def test_zip_bytes_do_not_depend_on_directory_mtime_or_file_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = self.build_from_copy(Path(tmp), "a", 1_000_000_000, False)
            second = self.build_from_copy(Path(tmp), "b", 1_700_000_000, True)
            self.assertEqual(first, second)

    def test_separate_processes_build_identical_zips(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = []
            for name in ("one", "two"):
                subprocess.run(
                    [sys.executable, "-I", str(ROOT / "scripts" / "ai_tool_bundle.py"), "t", "--dist", str(Path(tmp) / name)],
                    check=True,
                    capture_output=True,
                )
                paths.append(Path(tmp) / name / "legal-skills-ai-t.zip")
            self.assertEqual(paths[0].read_bytes(), paths[1].read_bytes())

    def test_write_zip_ignores_dict_order(self) -> None:
        files = {"b.txt": b"1", "a.txt": b"2"}
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "1.zip"
            second = Path(tmp) / "2.zip"
            bundle.write_zip(files, first)
            bundle.write_zip(dict(reversed(list(files.items()))), second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), ["legal-skills/a.txt", "legal-skills/b.txt"])

    def test_write_zip_ignores_the_clock(self) -> None:
        files = {"a.txt": b"1"}
        outputs = []
        with tempfile.TemporaryDirectory() as tmp:
            for index, now in enumerate((1_000_000_000.0, 1_900_000_000.0)):
                fake = time.gmtime(now)
                with (
                    mock.patch.object(time, "time", return_value=now),
                    mock.patch.object(time, "localtime", return_value=fake),
                    mock.patch.object(time, "gmtime", return_value=fake),
                ):
                    path = Path(tmp) / f"{index}.zip"
                    bundle.write_zip(files, path)
                    outputs.append(path.read_bytes())
        self.assertEqual(outputs[0], outputs[1])


class BundleCheckTests(unittest.TestCase):
    def test_flags_unresolved_link(self) -> None:
        problems = bundle.check_files({"a.md": b"[x](missing.md)\n"})
        self.assertTrue(any("does not resolve" in p for p in problems))

    def test_accepts_resolved_link(self) -> None:
        self.assertEqual(bundle.check_files({"a.md": b"[x](b.md)\n", "b.md": b"ok\n"}), [])

    def test_flags_code_and_excluded_path_references(self) -> None:
        for line in (b"run the script\n", b"see `scripts/x`\n", b"open tool.py\n", b"see tests/foo\n", b"use evals/x\n"):
            self.assertTrue(bundle.check_files({"a.md": line}), line)

    def test_flags_instruction_to_compute_a_hash(self) -> None:
        for line in (b"Compute a fingerprint over the table.\n", b"Record the SHA-256 of each APP.\n"):
            self.assertTrue(any("hash or fingerprint" in p for p in bundle.check_files({"a.md": line})), line)

    def test_flags_compute_instruction_even_when_it_mentions_not_computed(self) -> None:
        line = b"Compute the SHA-256 of each APP; if not computed, say so.\n"
        files = {"a.md": b"## AI-tool mode\n\n" + line}
        self.assertTrue(any("hash or fingerprint" in p for p in bundle.check_files(files)))

    def test_flags_code_path_in_json_data(self) -> None:
        self.assertTrue(bundle.check_files({"references/t.json": b'{"note": "see scripts/run.py"}\n'}))

    def test_accepts_hash_wording_that_says_not_computed(self) -> None:
        self.assertEqual(bundle.check_files({"a.md": b"Hash not computed, a person with code computes it.\n"}), [])

    def test_bundle_text_replaces_the_plugin_text(self) -> None:
        text = "x <!-- ai-tool:bundle: new --><!-- ai-tool:code -->old<!-- /ai-tool:code --> y\n"
        self.assertEqual(bundle.strip_code_regions(text), "x new y\n")

    def test_flags_leftover_marker(self) -> None:
        self.assertTrue(bundle.check_files({"a.md": b"<!-- ai-tool:code -->\n"}))

    def test_flags_script_backed_skill_missing_its_section_in_the_bundle(self) -> None:
        files = {"skills/check-nsw-legislation/SKILL.md": b"# No section\n"}
        self.assertTrue(any("AI-tool mode" in p for p in bundle.check_files(files)))

    def test_inline_marker_keeps_the_surrounding_space(self) -> None:
        text = "files<!-- ai-tool:code --> and scripts<!-- /ai-tool:code --> that run\n"
        self.assertEqual(bundle.strip_code_regions(text), "files that run\n")

    def test_strips_code_regions(self) -> None:
        text = "keep\n<!-- ai-tool:code -->\nrun python3 x.py\n<!-- /ai-tool:code -->\nafter\n"
        self.assertEqual(bundle.strip_code_regions(text), "keep\nafter\n")


class SourceCheckTests(unittest.TestCase):
    def make_plugin(self, tmp: str, body: str) -> Path:
        plugin = Path(tmp)
        skill = plugin / "skills" / "demo-skill"
        (skill / "scripts").mkdir(parents=True)
        (skill / "scripts" / "run.py").write_text("print(1)\n", encoding="utf-8")
        (skill / "SKILL.md").write_text(body, encoding="utf-8")
        return plugin

    def test_new_script_backed_skill_without_section_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            plugin = self.make_plugin(tmp, "---\nname: demo-skill\n---\n# Demo\n")
            problems = bundle.source_problems(plugin)
            self.assertTrue(any("AI-tool mode" in p for p in problems))

    def test_script_backed_skill_without_marker_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            plugin = self.make_plugin(tmp, "# Demo\n\n## AI-tool mode\n\nBy hand.\n")
            self.assertTrue(any("ai-tool:code" in p for p in bundle.source_problems(plugin)))

    def test_unbalanced_markers_fail(self) -> None:
        body = "# Demo\n<!-- ai-tool:code -->\nrun\n\n## AI-tool mode\n\nBy hand.\n"
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(any("unbalanced" in p for p in bundle.source_problems(self.make_plugin(tmp, body))))

    def test_marked_skill_without_section_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            plugin = Path(tmp)
            skill = plugin / "skills" / "demo-skill"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("<!-- ai-tool:code -->\nx\n<!-- /ai-tool:code -->\n", encoding="utf-8")
            self.assertTrue(any("no '## AI-tool mode'" in p for p in bundle.source_problems(plugin)))

    def test_script_backed_skill_with_section_passes(self) -> None:
        body = "# Demo\n<!-- ai-tool:code -->\nrun\n<!-- /ai-tool:code -->\n\n## AI-tool mode\n\nBy hand.\n"
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(bundle.source_problems(self.make_plugin(tmp, body)), [])


if __name__ == "__main__":
    unittest.main()
