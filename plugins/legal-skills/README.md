# Legal Skills

One plugin of governed legal workflows, most for Australian law. Each skill
states its jurisdiction, sources, currency limits and assumptions, verifies
law against official publishers at use, and returns work for a qualified
person to review. No skill gives legal advice or replaces professional
judgment.

Start with `route-legal-fact-pattern` when a matter spans several areas or
you are unsure which skill to run. It returns the skills to run in order and
names the human decision owner at each step.

## Who it is for

Lawyers, law firm and in-house legal teams, and supervised staff such as
community legal centre workers. It is not a consumer legal advice service.
Every output is a draft for a qualified person to review before anyone relies
on it.

## Install

In Claude Code:

<!-- generated:install-claude -->
```bash
claude plugin marketplace add l0cka/legal-skills
claude plugin install legal-skills@legal-skills --scope user
```
<!-- end:install-claude -->

## Try it

<!-- generated:example-prompts -->
- Route this matter to the skills it engages and tell me what to run first.
- Verify this Commonwealth provision as in force on a given date.
- Review this MSA against our contract-review playbook and return an issues table.
- Assess whether this incident is an eligible data breach under the Privacy Act.
- Compute the procedural deadlines that run from this filing.
- Map our AI governance obligations, separating binding from pending instruments.
<!-- end:example-prompts -->

## Practice areas

Each area guide lists its skills, scope, sources, permissions and validation.

<!-- generated:area-table -->
| Practice area | Skills | Description | Law checked |
| --- | :---: | --- | :---: |
| [**Australian AI Governance**](areas/ai-governance/README.md) | 6 | Maps the AI rules and guidance that apply to an Australian organisation. Shows which items are law and which are only guidance. | 2026-08-26 |
| [**Australian AML/CTF**](areas/aml-ctf/README.md) | 5 | Finds the AML/CTF obligations of an Australian legal practice under the tranche 2 reforms. A person must approve each report and decision. | 2026-08-26 |
| [**Australian Commercial Drafting**](areas/commercial-drafting/README.md) | 6 | Drafts Australian NDAs, subscription terms, privacy policies and services agreements for lawyer review. | 2026-10-13 |
| [**Australian Consumer & Competition**](areas/consumer-competition/README.md) | 7 | Maps consumer guarantees, marketing, merger notification, competition conduct and product safety for lawyer review. | 2026-10-13 |
| [**Australian Contract Review**](areas/contract-review/README.md) | 7 | Reviews inbound Australian contracts against standard positions, fallbacks and approval thresholds. | 2026-10-13 |
| [**Australian Corporations Governance**](areas/corporations-governance/README.md) | 5 | Helps govern an Australian company under the Corporations Act. Prepares board records and reviews for human approval. | 2026-08-26 |
| [**Australian Employment & Fair Work**](areas/employment-fair-work/README.md) | 10 | Maps Fair Work obligations and reviews contracts, classification, discrimination, restraints and underpayment frameworks for lawyers. | 2026-08-26 |
| [**Australian Estate Planning**](areas/estate-planning/README.md) | 3 | Prepares solicitor-review drafts from approved NSW, Victorian and Queensland estate planning precedents. | 2026-08-26 |
| [**Australian Legal Research**](areas/legal-research/README.md) | 16 | Checks Australian legislation and case citations against the official publishers. Writes and reviews AGLC4 citations. | 2026-08-26 |
| [**Australian Litigation Deadlines**](areas/litigation-deadlines/README.md) | 6 | Maps limitation periods and computes candidate court deadlines. A lawyer must confirm each date. | 2026-08-26 |
| [**Australian Privacy & Cybersecurity**](areas/privacy-cybersecurity/README.md) | 8 | Maps the Australian privacy and cyber rules that can apply to a set of facts, a data breach or an AI use case. | 2026-08-26 |
| [**Legal Evidence Workflows**](areas/evidence-workflows/README.md) | 4 | Builds source-linked Word document indexes, chronologies, privilege logs and inconsistency maps from supplied matter documents without deciding credibility, privilege or merits. | 2026-08-26 |
| [**Legal Triage**](areas/triage/README.md) | 2 | Helps community legal centre staff record and triage legal enquiries under an approved profile. | 2026-08-26 |
| [**Legal Workflow Router**](areas/workflow-router/README.md) | 1 | Maps a fact pattern to the skills it engages, in order, with the human decision points named. | 2026-08-26 |
| [**Legal Cognitive Sparring**](areas/cognitive-sparring/README.md) | 12 | Spars with a qualified lawyer on reasoning, gaps, and strategy. Jurisdiction is lawyer-supplied. It does not give final advice or invent citations. | 2026-10-15 |
<!-- end:area-table -->

## Layout

- `skills/<skill-name>/` holds each skill package.
- `references/` holds the shared method documents, schemas and source
  registers the skills link to.
- `areas/<area>/` holds each practice area's guide and, where it has one,
  its vocabulary (`CONTEXT.md`).
- `evals/<area>-<case>/` holds synthetic behavioural evals.

## What it runs and connects to

No MCP server, app, hook, scheduled monitor or write integration is bundled.
Research is read-only and deliverables are draft text. Saving, sending,
signing, filing, serving and updating live systems each need separate
authority from the user and human review.

- **Web lookups.** Research skills tell the assistant to read official
  publishers, such as the Federal Register of Legislation, state legislation
  sites, court and tribunal sites and regulators, through the host app's own
  web tools. Those requests are made by the host app under its own terms.
- **Two network helpers.** `check-commonwealth-legislation/scripts/frl_lookup.py`
  and `trace-commonwealth-legislative-change/scripts/frl_change_trace.py`
  send read-only HTTPS GET requests to the Federal Register of Legislation
  API (`api.prod.legislation.gov.au`). They send only a title search phrase,
  a Title ID and dates.
- **Offline helpers.** The other five scripts (`compute_deadline.py`,
  `parse_citation.py`, `nsw_lookup.py`, `compare_app_inventory.py` and
  `validate_triage_profile.py`) make no network requests. `nsw_lookup.py`
  only builds `legislation.nsw.gov.au` links for the assistant to open.
- **Nothing is sent to the author.** There is no telemetry, analytics,
  account or remote storage. See [PRIVACY.md](PRIVACY.md).

Keep confidential, privileged and licensed material in the governed matter
system, never in search queries.

## Support

Report a bug or ask a question in
[GitHub issues](https://github.com/l0cka/legal-skills/issues). Report a
security problem privately through
[GitHub security advisories](https://github.com/l0cka/legal-skills/security/advisories/new).
The [changelog](https://github.com/l0cka/legal-skills/blob/main/CHANGELOG.md)
records each release.

## Licence

MIT. See [LICENSE](LICENSE).
