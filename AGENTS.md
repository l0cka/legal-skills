# Repository instructions

This repository is the canonical public source for Legal Skills plugins shared
between Claude Cowork and ChatGPT Work.

## Rules

- Store every skill once at
  `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.
- Keep skill and plugin names lowercase and hyphenated. Directory names and
  manifest names must match.
- Give each plugin paired `.codex-plugin/plugin.json` and
  `.claude-plugin/plugin.json` manifests. Keep shared content provider-neutral.
- Register every plugin in both marketplace catalogs and every skill in
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
python3 -m unittest discover -s tests
git diff --check
```

All three commands must pass before a change is published.
