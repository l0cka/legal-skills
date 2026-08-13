# Legal Skills

Legal Skills is an open-source marketplace for portable legal-workflow plugins.
Each plugin is designed to package the same skills for Claude Cowork and
ChatGPT Work while keeping provider-specific manifests thin and separate.

## Status

The marketplace structure is ready, but no plugins have been published yet.
Installation instructions will be added with the first plugin release.

## Principles

- Legal workflows must be transparent about jurisdiction, currency, sources,
  assumptions, and human-review requirements.
- Skills must not contain client information, matter information, credentials,
  privileged material, or confidential firm content.
- Shared instructions live once. Provider manifests wrap that canonical
  content without creating divergent copies.
- External tools start read-only where practical. Write actions require clear
  approval boundaries.
- Discovery material is not authority. Legal propositions must be grounded in
  appropriate primary or otherwise authoritative sources.

## Repository layout

```text
legal-skills/
├── .agents/plugins/marketplace.json   # ChatGPT and Codex marketplace
├── .claude-plugin/marketplace.json    # Claude marketplace
├── plugins/                           # canonical plugin packages
├── skills.json                        # portable skill registry
├── scripts/validate_repository.py     # offline validation
└── docs/
```

When the first plugin is added, its structure will be:

```text
plugins/<plugin-name>/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
└── skills/<skill-name>/SKILL.md
```

## Validate

```bash
python3 scripts/validate_repository.py
```

The validator checks both marketplace catalogs, paired provider manifests,
plugin versions, skill frontmatter, and the canonical registry. It deliberately
accepts an empty marketplace while the first plugin is being designed.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/adding-a-plugin.md](docs/adding-a-plugin.md). Repository architecture and
provider boundaries are described in [docs/architecture.md](docs/architecture.md).

## Licence

MIT. See [LICENSE](LICENSE).
