---
name: assess-automated-decision-transparency
description: Assess current and commencing Australian privacy transparency obligations for automated and AI-assisted decisions, including Privacy Act APP 1.7–1.9 commencing 10 December 2026 and Western Australia PRIS IPP 10 from 1 July 2026. Use for decision inventories, privacy-policy readiness, consequential AI decisions, procurement and deployments spanning those dates. Do not use for case law, discrimination-law conclusions or autonomous deployment approval.
---

# Assess Automated Decision Transparency

Separate current law, enacted future law and transition work. Read
[references/automated-decision-method.md](references/automated-decision-method.md)
before starting.

## Workflow

1. Inventory each decision, affected people, rights or interests, consequence,
   data categories, program role, human role, entity, jurisdiction and decision
   date. Distinguish a solely automated decision from a program doing something
   substantially and directly related to making a decision.
2. Invoke `$check-commonwealth-legislation` for the Privacy Act at the current
   and decision dates and `$trace-commonwealth-legislative-change` through 10
   December 2026 where relevant. Invoke
   `$route-australian-privacy-jurisdiction` for State or Territory overlays.
3. Apply the future-law ledger in the reference even if no future compilation
   yet displays APP 1.7–1.9. For decisions after commencement, do not exclude a
   system merely because its arrangement, data use or acquisition occurred
   earlier.
4. Determine the privacy-policy information needed for in-scope program use:
   kinds of personal information, solely automated decisions and decisions
   involving relevant program-performed steps. Verify exact current text before
   stating an obligation.
5. Treat the Children’s Online Privacy Code as developing unless the current
   official register confirms registration and application. Keep guidance,
   discrimination, administrative and employment issues in separate rows.

## Result contract

Lead with one status:

- `CURRENT REQUIREMENTS MAPPED — FUTURE CHANGE NOT WITHIN HORIZON`
- `CURRENT TEXT VERIFIED — KNOWN FUTURE CHANGE MAPPED`
- `AUTOMATED-DECISION LAW CHECK REQUIRED — DO NOT RELY`

Then provide:

```text
Decision | Date | Entity and jurisdiction | Program role | Personal information |
Potential significant effect | Current law | Future law | Transition action |
Privacy-policy disclosure | Evidence gap | Owner and due date
```

State that case law was outside scope. Do not describe readiness work as proof
of compliance or approve the decision system.
