![Legal Skills banner](docs/assets/legal-skills-banner.png)

<p align="center">
  <a href="https://github.com/l0cka/legal-skills/actions/workflows/ci.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/l0cka/legal-skills/ci.yml?branch=main&amp;style=flat-square&amp;label=CI"></a>
  <a href="LICENSE"><img alt="MIT licence" src="https://img.shields.io/badge/licence-MIT-1f6f5f?style=flat-square"></a>
  <img alt="Seven plugins" src="https://img.shields.io/badge/plugins-7-31547a?style=flat-square">
  <img alt="Forty-eight skills" src="https://img.shields.io/badge/skills-48-31547a?style=flat-square">
  <img alt="Claude Cowork and ChatGPT Work" src="https://img.shields.io/badge/works%20with-Claude%20Cowork%20%2B%20ChatGPT%20Work-c59a46?style=flat-square">
</p>

# Legal Skills

Legal Skills is an open-source marketplace for portable legal-workflow plugins.
The marketplace supplies the same skills to Claude Cowork and ChatGPT Work.
Each provider has a small, separate manifest.

## Plugin suite

The marketplace contains seven plugins and forty-eight skills:

| Plugin | Skills | What it does | Boundaries |
| --- | :---: | --- | --- |
| [**Australian Legal Research**](plugins/australian-legal-research/README.md) | 16 | <ul><li>Verifies Commonwealth, State, and Territory legislation against each jurisdiction's official publisher, with point-in-time, commencement, currency, and authorisation qualifications</li><li>Verifies case citations, judgments, and quoted passages against the issuing courts' official publishers</li><li>Drafts, converts, reviews, and corrects AGLC4 citations and bibliographies</li></ul> | <ul><li>Flags citations absent from a court's own database as fabrication risks, kept separate from citations that simply cannot be checked</li><li>Never bypasses publisher bot challenges</li><li>Never invents a missing citation field</li><li>Excludes treatment analysis</li></ul> |
| [**Legal Triage**](plugins/legal-triage/README.md) | 2 | <ul><li>Configures a centre-approved staff triage profile</li><li>Prepares provisional enquiry records with limited client information</li><li>Escalates urgent or uncertain matters</li></ul> | <ul><li>Conflict checks stay outside the model</li><li>Authorized staff make every consequential decision</li></ul> |
| [**Australian Privacy & Cybersecurity**](plugins/australian-privacy-cybersecurity/README.md) | 8 | <ul><li>Maps facts to potentially applicable Australian privacy and cyber legislation</li><li>Assesses suspected data breaches and AI-system use cases</li><li>Verifies the applicable APP framework, records a framework fingerprint, and detects changes across the decision horizon</li></ul> | <ul><li>No fixed-list assumption about the framework</li><li>Relies on Australian Legal Research for authoritative point-in-time checks</li><li>Excludes case law</li></ul> |
| [**Australian Corporations Governance**](plugins/australian-corporations-governance/README.md) | 5 | <ul><li>Configures a controlled company governance profile</li><li>Issue-spots director-duty and conflict controls</li><li>Prepares draft board-decision records</li><li>Reviews governance frameworks and builds source-linked calendars</li><li>Separates listed, APRA, ACNC, and CATSI overlays</li></ul> | <ul><li>Never approves, files, executes, or invents corporate action</li></ul> |
| [**Australian AI Governance**](plugins/australian-ai-governance/README.md) | 6 | <ul><li>Configures a controlled AI-governance profile</li><li>Maps binding versus pending instruments for an AI use case</li><li>Issue-spots board and director-duty AI exposure</li><li>Checks documentation against the AI6, VAISS, and AS ISO/IEC 42001 layers</li><li>Routes government AI use to nine jurisdictional assurance tracks</li><li>Monitors the pending-instrument watch-list</li></ul> | <ul><li>Never asserts pending law as in force</li><li>Labels superseded and voluntary guidance layers</li><li>Routes privacy and board-process depth to the sibling plugins</li><li>Never certifies compliance with any standard</li></ul> |
| [**Australian AML/CTF**](plugins/australian-aml-ctf/README.md) | 5 | <ul><li>Configures a controlled AML/CTF practice profile for legal practices</li><li>Maps described legal services to the table 6 designated services under the tranche 2 reforms</li><li>Issue-spots AML/CTF programs and customer-due-diligence frameworks against the Act and the AML/CTF Rules 2025</li><li>Maps reporting triggers with legal-professional-privilege carve-outs and LPP-form mechanics</li><li>Monitors the pending AUSTRAC guidance watch-list</li></ul> | <ul><li>Legal practices only — other tranche 2 sectors and tranche 1 entities fail closed to human review</li><li>Never enrols, lodges or submits anything to AUSTRAC</li><li>Never performs customer due diligence or concludes a matter is suspicious</li><li>Never concludes that privilege applies — privilege calls go to the responsible lawyer</li></ul> |
| [**Australian Litigation Deadlines**](plugins/australian-litigation-deadlines/README.md) | 6 | <ul><li>Maps described causes of action to candidate limitation periods across all nine jurisdictions with special-regime flags and a conservative earliest-candidate marker</li><li>Computes candidate procedural and tribunal deadlines with a bundled deterministic script over evidence-gated rule tables and verified NSW and Victorian holiday tables</li><li>Maintains a source-linked matter deadline register and verifies the rule tables against official publishers with an evidence fingerprint</li></ul> | <ul><li>Every date is provisional until the responsible lawyer confirms it — the plugin is not a diary or practice-management system</li><li>The model never performs date arithmetic; unexpressible or unverified periods fail closed to identify-only output</li><li>Never determines accrual, discoverability or extension prospects</li><li>Criminal procedure and foreign limitation law are excluded; migration outputs always carry a specialist-review warning</li></ul> |

## Install with your Agent

If your Agent can manage plugins, copy this request. Then paste it into the
Agent.

```text
Add the plugin marketplace `l0cka/legal-skills`, then install its seven
plugins: `australian-legal-research`, `legal-triage`,
`australian-privacy-cybersecurity`, `australian-corporations-governance`,
`australian-ai-governance`, `australian-aml-ctf`, and
`australian-litigation-deadlines` (all `@legal-skills`, user scope if
supported). Leave other marketplaces and plugins unchanged. Verify all
seven are available and report the result. If you cannot manage plugins,
give me the exact manual steps and stop.
```

### Install from a terminal

For Codex, run:

```bash
codex plugin marketplace add l0cka/legal-skills
codex plugin add australian-legal-research@legal-skills
codex plugin add legal-triage@legal-skills
codex plugin add australian-privacy-cybersecurity@legal-skills
codex plugin add australian-corporations-governance@legal-skills
codex plugin add australian-ai-governance@legal-skills
codex plugin add australian-aml-ctf@legal-skills
codex plugin add australian-litigation-deadlines@legal-skills
```

For Claude, run:

```bash
claude plugin marketplace add l0cka/legal-skills
claude plugin install australian-legal-research@legal-skills --scope user
claude plugin install legal-triage@legal-skills --scope user
claude plugin install australian-privacy-cybersecurity@legal-skills --scope user
claude plugin install australian-corporations-governance@legal-skills --scope user
claude plugin install australian-ai-governance@legal-skills --scope user
claude plugin install australian-aml-ctf@legal-skills --scope user
claude plugin install australian-litigation-deadlines@legal-skills --scope user
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
