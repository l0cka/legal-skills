# NSW instruction record schema

The instruction table is the structured record for one client and the only
source of matter-specific factual values used in drafting. Clause text comes
from the approved precedent or drafting playbook; it is never an instruction-
table value. Every factual field carries:

- **value** — exactly as given; never inferred, normalised only for
  obvious formatting (dates, capitalisation of names);
- **provenance** — the page, section or question of the instruction sheet
  the value came from, or `interview` when gathered directly, or
  `cannot be determined` when the sheet is blank, illegible or ambiguous
  at that point.

Two entries naming the same person must spell the name identically; a
mismatch is flagged in the instruction summary and drafting-issues register,
never silently reconciled.

## Scope and risk flags

Record each flag as `yes`, `no` or `cannot be determined`, with provenance:

- minor children or a client who may be a minor;
- intended marriage, marriage, divorce or separation;
- a witness-beneficiary or other witness relationship;
- an existing will, power, guardianship appointment or related instrument;
- jointly held assets or a superannuation interest; and
- any possible capacity, undue influence or other practitioner concern.

## Common fields (all documents)

| Field | Required | Notes |
| --- | --- | --- |
| client_full_name | yes | the testator, principal and appointor |
| client_address | yes | |
| client_occupation | no | |
| client_date_of_birth | no | flag if client may be a minor — Succession Act 2006 (NSW) s 5 |
| matter_reference | no | firm matter identifier |

## Will

| Field | Required | Notes |
| --- | --- | --- |
| executor_1_full_name, executor_1_address | yes | |
| executor_2_full_name, executor_2_address | no | joint or substitute per instructions |
| substitute_executor_full_name, substitute_executor_address | no | |
| guardian_full_name, guardian_address | conditional | required if the client has minor children |
| specific_gifts | no | list: asset description, recipient full name, per-gift provenance |
| residue_disposition | yes | recipients and shares of residue |
| residue_substitution | no | what happens if a residue beneficiary predeceases |
| survivorship_period | no | if silent, the 30-day default in Succession Act 2006 (NSW) s 35 applies as a construction rule — record silence, do not fill a value |
| funeral_wishes | no | |

## Enduring power of attorney

| Field | Required | Notes |
| --- | --- | --- |
| attorney_1_full_name, attorney_1_address | yes | |
| attorney_2_full_name, attorney_2_address | no | |
| attorney_appointment_mode | conditional | jointly, severally, or jointly and severally — required when more than one attorney |
| substitute_attorney_full_name, substitute_attorney_address | no | |
| epoa_commencement | yes | when the power operates (immediately, on incapacity, other instruction) |
| epoa_conditions_limitations | no | verbatim from instructions |
| epoa_gift_authority | no | flag any gifting instruction for solicitor attention; never expand it |

## Appointment of enduring guardian

| Field | Required | Notes |
| --- | --- | --- |
| enduring_guardian_1_full_name, enduring_guardian_1_address | yes | eligibility limits in Guardianship Act 1987 (NSW) s 6B are flagged, not assessed |
| enduring_guardian_2_full_name, enduring_guardian_2_address | no | |
| guardian_appointment_mode | conditional | jointly, severally, or jointly and severally — required when more than one guardian |
| substitute_enduring_guardian_full_name, substitute_enduring_guardian_address | no | |
| guardianship_functions | yes | functions given, limited or excluded — Guardianship Act 1987 (NSW) s 6E list as the checklist |
| guardianship_directions | no | verbatim from instructions |

## Missing required fields

A missing required field does not prevent drafting supported content for that
document. Insert a review marker at every affected location, add the issue to
the drafting-issues register and report `PARTIAL DRAFT – UNRESOLVED ISSUES`.
Use `BLOCKED – NO DRAFT PRODUCED` only if the approved precedent is missing or
unusable, or the client, jurisdiction or requested document cannot be
identified. Never fill a plausible value.
