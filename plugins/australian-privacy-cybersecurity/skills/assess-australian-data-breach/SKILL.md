---
name: assess-australian-data-breach
description: Triage a suspected Australian privacy or cybersecurity incident for lawyers; extract incident facts; identify potentially applicable Commonwealth, State, Territory and sectoral breach regimes; verify Commonwealth and NSW legislation through the corresponding legislation skills; distinguish statutory, regulatory, contractual and voluntary reporting; and prepare a time-sensitive assessment and action matrix. Use for suspected unauthorised access, disclosure or loss, ransomware, cyber extortion, vendor incidents and breach-response planning. Do not use for case law, forensic conclusions, live containment, threat hunting, external reports or autonomous notification decisions.
---

# Assess Australian Data Breach

Prepare a privileged-workstream-ready preliminary assessment for a lawyer. Do
not conclude that a breach is notifiable merely because a security incident
occurred, and do not delay urgent human escalation while researching.

Read [references/breach-assessment-method.md](references/breach-assessment-method.md)
before starting. It defines the fact schema, regime prompts, deadline controls
and source rules.

## Workflow

1. Escalate and protect.
   - Flag immediate safety, ongoing compromise, destructive activity, material
     service disruption or an apparently running statutory clock for urgent
     human attention.
   - Ask only for the minimum de-identified facts. Do not request credentials,
     live malware, exploit code, unnecessary identifiers or complete datasets.
   - Do not take containment action, contact a threat actor, make a payment,
     notify a person or regulator, or submit a report. Preserve the lawyer's
     approval boundary and the forensic evidence-preservation plan.
2. Establish the incident record.
   - Separate known facts, source of each fact, estimates, inferences,
     assumptions, disputed facts and unknowns.
   - Record detection and awareness times with timezone; suspected occurrence
     window; systems and custodians; data types and protections; affected and
     potentially affected people; location; actors; containment/remediation;
     recipients; vendors; critical services; ransom demand or payment; and
     existing notices.
   - Do not equate detection, confirmation, containment, assessment completion
     or occurrence. Record each timestamp independently.
3. Map candidate regimes.
   - Test the Privacy Act Notifiable Data Breaches scheme and each applicable
     State, Territory, health, critical-infrastructure, cyber-extortion,
     telecommunications, financial-services or contractual regime.
   - Distinguish mandatory notice, assessment duties, voluntary reports,
     contractual notice, insurance conditions and internal escalation.
   - Treat numerical thresholds, triggering knowledge standards, recipients,
     content requirements and time periods as propositions requiring current
     verification.
4. Verify law and calculate cautiously.
   - Invoke `$check-commonwealth-legislation` for every material Commonwealth
     title or provision and the relevant incident date. Invoke
     `$check-nsw-legislation` for every material NSW title or provision.
   - For another State or Territory, inspect its official legislation source.
     If a version or commencement point cannot be established, use `NOT
     VERIFIED` and escalate the check.
   - Calculate a deadline only after verifying the trigger, period, counting
     rule and relevant facts. Show the trigger time, timezone, calculation and
     uncertainty. Never invent a date from an incomplete record.
   - State that case law was not considered. Do not search for or rely on it.
5. Assess and hand off.
   - Address reasonable-likelihood, serious-harm, remedial-action and
     multi-entity issues only against verified text and stated facts.
   - Build one row per possible obligation. Give the earliest plausible
     deadline prominence without describing an uncertain date as final.
   - Identify the decision owner, evidence needed and next action. Reserve all
     notification and legal conclusions for a lawyer and authorised incident
     lead.

## Result contract

Lead with `URGENT PRELIMINARY BREACH ASSESSMENT — HUMAN DECISION REQUIRED`, then
provide:

```text
Incident status: <suspected/ongoing/contained/unknown, not a legal conclusion>
Scope and exclusions: <including no case law and no forensic opinion>
Jurisdictions and sectors: <identified and unresolved>
As at: <YYYY-MM-DD HH:MM timezone>
Immediate human escalations: <owner and reason>
Known facts, assumptions, disputes and unknowns: <separate sections>

Potential-obligation matrix:
Priority | Regime | Entity/role | Trigger and threshold | Trigger facts |
Verification status | Earliest plausible deadline | Recipient/action |
Source | Missing evidence | Decision owner

Harm and remediation assessment: <facts for and against, uncertainty retained>
Notification coordination: <statutory, contractual, insurer and voluntary channels separated>
Action plan: <owner, action, time, dependency and approval>
Preservation and privilege considerations: <questions for the lawyer and forensic lead>
Limitations and review: <currency, factual and interpretation gaps>
```

Use `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `NOT VERIFIED`, `PRIMARY TEXT
CHECK REQUIRED`, or `OUTSIDE SCOPE` for legislation status. Link the official
text and version actually inspected. Do not describe an OAIC or ACSC web form,
guideline, policy, standard or contract as legislation.
