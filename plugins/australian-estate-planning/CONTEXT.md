# Estate planning document assembly

Vocabulary for the `australian-estate-planning` plugin: turning a client's
completed instruction sheet into filled drafts of the firm's own NSW or
Victorian precedents.

## Language

**Precedent**:
A firm's own human-designed source document, connected on the deployment
platform, kept unchanged during registration and never committed to this
repository.
_Avoid_: template, form, sample

**Instruction sheet**:
The completed client-facing questionnaire (PDF, Word or scan) a practitioner
uploads as the factual source for a matter.
_Avoid_: intake form, questionnaire

**Instruction record**:
The canonical structured set of fields extracted from an instruction sheet or
gathered by interview; the only source of factual values the fill step may use.
_Avoid_: intake data, client data

**Precedent profile**:
A sidecar registration of the precedent's identity, permitted sites, field
map, clause-choice register and solicitor confirmation. It is separate from
the source precedent.

**Registered site**:
One exact location in a precedent profile where a working copy may change,
identified by structural location, exact surrounding text, expected occurrence
count and a stable site identifier.

**Field map**:
The correspondence between instruction-record fields and registered factual
sites in a precedent profile.

**Clause-choice register**:
The stable variant identifiers, verbatim approved text, source and approval
state available for each registered clause site. A playbook may identify a
variant; it cannot create or approve one.

**Precedent drift**:
A fingerprint, anchor, target, structure or occurrence-count mismatch between
the source precedent and its confirmed profile. Drift blocks filling until a
new profile is confirmed.

**Extraction gate**:
The mandatory halt at which the solicitor confirms the extraction table —
every field with its provenance — before any document work begins.

**Change manifest**:
The per-fill reconciliation listing every registered site changed, its exact
before and after content, the factual value or registered clause variant used,
and proof that nothing outside registered sites changed.

**Gap report**:
The per-fill list of unfilled sites, unused record fields, unresolved clause
choices, ambiguous locations and precedent drift.
