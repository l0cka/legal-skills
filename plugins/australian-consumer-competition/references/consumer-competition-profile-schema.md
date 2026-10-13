# Consumer and competition profile schema

Reuse the controlled version/approval fields from Australian Employment & Fair
Work's employment profile schema and `configure-employment-profile`. This schema
adds consumer and competition facts, not a second approval mechanism.

| Field | Required content |
| --- | --- |
| Control | Profile ID, version, draft/approved/retired status, factual as-at date, review due, human approver role and timestamp; model sets draft only and leaves approval blank |
| Scope | Australian jurisdictions, entity and group structure, operations, business roles, conduct dates, decision horizon, responsible lawyer |
| Products and supply | Goods/services descriptions, supplier/manufacturer/importer roles, channels, customer cohorts, price evidence, purposes, exclusions claimed, sector regulators |
| Consumer dealings | Warranty documents, complaints, failure/repair records, purchase journeys, contracts and standard-form positions by version |
| Marketing | Claim owners, substantiation records, environmental methodology, comparison baseline, campaign dates, fee and subscription design |
| Competition | Market hypotheses, competitors, distribution restraints, pricing autonomy, meetings and information-sharing controls, asserted immunities with evidence |
| Acquisitions | Parties/connected entities, proposed shares/assets/control, Australian nexus, financial years, Australian revenue, global value, historical acquisitions and dates, land/supermarket facts, exemptions and waiver records |
| Safety | Products/batches, standards/bans asserted, testing evidence, incidents, awareness events, recalls, reporting and escalation owners |
| Controls | Source/version/date/confirmer/evidence state for each fact, unresolved assumptions, authoritative sources, specialist hand-offs and review triggers |

Use yes/no/unknown for coverage and applicability claims. Never infer no from
missing information or use turnover/headcount labels as verified legal thresholds.
Store authorised drafts only in the user's controlled system, never in this repository.
Approval of a profile does not approve advice, publication, reporting or completion.
