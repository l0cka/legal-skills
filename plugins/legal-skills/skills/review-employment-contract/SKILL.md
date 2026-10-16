---
name: review-employment-contract
description: Review an Australian employment contract against the NES, instrument coverage, set-off wording, IP, confidentiality, termination and fixed-term limits for qualified lawyer review. Use for onboarding or contract refreshes; never certify compliance or approve execution.
---

# Review Employment Contract

Jurisdiction: Australian employment contracts with a verified national system
basis for Fair Work obligations; state-system contract merits need specialist
review. Verify Commonwealth provisions at legislation.gov.au and instruments at
fwc.gov.au using `$check-commonwealth-legislation` and the applicable award or
agreement. Currency is limited to the linked extension reference; historical
sources must match the contract and employment dates.

Read the [source and control
method](../../references/fair-work-source-and-control-method.md), reuse the
[employment profile schema](../../references/employment-profile-schema.md) and
consult the [extension source
checklist](../../references/employment-extension-sources.md). Assume only
evidenced instructions and documents; unknown facts stay unknown. Every output
requires review by a qualified lawyer before reliance.

## Workflow

1. Load `$configure-employment-profile` output under the existing employment
   profile schema. Record approval, employer coverage basis, work location, role
   and duties, employment type, contract version, making/start dates, prior
   contracts, hours, remuneration and supplied instruments. Missing facts remain
   unknown; a draft profile cannot become approved by inference.
2. Use `$map-fair-work-obligations` to construct a clause-by-clause NES, modern
   award and enterprise agreement matrix. Verify Part 2-2 and s 61 on
   legislation.gov.au, and actual coverage/classification and current clauses at
   fwc.gov.au. Salary or a contract label does not establish award exclusion.
   Compare each contract clause with the applicable minimum; record conflict,
   silence or unresolved application.
3. Test set-off wording against named entitlements, payment periods, hours and
   records. Separate an annualised wage arrangement under an instrument from a
   contractual set-off. Require verified instrument conditions and case-law
   support through `$route-case-citation`; do not assume a generous salary cures
   every shortfall or permit cross-period offsets without support. Route missing
   payroll evidence to `$compute-underpayment-exposure-framework`.
4. Inspect IP ownership, pre-existing and third-party material,
   creator/chain-of-title evidence and any moral-rights consent. Do not promise
   ownership the employer cannot obtain or treat moral rights as assignable.
   Record unresolved legal propositions for official-source verification. For
   confidentiality, inspect protected information, duration, compelled
   disclosure, protected reporting, return/deletion and practical data access.
   Name the commercial-drafting area's clause-bank.md and
   `$review-draft-against-checklist` as optional drafting resources; use
   `$assess-australian-privacy-issues` for personnel-data handling rather than
   assume an employee-records exemption.
5. Review notice, payment in lieu, redundancy, misconduct and termination
   triggers against the verified NES and instruments. Use
   `$assess-termination-exposure` for dismissal issues and
   `$assess-restraint-of-trade` for post-employment restraints. Keep contractual
   rights and statutory remedies separate.
6. Use the [policy statutory hooks](../../references/policy-statutory-hooks.md)
   as the owner of fixed-term commencement and exception leads, and the
   extension reference for the clause checklist: verify ss 333E–333L, prior
   contracts, renewal options, continuity, exceptions, anti-avoidance and
   information-statement evidence. The s 333E limits include periods over two
   years, renewals and consecutive-contract conditions; test all limbs, not just
   the heading. An early-termination clause is not an automatic escape. Verify
   any s 333F exception and date-specific regulations on legislation.gov.au; do
   not treat the whole contract as void under s 333G.
7. Return prioritised clause findings, proposed options and unresolved
   decisions. A qualified lawyer must review coverage, legal effect and proposed
   changes before use.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

Return: Contract/instrument matrix; clause pinpoint; minimum/coverage source;
set-off and payroll evidence; IP/confidentiality gaps; fixed-term chronology and
exception evidence; termination hand-offs; proposed options. Include
scope/date/assumptions, evidence state for each proposition, official source
URL/identifier, version, provision or clause, actual checked date, unresolved
issue/resolver and qualified lawyer decisions. Snapshot dates never substitute
for the date a source was actually accessed. An unavailable named skill means
its step was not done; record it as not done or not verified and never perform
it from memory or substitute another skill.

## Fail closed

No contract text or no identifiable employer/role: `NOT READY`. Unknown award
coverage blocks the affected compliance conclusion. State-system contract
merits: `OUTSIDE SCOPE` with specialist hand-off. No signing, drafting final
advice or compliance certification. Unverified law is labelled `NOT VERIFIED`
with “verify against <official source>”; stop the affected conclusion while
completing supported issue spotting. No saving outside the approved matter
system, sending, filing, signing or payment is authorised by invocation of this
skill.
