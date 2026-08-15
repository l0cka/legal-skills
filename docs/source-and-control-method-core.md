# Source and control method core

Every plugin that uses the READY result vocabulary ships a
`references/<domain>-source-and-control-method.md` document. This file records
the parts of that document that are convention, so the next plugin copies them
deliberately instead of by drift. Conformance is enforced twice: the
evidence-states block is a generated region (`generate_registry.py --check`
fails CI when it drifts), and the invariant sentences below are asserted by
`tests/test_plugin_structure.py`.

## Two vocabularies, two axes

- **Evidence states** (`VERIFIED`, `VERIFIED WITH QUALIFICATIONS`,
  `NOT VERIFIED`, `OUTSIDE SCOPE`) attach to individual propositions — was
  this source checked in this session?
- **Result statuses** (`READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`,
  `NOT READY`, `OUTSIDE SCOPE`) attach to a whole workflow output in the
  skill's result contract.

They are different axes, not two generations of the same list. A workflow can
be `READY FOR HUMAN REVIEW` while individual propositions inside it are
`VERIFIED WITH QUALIFICATIONS`.

## The evidence-states block (generated)

Each method document wraps its four-bullet evidence-state list in
`<!-- generated:evidence-states -->` / `<!-- end:evidence-states -->` markers.
The canonical bullet text lives in `scripts/generate_registry.py`; the
per-plugin qualification lists are declared in the plugin's `catalog.json`:

```json
"evidenceStates": {
  "qualifications": ["commencement", "amendment", "application", "document-status"],
  "unverifiable": ["official source", "applicable version", "decisive fact"]
}
```

`qualifications` fills the `VERIFIED WITH QUALIFICATIONS` bullet and should
name the qualification types that genuinely arise in the domain (for example
`supersession` for layered AI guidance, `overlay` for corporations regimes,
`coverage` for holiday tables). `unverifiable` fills the `NOT VERIFIED`
bullet. Changing a list is a one-line, reviewable decision — never edit the
generated block directly.

## Invariant sentences (asserted by tests)

Every method document must carry, verbatim:

- the snapshot rule — dated facts are "a research snapshot, not a cached
  rule; every live workflow must recheck each source";
- the discovery boundary — commentary, "search results and model memory as
  discovery material, never authority";
- the profile conflict rule — "If profile content conflicts with a verified
  source, surface the conflict and stop the affected conclusion."; and
- the approval boundary — the model may draft a profile but "cannot mark it
  approved".

## Domain sections (hand-written)

Everything else is the domain's own: the scope and routing list, the
framework snapshot, the source hierarchy, the profile-precedence factual map,
and the human-control list of determinations the workflows never make. Write
them fresh for the domain; do not copy another plugin's wording for content
that is supposed to differ.

## Adding a plugin with a method document

1. Write `references/<domain>-source-and-control-method.md` with the section
   skeleton above and the marker pair around an empty evidence-states region.
2. Declare `evidenceStates` in the plugin's `catalog.json`.
3. Run `python3 scripts/generate_registry.py` to stamp the block.
4. Register the plugin in `tests/test_plugin_structure.py`.
