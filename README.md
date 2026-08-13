![Legal Skills banner](docs/assets/legal-skills-banner.png)

<p align="center">
  <a href="https://github.com/l0cka/legal-skills/actions/workflows/ci.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/l0cka/legal-skills/ci.yml?branch=main&amp;style=flat-square&amp;label=CI"></a>
  <a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-1f6f5f?style=flat-square"></a>
  <img alt="Three plugins" src="https://img.shields.io/badge/plugins-3-31547a?style=flat-square">
  <img alt="Twenty skills" src="https://img.shields.io/badge/skills-20-31547a?style=flat-square">
  <img alt="Claude Cowork and ChatGPT Work" src="https://img.shields.io/badge/works%20with-Claude%20Cowork%20%2B%20ChatGPT%20Work-c59a46?style=flat-square">
</p>

# Legal Skills

Legal Skills is an open-source marketplace for portable legal-workflow plugins.
Each plugin is designed to package the same skills for Claude Cowork and
ChatGPT Work while keeping provider-specific manifests thin and separate.

## Plugin suite

The marketplace contains three plugins and twenty skills:

- **Australian Legislation** — checks Commonwealth, State and Territory law
  against each jurisdiction's official publisher. It preserves point-in-time,
  commencement, currency and authorisation qualifications, and includes a
  separate Commonwealth legislative-change tracing workflow.
- **Legal Triage** — configures a centre-approved, staff-facing triage profile
  and prepares provisional enquiry records against it. It minimises client
  information, keeps conflict checks outside the model, escalates urgency and
  uncertainty, and reserves every consequential decision for authorised staff.
- **Australian Privacy & Cybersecurity** — maps facts to potentially applicable
  Australian privacy and cyber legislation and assesses suspected data
  breaches and AI-system use cases. It verifies and fingerprints the applicable
  APP framework without assuming a fixed list, detects change across the
  decision horizon, uses the Australian Legislation plugin for authoritative
  point-in-time checks, and excludes case law.

## Install

Add the marketplace and plugin independently in each provider's development
client:

```bash
codex plugin marketplace add l0cka/legal-skills
codex plugin add australian-legislation@legal-skills
codex plugin add legal-triage@legal-skills
codex plugin add australian-privacy-cybersecurity@legal-skills

claude plugin marketplace add l0cka/legal-skills
claude plugin install australian-legislation@legal-skills --scope user
claude plugin install legal-triage@legal-skills --scope user
claude plugin install australian-privacy-cybersecurity@legal-skills --scope user
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
