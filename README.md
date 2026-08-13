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
The marketplace supplies the same skills to Claude Cowork and ChatGPT Work.
Each provider has a small, separate manifest.

## Plugin suite

The marketplace contains three plugins and twenty skills:

- **Australian Legislation** checks Commonwealth, State, and Territory law
  against each jurisdiction's official publisher. It records qualifications
  about point-in-time status, commencement, currency, and authorisation. It
  also traces changes to Commonwealth legislation.
- **Legal Triage** configures a staff triage profile that the responsible
  centre has approved. It prepares provisional enquiry records and limits client
  information. It keeps conflict checks outside the model. It escalates urgent
  or uncertain matters. Authorized staff make every consequential decision.
- **Australian Privacy & Cybersecurity** maps facts to potentially applicable
  Australian privacy and cyber legislation. It assesses suspected data breaches
  and AI-system use cases. It verifies the applicable APP framework without a
  fixed-list assumption. It records a framework fingerprint and detects changes
  across the decision horizon. It uses the Australian Legislation plugin for
  authoritative point-in-time checks. It excludes case law.

## Install with your Agent

If your Agent can manage plugins, copy this request. Then paste it into the
Agent.

```text
Install the Legal Skills plugin suite in this environment.

1. Add the marketplace `l0cka/legal-skills`.
2. Install `australian-legislation@legal-skills`.
3. Install `legal-triage@legal-skills`.
4. Install `australian-privacy-cybersecurity@legal-skills`.
5. Keep all other marketplaces and plugins unchanged.
6. Use user scope if this client supports installation scopes.
7. Verify that all three plugins are available.
8. Report the actions and the verification result.

If you cannot manage plugins, give me the exact manual steps and stop.
```

### Install from a terminal

For Codex, run:

```bash
codex plugin marketplace add l0cka/legal-skills
codex plugin add australian-legislation@legal-skills
codex plugin add legal-triage@legal-skills
codex plugin add australian-privacy-cybersecurity@legal-skills
```

For Claude, run:

```bash
claude plugin marketplace add l0cka/legal-skills
claude plugin install australian-legislation@legal-skills --scope user
claude plugin install legal-triage@legal-skills --scope user
claude plugin install australian-privacy-cybersecurity@legal-skills --scope user
```

Claude users can also add `l0cka/legal-skills` from the personal plugin
marketplace in Cowork.

ChatGPT Work availability depends on the user's plan and workspace plugin
settings. The `.agents` catalog is the OpenAI marketplace package.

## Principles

- Legal workflows must state their jurisdiction, currency, sources,
  assumptions, and human-review requirements.
- Skills must not contain client information, matter information, credentials,
  privileged material, or confidential firm content.
- Shared instructions must have one canonical copy. Provider manifests must
  wrap that copy without creating different versions.
- External tools must start in read-only mode when practical. Write actions
  require clear approval boundaries.
- Discovery material is not authority. Legal propositions must use appropriate
  primary or authoritative sources.

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
├── README.md
└── skills/
    └── <skill-name>/
        ├── SKILL.md
        ├── agents/openai.yaml    # required
        ├── references/           # optional
        ├── scripts/              # optional
        └── assets/               # optional
```

## Validate

```bash
python3 scripts/validate_repository.py
```

The validator checks both marketplace catalogs and the paired provider
manifests. It also checks plugin versions, skill frontmatter, and the canonical
registry.

Run the focused tests:

```bash
python3 -m unittest discover -s tests
```

## Contributing

Use [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/adding-a-plugin.md](docs/adding-a-plugin.md) for contribution
instructions. [docs/architecture.md](docs/architecture.md) explains the
repository architecture and provider boundaries. [CHANGELOG.md](CHANGELOG.md)
records the release history.

## Licence

MIT. See [LICENSE](LICENSE).
