from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "legal-skills"
CATALOG = json.loads((PLUGIN / "catalog.json").read_text(encoding="utf-8"))
AREAS = {area["id"]: area for area in CATALOG["areas"]}


def area_skills(area: str) -> list[str]:
    return list(AREAS[area]["skills"])


def area_skill_files(area: str) -> list[Path]:
    return [PLUGIN / "skills" / skill / "SKILL.md" for skill in area_skills(area)]


def eval_case_files() -> list[Path]:
    return sorted((PLUGIN / "evals").glob("*/case.yaml"))


def load_case(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def area_cases(area: str) -> list[dict[str, Any]]:
    return [load_case(path) for path in sorted((PLUGIN / "evals").glob(f"{area}-*/case.yaml"))]


def case_prompt(case: dict[str, Any]) -> str:
    return case["execution"]["prompt"]


def area_dir(area: str) -> Path:
    return PLUGIN / "areas" / area


def area_markdown(area: str) -> list[Path]:
    files = [path for skill in area_skills(area) for path in (PLUGIN / "skills" / skill).rglob("*.md")]
    return sorted(files + list(area_dir(area).glob("*.md")))
