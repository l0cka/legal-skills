#!/usr/bin/env python3
"""Validate a centre-local Legal Triage profile without network access."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
ALLOWED_PROFILE_STATUSES = {"draft", "approved", "retired"}
REQUIRED_POLICY_CATEGORIES = {
    "service-scope",
    "urgent-escalation",
    "conflict-checking",
    "privacy-and-client-information",
    "referrals",
}
ALLOWED_RESULT_STATUSES = [
    "URGENT HUMAN ESCALATION",
    "HUMAN TRIAGE REQUIRED",
    "PROVISIONAL SERVICE PATHWAY",
    "OUTSIDE CONFIGURED SCOPE",
    "INSUFFICIENT INFORMATION",
]
FORBIDDEN_PROFILE_KEYS = {
    "client_name",
    "client_email",
    "client_phone",
    "date_of_birth",
    "home_address",
    "party_names",
    "matter_narrative",
    "document_number",
}
PLACEHOLDER_MARKERS = (
    "replace with",
    "replace before approval",
    "not yet approved",
)


class ProfileValidationError(Exception):
    """Raised when a profile violates the Legal Triage contract."""


def require_object(value: Any, location: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ProfileValidationError(f"{location}: expected an object")
    return value


def require_list(value: Any, location: str) -> list[Any]:
    if not isinstance(value, list) or not value:
        raise ProfileValidationError(f"{location}: expected a non-empty array")
    return value


def require_string(value: Any, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProfileValidationError(f"{location}: expected a non-empty string")
    return value.strip()


def require_slug(value: Any, location: str) -> str:
    text = require_string(value, location)
    if not SLUG.fullmatch(text):
        raise ProfileValidationError(
            f"{location}: expected lowercase letters, digits and hyphens"
        )
    return text


def require_semver(value: Any, location: str) -> str:
    text = require_string(value, location)
    if not SEMVER.fullmatch(text):
        raise ProfileValidationError(f"{location}: expected a semantic version")
    return text


def require_true(value: Any, location: str) -> None:
    if value is not True:
        raise ProfileValidationError(f"{location}: must be true")


def require_false(value: Any, location: str) -> None:
    if value is not False:
        raise ProfileValidationError(f"{location}: must be false")


def parse_iso_date(value: Any, location: str) -> date:
    text = require_string(value, location)
    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise ProfileValidationError(
            f"{location}: expected a real date in YYYY-MM-DD format"
        ) from exc


def require_string_list(value: Any, location: str) -> list[str]:
    items = require_list(value, location)
    return [require_string(item, f"{location}[]") for item in items]


def reject_client_fields(value: Any, location: str = "profile") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_PROFILE_KEYS:
                raise ProfileValidationError(
                    f"{location}.{key}: client or matter fields do not belong in a profile"
                )
            reject_client_fields(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_client_fields(child, f"{location}[{index}]")


def find_placeholders(value: Any, location: str = "root") -> list[str]:
    matches: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            matches.extend(find_placeholders(child, f"{location}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            matches.extend(find_placeholders(child, f"{location}[{index}]"))
    elif isinstance(value, str):
        lowered = value.strip().lower()
        if lowered == "draft" or any(marker in lowered for marker in PLACEHOLDER_MARKERS):
            matches.append(location)
    return matches


def require_unique(values: list[str], location: str) -> None:
    if len(values) != len(set(values)):
        raise ProfileValidationError(f"{location}: identifiers must be unique")


def validate_profile(
    payload: dict[str, Any],
    *,
    require_approved: bool = False,
    today: date | None = None,
) -> list[str]:
    """Validate a decoded profile and return non-fatal warnings."""

    today = today or date.today()
    if payload.get("schema_version") != 1:
        raise ProfileValidationError("schema_version: must be 1")
    reject_client_fields(payload)

    profile = require_object(payload.get("profile"), "profile")
    require_slug(profile.get("profile_id"), "profile.profile_id")
    require_semver(profile.get("profile_version"), "profile.profile_version")
    require_string(profile.get("centre_name"), "profile.centre_name")
    require_string_list(profile.get("jurisdictions"), "profile.jurisdictions")
    require_string_list(
        profile.get("intended_staff_roles"), "profile.intended_staff_roles"
    )
    status = require_string(profile.get("status"), "profile.status")
    if status not in ALLOWED_PROFILE_STATUSES:
        raise ProfileValidationError(
            "profile.status: expected draft, approved or retired"
        )

    governance = require_object(payload.get("governance"), "governance")
    policies = require_list(payload.get("policies"), "policies")
    policy_ids: list[str] = []
    policy_categories: set[str] = set()
    policy_review_dates: list[tuple[str, date]] = []
    for index, raw_policy in enumerate(policies):
        location = f"policies[{index}]"
        policy = require_object(raw_policy, location)
        policy_id = require_slug(policy.get("policy_id"), f"{location}.policy_id")
        policy_ids.append(policy_id)
        category = require_string(policy.get("category"), f"{location}.category")
        policy_categories.add(category)
        for field in ("title", "version", "owner", "source"):
            require_string(policy.get(field), f"{location}.{field}")
        effective = parse_iso_date(
            policy.get("effective_date"), f"{location}.effective_date"
        )
        review_due = parse_iso_date(
            policy.get("review_due"), f"{location}.review_due"
        )
        if review_due < effective:
            raise ProfileValidationError(
                f"{location}.review_due: cannot precede effective_date"
            )
        policy_review_dates.append((policy_id, review_due))
    require_unique(policy_ids, "policies[].policy_id")
    missing_categories = REQUIRED_POLICY_CATEGORIES - policy_categories
    if missing_categories:
        missing = ", ".join(sorted(missing_categories))
        raise ProfileValidationError(f"policies: missing categories: {missing}")
    known_policy_ids = set(policy_ids)

    data_handling = require_object(payload.get("data_handling"), "data_handling")
    require_true(data_handling.get("staff_facing_only"), "data_handling.staff_facing_only")
    require_string(
        data_handling.get("approved_environment"),
        "data_handling.approved_environment",
    )
    require_true(data_handling.get("minimum_necessary"), "data_handling.minimum_necessary")
    require_true(
        data_handling.get("client_notice_required"),
        "data_handling.client_notice_required",
    )
    require_false(
        data_handling.get("public_ai_personal_information"),
        "data_handling.public_ai_personal_information",
    )
    require_false(
        data_handling.get("model_training_with_client_data"),
        "data_handling.model_training_with_client_data",
    )
    require_false(
        data_handling.get("model_may_write_client_record"),
        "data_handling.model_may_write_client_record",
    )

    human_review = require_object(payload.get("human_review"), "human_review")
    require_true(human_review.get("required"), "human_review.required")
    require_string(human_review.get("responsible_role"), "human_review.responsible_role")
    require_true(human_review.get("can_override"), "human_review.can_override")
    require_false(
        human_review.get("automated_rejection_allowed"),
        "human_review.automated_rejection_allowed",
    )

    conflict = require_object(payload.get("conflict_check"), "conflict_check")
    require_true(conflict.get("required"), "conflict_check.required")
    require_true(
        conflict.get("performed_outside_model"),
        "conflict_check.performed_outside_model",
    )
    require_false(conflict.get("party_names_in_model"), "conflict_check.party_names_in_model")
    require_string(conflict.get("responsible_role"), "conflict_check.responsible_role")

    service_rules = require_object(payload.get("service_rules"), "service_rules")
    service_areas = require_list(
        service_rules.get("service_areas"), "service_rules.service_areas"
    )
    service_area_ids: list[str] = []
    for index, raw_area in enumerate(service_areas):
        location = f"service_rules.service_areas[{index}]"
        area = require_object(raw_area, location)
        service_area_ids.append(
            require_slug(area.get("service_area_id"), f"{location}.service_area_id")
        )
        require_string(area.get("name"), f"{location}.name")
        require_string_list(area.get("jurisdictions"), f"{location}.jurisdictions")
        require_policy_reference(area, location, known_policy_ids)
    require_unique(service_area_ids, "service_rules.service_areas[].service_area_id")

    eligibility = require_list(
        service_rules.get("eligibility_factors"),
        "service_rules.eligibility_factors",
    )
    factor_ids: list[str] = []
    for index, raw_factor in enumerate(eligibility):
        location = f"service_rules.eligibility_factors[{index}]"
        factor = require_object(raw_factor, location)
        factor_ids.append(
            require_slug(factor.get("factor_id"), f"{location}.factor_id")
        )
        require_string(factor.get("question"), f"{location}.question")
        require_policy_reference(factor, location, known_policy_ids)
        require_true(
            factor.get("human_decision_required"),
            f"{location}.human_decision_required",
        )
    require_unique(factor_ids, "service_rules.eligibility_factors[].factor_id")

    exclusions = require_list(
        service_rules.get("exclusions"), "service_rules.exclusions"
    )
    exclusion_ids: list[str] = []
    for index, raw_exclusion in enumerate(exclusions):
        location = f"service_rules.exclusions[{index}]"
        exclusion = require_object(raw_exclusion, location)
        exclusion_ids.append(
            require_slug(exclusion.get("exclusion_id"), f"{location}.exclusion_id")
        )
        require_string(exclusion.get("description"), f"{location}.description")
        require_policy_reference(exclusion, location, known_policy_ids)
        require_true(exclusion.get("referral_required"), f"{location}.referral_required")
    require_unique(exclusion_ids, "service_rules.exclusions[].exclusion_id")

    pathways = require_list(payload.get("escalation_pathways"), "escalation_pathways")
    pathway_ids: list[str] = []
    for index, raw_pathway in enumerate(pathways):
        location = f"escalation_pathways[{index}]"
        pathway = require_object(raw_pathway, location)
        pathway_ids.append(
            require_slug(pathway.get("pathway_id"), f"{location}.pathway_id")
        )
        for field in ("trigger", "action", "availability"):
            require_string(pathway.get(field), f"{location}.{field}")
        require_policy_reference(pathway, location, known_policy_ids)
    require_unique(pathway_ids, "escalation_pathways[].pathway_id")

    referrals = require_list(payload.get("referrals"), "referrals")
    referral_ids: list[str] = []
    referral_review_dates: list[tuple[str, date]] = []
    for index, raw_referral in enumerate(referrals):
        location = f"referrals[{index}]"
        referral = require_object(raw_referral, location)
        referral_id = require_slug(
            referral.get("referral_id"), f"{location}.referral_id"
        )
        referral_ids.append(referral_id)
        for field in ("name", "scope", "contact", "source"):
            require_string(referral.get(field), f"{location}.{field}")
        require_string_list(referral.get("jurisdictions"), f"{location}.jurisdictions")
        verified_at = parse_iso_date(
            referral.get("verified_at"), f"{location}.verified_at"
        )
        review_due = parse_iso_date(
            referral.get("review_due"), f"{location}.review_due"
        )
        if review_due < verified_at:
            raise ProfileValidationError(
                f"{location}.review_due: cannot precede verified_at"
            )
        referral_review_dates.append((referral_id, review_due))
        if not isinstance(referral.get("warm_referral_available"), bool):
            raise ProfileValidationError(
                f"{location}.warm_referral_available: expected true or false"
            )
        require_true(referral.get("consent_required"), f"{location}.consent_required")
    require_unique(referral_ids, "referrals[].referral_id")

    output = require_object(payload.get("output_control"), "output_control")
    if output.get("allowed_statuses") != ALLOWED_RESULT_STATUSES:
        raise ProfileValidationError(
            "output_control.allowed_statuses: must preserve the five governed statuses in order"
        )
    require_true(
        output.get("human_approval_required"),
        "output_control.human_approval_required",
    )
    require_true(output.get("reasons_required"), "output_control.reasons_required")
    require_true(
        output.get("policy_citations_required"),
        "output_control.policy_citations_required",
    )

    warnings: list[str] = []
    if status != "approved":
        warnings.append("profile is not approved and must not be used for live triage")

    if require_approved:
        if status != "approved":
            raise ProfileValidationError(
                "profile.status: must be approved for live triage"
            )
        placeholders = find_placeholders(payload)
        if placeholders:
            raise ProfileValidationError(
                f"{placeholders[0]}: placeholder content is not allowed for live triage"
            )
        require_string(governance.get("approved_by"), "governance.approved_by")
        approved_at = parse_iso_date(
            governance.get("approved_at"), "governance.approved_at"
        )
        review_due = parse_iso_date(
            governance.get("review_due"), "governance.review_due"
        )
        if review_due < approved_at:
            raise ProfileValidationError(
                "governance.review_due: cannot precede approved_at"
            )
        if approved_at > today:
            raise ProfileValidationError(
                "governance.approved_at: approval date cannot be in the future"
            )
        if review_due < today:
            raise ProfileValidationError("governance.review_due: profile review is overdue")
        for policy_id, policy_review_due in policy_review_dates:
            if policy_review_due < today:
                raise ProfileValidationError(
                    f"policies[{policy_id}].review_due: policy review is overdue"
                )
        for referral_id, referral_review_due in referral_review_dates:
            if referral_review_due < today:
                raise ProfileValidationError(
                    f"referrals[{referral_id}].review_due: referral review is overdue"
                )
    return warnings


def require_policy_reference(
    item: dict[str, Any], location: str, known_policy_ids: set[str]
) -> None:
    policy_id = require_slug(
        item.get("source_policy_id"), f"{location}.source_policy_id"
    )
    if policy_id not in known_policy_ids:
        raise ProfileValidationError(
            f"{location}.source_policy_id: unknown policy {policy_id}"
        )


def load_profile(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ProfileValidationError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ProfileValidationError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    return require_object(payload, "root")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a centre-local Legal Triage profile."
    )
    parser.add_argument("profile", type=Path, help="Path to profile JSON")
    parser.add_argument(
        "--require-approved",
        action="store_true",
        help="also require current approval, policies and referrals for live use",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        warnings = validate_profile(
            load_profile(args.profile), require_approved=args.require_approved
        )
    except (OSError, ProfileValidationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("VALID: Legal Triage profile passed validation.")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
