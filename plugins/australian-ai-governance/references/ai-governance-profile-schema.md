# AI governance profile schema

The profile is a controlled factual map that parameterises every other skill
in this plugin. Store it in the organisation's approved system, not in this
repository. The model can prepare a draft but cannot supply the approval
fields.

## Required fields

| Field | Content |
| --- | --- |
| Profile ID | Stable identifier chosen by the organisation |
| Profile version | Increment on any change |
| Status | `draft`, `approved` or `retired` — the model may only ever set `draft` |
| Entity label | Controlled name, no unnecessary personal data |
| Entity type | `private-company`, `listed-company`, `commonwealth-agency`, `state-territory-agency`, `local-government`, `other` (name it) |
| Jurisdiction | For government entities: Cth, NSW, Vic, Qld, WA, SA, Tas, ACT or NT |
| Sector | Primary industry or portfolio |
| As-at date | YYYY-MM-DD the factual content was confirmed |
| Approved by role | Blank until an authorised human completes it |
| Approved at | Blank until approval |
| Review due | Date the profile must be reconfirmed |

## Regulatory overlays

Record each as `yes`, `no` or `unknown` — never default a missing answer to
`no`:

- APRA-regulated entity or group (banks, insurers, superannuation);
- ASIC AFS or credit licensee;
- eSafety-relevant online service (industry codes or standards may apply);
- therapeutic goods or SaMD context (TGA framework applies by intended
  purpose);
- Commonwealth non-corporate entity (DTA AI-in-government policy is
  mandatory);
- state or territory agency (jurisdictional assurance framework applies); and
- EU footprint — AI outputs used by or affecting persons in the EU
  (extraterritorial EU AI Act exposure; specialist review).

## AI adoption facts

- AI inventory maturity: `none`, `partial`, `register-maintained`;
- AI use categories in scope (for example customer-facing decisioning,
  internal productivity, agentic systems, biometric or facial recognition);
- board-level AI oversight arrangements (policy adopted, committee, reporting
  cadence) with document identifiers; and
- governing documents: ID, title, version, effective date, status
  (`approved`, `draft`, `unknown`) and source location for each AI policy,
  risk framework, assessment template or register.

## Boundaries

The profile records facts, not conclusions. It cannot establish that an
instrument applies, that a use case is high or low risk, or that governance is
adequate. Matter facts, personal data and privileged advice belong in the
organisation's governed systems, never in this public plugin or a reusable
template.
