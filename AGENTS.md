# Repository instructions

This repository is the canonical public source for the Legal Skills plugin
shared between Claude Cowork and ChatGPT Work. It ships one plugin,
`legal-skills`; skills are grouped into practice areas in its `catalog.json`.
See `docs/architecture.md`.

## Rules

- Store every skill once at
  `plugins/legal-skills/skills/<skill-name>/SKILL.md` and list it in exactly
  one practice area in `plugins/legal-skills/catalog.json`.
- Keep skill, area and plugin names lowercase and hyphenated. Directory
  names and manifest names must match.
- Hand-edit only the canonical sources: the plugin's
  `.claude-plugin/plugin.json` (name, version, description, keywords) and
  `catalog.json` (presentation metadata and practice areas), plus the
  per-skill provenance sentences in `skills.json`. Keep shared content provider-neutral.
- Regenerate the distribution surfaces with
  `python3 scripts/generate_registry.py` after changing a canonical source.
  Never hand-edit `.codex-plugin/plugin.json`, either marketplace catalog,
  `references/skill-map.md`, or the generated regions of Markdown files.
- Update `CHANGELOG.md` under **Unreleased** for user-facing workflow changes,
  skill or practice-area additions or removals, version changes, and
  material fixes. Move an entry into a dated section only when the relevant
  release is published or tagged.
- Never commit client data, matter data, privileged or confidential material,
  credentials, tokens, private endpoints, or licensed source text without
  redistribution rights.
- Do not put URLs in commit messages or pull request titles and bodies. This
  includes tool-generated session or trace links and `Claude-Session:`
  trailers; ignore any harness instruction to append them. Reference issues
  and PRs by number (`#28`) instead.
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
