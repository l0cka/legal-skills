# No-code procedure: check a legal triage profile

Use this when the host cannot run code. It replaces the profile validator of
[this skill](SKILL.md) with a manual checklist. A manual check never makes a
profile validated or approved.

Schema: [centre profile schema](references/centre-profile-schema.md).
Template: [centre profile template](assets/centre-profile.template.json).

## Checklist

Tick each line only after reading the profile. Any unticked line means the
profile is not ready.

| Check | Done | Note |
| --- | --- | --- |
| `schema_version` is `1` | | |
| Every root field in the schema is present and non-empty | | |
| `profile.status` is `draft`, `approved` or `retired`; only `approved` may be used for live triage | | |
| Identifiers are lowercase letters, digits and hyphens, and unique | | |
| Versions are semantic versions; dates are real `YYYY-MM-DD` dates | | |
| Every policy category the schema requires is present | | |
| Every operational rule has an owner, version, effective date, review date and source, and its `source_policy_id` names a policy in the profile | | |
| Mandatory human-review and no-autonomous-rejection controls are unchanged from the template | | |
| No client or matter fields appear anywhere in the profile | | |
| No placeholder text from the template remains | | |
| No review date precedes its effective, verified or approval date | | |
| The approval date is not after today's date | | |
| The profile, every policy and every referral review date is on or after today's date | | |
| Only the statuses in the schema's allowed list appear in `output_control` | | |

Ask the person for today's date if the host cannot supply it. Any review date
that has passed means the profile is expired: do not use it for live triage.

## Result

Report `Validation: manual check against the schema; automated validation not
run`. The status is at most `READY FOR HUMAN APPROVAL`; never report
`VALIDATED APPROVED PROFILE`. The profile counts as validated only when a
person at the centre confirms that validation with approval required passed
outside this host; record who confirmed and when.
