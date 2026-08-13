---
name: check-south-australia-legislation
description: Verify the identity, status, point-in-time version, commencement and currency of South Australian legislation using the official SA legislation publisher. Use for current or historical SA Acts, regulations and provisions. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check South Australia Legislation

Use `legislation.sa.gov.au` as the controlling source.

1. Record the exact title, provision and date; use today's `Australia/Adelaide`
   date if none is supplied and say so.
2. Resolve one official title and instrument type. Reject ambiguous matches.
3. Select the official version covering the requested date and record its
   displayed effective information, current/repealed status and exact URL.
4. Inspect commencement, legislative history, amendment and currency notes
   relevant to the requested provision. Do not use a Bill or as-made text as
   proof of later operation.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, with identity, version, effective period, commencement,
   currency flags, sources and unresolved lawyer-review issues.

Fail closed if current official evidence is insufficient. Case law is outside
scope.
