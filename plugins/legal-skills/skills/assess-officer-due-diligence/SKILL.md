---
name: assess-officer-due-diligence
description: Review the evidence that an Australian company's directors and other officers exercise WHS due diligence — mapping board papers, reports, audits, resourcing, incident and hazard escalation, legal-compliance processes and verification against each element of the officer duty in the governing model WHS Act (s 27 in the model), or against officer liability in Victoria's OHS Act 2004 — and listing evidence gaps and questions for the board, with industrial manslaughter exposure flagged by jurisdiction. Use for board WHS governance reviews, director inductions, post-incident governance reviews and preparing officer briefings. Do not use to conclude that an officer did or did not exercise due diligence, to defend a prosecution, to decide officer status, or for general director duties (use $assess-director-duties-governance).
---

# Assess Officer Due Diligence

Map the evidence to each element of the officer duty and show the gaps. The
review never concludes that due diligence was or was not exercised; that is
for the responsible lawyer and, ultimately, a court.

Read the [source and control method](../../references/whs-source-and-control-method.md)
first and work from the [WHS framework reference](../../references/whs-framework.md).

## Workflow

1. Fix the scope.
   - Record the PCBU, its jurisdictions, the officers or roles under review
     and why each may be an officer (record officer status as a question),
     the review period and the documents supplied with their versions.
   - Record the purpose: routine governance review, induction, or a
     post-incident review. For a post-incident review, flag that privilege
     over the review must be settled by the responsible lawyer before work
     product is created, and route the incident itself to
     `$assess-notifiable-incident`.
2. Select the governing provision.
   - Model WHS Act jurisdictions: the officer duty and its due diligence
     elements. Victoria: officer liability under the OHS Act 2004, which is a
     different mechanism; never map the model elements onto Victoria as
     duties, though they may be used as a labelled governance benchmark.
3. Map evidence to elements.
   - For each element, record the supplied evidence (document, date, version),
     what it shows, what it does not show, and a rating of `evidence
     supplied`, `partial evidence` or `no evidence supplied`. A rating is about
     the record supplied, never a finding about the officer.
   - Include verification: evidence that officers checked that resources and
     processes were provided and used, not only that they were reported.
4. Flag exposure.
   - Record the offence categories and, where the jurisdiction has enacted
     one, the industrial or workplace manslaughter offence, each with its
     provision and evidence state. State no penalty figure without its
     source and effective date.
   - Route insurance and indemnity questions for officers to the responsible
     lawyer; route general director duties to
     `$assess-director-duties-governance`.
5. Prepare board questions.
   - List the questions the officers should be able to answer and the
     evidence that would answer each.
6. Verify.
   - Route every provision relied on to the jurisdiction's checker and record
     the evidence state.
7. Report using the result contract and name the responsible lawyer.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Scope: <PCBU; jurisdictions; officers or roles; officer-status questions; period; purpose>
Governing provision: <Act; provision; checker used; evidence state>
Evidence map: <element; evidence (document, date, version); shows; does not
  show; rating (evidence supplied / partial evidence / no evidence supplied)>
Exposure flags: <offence or manslaughter provision; jurisdiction; evidence state>
Board questions: <question; evidence that would answer it>
Gaps: <missing documents; unverified propositions; resolver>
Human decision gate: <responsible lawyer; decisions required>
Limitations: <evidence review only; no due diligence conclusion; no officer-status conclusion>
```

## Fail closed

Return `NOT READY` when no governance documents are supplied and no officer
role can be identified; say which documents would allow the review. Route
prosecution defence, enforceable undertakings and regulator correspondence to
`OUTSIDE SCOPE` with the specialist named. Never conclude that an officer did
or did not exercise due diligence, never conclude that a person is or is not
an officer, never state a penalty without its source and effective date, and
never map the model due diligence elements onto Victoria as duties.
