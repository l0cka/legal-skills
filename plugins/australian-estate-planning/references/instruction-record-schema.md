# Instruction record schema

The instruction record is the canonical structured output of the extraction
gate and the only input the fill step may read. Every field carries:

- **value** — exactly as given; never inferred, normalised only for
  obvious formatting (dates, capitalisation of names);
- **provenance** — the page, section or question of the instruction sheet
  the value came from, or `interview` when gathered directly, or
  `cannot be determined` when the sheet is blank, illegible or ambiguous
  at that point; and
- **confirmation status** — `pending` until the responsible solicitor
  confirms the extraction table, then `confirmed`. Only `confirmed`
  records may be used to fill a precedent.

Two entries naming the same person must spell the name identically; a
mismatch is flagged at the extraction gate, never silently reconciled.

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

A missing required field blocks only the document type that requires it:
the other document types still proceed. The blocked type is `NOT READY`
with the exact missing fields listed. Never fill a plausible value.
