# AML/CTF practice profile schema

The profile is a controlled factual map that parameterises every other skill
in this plugin. Store it in the practice's approved system, not in this
repository. The model can prepare a draft but cannot supply the approval
fields.

## Required fields

| Field | Content |
| --- | --- |
| Profile ID | Stable identifier chosen by the practice |
| Profile version | Increment on any change |
| Status | `draft`, `approved` or `retired` — the model may only ever set `draft` |
| Practice label | Controlled name, no unnecessary personal data |
| Practice structure | `sole-practitioner`, `partnership`, `incorporated-legal-practice`, `multi-disciplinary-practice`, `other` (name it) |
| Jurisdictions of practice | Australian states and territories where the practice operates |
| As-at date | YYYY-MM-DD the factual content was confirmed |
| Approved by role | Blank until an authorised human completes it |
| Approved at | Blank until approval |
| Review due | Date the profile must be reconfirmed |

## Regulatory position

Record each as `yes`, `no` or `unknown` — never default a missing answer to
`no`:

- enrolled with AUSTRAC (with enrolment date if known);
- provides, or intends to provide, any service the practice believes may be
  a designated service (list the service lines: conveyancing, corporate
  transactions, trust and company formation, shelf companies, registered
  office services, acting in corporate positions, holding or managing client
  property in transactions, equity or debt financing work);
- member of a reporting group (record the lead entity and arrangement);
- operates a trust account (state jurisdiction and regulator);
- claims a standing exemption (legal aid commission, community legal centre,
  barrister acting for Australian government bodies, incidental trust-money
  position) — record the claimed basis, not a conclusion;
- provides services with a possible foreign branch or subsidiary dimension;
  and
- believes it may act as an ordering or beneficiary institution for
  international funds transfers (specialist review flag — outside this
  plugin).

## Governance and program facts

- governance roles: governing body, senior manager or managers who approve
  the program, and AML/CTF compliance officer, each with role holder
  position titles (no unnecessary personal data);
- AML/CTF program status: `none`, `draft`, `approved`, `unknown`, with
  document identifiers, versions and effective dates for the ML/TF risk
  assessment and the AML/CTF policies;
- personnel due diligence and training arrangements with document
  identifiers; and
- governing documents: ID, title, version, effective date, status
  (`approved`, `draft`, `unknown`) and source location for each CDD policy,
  record-keeping policy or related control document.

## Boundaries

The profile records facts, not conclusions. It cannot establish that a
service is designated, that an exemption applies, that a program is
adequate or that any report is due. Client information, matter information
and privileged material belong in the practice's governed systems, never in
this public plugin or a reusable template.
