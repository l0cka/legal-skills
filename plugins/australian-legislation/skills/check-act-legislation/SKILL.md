---
name: check-act-legislation
description: Verify the identity, status, point-in-time republication, commencement and currency of Australian Capital Territory legislation using the official ACT legislation register. Use for current or historical ACT Acts, regulations and provisions. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check ACT Legislation

Use `legislation.act.gov.au` as the controlling source.

1. Record the title, provision and requested date; use today's
   `Australia/Sydney` date if none is supplied and say so.
2. Resolve one official registered title and instrument type. Reject ambiguity.
3. Select the official republication covering the requested date and record its
   republication number, effective information, present status and exact URL.
4. Inspect commencement, amendment history, endnotes and currency information
   relevant to the provision. Do not infer operation from registration alone.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, with identity, republication, period, commencement,
   currency flags, sources and unresolved lawyer-review issues.

Fail closed if the official register cannot establish the point-in-time text.
Case law is outside scope.
