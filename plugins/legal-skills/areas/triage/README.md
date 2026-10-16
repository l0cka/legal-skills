# Legal Triage

Two staff-facing workflows for Australian community legal centres to configure
and conduct governed legal enquiry triage.

## Skills

`configure-legal-triage` creates a centre-local, versioned triage profile from
approved policies. It requires explicit human ownership for service scope,
urgency pathways, conflict checking, privacy, eligibility and referrals. The
bundled validator checks the structural and safety controls without sending the
profile anywhere.

`triage-legal-enquiry` uses an approved profile to prepare a provisional triage
record. It minimises client information, records only the status of an external
conflict check, identifies urgency and access needs, explains its provisional
reasoning, and leaves every consequential decision to authorised staff.

## Scope

Version 0.1 is staff-facing only. It has no connectors, client-management-system
writes or public chatbot mode. It does not give legal advice, assess merits or
credibility, perform conflict checks, accept or reject clients, or guarantee
that a referral will provide assistance.

Centre profiles remain outside this public repository. Do not commit client or
matter information, internal policies, private referral contacts or other
confidential material.

## Source basis and currency

The workflow is informed by public guidance from Community Legal Centres
Australia, the Office of the Australian Information Commissioner, the National
AI Centre and Justice Connect. It does not reproduce the CLC Risk Management
Guide or National Accreditation Scheme materials available only to centres.

The public guidance was reviewed on 14 August 2026. Each centre must verify its
current legal, professional, accreditation, funding and policy obligations
before approving a profile and whenever the profile is reviewed.
