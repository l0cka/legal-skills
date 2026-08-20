# Precedent profile guide

A firm's human-designed precedent does not need machine markers. The workflow
keeps the original precedent unchanged and uses a separate, solicitor-confirmed
precedent profile to identify the only locations that a working copy may
change.

## Profile contract

Each profile records:

- **precedent identity** — jurisdiction, document type, firm title, version or
  approval date, and a content fingerprint when the platform can calculate
  one;
- **site register** — every permitted factual fill or clause choice, each with
  a stable `site_id`, its kind, exact location and permitted operation;
- **field map** — each factual `site_id` mapped to one instruction-record
  field;
- **clause-choice register** — each clause `site_id` mapped to one clause
  point and a closed list of firm-approved verbatim variants; and
- **confirmation record** — responsible solicitor, confirmation date and any
  qualifications.

The profile is firm-connected matter infrastructure. It is stored separately
from the precedent and is never embedded into, or committed with, client or
firm material in this public plugin.

## Exact site identity

Each site must be independently locatable in the unchanged precedent. Record
enough of the following to make it unambiguous:

```text
site_id: <stable identifier>
kind: <factual-fill | clause-choice>
structural_location: <heading; numbered clause; paragraph; table and cell;
  content control; existing blank or other visible location>
before_text: <exact visible text immediately before the site>
target_text: <exact text to replace, if any>
after_text: <exact visible text immediately after the site>
expected_occurrences: <normally 1>
operation: <replace target_text | insert between anchors | fill identified cell>
field_or_clause_point: <instruction field or registered clause point>
formatting_rule: <preserve site formatting or inherit from adjacent text>
```

A filename, page number, heading or approximate phrase alone is not a stable
site. For an empty table cell, content control or blank line, combine its
structural location with exact surrounding labels and expected occurrence
count. If the platform cannot distinguish the site from another location, it
is not registrable.

## Registration gate

On first use of a precedent, or after any drift:

1. Work from a read-only copy and identify every proposed factual and clause
   site. Do not edit the precedent.
2. Present the precedent identity, site register, field map and clause-choice
   register to the responsible solicitor.
3. Stop. The profile is not usable until that solicitor confirms it.
4. Record the confirmation without treating it as approval of any later
   matter-specific draft.

No confirmed profile means no fill. The workflow may return a proposed profile
under `NOT READY`; it must not fill a document in the same unconfirmed step.

## Clause-choice register

Each clause site has a closed list of approved variants. Every variant records
a stable identifier, verbatim clause text, its source in the precedent or a
connected firm playbook, and its approval state. The register is not
permission to compose, adapt, combine or improve clause text.

Before insertion for a matter, the responsible solicitor confirms the clause
point, variant identifier and verbatim text. A playbook may identify a
registered variant; it cannot add one or bypass confirmation. If no confirmed
variant resolves the clause point, leave the working copy unchanged at that
site and make the document `NOT READY`.

## Fill and drift rules

1. Make a working copy. Never modify the registered source precedent.
2. Before every fill, confirm that the working copy matches the profile's
   precedent identity. Where a content fingerprint is available, it must
   match. Every registered site's exact anchors, structural location and
   expected occurrence count must also match.
3. A mismatch, missing anchor, duplicate match, changed target text or
   unregistered blank is **precedent drift**. Stop the affected document and
   require a newly confirmed profile; never repair the locator by guesswork.
4. Fill a factual site only from the exact confirmed instruction-record field.
   Insert a clause only as the solicitor-confirmed verbatim registered
   variant. An unconfirmed or `cannot be determined` value leaves the site
   unchanged and appears in the gap report.
5. Repeated uses of one field require separately registered sites. Fill them
   identically and list every site in the change manifest.
6. Change nothing outside confirmed sites: not numbering, cross-references,
   punctuation, formatting-significant wording or metadata. Reconcile the
   complete output against the unchanged precedent. Any unregistered change
   makes the document `NOT READY`.

## Change manifest and gap report

For every registered site, the change manifest records the `site_id`, matched
location and anchors, source field or clause variant, exact before and after
content, and reconciliation result. The gap report lists unfilled registered
sites, unused instruction fields, unresolved clause choices, ambiguous or
unregistrable locations, and every drift finding.
