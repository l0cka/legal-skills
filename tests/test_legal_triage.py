from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = (
    ROOT
    / "plugins"
    / "legal-triage"
    / "skills"
    / "configure-legal-triage"
)
SCRIPT = SKILL_ROOT / "scripts" / "validate_triage_profile.py"
TEMPLATE = SKILL_ROOT / "assets" / "centre-profile.template.json"
TRIAGE_SKILL = (
    ROOT
    / "plugins"
    / "legal-triage"
    / "skills"
    / "triage-legal-enquiry"
    / "SKILL.md"
)
PROTOCOL = TRIAGE_SKILL.parent / "references" / "triage-protocol.md"

SPEC = importlib.util.spec_from_file_location("validate_triage_profile", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class LegalTriageProfileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.template = json.loads(TEMPLATE.read_text(encoding="utf-8"))

    def approved_profile(self) -> dict:
        profile = copy.deepcopy(self.template)
        profile["profile"]["status"] = "approved"
        profile["profile"]["centre_name"] = "Example Community Legal Centre"
        profile["profile"]["jurisdictions"] = ["New South Wales"]
        profile["profile"]["intended_staff_roles"] = ["Intake lawyer"]
        profile["governance"] = {
            "approved_by": "Responsible solicitor",
            "approved_at": "2026-08-13",
            "review_due": "2099-12-31",
        }
        for policy in profile["policies"]:
            policy["title"] = f"Example {policy['category']} policy"
            policy["version"] = "1.0"
            policy["owner"] = "Principal solicitor"
            policy["source"] = f"Controlled source for {policy['policy_id']}"
            policy["review_due"] = "2099-12-31"
        for referral in profile["referrals"]:
            referral["name"] = "Example Referral Service"
            referral["scope"] = "Example verified service scope"
            referral["jurisdictions"] = ["New South Wales"]
            referral["contact"] = "Public referral contact"
            referral["source"] = "Official service directory"
            referral["review_due"] = "2099-12-31"
        profile["data_handling"]["approved_environment"] = (
            "Approved enterprise workspace"
        )
        profile["human_review"]["responsible_role"] = "Supervising solicitor"
        profile["conflict_check"]["responsible_role"] = "Intake lawyer"
        area = profile["service_rules"]["service_areas"][0]
        area["name"] = "General civil law"
        area["jurisdictions"] = ["New South Wales"]
        factor = profile["service_rules"]["eligibility_factors"][0]
        factor["question"] = "Does the enquiry meet the approved service criteria?"
        exclusion = profile["service_rules"]["exclusions"][0]
        exclusion["description"] = "Excluded by the approved service scope"
        pathway = profile["escalation_pathways"][0]
        pathway["trigger"] = "A listed event is due within two business days"
        pathway["action"] = "Escalate immediately to the supervising solicitor"
        pathway["availability"] = "Business hours with an approved fallback"
        return profile

    def test_template_is_structurally_valid_but_not_live(self) -> None:
        warnings = VALIDATOR.validate_profile(
            self.template, today=date(2026, 8, 14)
        )
        self.assertIn("must not be used for live triage", warnings[0])
        with self.assertRaises(VALIDATOR.ProfileValidationError):
            VALIDATOR.validate_profile(
                self.template,
                require_approved=True,
                today=date(2026, 8, 14),
            )

    def test_current_approved_profile_passes_live_validation(self) -> None:
        warnings = VALIDATOR.validate_profile(
            self.approved_profile(),
            require_approved=True,
            today=date(2026, 8, 14),
        )
        self.assertEqual(warnings, [])

    def test_profile_fails_if_public_ai_can_receive_personal_information(self) -> None:
        profile = self.approved_profile()
        profile["data_handling"]["public_ai_personal_information"] = True
        with self.assertRaisesRegex(
            VALIDATOR.ProfileValidationError,
            "public_ai_personal_information",
        ):
            VALIDATOR.validate_profile(profile, today=date(2026, 8, 14))

    def test_live_profile_rejects_placeholder_content(self) -> None:
        profile = self.approved_profile()
        profile["profile"]["centre_name"] = "Replace with centre name"
        with self.assertRaisesRegex(
            VALIDATOR.ProfileValidationError, "placeholder content"
        ):
            VALIDATOR.validate_profile(
                profile,
                require_approved=True,
                today=date(2026, 8, 14),
            )

    def test_profile_rejects_client_fields(self) -> None:
        profile = self.approved_profile()
        profile["client_name"] = "Do not store this"
        with self.assertRaisesRegex(
            VALIDATOR.ProfileValidationError, "do not belong in a profile"
        ):
            VALIDATOR.validate_profile(profile, today=date(2026, 8, 14))

    def test_profile_requires_a_semantic_profile_version(self) -> None:
        profile = self.approved_profile()
        profile["profile"]["profile_version"] = "version one"
        with self.assertRaisesRegex(
            VALIDATOR.ProfileValidationError, "expected a semantic version"
        ):
            VALIDATOR.validate_profile(profile, today=date(2026, 8, 14))

    def test_profile_fails_if_policy_or_referral_is_stale(self) -> None:
        profile = self.approved_profile()
        profile["policies"][0]["effective_date"] = "2026-01-01"
        profile["policies"][0]["review_due"] = "2026-08-13"
        with self.assertRaisesRegex(
            VALIDATOR.ProfileValidationError, "policy review is overdue"
        ):
            VALIDATOR.validate_profile(
                profile,
                require_approved=True,
                today=date(2026, 8, 14),
            )

    def test_cli_reports_draft_warning_and_rejects_live_use(self) -> None:
        draft = subprocess.run(
            [sys.executable, str(SCRIPT), str(TEMPLATE)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(draft.returncode, 0)
        self.assertIn("WARNING", draft.stdout)

        live = subprocess.run(
            [sys.executable, str(SCRIPT), str(TEMPLATE), "--require-approved"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(live.returncode, 1)
        self.assertIn("must be approved for live triage", live.stderr)

    def test_cli_accepts_current_approved_profile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "approved-profile.json"
            path.write_text(
                json.dumps(self.approved_profile()), encoding="utf-8"
            )
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path), "--require-approved"],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("passed validation", result.stdout)


class LegalTriageSkillTests(unittest.TestCase):
    def test_skill_preserves_staff_and_human_review_boundaries(self) -> None:
        text = " ".join(TRIAGE_SKILL.read_text(encoding="utf-8").split())
        for phrase in (
            "staff-facing only",
            "HUMAN TRIAGE REQUIRED",
            "facts already supplied indicate apparent urgent risk",
            "Do not give legal advice",
            "Do not describe a person as ineligible",
            "Do not write to CLASS",
            "Never request or reproduce party names",
        ):
            self.assertIn(phrase, text)

    def test_protocol_contains_all_governed_statuses(self) -> None:
        text = PROTOCOL.read_text(encoding="utf-8")
        for status in VALIDATOR.ALLOWED_RESULT_STATUSES:
            self.assertIn(status, text)

    def test_plugin_has_no_connector_or_write_component(self) -> None:
        for provider in ("codex", "claude"):
            manifest_path = (
                ROOT
                / "plugins"
                / "legal-triage"
                / f".{provider}-plugin"
                / "plugin.json"
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertNotIn("apps", manifest)
            self.assertNotIn("mcpServers", manifest)
            self.assertNotIn("hooks", manifest)
        codex_manifest = json.loads(
            (
                ROOT
                / "plugins"
                / "legal-triage"
                / ".codex-plugin"
                / "plugin.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(codex_manifest["interface"]["capabilities"], ["Read"])


if __name__ == "__main__":
    unittest.main()
