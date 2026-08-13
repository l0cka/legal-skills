---
name: check-queensland-legislation
description: Verify the identity, status, point-in-time reprint, commencement and currency of Queensland legislation using the official Queensland legislation publisher. Use for current or historical Queensland Acts and subordinate legislation. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check Queensland Legislation

Use `legislation.qld.gov.au` as the controlling source.

1. Record the exact title, provision and requested date; use today's
   `Australia/Brisbane` date if none is supplied and say so.
2. Resolve one official title and legislation type; treat multiple candidates
   as ambiguous.
3. Select the official in-force or historical reprint covering the date and
   record the reprint period, current/repealed status and exact URL.
4. Inspect notes, commencement, amendment and reprint history relevant to the
   requested provision. Keep present title status separate from historical
   operation.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, with identity, applicable reprint, period, commencement,
   currency flags, official sources and unresolved lawyer-review issues.

Fail closed if the official evidence cannot tie the provision to the date.
Case law is outside scope.
