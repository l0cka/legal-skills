# Estate planning document assembly

Vocabulary for the `australian-estate-planning` plugin: turning a client's
completed instruction sheet into filled drafts of the firm's own precedents.

## Language

**Precedent**:
A firm's own template document containing `{{field_name}}` markers, connected
on the deployment platform and never committed to this repository.
_Avoid_: template, form, sample

**Instruction sheet**:
The completed client-facing questionnaire (PDF, Word or scan) a practitioner
uploads as the factual source for a matter.
_Avoid_: intake form, questionnaire

**Instruction record**:
The canonical structured set of fields extracted from an instruction sheet or
gathered by interview; the only source of factual values the fill step may use.
_Avoid_: intake data, client data

**Field map**:
The correspondence between instruction-record fields and a precedent's
factual markers, confirmed by the solicitor the first time a precedent is used.

**Clause-choice marker**:
A typed `{{clause_choice:clause_point}}` slot that accepts only verbatim text
from the precedent's closed, solicitor-confirmed clause-choice register.

**Clause-choice register**:
The stable variant identifiers, verbatim approved text, source and approval
state available for each clause-choice marker. A playbook may identify a
variant; it cannot create or approve one.

**Extraction gate**:
The mandatory halt at which the solicitor confirms the extraction table —
every field with its provenance — before any document work begins.

**Change manifest**:
The per-fill reconciliation listing every location changed, the marker
removed and the factual value or registered clause variant inserted, proving
nothing outside markers moved.

**Gap report**:
The per-fill list of unfilled markers, unused record fields and clause
choices awaiting the solicitor.
