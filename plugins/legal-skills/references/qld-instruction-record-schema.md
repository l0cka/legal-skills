# Queensland instruction record schema

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
- intended marriage, marriage, divorce, the end of a de facto relationship or
  separation;
- a witness or attorney relationship or eligibility concern, including a paid
  carer, health provider or a person who is bankrupt;
- an existing will, enduring power of attorney or advance health directive;
- jointly held assets or a superannuation interest; and
- any possible capacity, undue influence or other practitioner concern.

## Common fields

| Field | Required | Notes |
| --- | --- | --- |
| client_full_name | yes | testator and principal |
| client_address | yes | |
| client_date_of_birth | conditional | required for the enduring power of attorney approved form; flag if the client may be under 18 |
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
| survivorship_period | no | if silent, the 30-day rule in Succession Act 1981 (Qld) s 33B is a construction rule — record silence, do not fill a value |
| funeral_wishes | no | |

## Enduring power of attorney

| Field | Required | Notes |
| --- | --- | --- |
| epoa_form | yes | short form or long form of the approved form, as instructed by the practitioner — record the instruction, never choose |
| attorney_1_full_name, attorney_1_address | yes | eligibility in Powers of Attorney Act 1998 (Qld) s 29 is flagged, not assessed |
| attorney_2_full_name, attorney_2_address | no | repeat as required; Powers of Attorney Act 1998 (Qld) s 43 allows no more than four joint attorneys for a matter — flag, never trim |
| attorney_matters | yes | financial matters, personal (including health) matters, or both — record the instruction, never choose |
| attorney_appointment_mode | conditional | jointly, severally, jointly and severally, by majority or another stated basis — required when more than one attorney |
| successive_attorney_full_name, successive_attorney_address | no | record which attorney the successive attorney replaces and the stated circumstance |
| epoa_financial_commencement | conditional | immediately, on a stated date or occasion, or on loss of capacity — required when financial matters are included; preserve each instruction separately |
| epoa_terms_instructions | no | verbatim from instructions, including any gifting, conflict-transaction or maintenance instruction; flag, never expand |
| existing_epoa_preserved | no | record any instruction not to revoke an existing enduring power; flag for solicitor review |
| advance_health_directive_identified | no | record whether one exists and its date/location; never draft, interpret or assess it |

## Missing required fields

A missing required field does not prevent drafting supported content for that
document. Insert a review marker at every affected location, add the issue to
the drafting-issues register and report `PARTIAL DRAFT – UNRESOLVED ISSUES`.
Use `BLOCKED – NO DRAFT PRODUCED` only if the approved precedent is missing or
unusable, or the client, jurisdiction or requested document cannot be
identified. Never fill a plausible value.
