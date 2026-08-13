# Adding a plugin

## 1. Define the workflow

Record the plugin name, intended users, legal task, jurisdiction, authoritative
sources, expected output, known limitations, and required human review. Decide
whether any connector or write action is necessary.

## 2. Create the canonical package

```text
plugins/<plugin-name>/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    └── <skill-name>/
        ├── SKILL.md
        ├── references/       # optional
        ├── scripts/          # optional
        └── assets/           # optional
```

Names must use lowercase words separated by hyphens. Each `SKILL.md` needs
frontmatter whose `name` matches its directory.

## 3. Add provider wrappers

Use the same plugin name, semantic version, description, author, repository,
licence, keywords, and `./skills/` path in both manifests. Add presentation
metadata only where the provider supports it. Declare apps, MCP servers, hooks,
or other components only when the corresponding files exist.

## 4. Register the package

Add the plugin to:

- `.agents/plugins/marketplace.json`
- `.claude-plugin/marketplace.json`

Add every skill to `skills.json`. The owning plugin and plugin version must
match the manifests.

## 5. Validate

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests
git diff --check
```

Then test a clean installation in Claude Cowork and ChatGPT Work before
describing the plugin as released.
