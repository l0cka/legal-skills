# Consumer and competition source and control method

## Scope and currency

Australian Commonwealth CCA and ACL workflows, with the relevant state or territory
application legislation and product-sector regimes checked independently. Confirm
legal as-at date, conduct/supply/acquisition dates, jurisdiction, intended use horizon
and responsible lawyer before assessment. The 2026-10-13 snapshot is a research snapshot, not a cached rule.
Assumptions about coverage, markets, consumer status and transaction structure remain
explicit and unresolved until supported. A qualified lawyer must review every output.

## Source hierarchy

Use `$check-commonwealth-legislation` for the Act, Regulations, instruments and
commencement; `$trace-commonwealth-legislative-change` for amendments and transition.
Use the [official source register](official-source-register.md) for statutory leads
and verify each citation there in the relying session. Check applicable state or
territory legislation at its official publisher. A missing research skill is a step
not done; name its plugin and leave affected propositions not verified.

Label ACCC and Product Safety material as regulator guidance, not legislation.
Verify instrument text at legislation.gov.au even where ACCC explains it. Record
source title, URL, compilation or instrument ID, provision and pinpoint, effective
date, retrieved date, relevant observation and evidence state. Treat search results and model memory as discovery material, never authority.
Do not infer commencement from a landing page's generic 'in force' badge, assent,
a press release or a proposed date. Separate current law, enacted but uncommenced
law, proposals, guidance and allegations in enforcement announcements. Court orders
and reasons require verification through `$route-case-citation`.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  amendment, application, jurisdiction or fact qualification remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

A missing official text, decisive fact or temporal application blocks the affected
conclusion. Say 'verify against <official source>' and record the missing step.
Do not turn a search snippet into a VERIFIED statement or conclude that no law
exists merely because a search found none. Urgent safety escalation can proceed
while legal conclusions remain unresolved.

## Profile control and reuse

Read the [profile schema](consumer-competition-profile-schema.md). Reuse the
employment profile schema and `$configure-employment-profile` for the control fields
and steps enumerated in the profile schema, not an employment assessment or consumer
or competition coverage. If profile content conflicts with a verified source, surface the conflict and stop the affected conclusion.
The model may draft a profile but cannot mark it approved. Unknown facts remain
unknown; each supplied fact has a source, confirmer, date and evidence state.

Use Australian Commercial Drafting's unfair-contract-terms checklist and UTPA 2026
notes via `$review-draft-against-checklist` and `$draft-website-terms`; use
`$draft-services-agreement` for drafting. Do not duplicate those checklists here.
Route privacy/data-driven advertising to `$assess-australian-privacy-issues` and
future decision transparency to `$assess-automated-decision-transparency`.
Missing hand-off skills mean hand-off not made, with plugin to install stated.

## Human control

Outputs lead with a result status and give a source-linked issue matrix, facts,
assumptions, gaps, urgency, affected outputs and decisions for a named qualified
lawyer. Never certify lawfulness, issue final advice, compute a binding deadline
from uncertain events or act externally. Read-only research and draft text are
permitted; saving to a named controlled location requires user authority. Filing,
publication, payment, acquisition completion, regulator contact, competitor contact
and recall execution need separate authority. Keep client material out of Git and
public searches. Never silently change a published watch register or approved profile.
