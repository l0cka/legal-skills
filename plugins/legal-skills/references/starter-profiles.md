# Starter profiles

Fictional starting points for each profile, to edit with the matching
`configure-*` skill. Read the [profile guide](profile-guide.md) first.

Every value below is an invented example for a business that does not
exist. None is legal content, a recommended position or a default. Replace
each value with the organisation's own fact, or write `unknown`. Approval
fields are blank on purpose: only an authorised person can complete them.
The schema named under each heading remains the authority for the fields.

## Litigation deadlines

Schema: [deadline-profile-schema.md](deadline-profile-schema.md). Skill:
`configure-litigation-deadline-profile`.

```yaml
profile:
  identifier: example-deadlines
  version: 1
  approved_by:
  approved_date:

practice:
  jurisdictions: [NSW, Cth]
  forums: [Supreme Court of NSW, District Court of NSW, NCAT, Federal Court of Australia]
  matter_types: [commercial disputes, debt recovery]

confirmation:
  confirmer: EXAMPLE - principal solicitor
  diary_system: EXAMPLE - practice management system court diary
  confirmation_note: >
    Computed dates are provisional until entered and confirmed in the
    diary system by the confirmer.

verification:
  posture: per-matter
```

## Employment and Fair Work

Schema: [employment-profile-schema.md](employment-profile-schema.md). Skill:
`configure-employment-profile`.

| Field | Example value |
| --- | --- |
| Profile ID | example-employer |
| Profile version | 1 |
| Status | draft |
| Employer label | Example Cafe Group |
| Entity type | company |
| Jurisdictions of operation | NSW, Qld |
| As-at date | 2026-11-09 |
| Approved by role | |
| Approved at | |
| Review due | 2027-05-09 |
| National system employer | yes; basis claimed: trading corporation |
| Small business employer | no; 22 employees counted on 2026-11-01, basis: payroll report |
| Labour hire, group or franchise | unknown |
| Awards believed to cover employees | Restaurant Industry Award (belief; basis: prior payroll advice, not verified) |
| Enterprise agreements | none known |
| Contract templates and policies | EMP-T1 full-time contract v2 (approved); POL-3 leave policy v1 (unknown) |
| Employment types in use | full-time, part-time, casual |
| Employees above the high income threshold | 0 |
| Governance roles | owner-directors; operations manager (people); external bookkeeper (payroll); responsible lawyer: external |

## Commercial drafting

Schema: [drafting-profile-schema.md](drafting-profile-schema.md). Skill:
`configure-drafting-profile`.

```text
Profile ID and immutable version: example-drafting v1
Status: draft
As-at date, review owner and review trigger: 2026-11-09; general counsel; any change to standard terms
Approved by role and approval date:
Drafting party legal name and entity type: Example Software Pty Ltd; proprietary company
Trading name, registered/service address and notice contact: unknown
ACN and ABN: unknown; not yet checked against a register
GST registration: unknown
Governing state or territory; jurisdiction preference and rationale: New South Wales; head office
Commercial perimeter: NDAs and SaaS subscription terms; business customers; supplier side
House style: Australian spelling; defined terms capitalised; numbered clauses
Risk appetite: unknown - no authorised owner recorded
Controlled documents: none recorded
Standard positions, each with owner, approval, rationale and fallback:
- NDA direction, purpose boundaries, disclosure period and survival: unknown
- Liability: unknown
- (list the remaining positions from the schema, each as a fact or unknown)
Known conflicts, overlays and unknowns: all standard positions
Qualified lawyer responsible for review: EXAMPLE - general counsel
```

## Contract review playbook

Schema: [review-playbook-schema.md](review-playbook-schema.md). Skill:
`configure-review-playbook`.

| Field | Example value |
| --- | --- |
| Identity and version | example-playbook v1; owner: general counsel; status draft; review date 2027-05-09 |
| Review perimeter | customer side; SaaS and services agreements; New South Wales; as-at 2026-11-09 |
| Source profiles | example-drafting v1 (draft, not approved) |
| Risk appetite | unknown until instructed |
| Clause positions | Liability cap: preferred position, fallback and unacceptable trigger all unknown - to be instructed |
| Approval thresholds | unknown - no delegation evidence recorded |
| Field provenance | each row above: source `EXAMPLE`, confirmer blank |
| Approval evidence | |
| Changes | first version |

