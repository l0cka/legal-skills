---
name: verify-qld-judgment
description: Verify that a Queensland court or tribunal decision exists at the Queensland Judgments website, for medium-neutral Queensland citations and Qd R. Use via route-case-citation or for a known Queensland citation. Not for case treatment.
---

# Verify Queensland Judgment

## Scope

Verify that a cited Queensland court or tribunal decision exists at the
Queensland Judgments website, resolving medium-neutral Queensland citations
and Queensland Reports references to the published decision and recording
provenance. Use when the citation is already known to be a Queensland
citation (route-case-citation sends Queensland citations here) and a user
asks whether it is genuine, what case a Queensland citation refers to, or to
check Queensland authorities in a document for fabrication. Do not use for
other jurisdictions, subsequent treatment, case summaries or legal advice.

Use `queenslandjudgments.com.au` as the controlling source. The site states
that it is published by the Incorporated Council of Law Reporting for the
State of Queensland and the Supreme Court Library of Queensland, to publish
a collection of the Supreme Court's judgments on the Court's behalf, free of
charge (read 2026-11-09). Its collections also list other Queensland courts
and tribunals. Produce a provenance record, not a bare assertion that a case
"exists".

Coverage differs by court and is still being extended backwards, so read the
coverage the site shows for the issuing court at the time of the check and
never assume a start year. The site holds the authorised Queensland Reports,
which it asks users to register to read.

Read [../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
before verifying. It defines the outcome semantics, access rules and
restriction handling.

## Workflow

1. Fix the scope.
   - Accept medium-neutral Queensland citations (`QSC`, `QSCPR`, `QCA`,
     `QDC`, `QMC`, `QCAT`, `QCATA`, `QPEC`, `QLC`, `QLAC`, `QIRC`, `ICQ`,
     `QCHC`, `QMHC`), Queensland Reports (`Qd R`) citations and Queensland
     case names.
   - Return `OUTSIDE SCOPE` for other jurisdictions, treatment analysis or
     advice.
2. Resolve the citation at the official publisher.
   - A medium-neutral citation maps to a decision path of the form
     `/caselaw/<court identifier in lower case>/<year>/<number>`, for
     example `/caselaw/qca/2023/1` for `[2023] QCA 1` (confirmed for the
     Court of Appeal on 2026-11-09). Open that path. Cite it only after it
     resolved and the page was read.
   - If the path does not resolve, search the site by distinctive case name
     terms before concluding anything. A path that fails for a court whose
     pattern was not confirmed is not evidence of absence.
   - For a `Qd R` citation, resolve to the medium-neutral citation through
     the site before concluding anything. Where the report text needs a
     registered account, ask the user to open it; never create an account or
     sign in for them.
   - Make one targeted lookup per citation; never crawl or bulk-download
     listings.
3. Confirm identity.
   - Match the `CITATION` field, parties, court or division and file number
     as published, and record the decision URL.
   - The page can show two dates under `DELIVERED ON`: the date of orders
     and the date of publication of reasons. Record both, and treat a
     supplied date that matches neither as a qualification.
   - Treat a supplied case name that differs materially from the published
     name as a qualification, and say which differs.
4. Check restrictions before reproducing anything.
   - Look for non-publication, suppression or anonymisation notations and
     pseudonymised parties on the decision page. Preserve any found and
     treat them as qualifications.
5. Report using the result contract.

## Result contract

Lead with one status: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`,
`UNVERIFIABLE`, `NOT FOUND` or `OUTSIDE SCOPE`, as defined in the shared
method. `NOT FOUND` means the site was searched by citation and case name
inside the coverage it shows for that court and contains no matching
decision. Report it as a fabrication flag for human confirmation, never as
an accusation.

```text
Requested check: <citation or case name as supplied>
Jurisdiction: Queensland, Australia
Citation type: <medium-neutral / reported / case name>
Official case name: <as published, or not established>
Medium-neutral citation: <[YEAR] COURT N, or not established>
Court or tribunal: <as published, or not established>
Decision date: <date of orders and date of publication of reasons, or not established>
Coverage note: <inside the coverage shown for the court / possible pre-coverage decision>
Restrictions: <none observed / notation preserved verbatim>
Official sources: <exact queenslandjudgments.com.au URLs actually inspected>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

## Fail closed

Return `UNVERIFIABLE`, not `NOT FOUND`, when the site is unreachable, the
page does not render for the client in use, the search fails, the citation
predates the coverage shown for the court, or a `Qd R` citation cannot be
resolved to a medium-neutral form. Return `NOT FOUND` only after both the
citation path and a case name search inside the coverage period returned no
match. Never infer existence from an aggregator, secondary source or model
memory.
