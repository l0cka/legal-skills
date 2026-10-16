---
name: track-accc-developments
description: Check the Australian ACCC watch register on demand against official legislation, guidance and reform sources. Use before advice or a periodic horizon review to identify changed merger, consumer, competition and safety positions. Do not use as an unattended monitor, auto-update a register or treat proposals and allegations as obligations.
---

# Track ACCC Developments

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

1. Record review date, prior review, jurisdiction, legal decision horizon and affected
   standing advice. Read the [watch register](references/watch-register.json).
2. Retrieve every item's official text or publication and compare snapshot status with now.
   For statutory items use `$check-commonwealth-legislation` and
   `$trace-commonwealth-legislative-change`; check provisions and commencement, not just
   publication badges. Record unchanged, moved, resolved or cannot be determined.
3. Sweep legislation.gov.au, ACCC guidance/enforcement/priorities and Product Safety
   publications for new items. Separate enacted/in-force, enacted/not-yet-in-force,
   announced/proposed only, guidance and enforcement allegations. Verify decisions through
   `$route-case-citation` before treating a case result as authority.
4. Map each movement to guarantee, marketing, merger, competition and safety outputs.
   Recommend re-running affected assessments; do not silently preserve stale conclusions.
5. Produce proposed register changes with old/new status, source, checked date, evidence
   and review trigger. A qualified lawyer/register owner decides adoption; do not modify
   the shipped register, install monitoring, notify people or schedule tasks.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`. Evidence states apply to individual propositions separately.

Review context; item status/movement/source/evidence table; proposed new items; impacted workflows and rechecks; unavailable sources; qualified lawyer/register-owner decisions.
Every finding records source, version, pinpoint, checked date, assumptions, evidence
state, missing step and responsible qualified lawyer. No output is approval to act.

## Fail closed

When most primary sources cannot be reached return NOT READY. Never report no change from an unavailable source, treat a Bill as enacted or silently update a snapshot.
