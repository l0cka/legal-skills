---
name: check-tasmania-legislation
description: Verify the identity, status, point-in-time version, commencement and currency of Tasmanian legislation using the official Tasmanian legislation publisher. Use for current or historical Tasmanian Acts, statutory rules and provisions. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check Tasmania Legislation

Use `legislation.tas.gov.au` as the controlling source.

1. Record the title, provision and requested date; use today's
   `Australia/Hobart` date if none is supplied and say so.
2. Resolve the official title and instrument type. Reject ambiguity.
3. Select the in-force or historical official text covering the date and record
   the displayed effective information, reprint status and exact URL.
4. Inspect commencement, amendment, version and currency notes relevant to the
   provision. Keep current title status separate from historical operation.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, with identity, applicable version, date range,
   commencement, currency flags, sources and lawyer-review issues.

Fail closed where the version or commencement is not established. Case law is
outside scope.
