---
name: assess-consumer-guarantees
description: Assess Australian goods and services consumer-guarantee issues, remedy candidates, manufacturer exposure and warranty documents for lawyer review. Use for defects, failed services, refund disputes and limitation clauses. Do not use to decide entitlement, direct payment or treat a commercial warranty as the limit of statutory rights.
---

# Assess Consumer Guarantees

Australian Commonwealth law and ACL application in the identified state or territory.
Snapshot 2026-10-13; verify law at the conduct date and intended decision horizon.
Record assumptions explicitly; no missing fact defaults to a favourable answer.
Every output requires review by a qualified lawyer and does not replace professional judgment.

Read the [source and control method](../../references/consumer-competition-source-and-control-method.md)
and [official source register](../../references/official-source-register.md).
Verify every statutory citation at legislation.gov.au through `$check-commonwealth-legislation`;
for state or territory application use its official legislation publisher. Record provision,
version, effective date, checked date, observation and evidence state. If unavailable, say
'verify against <official source>' and leave the affected proposition not verified.

## Workflow

1. Fix supply date, jurisdiction, goods/services/mixed classification, price and purpose,
   supplier/manufacturer/importer roles, contract, warranty, defects and repair history.
   Verify ACL s 3 and Competition and Consumer Regulations 2010 reg 77A at
   legislation.gov.au before applying any guarantee: amount paid/payable calculation,
   prescribed amount, ordinary personal/domestic/household type, vehicle/trailer limb
   where relevant, and exclusions. Business purchase alone does not exclude consumer
   status. Verify the monetary amount at the supply date rather than assuming the
   Act's printed base figure is the operative threshold.
2. Verify ACL ss 51–64A in the official CCA Schedule 2 text. Map each relevant guarantee
   to an evidenced failure; do not collapse all guarantees into acceptable quality.
3. Assess major versus non-major/remediable failure separately for goods (ss 259–260)
   and services (ss 267–268), including cumulative failures, safety, purpose and repairability.
   Record disputed technical evidence and reasonable-time assumptions without deciding them.
4. Verify remedy pathways, rejection restrictions and consequences (ss 261–269),
   foreseeable loss and manufacturer pathways (ss 271–276). Distinguish supplier remedies,
   manufacturer damages and supplier indemnities; do not simply send the consumer away
   to the manufacturer or promise a refund for every defect.
5. Check s 64 non-exclusion and the limited s 64A pathway. Verify ordinary personal,
   domestic or household type, permitted remedy limits, excluded guarantees and fairness;
   business customer status alone does not justify a blanket cap or no-refund clause.
6. Verify ACL s 102 and Regulations reg 90 at legislation.gov.au: goods/services/mixed
   prescribed wording, exceptions, transparency, warrantor details, period, procedure,
   expenses and additional-rights statement. Record missing document elements; warranty
   expiry does not decide statutory entitlement. For operative wording use
   `$draft-services-agreement`; use `$review-draft-against-checklist` and the commercial
   drafting unfair-contract-terms checklist rather than duplicate its UCT assessment.
7. Give remedy candidates with evidence, limitations and questions for the qualified lawyer.
   Route possible harm to `$map-product-safety-obligations` immediately.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`. Evidence states apply to individual propositions separately.

Supply and coverage matrix; guarantee/failure/remedy rows; major-failure evidence; supplier/manufacturer distinction; limitation and warranty defects; urgent safety hand-off; reviewer decisions.
Every finding records source, version, pinpoint, checked date, assumptions, evidence
state, missing step and responsible qualified lawyer. No output is approval to act.

## Fail closed

If consumer status, failure severity, source version or decisive technical evidence is unresolved, give qualified alternatives or NOT READY for that conclusion. Never certify entitlement or extinguish rights from a warranty date.
