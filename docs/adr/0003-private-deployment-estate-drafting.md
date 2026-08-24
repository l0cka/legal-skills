---
status: accepted
date: 2026-08-24
supersedes: 0002-sidecar-precedent-profiles-for-human-designed-precedents.md
---

# Private deployment for estate planning drafting

## Context

The estate-planning workflow will be deployed in an enterprise legal AI
workspace using the firm's existing wills and estate-planning precedents. The
sidecar registration model in ADR 0002 added a third public workflow and a
second source-of-truth layer. That complexity is unnecessary where approved
precedents and operational instructions can be centrally embedded and governed
inside the private deployment.

The public repository must remain provider-neutral and must not contain firm
precedents, private Vault names, client information or matter data.

## Decision

Keep two public workflow interfaces: one for New South Wales and one for
Victoria. Deploy them as separate jurisdictional agents. Each run concerns one
client, including where a couple receives parallel advice.

Each private workflow embeds one senior-lawyer-maintained jurisdiction Vault
containing the current approved precedents, instruction sheet and drafting
playbook. The embedded jurisdiction Vault and the workflow's exact file-name
references are the operational source of truth. Do not create a separate
machine-readable configuration layer that the platform does not natively
support.

The agent extracts a provenance-cited instruction table and prepares working
copies of the approved precedents in the same run. It applies standing drafting
positions from the approved playbook, drafts all supported content, and visibly
marks every missing fact, conflict or unsupported decision in the document and
a matching drafting-issues register. The responsible solicitor reviews the
drafts and issues after the run. Missing facts ordinarily produce a partial
draft rather than no draft.

The precedents and playbooks express the firm's current, senior-lawyer-approved
drafting position. The drafting workflow does not separately research the law,
test those materials for currency or require confirmation of each playbook
choice. It flags conflicts and points outside the approved materials.

Block drafting only when the client, jurisdiction or requested document cannot
be identified, or when the required approved precedent is missing or unusable.
Never use a generic or uploaded substitute, modify the approved source, resolve
legal judgment reserved to the solicitor, or describe a draft as approved or
ready to sign.

## Public and private boundary

The public repository contains:

- the two jurisdictional skill interfaces;
- provider-neutral instruction schemas and approved-material placeholders;
- the shared source-and-control method; and
- deployment guidance and regression tests using generic asset labels.

The private deployment contains:

- the jurisdictional Workflow agents and embedded Vault selections;
- approved precedents, instruction sheets and drafting playbooks maintained in
  those Vaults;
- workspace permissions, asset identifiers and approval records; and
- client and matter data supplied for an authorised run.

## Consequences

- The public plugin exposes two skills instead of a separate onboarding skill.
- Precedent approval and version control occur centrally in the private
  deployment rather than through a public registration workflow.
- The affected document must fail closed if a named Vault source is missing or
  inaccessible.
- Deployment acceptance tests must prove one-client isolation, jurisdictional
  separation, source preservation, visible unresolved issues and solicitor
  control of instructions and clauses.
- ADR 0002 remains as decision history but no longer describes the active
  architecture.
