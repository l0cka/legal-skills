---
name: generate-precedent-profile
description: Generate a proposed sidecar precedent profile from uploaded, human-designed firm estate-planning precedents for New South Wales or Victoria. Inspect each source read-only, record its identity and fingerprint, locate exact factual and clause sites, map factual sites to the relevant instruction-record schema, register only existing verbatim clause variants, report coverage and gaps, and stop for responsible-solicitor confirmation. Use when a practitioner uploads a clean firm precedent that has no confirmed profile or has changed since profiling. Do not use to modify or fill a precedent, process executed or client-completed documents, invent clauses or fields, approve a profile, or handle other jurisdictions or document types.
---

# Generate Precedent Profile

Turn each uploaded clean firm precedent into a proposed sidecar profile without
modifying the source or inserting matter data. The responsible solicitor, not
the workflow, decides whether the proposal becomes a confirmed profile.

Read the
[source and control method](../../references/estate-planning-source-and-control-method.md)
and [precedent profile guide](../../references/precedent-profile-guide.md)
first. For NSW, use the
[NSW instruction record schema](../../references/instruction-record-schema.md).
For Victoria, use the
[Victorian instruction record schema](../../references/vic-instruction-record-schema.md).

## Workflow

1. Fix scope and source integrity.
   - Confirm the uploader is acting in a professional capacity and identifies
     the jurisdiction, document type and responsible solicitor. Supported
     documents are the NSW or Victorian estate-planning documents covered by
     the two assembly skills.
   - Treat each upload as confidential firm material. Work read-only and never
     commit, publish or embed the source in the profile.
   - Stop if a file appears executed, client-completed, matter-specific,
     corrupted, password-locked or unrelated to a supported firm precedent.
     Ask for a clean source precedent; do not extract client data into a
     profile.
2. Record precedent identity.
   - Record the original filename, native format, jurisdiction, document type,
     firm title, stated version or approval date, and inspection date. Do not
     infer missing version metadata.
   - Calculate a content fingerprint from the original upload when the
     platform permits. Otherwise record `fingerprint not available` and the
     `format-fidelity` qualification. Never fingerprint a transformed export
     and present it as the original.
   - Record any conversion, OCR or text-extraction step. Extracted text is
     navigation evidence, not proof that a location is stable in the original.
3. Inventory proposed sites.
   - Inspect headings, numbered clauses, paragraphs, tables and cells, content
     controls, existing blanks, drafting notes, alternative clauses and
     repeated factual locations. Do not assume every blank or example value is
     intended to be replaced.
   - Give each independently locatable site a stable `site_id`. Record its
     structural location, exact `before_text`, `target_text` where present,
     exact `after_text`, expected occurrence count, operation and formatting
     rule under the precedent profile guide.
   - A page number, approximate phrase or extracted-text offset alone is not a
     stable locator. Mark an indistinguishable, OCR-dependent or ambiguous
     location `unregistrable`; never manufacture certainty.
4. Map facts and clause choices.
   - Map each factual site to exactly one field in the relevant jurisdictional
     instruction-record schema. Record every schema field as `mapped`,
     `not present`, `not applicable` or `cannot be determined`, with the source
     location and reason. Never invent a new field merely to explain precedent
     text; list a genuine extra requirement as an unmapped precedent field for
     solicitor review.
   - For each clause site, register only variants already present verbatim in
     the precedent or a connected firm playbook. Record the variant identifier,
     verbatim text, source and approval state. Never compose, combine, improve
     or select a variant.
   - Register repeated uses of a fact as separate sites mapped to the same
     field. Identify cross-document consistency needs without merging profiles.
5. Produce the proposal and halt.
   - Return one separate proposed sidecar profile per uploaded precedent. Use
     Markdown unless the practitioner requests another portable structured
     format.
   - Include the precedent identity, site register, field map, clause-choice
     register, schema-coverage table, gap report and confirmation block. Set
     `profile_status: proposed` and `confirmation_status: pending`.
   - Present the confirmation checklist and stop. Do not modify or fill the
     source, create a working copy, or mark the profile confirmed. A later
     assembly workflow may use it only after the named responsible solicitor
     confirms the exact profile version.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Upload inventory: <one row per file; clean/blocked; jurisdiction; document type>
Proposed profiles: <profile_id; profile_version; source identity and fingerprint;
  profile_status: proposed; confirmation_status: pending>
Site register: <site_id; kind; structure; exact anchors and target; occurrence;
  operation; field or clause point; formatting rule>
Schema coverage: <every relevant field: mapped/not present/not applicable/
  cannot be determined; source and reason>
Clause-choice register: <site; variant IDs; verbatim source text; approval state>
Gap report: <unregistrable or ambiguous locations; unmapped precedent fields;
  unavailable metadata; conversion/OCR qualifications; unresolved variants>
Confirmation gate: <responsible solicitor; exact profile version; checks and
  confirmation outstanding>
Limitations: <source unchanged; no matter fill; no legal advice; profile cannot
  be used until confirmed>
```

Use `READY FOR HUMAN REVIEW` when the clean original was inspected and every
proposed site is unambiguous. Use `READY WITH QUALIFICATIONS` only for a
non-blocking limitation such as an unavailable original-file fingerprint where
all sites remain stable in the native source. Use `NOT READY` when source
integrity, classification, coverage or any intended site is unresolved. Use
`OUTSIDE SCOPE` for unsupported jurisdictions, document types or requested
document filling or drafting.

## Fail closed

Return `NOT READY` for an upload that is not a clean source precedent, cannot
be inspected in its native structure, has an ambiguous jurisdiction or
document type, contains an intended but unregistrable site, or cannot be
reconciled against the relevant instruction schema. List the exact file and
reason. Never alter the upload, rely on an extracted-text position as the sole
anchor, copy client data into a profile, invent a field or clause, treat silence
as approval, or mark a proposal confirmed — one blocked file never blocks a
separate clean precedent.
