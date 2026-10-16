---
name: assess-statutory-privacy-tort
description: Screen facts and AI-system use cases against the legislation-only statutory tort for serious invasions of privacy in Schedule 2 to the Privacy Act 1988 (Cth), including scope, elements, public-interest balancing, defences, exemptions, remedies and limitation issues. Use for surveillance, recording, scraping, profiling, inference, deepfakes, publication, disclosure or handling of intimate, location, health or financial information. Do not use case law or treat APP-entity coverage as a prerequisite.
---

# Assess Statutory Privacy Tort

Conduct a legislation-only screen under Privacy Act Schedule 2. Read
[references/statutory-tort-method.md](references/statutory-tort-method.md) before
starting.

## Workflow

1. Record the conduct date, actor, affected person, information, place,
   technology, purpose, audience, intent or recklessness facts, seriousness and
   alleged harm. Separate evidence, allegations, inferences and unknowns.
2. Invoke `$check-commonwealth-legislation` for Privacy Act section 94A and
   Schedule 2 at the relevant date. If the conduct or claim horizon crosses a
   change, invoke `$trace-commonwealth-legislative-change`.
3. Assess the statutory pathways separately: intrusion upon seclusion, misuse
   of information, or both. Test every statutory element without importing
   case-derived gloss.
4. Test the statutory public-interest balance, defences, exemptions, remedies
   and limitation provisions against verified text. State which party bears
   each statutory burden only where the text was checked.
5. Keep the tort screen independent from APP coverage. An actor can be outside
   the APP regime or within an APP exemption while Schedule 2 still requires
   analysis.

## Result contract

Lead with `STATUTORY PRIVACY TORT SCREEN — HUMAN REVIEW REQUIRED`:

```text
Conduct and date: <bounded facts>
APP coverage: <separate and not determinative>
Pathway | Statutory element | Facts for | Facts against | Unknown |
Verified provision | Preliminary status
Public-interest balance: <privacy interest and countervailing interests>
Defences and exemptions: <candidate only unless verified and fact-supported>
Remedies and limitation: <issues and dates requiring lawyer decision>
Evidence required: <shortest path>
```

Use `POTENTIALLY ENGAGED`, `NOT ESTABLISHED ON CURRENT FACTS` or `INSUFFICIENT
INFORMATION`, not a final liability conclusion. State that case law was outside
scope and not considered.
