---
name: configure-legal-triage
description: Create or update a community legal centre's enquiry triage profile, recording service scope, urgency pathways, eligibility and referrals. Use before legal triage. Never invents centre policy or approves the profile.
---

# Configure Legal Triage

## Scope

Create, revise or validate a governed staff-facing legal enquiry triage
profile for an Australian community legal centre or legal assistance service.
Use when a centre needs to translate its approved service scope, urgency
pathways, conflict-check process, privacy controls, eligibility factors,
accessibility commitments and referral arrangements into a versioned local
profile for the Legal Triage workflows. Do not use client or matter data,
invent centre policy, or approve a profile on the centre's behalf.

Create a centre-local control document for staff-assisted triage. Keep the
public skill generic and make the approved profile the controlling source for
centre-specific decisions.

Read [references/centre-profile-schema.md](references/centre-profile-schema.md)
before creating or changing a profile. Read
[references/governance-basis.md](references/governance-basis.md) when assessing
privacy, accreditation, responsible-AI or source requirements.

To start quickly, edit the matching starter in
[starter-profiles.md](../../references/starter-profiles.md). The
[profile guide](../../references/profile-guide.md) says where to keep the
approved profile and how a person approves it.

## Workflow

1. Fix the authority and scope.
   - Identify the centre, jurisdiction, intended staff roles and accountable
     approver.
   - Confirm that version 0.1 is staff-facing only.
   - Exclude client, matter, adverse-party and other personal information from
     the configuration task.
2. Collect controlling material.
   - Use only current centre-approved policies and authorised sector material.
   - Record a policy owner, version, effective date, review date and
     centre-controlled source for every operational rule.
   - Mark an unresolved rule `DRAFT`; never fill a gap from general knowledge.
3. Build the profile.
   - Copy [assets/centre-profile.template.json](assets/centre-profile.template.json)
     to a centre-controlled location outside this public repository.
   - Configure service areas, jurisdictions, eligibility factors, exclusions,
     escalation pathways, conflict checking, data handling and referrals.
   - Preserve the mandatory human-review and no-autonomous-rejection controls.
4. Validate locally.
   - Hosts that cannot run code follow AI-tool mode below.
   <!-- ai-tool:code -->
   ```bash
   python3 <skill-root>/scripts/validate_triage_profile.py <profile.json>
   python3 <skill-root>/scripts/validate_triage_profile.py \
     <profile.json> --require-approved
   ```

   Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
   first command checks a draft. The second also checks approval and currency.
   The helper is read-only and offline. If command execution is unavailable,
   do not treat the profile as approved; an authorised person must run the
   validation in an environment that supports it.
   <!-- /ai-tool:code -->
5. Obtain human approval.
   - Give the draft and validation result to the centre's authorised legal,
     operational and privacy or governance reviewers.
   - Change `profile.status` to `approved` only after they approve the exact
     profile.
   - Record the approver, approval date and review due date. Do not state that
     a centre complies with accreditation, privacy or professional obligations.

## Result contract

Return:

```text
Profile status: DRAFT / READY FOR HUMAN APPROVAL / VALIDATED APPROVED PROFILE
Centre and jurisdiction: <centre; jurisdictions>
Intended users: <staff roles>
Controlling sources: <policy IDs and versions>
Configured controls: <service, escalation, conflicts, privacy, referrals>
Validation: <command and result>
Unresolved items: <questions or expired sources>
Required approval: <roles; never fabricate names or approval>
Limitations: <currency, legal and operational limits>
```

Never publish or commit the completed centre profile unless the centre has
separately confirmed that it contains no confidential or restricted material.

## AI-tool mode

Use this section when the host cannot run
code. The AI-tool bundle ships this section and
leaves the code steps out; hosts that can run code ignore it. General rules:
[AI-tool mode](../../references/ai-tool-mode.md).

Check the profile by hand against
[the centre profile schema](references/centre-profile-schema.md) and the
template in [assets](assets/centre-profile.template.json).

1. Confirm every required field in the schema is present and non-empty.
2. Confirm the mandatory human-review and no-autonomous-rejection controls
   are unchanged.
3. Confirm every operational rule has an owner, version, effective date,
   review date and source.
4. Compare each profile, policy and referral review date with today's date
   (ask the person for it if the host cannot supply it).
   Any date that has passed means the profile is expired: do not use it for
   live triage.
5. Report `Validation: manual check against the schema; automated validation
   not run`. The status is at most `READY FOR HUMAN APPROVAL`. Never report
   `VALIDATED APPROVED PROFILE`. The profile counts as validated only when a
   person at the centre confirms that validation with approval required passed
   outside this host; record who confirmed and when.
