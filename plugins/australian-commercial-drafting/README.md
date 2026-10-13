# Australian Commercial Drafting

Six practitioner-led workflows prepare first drafts of Australian commercial
documents for a qualified lawyer to review:

- `configure-drafting-profile` records the drafting party and standard positions;
- `draft-nda` prepares mutual or one-way confidentiality terms;
- `draft-website-terms` prepares SaaS or subscription terms for consumers and small businesses;
- `draft-privacy-policy` translates evidenced data practices into policy wording;
- `draft-services-agreement` prepares B2B services terms and a statement of work;
- `review-draft-against-checklist` returns a prioritised issues table.

## Scope and sources

Australian Commonwealth law plus the identified governing state or territory.
Confirm the legal as-at date, jurisdiction, drafting side and facts for each run.
Specialist, regulated, cross-border and employment issues need separate review.
A qualified lawyer must review every output; these workflows do not certify
compliance or replace professional judgment.

Read the [source and control method](references/drafting-source-and-control-method.md)
for official-source verification, currency limits, source provenance and permissions.
Use the [profile schema](references/drafting-profile-schema.md), optional
[original clause bank](references/clause-bank.md) and
[unfair contract terms checklist](references/unfair-contract-terms-checklist.md).
Legal hooks were checked on 13 October 2026; recheck at use. Future automated-decision
privacy duties commencing on 10 December 2026 remain separate from current duties.

## Permissions

No MCP server, app, hook or write integration is bundled. The plugin provides
read-only research and draft text. Saving a profile or draft requires an explicit
user instruction naming a controlled destination; do not overwrite approved source
material. Publishing, sending, signing, executing, filing and updating live systems
are outside these workflows and require separate authority and human review.
Keep client data and licensed precedents in the user's governed system, never here.
Do not send confidential facts or names in public search queries.

## Validation

Each skill has a synthetic eval under `evals/`, including fail-closed scenarios.
Repository tests validate packaging and controls; they do not demonstrate live
model behaviour or installation in either client. Run live evals and clean-client
installation checks separately before describing the plugin as released.

## Licence and provenance

MIT. All workflow and example clause wording is original. Statutes and regulator
publications are linked as official verification sources; no licensed precedent
text is redistributed.

<!-- generated:plugin-dependencies -->
## Plugin dependencies

- `australian-legal-research` (required) — Verifies Commonwealth and state
  legislation at the relevant drafting date.
- `australian-employment-fair-work` (hand-off) — Assesses worker
  classification and sham-contracting concerns before contractor wording is
  settled.
- `australian-privacy-cybersecurity` (hand-off) — Assesses privacy coverage,
  APP obligations and automated-decision transparency.

Install every required plugin with this one. A skill whose required or
hand-off plugin is missing reports the step as not done rather than performing
it from memory.
<!-- end:plugin-dependencies -->
