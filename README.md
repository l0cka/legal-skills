![Legal Skills banner](docs/assets/legal-skills-banner.png)

<p align="center">
  <a href="https://github.com/l0cka/legal-skills/actions/workflows/ci.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/l0cka/legal-skills/ci.yml?branch=main&amp;style=flat-square&amp;label=CI"></a>
  <a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-1f6f5f?style=flat-square"></a>
  <img alt="Four plugins" src="https://img.shields.io/badge/plugins-4-31547a?style=flat-square">
  <img alt="Thirty-one skills" src="https://img.shields.io/badge/skills-31-31547a?style=flat-square">
  <img alt="Claude Cowork and ChatGPT Work" src="https://img.shields.io/badge/works%20with-Claude%20Cowork%20%2B%20ChatGPT%20Work-c59a46?style=flat-square">
</p>

# Legal Skills

Legal Skills is an open-source marketplace for portable legal-workflow plugins.
The marketplace supplies the same skills to Claude Cowork and ChatGPT Work.
Each provider has a small, separate manifest.

## Plugin suite

The marketplace contains four plugins and thirty-one skills:

| Plugin | Skills | What it does | Boundaries |
| --- | :---: | --- | --- |
| [**Australian Legal Research**](plugins/australian-legal-research/README.md) | 16 | Verifies Commonwealth, State, and Territory legislation against each jurisdiction's official publisher, with point-in-time, commencement, currency, and authorisation qualifications. Verifies case citations, judgments, and quoted passages against the issuing courts' official publishers. Drafts, converts, reviews, and corrects AGLC4 citations and bibliographies. | Flags citations absent from a court's own database as fabrication risks and keeps them separate from citations that simply cannot be checked. Never bypasses publisher bot challenges, never invents a missing citation field. Excludes treatment analysis. |
| [**Legal Triage**](plugins/legal-triage/README.md) | 2 | Configures a centre-approved staff triage profile, prepares provisional enquiry records with limited client information, and escalates urgent or uncertain matters. | Conflict checks stay outside the model. Authorized staff make every consequential decision. |
| [**Australian Privacy & Cybersecurity**](plugins/australian-privacy-cybersecurity/README.md) | 8 | Maps facts to potentially applicable Australian privacy and cyber legislation. Assesses suspected data breaches and AI-system use cases. Verifies the applicable APP framework, records a framework fingerprint, and detects changes across the decision horizon. | No fixed-list assumption about the framework. Relies on Australian Legal Research for authoritative point-in-time checks. Excludes case law. |
| [**Australian Corporations Governance**](plugins/australian-corporations-governance/README.md) | 5 | Configures a controlled company governance profile, issue-spots director-duty and conflict controls, prepares draft board-decision records, reviews governance frameworks, and builds source-linked calendars. Separates listed, APRA, ACNC, and CATSI overlays. | Never approves, files, executes, or invents corporate action. |

## Install with your Agent

If your Agent can manage plugins, copy this request. Then paste it into the
Agent.

```text
Install the Legal Skills plugin suite in this environment.

1. Add the marketplace `l0cka/legal-skills`.
2. Install `australian-legal-research@legal-skills`.
3. Install `legal-triage@legal-skills`.
4. Install `australian-privacy-cybersecurity@legal-skills`.
5. Install `australian-corporations-governance@legal-skills`.
6. Keep all other marketplaces and plugins unchanged.
7. Use user scope if this client supports installation scopes.
8. Verify that all four plugins are available and report the result.

If you cannot manage plugins, give me the exact manual steps and stop.
```

### Install from a terminal

For Codex, run:

```bash
codex plugin marketplace add l0cka/legal-skills
codex plugin add australian-legal-research@legal-skills
codex plugin add legal-triage@legal-skills
codex plugin add australian-privacy-cybersecurity@legal-skills
codex plugin add australian-corporations-governance@legal-skills
```

For Claude, run:

```bash
claude plugin marketplace add l0cka/legal-skills
claude plugin install australian-legal-research@legal-skills --scope user
claude plugin install legal-triage@legal-skills --scope user
claude plugin install australian-privacy-cybersecurity@legal-skills --scope user
claude plugin install australian-corporations-governance@legal-skills --scope user
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
