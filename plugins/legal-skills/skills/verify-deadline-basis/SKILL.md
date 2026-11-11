---
name: verify-deadline-basis
description: Verify the court-rule and public-holiday tables behind the litigation-deadlines skills against official publishers. Use before first computed reliance or when a rule change is suspected. Never computes dates.
---

# Verify Deadline Basis

## Scope

Verify the computation-rule tables and holiday tables that the Australian
litigation-deadlines workflows rely on against the official publishers —
legislation sites for Interpretation Acts, court rules and tribunal Acts, and
government publications for public holidays — recording source URL, version
identifier, <!-- ai-tool:bundle: checked date (a table fingerprint is not computed, a person with code computes it) and detecting --><!-- ai-tool:code -->checked date and a table fingerprint, and detecting<!-- /ai-tool:code --> changes since
the last verification. This is the only path that moves a table entry to the
verified state that activates computation. Use before first computed reliance
in a matter, on the profile's verification posture, or when a rule amendment
is suspected. Do not use to compute dates, to verify Acts that the Australian
Legal Research checkers cover, or to bypass a publisher's bot protections.

Verify the tables computation depends on, entry by entry, against the
official publishers, and record the evidence. An entry stays
`pending-verification` — and the computation step keeps refusing to compute from it —
until this workflow confirms it.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
and verify the [computation-rule tables](../../references/computation-rules/)
and [holiday tables](../../references/holidays/).

## Workflow

1. Fix the verification scope.
   - Record which tables and entries the matter relies on, the assessment
     date and the <!-- ai-tool:bundle: previous version of each table if one exists --><!-- ai-tool:code -->previous fingerprint if one exists<!-- /ai-tool:code -->.
2. Verify each entry against its publisher.
   - For Acts (Interpretation Acts, Limitation Acts, tribunal Acts), route
     to the Australian Legal Research checkers
     (`$check-commonwealth-legislation`, `$check-nsw-legislation`,
     `$check-victoria-legislation` or the applicable sibling) and record
     the result.
   - For court rules and procedural instruments, check the official
     legislation publisher for the jurisdiction directly: confirm the
     provision exists, its current text supports the table's summary and
     period, and record the version identifier and checked date. Never
     bypass a publisher's bot protections; an unreachable source leaves the
     entry `pending-verification`.
   - For holiday tables, check the official government publication, confirm
     the dates and uncertain windows, and record the page's last-updated
     signal.
3. Record the outcome.
   - For each entry: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS` or
     `NOT VERIFIED`, with source URL, version identifier and checked date.
<!-- ai-tool:code -->
     Compute a fingerprint over the verified table content and compare with
     the previous fingerprint; report every change as a change, never
     silently.
<!-- /ai-tool:code -->
   - Present table updates as drafts for the practice to apply and store —
     the workflow itself marks nothing verified without the human applying
     the update.
4. Set the human decision gate.
   - Name who applies the table updates and who decides reliance where an
     entry stays `NOT VERIFIED`.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Scope: <tables and entries; assessment date<!-- ai-tool:bundle: ; previous version> --><!-- ai-tool:code -->; previous fingerprint><!-- /ai-tool:code -->
Verification: <per entry: state; source URL; version; checked date>
Changes: <differences from <!-- ai-tool:bundle: previous version; fingerprint not computed, a person with code computes it; affected --><!-- ai-tool:code -->previous fingerprint; affected<!-- /ai-tool:code --> period rules>
Draft updates: <table edits proposed for human application>
Human decision gate: <who applies updates; reliance decisions required>
Limitations: <verification is point-in-time; recheck per the profile's
  posture; no computation performed here; every date elsewhere remains
  provisional until confirmed>
```

## Fail closed

Return `NOT READY` when a publisher is unreachable or a provision cannot be
found — the entry stays `pending-verification` and computation stays off.
Never mark an entry verified from commentary, memory or a non-official
mirror, never bypass bot protections, and <!-- ai-tool:bundle: report every change --><!-- ai-tool:code -->report every fingerprint change<!-- /ai-tool:code -->
rather than reconciling it silently.

## AI-tool mode

Use this section when the host cannot run code. General rules:
[AI-tool mode](../../references/ai-tool-mode.md).

A fingerprint over table content needs code. Never state, estimate or invent
a hash. Record `fingerprint not computed` in the result, compare the table
text with the previous version by eye and report every difference as a change.
A person with code access computes and compares the fingerprint before the
update is applied. Every other step applies as written.
