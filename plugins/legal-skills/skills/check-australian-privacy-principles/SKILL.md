---
name: check-australian-privacy-principles
description: Verify the Australian Privacy Principles, coverage, exemptions, codes and pending amendments from official sources. Use whenever a workflow relies on an APP or reuses an earlier APP analysis. Issue spotting: `$assess-australian-privacy-issues`. No case law.
---

# Check Australian Privacy Principles

## Scope

Verify the Australian Privacy Principles and their application framework from
current official sources; distinguish APP text, coverage and exemptions,
regulations and registered codes, known future amendments and versioned OAIC
guidance; detect change across a decision horizon; and return fail-closed
statuses for downstream privacy, breach and AI assessments. Use whenever an
Australian workflow relies on an APP or reuses an earlier APP analysis. Do not
treat schema-valid user JSON as verified law or use case law. For issue
spotting from facts use `$assess-australian-privacy-issues`.

Verify every fact-triggered APP framework layer before applying an APP. Never
assume that the text, application perimeter, instruments, codes, future changes
or guidance remains unchanged.

Read [references/app-verification-method.md](references/app-verification-method.md)
before starting.

## Workflow

1. Fix dates and facts.
   - Record the legal as-at date and decision horizon, including deployment,
     contract, retention and review dates actually known.
   - Identify the relevant entity, conduct, location, information, exemption,
     code and instrument facts. Do not invent a future horizon.
2. Establish official versions.
   - Invoke `$check-commonwealth-legislation` for the Privacy Act, Schedule 1
     and every material application provision at the as-at date.
   - Invoke `$trace-commonwealth-legislative-change` through the horizon when a
     version boundary, amendment or commencement may intervene.
   - Check current Privacy Regulations and the OAIC registered-code inventory.
     Treat OAIC APP text and Guidelines as regulator material, not legislation.
3. Build provenance-bound inventories.
   - Inspect complete Schedule 1 boundaries and enumerate every displayed APP
     without a hard-coded count or list.
   - Capture the official canonical and final URL, effective period, retrieval
     <!-- ai-tool:bundle: timestamp and the complete text; digests are not computed, a person with code computes them. --><!-- ai-tool:code -->timestamp, raw document SHA-256 and the complete text needed for
     fingerprinting.<!-- /ai-tool:code --> Do not reproduce full statutory text in the work product.
   - <!-- ai-tool:bundle: Record the application perimeter, applicable regulations and codes,
     and versioned guidance as separate layers using the reference schema; fingerprints are not computed, a person with code computes them --><!-- ai-tool:code -->Fingerprint the application perimeter, applicable regulations and codes,
     and versioned guidance as separate layers using the reference schema<!-- /ai-tool:code -->.
4. Compare the inventories layer by layer (APP text, application perimeter,
   instruments and codes, guidance). Hosts without code follow AI-tool mode.

   <!-- ai-tool:code -->
   ```bash
   python3 <skill-root>/scripts/compare_app_inventory.py validate <inventory.json>
   python3 <skill-root>/scripts/compare_app_inventory.py compare \
     <earlier.json> <later.json> --horizon <YYYY-MM-DD>
   ```

   `validate` returns only `INVENTORY SCHEMA VALID`. The script cannot prove
   that supplied content is official and never independently returns `APP
   FRAMEWORK VERIFIED`. The helper is optional, read-only and offline. Without
   command execution, perform the same comparison manually and record that the
   scripted check was not run.
   <!-- /ai-tool:code -->
5. Apply fail-closed statuses.
   - Use `APP FRAMEWORK VERIFIED` only after legislation checks establish the
     official source, applicable period, complete Schedule and every
     fact-triggered layer.
   - Use `APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED` for an
     APP text, application-perimeter, regulation or applicable-code change.
   - Use `APP TEXT UNCHANGED – APPLICATION LAW REVIEW REQUIRED` for a mapped
     future change or unresolved application layer.
   - Use `GUIDANCE REFRESH REQUIRED` for a guidance-only change, separately
     from statutory status.
   - Use `APP FRAMEWORK NOT VERIFIED – DO NOT RELY` whenever any required
     source, version, Schedule boundary, layer or comparison is unresolved.

## Result contract

Lead with the overall fail-closed status, then provide:

```text
As at and decision horizon: <dates and Australia/Sydney timezone>
APP text status: <source, compilation, effective period and comparison>
Application perimeter status: <definitions, coverage, exemptions and provisions>
Codes and instruments status: <Privacy Regulations and applicable registered code>
Known future amendments: <mapped change and horizon effect>
Guidance status: <page versions and refresh result>
Inventory: <identifier, heading, <!-- ai-tool:bundle: clause range; hash not computed, a person with code computes it> --><!-- ai-tool:code -->clause range and SHA-256 for every APP><!-- /ai-tool:code -->
Official sources: <links actually inspected>
Downstream effect: <proceed, refresh or do not rely>
Limitations and lawyer review: <unresolved legal or factual issues>
```

Case law is outside scope. Framework verification does not prove entity
coverage, compliance, interpretation or application to the facts.

## AI-tool mode

Use this section when the host cannot run
code. The AI-tool bundle ships this section and
leaves the code steps out; hosts that can run code ignore it. General rules:
[AI-tool mode](../../references/ai-tool-mode.md).

Compare the earlier and later inventories by hand.

1. For each of the four layers (APP text, application perimeter, regulations
   and codes, guidance), put the earlier and later text side by side.
2. Treat any difference in wording, heading, clause range or source URL as a
   change in that layer. Do not compute a hash: write `hash not computed, a person with code computes it` in
   the Inventory line of the result.
3. Apply the fail-closed statuses in step 5. A manual comparison never
   supports `APP FRAMEWORK VERIFIED` unless the official sources were opened
   and every layer was compared.
4. State in the result that the comparison was manual.
