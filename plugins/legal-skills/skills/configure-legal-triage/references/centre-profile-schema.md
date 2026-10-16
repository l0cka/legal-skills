# Centre profile schema

Use the profile to separate stable public workflow instructions from each
centre's approved operational rules. Store completed profiles in a
centre-controlled location outside the public plugin repository.

## Root fields

- `schema_version`: use `1`.
- `profile`: identify the profile, semantic profile version, centre,
  jurisdictions and lifecycle status.
- `governance`: record approval and review details.
- `policies`: provide provenance for every operational rule.
- `data_handling`, `human_review`, `conflict_check`: preserve mandatory safety
  controls.
- `service_rules`, `escalation_pathways`, `referrals`: define centre-specific
  routing content.
- `output_control`: constrain the statuses and evidence required in a triage
  result.

## Lifecycle

Use only these values for `profile.status`:

- `draft`: incomplete or awaiting review; never use for live triage.
- `approved`: approved for the stated users, environment and review period.
- `retired`: retained for provenance but unavailable for new triage.

Run the validator with `--require-approved` before live use. An approved profile
fails closed when its profile, policy or referral review date has passed.

## Policy provenance

Include each of these categories:

- `service-scope`
- `urgent-escalation`
- `conflict-checking`
- `privacy-and-client-information`
- `referrals`

Every policy entry requires a unique `policy_id`, title, version, owner,
centre-controlled source, effective date and review due date. Refer to the
`policy_id` from service rules and escalation pathways. Do not paste restricted
policy text into the profile; record concise operational rules and a local
source pointer.

## Data boundary

Keep `staff_facing_only`, `minimum_necessary` and `client_notice_required`
true. Keep `public_ai_personal_information`, `model_training_with_client_data`
and `model_may_write_client_record` false.

Do not add client names, contact details, addresses, dates of birth, adverse
party names, matter narratives or document identifiers to a profile. A profile
defines the process; it is not a client record.

## Service rules

Define service areas and jurisdictions in language a staff member can apply.
Represent eligibility factors as questions for authorised staff, not automatic
scoring rules. Set `human_decision_required` true for every factor.

Represent exclusions narrowly. Set `referral_required` true so an apparent
scope mismatch does not become a dead end. Do not encode protected attributes
as negative factors unless a lawful, authorised positive-priority rule requires
their voluntary collection.

## Escalation and referrals

Define local escalation triggers and actions for the centre's actual service
model, including after-hours limits. Do not rely on a generic national crisis
list.

For each referral, record its scope, jurisdictions, public or approved contact,
source, verification date, review due date, warm-referral availability and
consent requirement. A listed referral is a lead, not evidence that the service
will accept the person.

## Allowed result statuses

Preserve exactly these statuses:

- `URGENT HUMAN ESCALATION`
- `HUMAN TRIAGE REQUIRED`
- `PROVISIONAL SERVICE PATHWAY`
- `OUTSIDE CONFIGURED SCOPE`
- `INSUFFICIENT INFORMATION`

Do not add `eligible`, `ineligible`, `accepted`, `rejected` or a merits rating.
