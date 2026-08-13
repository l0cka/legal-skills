# Legal Skills

Legal Skills is an open-source marketplace for portable legal-workflow plugins.
Each plugin is designed to package the same skills for Claude Cowork and
ChatGPT Work while keeping provider-specific manifests thin and separate.

## Plugin suite

The marketplace contains one plugin and one skill:

- **Commonwealth Legislation** — checks the identity, status and applicable
  point-in-time version of Commonwealth Acts and registered instruments against
  the official Federal Register of Legislation. It reports Register IDs and
  currency qualifications instead of treating "current" as a binary label.

## Install

Add the marketplace and plugin independently in each provider's development
client:

```bash
codex plugin marketplace add l0cka/legal-skills
codex plugin add commonwealth-legislation@legal-skills

claude plugin marketplace add l0cka/legal-skills
claude plugin install commonwealth-legislation@legal-skills --scope user
```

Claude users can also add `l0cka/legal-skills` from Cowork's personal plugin
marketplace interface. ChatGPT Work availability remains subject to the user's
plan and workspace plugin settings; the `.agents` catalog is the OpenAI-side
marketplace package.

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

Each plugin uses this structure:

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
plugin versions, skill frontmatter, and the canonical registry.

Run the focused tests:

```bash
python3 -m unittest discover -s tests
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/adding-a-plugin.md](docs/adding-a-plugin.md). Repository architecture and
provider boundaries are described in [docs/architecture.md](docs/architecture.md).

## Licence

MIT. See [LICENSE](LICENSE).
