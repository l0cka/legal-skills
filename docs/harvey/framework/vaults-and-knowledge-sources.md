# Vaults and Knowledge Sources

How to structure the firm knowledge a Harvey agent draws on, and how to wire
it into the agent. Labels follow the [source policy](README.md#source-policy).
Checked 25 August 2026.

## 1. One Vault per jurisdiction and practice, maintained by a named owner

**Documented.** Harvey positions Vaults as "curated repositories of internal
knowledge like precedents, templates, and playbooks" that "drive consistency
across your organization".
([Vault product page](https://www.harvey.ai/platform/vault))
**Indexed.** A Vault can be converted to a Knowledge Base "in a single click"
(5 February 2026); owners can "transfer ownership" (16 October 2025).
([Vault release notes](https://help.harvey.ai/release-notes/category/vault))

**Inference.** Give each agent one embedded Vault scoped to a single
jurisdiction and practice area, holding only current approved materials, with
a senior practitioner as owner. Do not mix NSW and Victorian precedents in
one Vault; the per-skill estate planning guides in `docs/harvey/` follow this.
Vault governance, not a separate version record, decides what the agent can
see.

## 2. Mirror the folder structure you already trust

**Documented.** Folder import preserves "nested folders, their associated
files, and all relevant metadata" from a DMS, and one-way sync means "when
files or folders change in the DMS, Harvey automatically detects and syncs
the updates" (early access at time of writing).
([File ingestion blog](https://www.harvey.ai/blog/building-new-file-ingestion-system-to-scale-firm-knowledge))
**Indexed.** "Upload and Sync entire folders into Vault" (19 March 2026);
Auto-group "converts each folder, along with the files inside it, into a file
group in review tables" (16 February 2026).
([Vault release notes](https://help.harvey.ai/release-notes/category/vault);
[Review Tables release notes](https://help.harvey.ai/release-notes/category/review-tables))

**Inference.** Because folders become Review Table file groups, a folder is
the unit an agent can reason about. Structure a Vault as:

```text
<jurisdiction>-<practice>/
  precedents/        one approved precedent per document type
  playbooks/         drafting rules the agent applies over the precedent
  instruction-sheets/ blank intake forms the user completes
  examples/          golden examples, if any; never client documents
```

Sync from the DMS folder the practice group already maintains rather than
uploading copies; a synced Vault cannot drift from the source of truth.

## 3. Name files so the agent can select them by exact name

**Documented.** Harvey's prompt guidance: refer to "sections or document
names", never pages.
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))

**Inference.** The agent's prompt selects a precedent by its exact Vault file
name. Use stable, self-describing names (`NSW-Will-Precedent-v3.docx`) and
record each name in the build record as a placeholder, as the estate planning
guides do. Rename a file only with a matching prompt change.

## 4. Know the limits before you design the run

**Indexed.** "Store up to 100k files or 100GB per vault" (22 September
2025); upload limit "500 MB" (11 February 2026); "Attach up to five knowledge
sources in a single query" (19 August 2026).
([Vault release notes](https://help.harvey.ai/release-notes/category/vault);
[Knowledge release notes](https://help.harvey.ai/release-notes/category/knowledge))
**Documented.** A Review Table can be built over "up to 10,000 files".
([Applied Compute blog](https://www.harvey.ai/blog/training-frontier-review-table-models-with-applied-compute))

**Inference.** Precedent Vaults are small by design. If a knowledge base
grows past what a reviewer can audit, split it; the agent's accuracy is
bounded by the curation, not the capacity.

## 5. Embed the Vault in the agent; let uploads be optional

**Indexed.** "Embed Vaults and Regional Knowledge Sources in Workflow
Builder" (3 December 2025); workflows "combine local uploads, DMS files, and
Vault files in a single run" (21 October 2025); Optional Steps let users
"skip inputs and use embedded content automatically" (2 December 2025);
embedded files can be added, deleted and replaced through "a new file
management UI" (9 October 2025); Knowledge Sources can be embedded by
"describing the Knowledge Sources you want to embed" in Words to Workflows
(1 April 2026).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

**Inference.** Embed the Vault at build time so every run sees the same
approved set. Make the file-upload step optional only when the embedded
content alone produces a valid deliverable; otherwise keep it required so a
run cannot silently proceed without matter inputs.

## 6. State the precedence rule in the prompt, because Harvey does not

**Inference.** No public page says what happens when a user upload and a
Vault file conflict. Write the rule into the Prompt block (see
[prompt principle 11](prompt-and-instruction-design.md#11-bound-the-agent-in-the-prompt-not-only-in-the-sharing-settings)):
"Use the embedded Vault precedent. Do not substitute an uploaded document for
a Vault precedent even if the user asks." Test it with an upload that
imitates a precedent.

## 7. Use a Review Table as the knowledge source for structured facts

**Indexed.** "Select review tables as a knowledge source to power analysis
and complete workflows" (18 February 2026); tables can be created from
knowledge bases or from vaults you have view-only access to (15 January and
11 February 2026).
([Review Tables release notes](https://help.harvey.ai/release-notes/category/review-tables))

**Inference.** Where an agent needs facts extracted from many documents (a
chronology, a clause register), feed it the Review Table, not the Vault, so
provenance is sentence-level and the extraction is reviewable before the
drafting step runs.

## 8. Choose Regional Knowledge Sources deliberately and name the jurisdiction

**Documented.** Knowledge Sources "are now organized into Regional Bundles";
Australia sits in the APAC bundle.
([100+ Knowledge Sources blog](https://www.harvey.ai/blog/100-knowledge-sources-available-in-harvey))
**Indexed.** Admins "manage access for public knowledge sources via new
toggles in Knowledge Settings" (2 February 2026).
([Knowledge release notes](https://help.harvey.ai/release-notes/category/knowledge))

**Inference.** Embed only the sources the skill's method actually cites, and
name the jurisdiction in the prompt as Harvey's own guidance requires. An
agent for an Australian workflow should not have a US bundle attached; it
widens the retrieval surface and the hallucination risk.

## 9. Lock the Vault down to what the agent's users need

**Indexed.** Owners "can now restrict what view-only users can do, blocking
file downloads, duplication, and visibility into review table prompts"
(7 July 2026); agents are shared with "Run, View, Edit, or Full access"
(11 March 2026); deleted Vaults have a 30-day recovery window (22 July 2026);
admins configure Vault retention per client matter (8 April 2026).
([Vault release notes](https://help.harvey.ai/release-notes/category/vault);
[Agents release notes](https://help.harvey.ai/release-notes/category/agents))

**Inference.** Agent users get Run access to the agent and view-only access
to the Vault with downloads blocked; only the Vault owner edits. Set
retention on any Vault that holds matter material; precedent Vaults are not
matter-scoped and should not sit under a client-matter retention rule.

## Review

Before publishing, record in the build notes: Vault name and owner, folder
layout, every exact file name the prompt selects, which inputs are optional,
the precedence rule text, the knowledge-source bundles attached, and the
sharing levels set. Re-check items 4, 5 and 9 against the release notes on
each rebuild; those limits and controls change most often.
