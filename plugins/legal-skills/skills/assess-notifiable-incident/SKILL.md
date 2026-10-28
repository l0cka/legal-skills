---
name: assess-notifiable-incident
description: Prepare an urgent preliminary assessment of an Australian workplace incident for a lawyer — whether the facts are a candidate notifiable incident (death, serious injury or illness, dangerous incident, and any extended-absence, violent-incident or suicide category the jurisdiction has enacted) under the governing WHS Act or Victoria's OHS Act 2004, who must notify which regulator and how quickly, site-preservation duties, and the parallel workstreams (privilege, insurer, workers compensation, police or coroner, employment) — with known facts, assumptions and unknowns kept apart. Use straight after an incident or when reviewing whether an earlier incident should have been notified. Do not use to decide whether to notify, to notify a regulator, to release a site, to respond to an inspector or to assess officer due diligence (use $assess-officer-due-diligence).
---

# Assess Notifiable Incident

Put the urgent steps first, then the analysis. Never delay a human escalation
while researching, and never decide that an incident is or is not notifiable;
the lawyer and the PCBU decide.

Read the [source and control method](../../references/whs-source-and-control-method.md)
first and work from the [WHS framework reference](../../references/whs-framework.md).

## Workflow

1. Escalate.
   - Open the output with `URGENT PRELIMINARY INCIDENT ASSESSMENT` and a
     `HUMAN DECISION REQUIRED` line naming the decision owner (the PCBU,
     advised by the responsible lawyer). State that
     notification under the governing Act is required immediately on
     becoming aware of a notifiable incident, so the notification decision
     cannot wait for this assessment to be finished.
   - Flag ongoing danger, a person still at risk, and any site that must not
     be disturbed, at the top. Do not instruct anyone to disturb, clean up or
     release a site.
2. Establish the incident record.
   - Separate known facts with their source, estimates, assumptions, disputed
     facts and unknowns. Record the time of the incident and the time the PCBU
     became aware, each with timezone, and never treat one as the other.
   - Record the workplace and the State or Territory where the work was
     carried out, the PCBU and any other PCBU on site, the people involved
     and their roles (de-identified), the injury, illness or exposure as
     described, any treatment received, the plant, substance or structure
     involved, and any notice already given.
   - Ask only for the minimum facts needed. Do not request medical records,
     names or images that the assessment does not need.
3. Select the governing Act.
   - Use the jurisdiction table. Where more than one PCBU is involved, record
     who may hold the notification duty and the site-preservation duty.
4. Test each candidate category.
   - For each category in the governing Act (death, serious injury or
     illness, dangerous incident, and any extended-absence, violent-incident
     or suicide category), record the defining provision, the facts that
     engage or tell against it, and a candidate status of `candidate`,
     `not engaged on known facts` or `cannot be determined`. Never resolve
     a `cannot be determined` row by assumption.
   - Apply the December 2025 model amendments only where the jurisdiction's
     enactment is verified; otherwise record them as model law that may
     become relevant.
5. Map the duties and workstreams.
   - Notification: who notifies, the regulator, the immediacy requirement and
     any written-notice period, each with its provision. Route any period that
     ends on a date to `$compute-procedural-deadlines`; do not compute it.
   - Site preservation: the duty, its exceptions and how long it lasts under
     the provision.
   - Parallel workstreams to name with an owner: legal professional privilege
     over the investigation, insurer notice, workers compensation claim,
     police or coroner involvement, employment steps for anyone involved
     (route to the employment-fair-work skills), and communications.
6. Verify.
   - Route every category definition, notification provision and
     commencement relied on to the jurisdiction's checker and record the
     evidence state.
7. Report using the result contract.

## Result contract

Lead with `URGENT PRELIMINARY INCIDENT ASSESSMENT`, then `READY FOR HUMAN
REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or `OUTSIDE SCOPE`.

```text
URGENT PRELIMINARY INCIDENT ASSESSMENT
HUMAN DECISION REQUIRED: <decision owner; notify or not; by when (immediately on awareness)>
Immediate flags: <ongoing danger; site not to be disturbed; people at risk>
Incident record: <known facts and source; assumptions; disputed; unknowns;
  incident time; awareness time; workplace and jurisdiction>
Governing Act: <Act; basis; checker used; evidence state>
Category matrix: <category; provision; facts for; facts against; candidate
  status; evidence state>
Notification and site duties: <duty holder; regulator; timing; provision;
  evidence state>
Parallel workstreams: <workstream; owner; next step>
Gaps: <facts needed to resolve each cannot-be-determined row>
Limitations: <preliminary assessment; no decision to notify or not; no breach conclusion>
```

## Fail closed

Return `NOT READY` only after the urgent block when the State or Territory or
the nature of the harm cannot be identified, and say which fact resolves it.
Route criminal defence strategy, coronial representation and workers
compensation merits to `OUTSIDE SCOPE` with the specialist named. Never decide
that an incident is or is not notifiable, never notify or draft a notification
as sent, never advise that a site may be disturbed or released, never treat
awareness time and incident time as the same, and never apply a model-law
amendment as the law in force.