## Consumer and competition

Schema: [consumer-competition-profile-schema.md](consumer-competition-profile-schema.md).
Skill: `configure-consumer-competition-profile`.

| Field | Example value |
| --- | --- |
| Control | example-consumer v1; draft; as-at 2026-11-09; review due 2027-05-09; approver blank |
| Scope | Australia-wide online sales; single company; responsible lawyer: external |
| Products and supply | Household appliances; importer and retailer; online channel; consumer customers |
| Consumer dealings | Warranty document WAR-1 v3; complaints log held by customer service lead |
| Marketing | Claim owner: marketing manager; substantiation records: unknown |
| Competition | Distribution restraints: unknown; pricing autonomy: unknown |
| Acquisitions | none proposed |
| Safety | Standards asserted: unknown; incident owner: operations manager |
| Controls | every fact above is an unverified example; no authoritative source recorded |

## Corporations governance

Schema: [governance-profile-schema.md](governance-profile-schema.md). Skill:
`configure-corporations-governance`.

```text
Profile ID: example-governance
Profile version: 1
Status: draft
Entity label: Example Holdings
Entity type: proprietary
Registration basis: Corporations Act company
Governance perimeter: single company
As-at date: 2026-11-09
Approved by role:
Approved at:
Review due: 2027-05-09

Overlays:
- ASX-listed or disclosing entity: no
- APRA-regulated entity or group: no
- ACNC-registered charity: no
- CATSI Act corporation: no
- Other regulated status: unknown

Governing documents:
- CON-1, Constitution, v2, effective date unknown, status unknown, location unknown

Replaceable-rules posture: unknown
Board decision authority: unknown
Board quorum and voting: unknown
Member-reserved matters: unknown
Delegations: none recorded
Committees: none recorded
Registers and record owners: company secretary (role)
Governance calendar sources: none recorded
Known conflicts or unresolved document inconsistencies: none recorded
```

## AI governance

Schema: [ai-governance-profile-schema.md](ai-governance-profile-schema.md).
Skill: `configure-ai-governance-profile`.

| Field | Example value |
| --- | --- |
| Profile ID | example-ai |
| Profile version | 1 |
| Status | draft |
| Entity label | Example Insurance Broker |
| Entity type | private-company |
| Jurisdiction | not a government entity |
| Sector | insurance broking |
| As-at date | 2026-11-09 |
| Approved by role | |
| Approved at | |
| Review due | 2027-05-09 |
| APRA-regulated entity or group | no |
| ASIC AFS or credit licensee | yes |
| eSafety-relevant online service | no |
| Therapeutic goods or SaMD context | no |
| Commonwealth non-corporate entity | no |
| State or territory agency | no |
| EU footprint | unknown |
| AI inventory maturity | partial |
| AI use categories in scope | internal productivity; customer email drafting |
| Board-level AI oversight | none recorded |
| Governing documents | AI-POL-1 Acceptable use of AI, v1, status draft |

## AML/CTF practice

Schema: [aml-ctf-practice-profile-schema.md](aml-ctf-practice-profile-schema.md).
Skill: `configure-aml-ctf-practice-profile`. The AML/CTF skills require this
profile to be approved before they run.

| Field | Example value |
| --- | --- |
| Profile ID | example-amlctf |
| Profile version | 1 |
| Status | draft |
| Practice label | Example Legal |
| Practice structure | incorporated-legal-practice |
| Jurisdictions of practice | NSW |
| As-at date | 2026-11-09 |
| Approved by role | |
| Approved at | |
| Review due | 2027-05-09 |
| Enrolled with AUSTRAC | unknown |
| Service lines the practice believes may be designated | conveyancing; company formation |
| Member of a reporting group | no |
| Operates a trust account | yes; NSW |
| Claims a standing exemption | no |
| Foreign branch or subsidiary dimension | no |
| International funds transfer role | unknown |
| Governance roles | principals (governing body); managing principal (program approval); compliance officer: unknown |
| AML/CTF program status | none |
| Governing documents | none recorded |

## Legal triage

The triage profile is JSON with its own template and validator. Start from
`configure-legal-triage/assets/centre-profile.template.json` and check it
with that skill's `validate_triage_profile.py`.
