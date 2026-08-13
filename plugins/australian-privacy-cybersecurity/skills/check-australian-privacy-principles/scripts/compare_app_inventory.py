#!/usr/bin/env python3
"""Validate and compare complete APP inventories from official compilations."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import unicodedata
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


VERIFIED = "APP FRAMEWORK VERIFIED"
CHANGE_DETECTED = "APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED"
NOT_VERIFIED = "APP FRAMEWORK NOT VERIFIED – DO NOT RELY"


class InventoryError(ValueError):
    """Raised when an APP inventory cannot support verification."""


def normalize_text(value: str) -> str:
    """Normalize Unicode and insignificant whitespace before fingerprinting."""
    return " ".join(unicodedata.normalize("NFC", value).split())


def require_string(data: dict[str, Any], key: str, location: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise InventoryError(f"{location}.{key}: required non-empty string")
    return value.strip()


def validate_date(value: str, location: str) -> str:
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise InventoryError(f"{location}: expected YYYY-MM-DD") from exc
    return value


def validate_source_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or parsed.hostname not in {
        "legislation.gov.au",
        "www.legislation.gov.au",
    }:
        raise InventoryError(
            "source_url: expected an HTTPS Federal Register of Legislation URL"
        )
    return value


def validate_inventory(data: Any) -> dict[str, Any]:
    """Return a sanitized inventory with fingerprints instead of source text."""
    if not isinstance(data, dict):
        raise InventoryError("inventory root: expected object")

    title_id = require_string(data, "title_id", "inventory")
    compilation_id = require_string(data, "compilation_id", "inventory")
    as_at = validate_date(require_string(data, "as_at", "inventory"), "inventory.as_at")
    source_url = validate_source_url(require_string(data, "source_url", "inventory"))

    coverage = data.get("coverage")
    if not isinstance(coverage, dict):
        raise InventoryError("inventory.coverage: expected object")
    if coverage.get("schedule") != "Schedule 1":
        raise InventoryError("inventory.coverage.schedule: expected Schedule 1")
    if coverage.get("complete") is not True:
        raise InventoryError("inventory.coverage.complete: must be true")
    method = require_string(coverage, "method", "inventory.coverage")

    principles = data.get("principles")
    if not isinstance(principles, list) or not principles:
        raise InventoryError("inventory.principles: expected non-empty array")

    sanitized: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, principle in enumerate(principles):
        location = f"inventory.principles[{index}]"
        if not isinstance(principle, dict):
            raise InventoryError(f"{location}: expected object")
        identifier = normalize_text(require_string(principle, "identifier", location))
        if identifier in seen:
            raise InventoryError(f"{location}.identifier: duplicate {identifier!r}")
        seen.add(identifier)
        heading = normalize_text(require_string(principle, "heading", location))
        text = normalize_text(require_string(principle, "text", location))
        clause_range_value = principle.get("clause_range", "")
        if not isinstance(clause_range_value, str):
            raise InventoryError(f"{location}.clause_range: expected string")
        sanitized.append(
            {
                "identifier": identifier,
                "heading": heading,
                "clause_range": normalize_text(clause_range_value),
                "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            }
        )

    return {
        "title_id": title_id,
        "compilation_id": compilation_id,
        "as_at": as_at,
        "source_url": source_url,
        "coverage": {
            "schedule": "Schedule 1",
            "complete": True,
            "method": method,
        },
        "principles": sanitized,
    }


def compare_inventories(earlier: Any, later: Any) -> dict[str, Any]:
    """Compare two validated inventories and return a fail-closed result."""
    before = validate_inventory(earlier)
    after = validate_inventory(later)
    before_by_id = {item["identifier"]: item for item in before["principles"]}
    after_by_id = {item["identifier"]: item for item in after["principles"]}

    added = [
        after_by_id[item_id]
        for item_id in after_by_id.keys() - before_by_id.keys()
    ]
    removed = [
        before_by_id[item_id]
        for item_id in before_by_id.keys() - after_by_id.keys()
    ]
    modified: list[dict[str, Any]] = []
    for item_id in before_by_id.keys() & after_by_id.keys():
        changed_fields = [
            field
            for field in ("heading", "clause_range", "text_sha256")
            if before_by_id[item_id][field] != after_by_id[item_id][field]
        ]
        if changed_fields:
            modified.append(
                {
                    "identifier": item_id,
                    "changed_fields": changed_fields,
                    "earlier": before_by_id[item_id],
                    "later": after_by_id[item_id],
                }
            )

    before_common = [
        item["identifier"]
        for item in before["principles"]
        if item["identifier"] in after_by_id
    ]
    after_common = [
        item["identifier"]
        for item in after["principles"]
        if item["identifier"] in before_by_id
    ]
    reordered = before_common != after_common
    changed = bool(added or removed or modified or reordered)

    return {
        "status": CHANGE_DETECTED if changed else VERIFIED,
        "comparison": {
            "earlier": {
                "compilation_id": before["compilation_id"],
                "as_at": before["as_at"],
                "source_url": before["source_url"],
            },
            "later": {
                "compilation_id": after["compilation_id"],
                "as_at": after["as_at"],
                "source_url": after["source_url"],
            },
            "compilation_changed": (
                before["compilation_id"] != after["compilation_id"]
            ),
        },
        "changes": {
            "added": sorted(added, key=lambda item: item["identifier"]),
            "removed": sorted(removed, key=lambda item: item["identifier"]),
            "modified": sorted(modified, key=lambda item: item["identifier"]),
            "reordered": reordered,
            "earlier_order": before_common if reordered else [],
            "later_order": after_common if reordered else [],
        },
        "warning": (
            "This comparison detects Schedule 1 text and structure changes only; "
            "it does not establish commencement, legal effect, coverage, "
            "exemptions or interpretation."
        ),
    }


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise InventoryError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise InventoryError(
            f"invalid JSON in {path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("inventory", type=Path)
    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("earlier", type=Path)
    compare_parser.add_argument("later", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            result = {
                "status": VERIFIED,
                "inventory": validate_inventory(load_json(args.inventory)),
                "warning": (
                    "Inventory validation does not establish substantive APP "
                    "compliance or legal effect."
                ),
            }
        else:
            result = compare_inventories(
                load_json(args.earlier), load_json(args.later)
            )
    except (OSError, InventoryError) as exc:
        print(json.dumps({"status": NOT_VERIFIED, "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
