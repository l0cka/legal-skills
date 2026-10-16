# Review playbook schema

Reuse Australian Commercial Drafting's `drafting-profile-schema.md` through
`$configure-drafting-profile` for party identity, style and existing positions;
reuse Australian Employment Fair Work's `employment-profile-schema.md` governance
pattern through `$configure-employment-profile`. Those areas own their schemas.
This schema adds review-specific fields rather than copying either source.

| Field | Required control |
| --- | --- |
| Identity and version | Profile ID, version, owner, draft/approved/retired status, review date |
| Review perimeter | Reviewing side, contract families, sectors, governing state/territory, legal as-at and intended use dates |
| Source profiles | Owner skill, profile/version, approval evidence, fields reused and conflicts |
| Risk appetite | Authorised tolerance by risk category; unknown until instructed |
| Clause positions | Clause type, context, preferred wording/position, rationale, acceptable fallback and unacceptable trigger |
| Approval thresholds | Quantitative basis/currency/period and non-financial triggers, approving role, delegation evidence and escalation route |
| Field provenance | Source document/clause or instruction, date, named confirmer, evidence state and qualification |
| Approval evidence | Human approving role, date and approved version; blank for a newly prepared draft |
| Changes | Previous version, authorised departures, unresolved conflicts, reviewer and review triggers |

Keep transaction-specific facts in an instruction table with source, date and
confirmer; do not silently promote a negotiated one-off into standing policy.
Compare legally permitted choices against commercial preferences separately.
Standard positions must not override mandatory law. An approved drafting profile
is not automatically an approved review playbook: threshold and fallback owners
must confirm the mapped review authority. No approval can be inferred from silence.

For triage, green means all material terms fit evidenced approved positions and
no decisive uncertainty remains. Yellow requires a bounded fallback/review decision.
Red requires escalation or identifies a material gap; it does not establish illegality.
No colour authorises execution. Profiles contain no matter/client data in this repo.
