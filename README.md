![Legal Skills banner](docs/assets/legal-skills-banner.png)

<p align="center">
  <a href="https://github.com/l0cka/legal-skills/actions/workflows/ci.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/l0cka/legal-skills/ci.yml?branch=main&amp;style=flat-square&amp;label=CI"></a>
  <a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-1f6f5f?style=flat-square"></a>
  <!-- generated:badges -->
  <img alt="Eight plugins" src="https://img.shields.io/badge/plugins-8-31547a?style=flat-square">
  <img alt="Fifty-one skills" src="https://img.shields.io/badge/skills-51-31547a?style=flat-square">
  <img alt="Claude Cowork and ChatGPT Work" src="https://img.shields.io/badge/works%20with-Claude%20Cowork%20%2B%20ChatGPT%20Work-c59a46?style=flat-square">
<!-- end:badges -->
</p>

# Legal Skills

Legal Skills is an open-source marketplace for portable legal-workflow plugins.
The marketplace supplies the same skills to Claude Cowork and ChatGPT Work.
Each provider has a small, separate manifest.

## Plugin suite

<!-- generated:counts -->
The marketplace contains eight plugins and fifty-one skills:
<!-- end:counts -->

<!-- generated:plugin-table -->
| Plugin | Skills | Description |
| --- | :---: | --- |
| [**Australian AI Governance**](plugins/australian-ai-governance/README.md) | 6 | Maps the AI rules and guidance that apply to an Australian organisation. Shows which items are law and which are only guidance. |
| [**Australian AML/CTF**](plugins/australian-aml-ctf/README.md) | 5 | Finds the AML/CTF obligations of an Australian legal practice under the tranche 2 reforms. A person must approve each report and decision. |
| [**Australian Corporations Governance**](plugins/australian-corporations-governance/README.md) | 5 | Helps govern an Australian company under the Corporations Act. Prepares board records and reviews for human approval. |
| [**Australian Estate Planning**](plugins/australian-estate-planning/README.md) | 3 | Profiles uploaded NSW and Victorian estate precedents, then fills confirmed sites safely. Source precedents remain unchanged. |
| [**Australian Legal Research**](plugins/australian-legal-research/README.md) | 16 | Checks Australian legislation and case citations against the official publishers. Writes and reviews AGLC4 citations. |
| [**Australian Litigation Deadlines**](plugins/australian-litigation-deadlines/README.md) | 6 | Maps limitation periods and computes candidate court deadlines. A lawyer must confirm each date. |
| [**Australian Privacy & Cybersecurity**](plugins/australian-privacy-cybersecurity/README.md) | 8 | Maps the Australian privacy and cyber rules that can apply to a set of facts, a data breach or an AI use case. |
| [**Legal Triage**](plugins/legal-triage/README.md) | 2 | Helps community legal centre staff record and triage legal enquiries under an approved profile. |
<!-- end:plugin-table -->

## Install with your Agent

If your Agent can manage plugins, copy this request. Then paste it into the
Agent.

<!-- generated:install-agent -->
```text
Add the plugin marketplace `l0cka/legal-skills` and install all eight of
its plugins (user scope if supported). Verify the plugins are available
and report the result.
```
<!-- end:install-agent -->

### Install from a terminal

For Codex, run:

<!-- generated:install-codex -->
```bash
codex plugin marketplace add l0cka/legal-skills
codex plugin add australian-ai-governance@legal-skills
codex plugin add australian-aml-ctf@legal-skills
codex plugin add australian-corporations-governance@legal-skills
codex plugin add australian-estate-planning@legal-skills
codex plugin add australian-legal-research@legal-skills
codex plugin add australian-litigation-deadlines@legal-skills
codex plugin add australian-privacy-cybersecurity@legal-skills
codex plugin add legal-triage@legal-skills
```
<!-- end:install-codex -->

For Claude, run:

<!-- generated:install-claude -->
```bash
claude plugin marketplace add l0cka/legal-skills
claude plugin install australian-ai-governance@legal-skills --scope user
claude plugin install australian-aml-ctf@legal-skills --scope user
claude plugin install australian-corporations-governance@legal-skills --scope user
claude plugin install australian-estate-planning@legal-skills --scope user
claude plugin install australian-legal-research@legal-skills --scope user
claude plugin install australian-litigation-deadlines@legal-skills --scope user
claude plugin install australian-privacy-cybersecurity@legal-skills --scope user
claude plugin install legal-triage@legal-skills --scope user
```
<!-- end:install-claude -->

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
