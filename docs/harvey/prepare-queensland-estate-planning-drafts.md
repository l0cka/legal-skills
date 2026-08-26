# Harvey Workflow Builder: Prepare Queensland Estate Planning Drafts

This guide maps `assemble-qld-estate-documents` to one private Harvey Workflow
agent. It contains no firm precedent, matter data or client information.

Harvey's public documentation confirms that Workflow Builder can embed Vaults
and knowledge sources, combine Vault and uploaded files in a run, and create or
edit Word files. It does not document a general-purpose private configuration
record or a mid-run approval pause. This design therefore uses the embedded
Vault and the workflow's selected files as its source of truth. Confirm these
features in the target workspace before publishing. The end-to-end block path
below is an implementation inference from those documented capabilities and
must be tested in the target workspace.

## Workflow boundary

Create one Workflow agent named **Prepare Queensland Estate Planning Drafts**
for one client in a practitioner-led Queensland matter. Start a separate run
for each member of a couple. Do not combine it with the NSW or Victorian
workflows.

The agent may prepare a will and an enduring power of attorney. Advance health
directives are flagged, never drafted.

## Harvey Vault placeholders

Create or select a senior-lawyer-maintained Queensland Vault containing only
the current approved drafting materials. Complete these placeholders in the
private workflow build record:

```text
jurisdiction: QLD
Harvey Vault: <ADD EXACT QUEENSLAND VAULT NAME>
Will precedent: <ADD EXACT QUEENSLAND WILL PRECEDENT FILE NAME>
Enduring power of attorney precedent: <ADD EXACT QUEENSLAND EPOA PRECEDENT FILE NAME>
Instruction sheet: <ADD EXACT QUEENSLAND INSTRUCTION SHEET FILE NAME>
Drafting playbook: <ADD EXACT QUEENSLAND DRAFTING PLAYBOOK FILE NAME>
```

Embed that Vault in the workflow. Do not duplicate version information in a
separate YAML record: Vault governance and the workflow's embedded Vault
selection control which materials are available. Do not permit a user-uploaded
precedent to replace a Vault precedent.

## Block design

Build this path:

```text
File upload -> Prompt using embedded Vault -> Word document editing -> Response
```

The File upload receives the completed instruction sheet and any authorised
matter materials for one client. The Prompt block:

1. builds the provenance-cited instruction table;
2. selects the requested precedent by its exact Vault file name;
3. applies the approved drafting playbook and preserves the precedent where the
   playbook is silent;
4. drafts all supported content and visibly marks every unresolved issue; and
5. produces the instruction summary, drafting-issues register and change
   summary required by the canonical skill.

Use Word document editing to populate a working copy of each requested Vault
precedent. Keep the Vault source unchanged. Return the working drafts and
supporting review material through the Response block. The responsible
solicitor reviews the completed output; the workflow does not assume an
interactive approval step during the run.

## Acceptance checks

1. Run one complete Queensland instruction set and confirm each draft uses the
   named Vault precedent and leaves the source unchanged.
2. Omit a material fact and confirm the agent returns a partial draft with a
   document marker and matching register entry.
3. Test a playbook position, a silent playbook point and a conflict with the
   client's instructions.
4. Upload a substitute precedent and confirm the agent refuses to use it.
5. Supply NSW, Victorian or two-client instructions and confirm the agent stops
   or routes without drafting.
6. Request an advance health directive and confirm the agent flags it as
   outside scope without drafting.

Record the tested Vault contents, workflow version, tester, date and result in
the private deployment record. Publishing, sharing and later Vault changes
remain subject to the workspace's normal approval controls.

Official product references:
[Agents and Workflows](https://eu.help.harvey.ai/topics/workflows) and
[Agents release notes](https://help.harvey.ai/release-notes/category/agents).
