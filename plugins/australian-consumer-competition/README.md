# Australian Consumer & Competition

Seven practitioner-led skills configure a consumer and competition profile,
assess consumer guarantees, review marketing claims, map merger notification,
assess cartel and resale price maintenance risk, map product safety obligations
and track ACCC developments.

## Scope and sources

Australian Commonwealth competition law and the Australian Consumer Law (ACL),
with state and territory application and sectoral overlays verified per matter.
The snapshot is 2026-10-13; it is not a currency guarantee. A qualified lawyer
must review every result and decide application, remedies, reporting and action.
The workflows do not replace professional judgment or certify compliance.

Read the [source and control method](references/consumer-competition-source-and-control-method.md),
[profile schema](references/consumer-competition-profile-schema.md),
[official source register](references/official-source-register.md) and
[merger pathway checklist](references/merger-pathways.md).
The [watch register](skills/track-accc-developments/references/watch-register.json)
is an on-demand research snapshot. Current rules and future reforms stay separate.

Reuse Australian Commercial Drafting's unfair-contract-terms checklist and UTPA
2026 notes through `review-draft-against-checklist` and `draft-website-terms`;
use `draft-services-agreement` for operative services wording. Reuse the controlled
profile pattern of `configure-employment-profile` and its employment profile
schema without importing employment-law conclusions. Privacy issues belong to
`assess-australian-privacy-issues` and `assess-automated-decision-transparency`.

## Permissions

No MCP servers, apps, hooks or write integrations are bundled. Research and draft
outputs only. Saving requires an explicit instruction naming a controlled destination.
Never overwrite an approved profile, publish advertising, change prices, complete
an acquisition, contact competitors, lodge notifications, report to regulators,
or commence a recall. Those actions require separate authority and human review.
Never put client data, personal information, licensed text or confidential facts in
this public repository or public search queries.

## Verification

Repository gates check packaging and fixtures. Synthetic evals cover all seven
skills, including unavailable-source and unsafe-instruction scenarios. They have
not been run against live clients; installation and live model behaviour require
separate evaluation. There is no executable application build for this plugin.

## Licence and provenance

MIT. Original workflows and checklists, with official legislation and regulator
publications linked for verification. No licensed precedent text is redistributed.

<!-- generated:plugin-dependencies -->
## Plugin dependencies

- `australian-legal-research` (required) — Verifies legislation, instruments,
  commencement and case-law leads at official publishers.
- `australian-commercial-drafting` (hand-off) — Reuses the UCT checklist, UTPA
  2026 notes and operative website/services drafting.
- `australian-employment-fair-work` (hand-off) — Reuses controlled profile
  approval and versioning patterns without importing coverage conclusions.
- `australian-privacy-cybersecurity` (hand-off) — Assesses advertising data,
  decision transparency and safety-incident privacy issues.

Install every required plugin with this one. A skill whose required or
hand-off plugin is missing reports the step as not done rather than performing
it from memory.
<!-- end:plugin-dependencies -->
