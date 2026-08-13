---
name: check-northern-territory-legislation
description: Verify the identity, status, point-in-time reprint, commencement and currency of Northern Territory legislation using the official NT legislation database. Use for current or historical NT Acts, regulations and provisions. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check Northern Territory Legislation

Use `legislation.nt.gov.au` as the controlling source.

1. Record the title, provision and requested date; use today's
   `Australia/Darwin` date if none is supplied and say so.
2. Resolve one official title and instrument type. Reject ambiguous matches.
3. Select the official reprint or historical text covering the date and record
   its in-force date, current/repealed status and exact URL.
4. Inspect commencement, amendment, reprint and currency material relevant to
   the provision. Keep registration and present status separate from operation
   on the requested date.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, with identity, reprint, period, commencement, currency
   flags, sources and unresolved lawyer-review issues.

Fail closed if the official database does not establish the proposition. Case
law is outside scope.
