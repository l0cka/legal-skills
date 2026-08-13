---
name: check-victoria-legislation
description: Verify the identity, status, point-in-time version, commencement and currency of Victorian Acts and statutory rules using the official Victorian legislation publisher. Use for current or historical Victorian legislative text and provision checks. Do not use for Bills, case law, interpretation, application or final legal advice.
---

# Check Victoria Legislation

Use `legislation.vic.gov.au` as the controlling source.

1. Record the exact title, provision and requested date; use today's
   `Australia/Melbourne` date if none is supplied and say so.
2. Resolve the official title and legislation type. Reject ambiguous matches.
3. Select the official authorised version covering the requested date and
   record its version number or effective date, status and source URL.
4. Inspect the displayed commencement, amendment, version-history and currency
   information relevant to the provision. Do not infer operation from an
   as-made document or URL date alone.
5. Return `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED` or
   `OUTSIDE SCOPE`, followed by the title, provision, date, applicable version,
   present status, commencement evidence, currency flags, sources actually
   inspected and unresolved lawyer-review issues.

Fail closed if the official source is unavailable or does not establish the
version or commencement. Case law is outside scope.
