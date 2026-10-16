# Legal Skills

One plugin of governed legal workflows, most for Australian law. Each skill
states its jurisdiction, sources, currency limits and assumptions, verifies
law against official publishers at use, and returns work for a qualified
person to review. No skill gives legal advice or replaces professional
judgment.

Start with `route-legal-fact-pattern` when a matter spans several areas or
you are unsure which skill to run. It returns the skills to run in order and
names the human decision owner at each step.

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

## Permissions

No MCP server, app, hook, scheduled monitor or write integration is bundled.
Research is read-only and deliverables are draft text. Saving, sending,
signing, filing, serving and updating live systems each need separate
authority from the user and human review. Keep confidential, privileged and
licensed material in the governed matter system, never in search queries.
