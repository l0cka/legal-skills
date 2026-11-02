# Australian Work Health & Safety

Five skills map work health and safety duty holders, prepare an urgent
preliminary assessment of a workplace incident, review the evidence of officer
due diligence, gap-check psychosocial risk controls and track WHS developments.

- `map-whs-duties` selects the governing Act for each workplace and maps every
  PCBU, shared duty, officer question, worker duty and consultation duty.
- `assess-notifiable-incident` puts the notification and site-preservation
  steps first, then tests each notifiable category for the governing Act.
- `assess-officer-due-diligence` maps board and governance evidence to each
  element of the officer duty and lists gaps and board questions.
- `review-psychosocial-risk-controls` checks a risk register and policies
  against the psychosocial regulations and approved code for the jurisdiction.
- `track-whs-developments` checks the watch register, including each
  jurisdiction's adoption of the December 2025 model incident notification
  amendments.

## Scope and sources

The harmonised Work Health and Safety Acts of the Commonwealth, the states and
the territories, and Victoria's Occupational Health and Safety Act 2004, with
their regulations and approved codes of practice or compliance codes. The
snapshot is 2026-10-28; it is not a currency guarantee. A qualified lawyer must
review every result and decide notification, breach, due diligence, adequacy
of controls and any regulator response. The workflows do not replace
professional judgment or certify compliance.

Read the [source and control method](../../references/whs-source-and-control-method.md)
and the [WHS framework reference](../../references/whs-framework.md), which
records exactly what was checked on the snapshot date and which rows remain
leads. The [watch register](../../skills/track-whs-developments/references/watch-register.json)
is an on-demand research snapshot. Model-law amendments stay separate from the
law in force in each jurisdiction.

Workers compensation, criminal defence strategy, coronial matters and the
specialist safety regimes (mining, petroleum, rail, maritime, aviation,
dangerous goods, electrical licensing, explosives) are outside scope.

## Reuse of other areas

Each skill verifies legislation with the jurisdiction's checker from Australian
Legal Research. An approved employment profile from `configure-employment-profile`
can supply entity and workforce facts; there is no separate WHS profile.
Employment consequences of an incident go to the employment-fair-work skills,
the Sex Discrimination Act positive duty to `assess-discrimination-and-positive-duty`,
general director duties to `assess-director-duties-governance`, and any dated
period to `compute-procedural-deadlines`.

## Permissions

No MCP servers, apps, hooks or write integrations are bundled. Research and
draft outputs only. Never notify or correspond with a regulator, respond to an
inspector or notice, disturb or release an incident site, or contact a worker,
union, health and safety representative or family. Those actions require
separate authority and human review. Never put client data, personal or health
information, or confidential incident facts in this public repository or in
public search queries.

## Verification

Repository gates check packaging, fixtures and the area's legal invariants.
Synthetic evals cover all five skills, including an incident where the urgent
block must come first, a Victorian matter where model WHS sections must not be
applied, and an officer review that must not conclude due diligence. They have
not been run against live clients; installation and live model behaviour
require separate evaluation. There is no executable application build for this
area.

## Licence and provenance

MIT. Original workflows, with official legislation, Safe Work Australia and
regulator publications linked for verification. No licensed text is
redistributed.
