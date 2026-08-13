---
name: check-australian-privacy-principles
description: Verify the Australian Privacy Principles framework in the applicable point-in-time compilation of the Privacy Act 1988 (Cth), enumerate every principle from official Schedule 1 text without assuming a fixed count or numbering, detect textual or structural change across relevant dates, and return a fail-closed status for downstream privacy, breach and AI-use-case assessments. Use whenever an Australian legal workflow relies on an APP, spans a future deployment or retention period, updates an earlier APP assessment, or needs to determine whether cached APP content remains reliable. Do not use OAIC guidance as a substitute for the current Act, and do not use for case law or final legal advice.
---

# Check Australian Privacy Principles

Verify the APP framework from official point-in-time legislation before applying
an APP to facts. Never assume that the number, numbering, heading or text of the
principles remains unchanged.

Read [references/app-verification-method.md](references/app-verification-method.md)
before starting. It defines the inventory schema, source hierarchy, comparison
method, decision horizon and downstream stop rule.

## Workflow

1. Fix the dates and scope.
   - Record the legal as-at date and the decision horizon. The horizon must
     include any proposed deployment, contract, retention or scheduled review
     date relevant to the advice.
   - Use today's `Australia/Sydney` date if no as-at date is supplied and state
     that choice. Do not invent a future horizon.
   - Limit this check to Schedule 1 APP text and identified framework changes.
     Verify definitions, APP-entity coverage, exemptions, codes, regulations
     and other application provisions separately.
2. Establish the official versions.
   - Invoke `$check-commonwealth-legislation` for the *Privacy Act 1988* (Cth),
     Schedule 1, at the as-at date. Preserve the Title ID, compilation Register
     ID, effective period, currency flags and official links.
   - If the decision horizon passes the applicable compilation's end date, or
     any amendment, commencement or currency flag may affect the analysis,
     invoke `$trace-commonwealth-legislative-change` through the horizon.
   - Treat the Federal Register of Legislation as controlling. Label OAIC APP
     pages and Guidelines as regulator guidance, not the current statutory
     text.
3. Build complete inventories.
   - Inspect official Schedule 1 text in every compilation needed for the
     comparison. Enumerate every provision presented as an Australian Privacy
     Principle; do not start from a hard-coded APP list.
   - For each principle capture its displayed identifier, complete heading,
     clause range if shown, and complete statutory text. Attest that the whole
     Schedule was inspected. Follow the JSON schema in the reference.
   - Do not copy the statutory text into the legal work product. Use it only to
     produce a normalized SHA-256 fingerprint and pinpointed analysis.
4. Compare deterministically.
   - Validate each inventory and, when more than one version is relevant, run:

     ```bash
     python3 <skill-root>/scripts/compare_app_inventory.py validate <inventory.json>
     python3 <skill-root>/scripts/compare_app_inventory.py compare \
       <earlier.json> <later.json>
     ```

     Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
     script checks provenance and completeness fields, fingerprints normalized
     full text, and detects additions, removals, reordered identifiers, heading
     changes, clause-range changes and text changes. It does not retrieve or
     interpret legislation.
5. Apply the stop rule and report.
   - Use `APP FRAMEWORK VERIFIED` only when the applicable official inventory
     was completed and every required comparison shows no APP change.
   - Use `APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED` when
     any structural or textual change is detected. Do not reuse prior APP
     conclusions or issue a downstream suitability recommendation until a
     lawyer refreshes the affected analysis.
   - Use `APP FRAMEWORK NOT VERIFIED – DO NOT RELY` when the source, applicable
     version, complete Schedule, horizon or comparison cannot be established.
     Do not fall back to memory, a static checklist, the OAIC page or a search
     snippet.

## Result contract

Lead with exactly one framework status, then provide:

```text
As at: <YYYY-MM-DD, Australia/Sydney>
Decision horizon: <date or not supplied>
Official title and Title ID: <Privacy Act 1988 and verified ID>
Applicable compilation: <Register ID, number and effective period>
Compared compilation(s): <Register IDs and effective periods, or not required>
Schedule coverage: <complete/not established>
Inventory: <identifier, heading, clause range and SHA-256 for every item>
Detected changes: <added, removed, reordered or modified items with fields>
Related application provisions: <checks completed and checks still required>
Official sources: <Federal Register links actually inspected>
Guidance used: <OAIC material, clearly labelled, or none>
Downstream effect: <may proceed / affected analysis must be refreshed / do not rely>
Limitations and lawyer review: <unresolved legal or factual issues>
```

Case law is outside scope. Do not interpret a detected change, determine legal
effect or claim that framework verification proves substantive APP compliance.
