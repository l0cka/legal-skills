# Governance profile schema

Use one controlled profile per company or governance perimeter. Store it in the
organisation's approved system, not in this repository. The model can prepare a
draft but cannot supply the approval fields.

## Required fields

```text
Profile ID: <stable identifier>
Profile version: <version>
Status: <draft / approved / retired>
Entity label: <non-sensitive identifier>
Entity type: <proprietary / public / company limited by guarantee / other>
Registration basis: <Corporations Act company / unknown>
Governance perimeter: <single company / identified group entities>
As-at date: <YYYY-MM-DD>
Approved by role: <authorised role, never inferred>
Approved at: <date, never inferred>
Review due: <date or trigger>

Overlays:
- ASX-listed or disclosing entity: <yes / no / unknown>
- APRA-regulated entity or group: <yes / no / unknown>
- ACNC-registered charity: <yes / no / unknown>
- CATSI Act corporation: <yes / no / unknown>
- Other regulated status: <identified / none confirmed / unknown>

Governing documents:
- <document ID, title, version, effective date, approved/draft/unknown,
  controlled source location>

Replaceable-rules posture: <applies / displaced / modified / unknown>
Board decision authority: <document and clause IDs>
Board quorum and voting: <document and clause IDs>
Member-reserved matters: <document and clause IDs>
Delegations: <instrument IDs, owners, limits and review dates>
Committees: <charter IDs, reporting lines and review dates>
Registers and record owners: <record class and accountable role>
Governance calendar sources: <source IDs and accountable role>
Known conflicts or unresolved document inconsistencies: <controlled references>
```

## Validation rules

- An `approved` profile requires a human-supplied approving role, approval date
  and immutable version identifier.
- `unknown` is valid and must not be silently converted to `no`, `none` or an
  assumed rule.
- Cite documents by controlled identifier and version; do not paste privileged
  advice or confidential board content into the profile.
- Record people by governance role unless identity is necessary and authorised
  for the current matter.
- A profile with an unknown registration basis or decisive overlay is not ready
  for consequential governance work.
