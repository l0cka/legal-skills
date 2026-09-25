# Employment profile schema

The profile is a controlled factual map that parameterises every other skill
in this plugin. Store it in the employer's or firm's approved system, not in
this repository. The model can prepare a draft but cannot supply the
approval fields.

## Required fields

| Field | Content |
| --- | --- |
| Profile ID | Stable identifier chosen by the practice |
| Profile version | Increment on any change |
| Status | `draft`, `approved` or `retired` — the model may only ever set `draft` |
| Employer label | Controlled name, no unnecessary personal data |
| Entity type | `company`, `partnership`, `sole-trader`, `incorporated-association`, `government-entity`, `other` (name it) |
| Jurisdictions of operation | Australian states and territories where employees work |
| As-at date | YYYY-MM-DD the factual content was confirmed |
| Approved by role | Blank until an authorised human completes it |
| Approved at | Blank until approval |
| Review due | Date the profile must be reconfirmed |

## Coverage and size

Record each as `yes`, `no` or `unknown` — never default a missing answer to
`no`:

- national system employer (constitutional corporation, Commonwealth entity,
  or employer in a referring state or territory) — record the basis claimed,
  not a conclusion;
- state public sector, local government or non-constitutional-corporation
  employer in a state that has not referred that employer — flag for
  specialist review;
- small business employer (fewer than 15 employees counted as the Act
  requires, including regular and systematic casuals) — record the headcount
  basis and date;
- headcount bands relevant to other thresholds (for example, 15 or more for
  redundancy pay);
- any labour hire, host, group or franchise arrangement.

## Instruments

- modern awards the employer believes cover any employees (award code and
  title) — record the belief and its basis;
- enterprise agreements in operation (title, FWC approval reference, nominal
  expiry date);
- individual flexibility arrangements, guarantees of annual earnings, and
  common-law contract templates (ID, version, effective date);
- workplace policies in force (ID, title, version, effective date, status
  `approved`, `draft` or `unknown`).

## Workforce composition

- employment types in use: full-time, part-time, casual, fixed-term,
  maximum-term, apprentices and trainees, labour hire, contractors — record
  the employer's classification, never re-characterise;
- employees above the high income threshold (count, not names);
- employees with more than 12 months' service and fewer than 6 or 12 months'
  service (counts) — minimum employment period bands;
- employees on parental leave, flexible working arrangements or with recent
  workplace-right exercises the employer has flagged (counts).

## Governance

- roles: governing body, executive responsible for people, HR lead, payroll
  lead, and the responsible lawyer, each by position title;
- record-keeping and pay-slip systems with version or vendor identifiers;
- consultation mechanisms (award consultation clause, agreement clause,
  union delegates recognised).

## Boundaries

The profile records what the employer believes and holds. It never
determines national system coverage, award coverage, small-business status
or any threshold; those are flagged for verification in the skill that
relies on them.
