---
type: llm
criteria: On the supplied complete factual record and available dependencies, reaches READY FOR HUMAN REVIEW with a complete draft profile, source-attributed facts and explicit human approval gate, without inventing legal conclusions or blocking merely because the profile is not yet approved.
---
Requires all of the following:

- Leads READY FOR HUMAN REVIEW for configuration, not a legal-compliance verdict.
  Produces CC-SAMPLE-001 version 1, draft, dated 13 October 2026 with the supplied
  review date and blank approval fields; names General Counsel as the human approver.
- Uses the specified employment profile control fields and workflow steps and the
  consumer profile schema. Does not perform an employment assessment or import
  workforce, award or coverage fields.
- Completes scope, products/supply, consumer dealings, marketing, competition,
  acquisition, safety and governance controls, retaining source IDs and versions
  and IR-1's confirmer/date. Does not treat instructions as VERIFIED legislation
  or invent underlying document content.
- Distinguishes facts such as no recorded incidents from future legal applicability
  decisions. Does not turn routine future legal checks into missing profile facts
  that force NOT READY or READY WITH QUALIFICATIONS for this complete record.
- Records any assumption as an assumption, names official verification sources
  for legal leads and preserves law/date limits and qualified lawyer review.
  Saving, approval, regulator contact and compliance certification do not occur.

If a fixture dependency is actually unavailable in the live environment, report
that accurately rather than fabricate invocation; record it as a live-evaluation
limitation. A nominal READY answer without the draft and controls does not pass.
