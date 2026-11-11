# AI-tool mode

Rules for hosts that cannot run code. The AI-tool
bundle (`legal-skills-ai-<version>.zip`) is built for these hosts. Hosts that
can run code use the plugin and ignore this file.

## What changes

- Seven skills ship code in the plugin: `check-commonwealth-legislation`,
  `check-nsw-legislation`, `trace-commonwealth-legislative-change`,
  `check-australian-privacy-principles`, `route-case-citation`,
  `configure-legal-triage` and `compute-procedural-deadlines`.
  `map-tribunal-review-deadlines` uses the deadline computation, and
  `verify-deadline-basis` has a table fingerprint that is not computed here. In
  the bundle each of the nine has an `AI-tool mode` section in place of that
  step.
- Dates are never computed. A deadline result names the rule, its source, the
  inputs a person needs and `not computed`.
- Legislation checks give the official source and the search steps. If the
  host cannot browse, the result is `NOT VERIFIED` until a person supplies the
  source text.
- Validation and comparison steps are manual and are reported as manual. A
  manual check never supports an approved status. A skill's own `AI-tool mode`
  section says which other statuses a manual check can support.

## Reading the skills

- A dollar-prefixed skill name inside a skill's text means: open
  `skills/<name>/SKILL.md`. If that skill is not in this zip, say so and flag
  it; do not guess its content.
- Skills described as typed commands (`setup`, `start`, `check-citations`,
  `help`) are asked for by name here. When the user types one, ignore any
  `/legal-skills:` or `$` prefix on the command.
- A passing `--require-approved` validation for a legal triage profile cannot
  run here. Treat the profile as validated only when a person at the centre
  confirms it passed outside this host, and compare its review dates with
  today's date (ask the person for it if the host cannot supply it): any date that has passed means do not use it for live triage.
- Warnings in the rule tables that describe how the computation counts or
  rounds do not apply: nothing is computed. Read them as the rule's caveats.

## What does not change

- Official-source verification at use, fail-closed statuses, the result
  contracts and the human review gates apply as written in each skill.
- The model never does date arithmetic, with or without code.
- Any other mention of a computation step in a skill means the same
  identify-only output in this mode.

## Firm context

Firm material goes in `reference/firm/` after upload or in the host's own
store, never in the repository. See `reference/firm/README.md`.
