# Repository instructions

This repository is the canonical public source for Legal Skills plugins shared
between Claude Cowork and ChatGPT Work.

## Rules

- Store every skill once at
  `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.
- Keep skill and plugin names lowercase and hyphenated. Directory names and
  manifest names must match.
- Hand-edit only the canonical sources: each plugin's
  `.claude-plugin/plugin.json` (name, version, description, keywords) and
  `catalog.json` (presentation metadata), plus the per-skill `source`
  sentences in `skills.json`. Keep shared content provider-neutral.
- Regenerate the distribution surfaces with
  `python3 scripts/generate_registry.py` after changing a canonical source.
  Never hand-edit `.codex-plugin/plugin.json`, either marketplace catalog,
  `plugins/README.md`, the generated README regions, or the derived fields of
  `skills.json`.
- Update `CHANGELOG.md` under **Unreleased** for user-facing workflow changes,
  plugin additions or removals, version changes, and material fixes. Move an
  entry into a dated section only when the relevant release is published or
  tagged.
- Never commit client data, matter data, privileged or confidential material,
  credentials, tokens, private endpoints, or licensed source text without
  redistribution rights.
- State jurisdiction, source provenance, currency limits, assumptions, and
  human-review requirements where they affect a legal workflow.
- Do not present discovery leads as legal authority or claim that a workflow
  replaces professional judgment.
- Keep detailed optional material in directly linked `references/` files.
- Preserve upstream attribution and licence notices for imported material.
- Do not add MCP servers, apps, hooks, or write actions without documenting
  their permissions and approval boundaries.

## Completion gate

Run:

```bash
python3 scripts/validate_repository.py
python3 scripts/generate_registry.py --check
python3 -m unittest discover -s tests
git diff --check
```

All four commands must pass before a change is published.
