# Australian estate planning source and control method

## Scope

Use this method when extracting an instruction record from a completed
instruction sheet or filling a firm precedent for a New South Wales or
Victorian estate planning matter covered by a jurisdiction-specific workflow.
Every output is a draft until the responsible solicitor reviews it, and no
output may be presented as a finished or executable document.

The workflows serve Australian legal practitioners only. Route rather than
duplicate:

- point-in-time verification of Acts belongs to the relevant jurisdiction
  checker where available, and otherwise to the official publisher directly;
- self-represented parties, jurisdictions not covered by an installed
  workflow, advance care directives, superannuation death benefit
  nominations, trusts and testamentary trusts, and probate or administration
  are `OUTSIDE SCOPE` — flagged, never assessed; and
- testamentary capacity, undue influence, family provision and notional
  estate exposure, and tax consequences are the responsible solicitor's
  calls in every workflow, flagged and never resolved.

## The precedent-profile assembly rule

The workflows never compose a legal document and never require the firm to
add machine markers to a human-designed precedent. The unchanged source
precedent remains read-only. A separate, solicitor-confirmed precedent profile
registers the only factual and clause sites that a working copy may change,
using structural locations and exact surrounding text under the
[precedent profile guide](precedent-profile-guide.md).

Every fill returns:

1. a **change manifest** — every registered site changed, its exact before and
   after content, source field or clause variant, anchor match and complete
   reconciliation against the unchanged precedent; any unregistered change
   makes the result `NOT READY`;
2. a **gap report** — every unfilled registered site, unused
   instruction-record field, unresolved clause choice, ambiguous location and
   drift finding (each of which makes that document `NOT READY`); and
3. the **draft banner** — `DRAFT — SOLICITOR REVIEW REQUIRED` above every
   document, outside the copyable document body.

No firm precedent means that document is `NOT READY`. A precedent without a
confirmed profile may be analysed to propose one, but it must not be filled
until the responsible solicitor confirms the precedent identity, site
register, field map and clause-choice register. There is no generic fallback
document, in any circumstance.

Before every fill, the source precedent and every registered site must match
the confirmed profile. A changed fingerprint, missing or duplicate anchor,
changed target text or ambiguous structural location is precedent drift: stop
and require a newly confirmed profile rather than adjusting a locator by
guesswork. A playbook may identify a registered clause variant, but only the
responsible solicitor may confirm its identifier and verbatim text for
insertion. The workflow never composes or adapts clause text.

This is an instruction-level contract rather than a deterministic script —
a deliberate decision recorded in `docs/adr/0001` of this repository: the
pack must remain plain markdown deployable on platforms that cannot execute
bundled code. The sidecar-profile and drift contract superseding the original
machine-marker mechanism is recorded in `docs/adr/0002`.

## Snapshot of the framework

At 20 August 2026 — this is a research snapshot, not a cached rule; every live
workflow must recheck its jurisdiction-specific sources:

1. **NSW wills** — Succession Act 2006 No 80 (NSW), current version 14 July
   2023 to date. Execution formalities in Part 2.1 (ss 5–10), revocation in
   ss 11–13, the 30-day survivorship construction default in s 35.
2. **NSW enduring powers of attorney** — Powers of Attorney Act 2003 No 53
   (NSW), current version 2 March 2025 to date. Creation requirements,
   prescribed witness classes and the witness certificate in s 19;
   attorney acceptance in s 20.
3. **NSW enduring guardianship** — Guardianship Act 1987 No 257 (NSW), current
   version 27 March 2021 to date. Appointment in Part 2 (ss 5–6E),
   including the prescribed-form requirement, eligible witness
   certification and appointee acceptance in s 6C.
4. **NSW prescribed forms** — the forms for enduring powers of attorney and
   enduring guardianship appointments are prescribed by regulation. The
   regulations were not verified for this snapshot: any reliance on a
   prescribed form carries a `form-prescription` qualification until the
   current regulation is checked.

5. **Victorian wills** — Wills Act 1997 (Vic), in-force version 036 from
   26 April 2021. Execution in ss 7–8C, witness rules in ss 10–11, marriage
   and divorce in ss 13–14, and the 30-day survivorship rule in s 39.
6. **Victorian enduring powers of attorney** — Powers of Attorney Act 2014
   (Vic), in-force version 007 from 26 April 2021, and Powers of Attorney
   Regulations 2025, in-force version 001 from 10 August 2025. Form,
   execution, witnessing and acceptance are addressed in ss 32–38 and
   regulation 6 with schedule 1 form 1.
7. **Victorian medical treatment decision makers** — Medical Treatment
   Planning and Decisions Act 2016 (Vic), in-force version 012 from 1 July
   2024, and Medical Treatment Planning and Decisions Regulations 2018,
   in-force version 001 from 12 March 2018. Appointment, acceptance and
   witnessing are addressed in ss 26–29 and 36–37 and regulation 6.

The provision texts relied on by these workflows are recorded, with their
version lines and access date, in the relevant execution formalities
reference.

## Sources

The controlling legislation sources are legislation.nsw.gov.au for NSW and
legislation.vic.gov.au for Victoria. Treat commentary, firm knowledge bases,
search results and model memory as discovery material, never authority. When
the deployment platform allows web access, re-verify every cited provision
against the relevant official publisher before relying on it; when it does
not, the dated formalities reference governs and the solicitor verifies
manually.

## Firm material and precedence

Firm-connected material — source precedents, confirmed precedent profiles,
the instruction-sheet template and a connected drafting playbook — is profile
content: it configures the workflows but is never authority for the law.
If profile content conflicts with a verified source, surface the conflict
and stop the affected conclusion. Playbook positions may identify only
registered variants, and every insertion requires solicitor confirmation and
is noted in the change manifest; where the playbook is silent or absent, the
working copy remains unchanged at that site, the clause choice goes to the gap
report and the document is `NOT READY`.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  application, form-prescription or extraction-provenance qualification
  remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

`extraction-provenance` qualifies a field extracted from an unregistered or
free-form instruction sheet, or from handwriting: the value was found but
its mapping is lower-confidence and the extraction gate must say so.

## Human control

The model may draft an instruction record, a proposed precedent profile or a
filled document set, but cannot mark it approved, confirmed or ready to
execute — only the responsible solicitor can. The workflows never:

- decide which documents a client needs;
- assess testamentary capacity or undue influence;
- resolve a conflict between instructions, or between an instruction and a
  playbook position;
- determine that an execution formality has been satisfied; or
- witness, execute, file, register or submit anything.
