# Australian work health and safety source and control method

## Scope

This method governs every skill in the work-health-safety practice area. The
area serves Australian legal practitioners and in-house lawyers advising
persons conducting a business or undertaking (PCBUs), officers and workers
under the harmonised Work Health and Safety Acts of the Commonwealth, the
states and the territories, and under Victoria's Occupational Health and
Safety Act 2004. It maps duties, issue-spots and prepares review material; it
never concludes that a duty was breached, that an officer exercised due
diligence, that an incident is or is not notifiable, or that a workplace is
safe or compliant.

Workers compensation, rehabilitation and return-to-work merits, criminal
defence strategy, coronial inquests, dangerous goods and mining, petroleum,
rail, maritime and aviation safety regimes, electrical safety licensing and
explosives are routed to human or specialist review. Employment-law
consequences (dismissal, discipline, general protections, discrimination)
belong to the employment-fair-work area.

Section numbers, thresholds, penalty figures and dates in this plugin are a
research snapshot, not a cached rule; every live workflow must recheck each
source. Each is a routing lead until the official source is checked in the
session that relies on it.

## Snapshot of the framework

At 28 October 2026 the framework has these layers (see the
[WHS framework reference](whs-framework.md) for the per-jurisdiction table and
what was checked on that date):

1. **The jurisdiction's Act.** The model WHS Act as enacted in the
   Commonwealth, New South Wales, Queensland, South Australia, Western
   Australia, Tasmania, the Australian Capital Territory and the Northern
   Territory, each with local variations; or, in Victoria, the Occupational
   Health and Safety Act 2004. Safe Work Australia states that Victoria is the
   only jurisdiction that has not implemented the model WHS laws.
2. **Regulations.** The jurisdiction's WHS Regulations, or Victoria's OHS
   Regulations, including the psychosocial hazard provisions and, in
   Victoria, the Occupational Health and Safety (Psychological Health)
   Regulations 2025.
3. **Codes of practice and compliance codes.** Approved codes are admissible
   as evidence of what is known about a hazard and how to control it. They are
   not themselves the duty; label them as approved codes, never as statute.
4. **Model laws and regulator guidance.** The model WHS Act and Regulations
   published by Safe Work Australia, and regulator guidance. A model-law
   amendment does not apply in a jurisdiction until that jurisdiction enacts
   it; label it as model law, never as the law in force.
5. **PCBU-supplied documents.** Risk registers, policies, safe work method
   statements, board papers, incident records and consultation records,
   version-identified.

## Source hierarchy

1. Verify the jurisdiction's Act and Regulations, and every commencement, with
   the jurisdiction's legislation checker: `$check-commonwealth-legislation`,
   `$check-nsw-legislation`, `$check-victoria-legislation`,
   `$check-queensland-legislation`, `$check-western-australia-legislation`,
   `$check-south-australia-legislation`, `$check-tasmania-legislation`,
   `$check-act-legislation` or `$check-northern-territory-legislation`. Never
   apply one jurisdiction's checker or text to another jurisdiction.
2. Use approved codes of practice and compliance codes as published by the
   jurisdiction's regulator, recording the title, version and approval or
   commencement date.
3. Use Safe Work Australia and regulator publications as model law,
   expectations and interpretation, labelled as such and never restated as
   the law in force. Record each page's last-updated date.
4. Use PCBU-supplied, version-identified documents for the PCBU's own
   position.
5. Treat law-firm commentary, safety consultancy content, search results and
   model memory as discovery material, never authority.
6. Route case law to `$route-case-citation`; do not rely on a decision that has
   not been verified at its official publisher.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  jurisdiction adoption, model-law status or document-status qualification
  remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

Give each finding its source URL or document identifier, version or effective
date, relevant provision, code clause or guidance section, checked date and
evidence state.

## Profile precedence

There is no separate WHS profile. Where an approved employment profile exists
(see the [employment profile schema](employment-profile-schema.md)), use it
only as a controlled factual map of the entity, its jurisdictions of
operation and its workforce. WHS facts that the profile does not hold
(workplaces, high-risk work, licences, contractors and labour hire on site,
officers and their roles) are recorded per matter as claims with their
source. A profile cannot establish who is a PCBU or an officer, what is
reasonably practicable, or that a control is adequate. If profile content
conflicts with a verified source, surface the conflict and stop the affected
conclusion. The model may draft a profile but cannot mark it approved.

## Time limits

Notification to a regulator is required immediately on becoming aware of a
notifiable incident under the jurisdiction's Act; the skills put that step
first and never wait for research to finish. Prosecution limitation periods,
review and appeal periods and any written-notice period are never computed
by the model. Name the governing provision and route the candidate date to
`$compute-procedural-deadlines`; where that skill has no verified table for the
step, report the period as identify-only with the provision cited.

## Human control

Every output names the responsible lawyer or decision owner and the decision
they must make. These skills never notify a regulator, never respond to an
inspector, notice or enforceable undertaking, never disturb or release an
incident site, never contact a worker, union, health and safety
representative or family, and never represent that a duty has been met.
