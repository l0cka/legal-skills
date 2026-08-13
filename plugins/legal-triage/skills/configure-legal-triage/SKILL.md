---
name: configure-legal-triage
description: Create, revise or validate a governed staff-facing legal enquiry triage profile for an Australian community legal centre or legal assistance service. Use when a centre needs to translate its approved service scope, urgency pathways, conflict-check process, privacy controls, eligibility factors, accessibility commitments and referral arrangements into a versioned local profile for the Legal Triage plugin. Do not use client or matter data, invent centre policy, or approve a profile on the centre's behalf.
---

# Configure Legal Triage

Create a centre-local control document for staff-assisted triage. Keep the
public skill generic and make the approved profile the controlling source for
centre-specific decisions.

Read [references/centre-profile-schema.md](references/centre-profile-schema.md)
before creating or changing a profile. Read
[references/governance-basis.md](references/governance-basis.md) when assessing
privacy, accreditation, responsible-AI or source requirements.

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

   ```bash
   python3 <skill-root>/scripts/validate_triage_profile.py <profile.json>
   python3 <skill-root>/scripts/validate_triage_profile.py \
     <profile.json> --require-approved
   ```

   Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
   first command checks a draft. The second also checks approval and currency.
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
