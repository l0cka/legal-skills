---
name: check-western-australia-legislation
description: Verify the identity, status, point-in-time version, commencement and currency of Western Australian legislation using the official WA legislation publisher. Use for current or historical WA Acts, regulations and provisions. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check Western Australia Legislation

Use `legislation.wa.gov.au` as the controlling source.

1. Record the title, provision and requested date; use today's `Australia/Perth`
   date if none is supplied and say so.
2. Resolve the official title page and instrument type. Reject ambiguity.
3. Select the official compilation or version covering the requested date and
   record its effective information, status and exact source URL.
4. Inspect commencement, amendment history, subsidiary legislation and
   currency notes relevant to the provision. Treat future commencements as
   future law.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, with title, version, date range, commencement, currency,
   sources inspected and unresolved lawyer-review issues.

Fail closed where the publisher does not establish point-in-time operation.
Case law is outside scope.
