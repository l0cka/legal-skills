# Victorian instruction record schema

The instruction table is the structured record for one client and the only
source of matter-specific factual values used in drafting. Clause text comes
from the approved precedent or drafting playbook; it is never an instruction-
table value. Every factual field carries:

- **value** — exactly as given; never inferred, normalised only for obvious
  formatting such as dates and capitalisation of names;
- **provenance** — the page, section or question of the instruction sheet,
  `interview` when gathered directly, or `cannot be determined` when the
  source is blank, illegible or ambiguous.

Two entries naming the same person must spell the name identically. A mismatch
is flagged in the instruction summary and drafting-issues register, never
silently reconciled.

## Scope and risk flags

Record each flag as `yes`, `no` or `cannot be determined`, with provenance:

- minor children or a client who may be under 18;
- intended marriage, marriage, divorce or separation;
- a witness, attorney or appointee relationship or eligibility concern;
- an existing will, enduring power, appointment or advance care directive;
- jointly held assets or a superannuation interest; and
- any possible capacity, undue influence or other practitioner concern.

## Common fields

| Field | Required | Notes |
| --- | --- | --- |
| client_full_name | yes | testator, principal and appointor |
| client_address | yes | |
| client_date_of_birth | conditional | required for the medical treatment decision-maker appointment; flag if the client may be under 18 |
| client_occupation | no | |
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
| survivorship_period | no | if silent, the 30-day rule in Wills Act 1997 (Vic) s 39 is a construction rule — record silence, do not fill a value |
| funeral_wishes | no | |

## Enduring power of attorney

| Field | Required | Notes |
| --- | --- | --- |
| attorney_1_full_name, attorney_1_address | yes | eligibility in Powers of Attorney Act 2014 (Vic) s 28 is flagged, not assessed |
| attorney_2_full_name, attorney_2_address | no | repeat as required |
| attorney_authorised_matters | yes | all lawful matters, personal matters, financial matters, or specified matters — record the instruction, never choose |
| attorney_appointment_mode | conditional | joint, several, joint and several, or majority — required when more than one attorney |
| alternative_attorney_full_name, alternative_attorney_address | no | record which attorney or attorneys the alternative replaces |
| alternative_attorney_trigger | no | circumstances specified by the principal; record silence rather than importing the statutory default |
| epoa_commencement | yes | commencement may differ by matter; preserve each instruction separately |
| epoa_conditions_instructions | no | verbatim from instructions |
| existing_epoa_preserved | no | record any instruction not to revoke an existing enduring power; flag for solicitor review |
| epoa_gift_authority | no | flag any gifting instruction; never expand it |

## Appointment of medical treatment decision maker

| Field | Required | Notes |
| --- | --- | --- |
| medical_decision_maker_1_full_name | yes | appointee must be an adult under s 26 |
| medical_decision_maker_1_date_of_birth | yes | prescribed detail under regulation 6 |
| medical_decision_maker_1_address | yes | prescribed detail under regulation 6 |
| medical_decision_maker_2_full_name, medical_decision_maker_2_date_of_birth, medical_decision_maker_2_address | no | repeat as required; listing order controls priority under s 28(2) |
| medical_decision_maker_order | conditional | required when more than one appointee; never infer priority |
| medical_decision_maker_limitations_conditions | no | verbatim from instructions |
| existing_advance_care_directive | no | record whether one is identified and its date/location; never draft, interpret or assess it |

## Missing required fields

A missing required field does not prevent drafting supported content for that
document. Insert a review marker at every affected location, add the issue to
the drafting-issues register and report `PARTIAL DRAFT – UNRESOLVED ISSUES`.
Use `BLOCKED – NO DRAFT PRODUCED` only if the approved precedent is missing or
unusable, or the client, jurisdiction or requested document cannot be
identified. Never fill a plausible value.
