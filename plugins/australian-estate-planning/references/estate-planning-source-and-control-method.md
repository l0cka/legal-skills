# Australian estate planning source and control method

## Purpose and scope

This method governs practitioner-led preparation of estate planning drafts for
New South Wales, Victoria and Queensland. Each run concerns one client and uses the
jurisdiction-specific skill. Start a separate run for each member of a couple.

Every document is a draft until the responsible solicitor reviews it. The
workflow does not decide which documents a client needs, advise a self-
represented person, assess capacity or undue influence, or execute, witness,
file or register a document.

## Approved drafting materials

Before private deployment, replace the placeholders below with the exact names
of the approved library and files. Do not add confidential files or private
identifiers to this public repository.

```text
NSW approved library: <NSW APPROVED LIBRARY NAME>
NSW will precedent: <NSW WILL PRECEDENT FILE NAME>
NSW enduring power of attorney precedent: <NSW EPOA PRECEDENT FILE NAME>
NSW enduring guardian precedent: <NSW ENDURING GUARDIAN PRECEDENT FILE NAME>
NSW instruction sheet: <NSW INSTRUCTION SHEET FILE NAME>
NSW drafting playbook: <NSW DRAFTING PLAYBOOK FILE NAME>

Victorian approved library: <VICTORIAN APPROVED LIBRARY NAME>
Victorian will precedent: <VICTORIAN WILL PRECEDENT FILE NAME>
Victorian enduring power of attorney precedent: <VICTORIAN EPOA PRECEDENT FILE NAME>
Victorian medical treatment decision-maker precedent: <VICTORIAN MTDM PRECEDENT FILE NAME>
Victorian instruction sheet: <VICTORIAN INSTRUCTION SHEET FILE NAME>
Victorian drafting playbook: <VICTORIAN DRAFTING PLAYBOOK FILE NAME>

Queensland approved library: <QUEENSLAND APPROVED LIBRARY NAME>
Queensland will precedent: <QUEENSLAND WILL PRECEDENT FILE NAME>
Queensland enduring power of attorney precedent: <QUEENSLAND EPOA PRECEDENT FILE NAME>
Queensland instruction sheet: <QUEENSLAND INSTRUCTION SHEET FILE NAME>
Queensland drafting playbook: <QUEENSLAND DRAFTING PLAYBOOK FILE NAME>
```

Use only these approved materials. The precedents and playbooks are maintained
and approved by the firm's senior lawyers as the current drafting position.
The workflow does not independently research the law, test those materials for
currency or rewrite them. If a listed file is missing or two approved materials
conflict, flag the issue for the responsible solicitor.

Keep each approved precedent unchanged and prepare a working copy. There is no
generic fallback document and an uploaded substitute must not be used.

## Instructions and playbook

Create one instruction table containing every applicable field, value,
provenance citation, inconsistency and risk flag. Record information that is
blank, illegible, ambiguous or inconsistent as `cannot be determined`. Never
fill a plausible value.

Use the approved playbook for the firm's standing drafting positions. Apply a
playbook position when it clearly covers the client's express instructions and
the selected precedent. If the playbook is silent, ambiguous or inconsistent
with the client's express instructions, preserve the approved precedent text
where possible and flag the point for solicitor review. Never use a playbook to
supply a client fact. Never invent, combine or improve clause text.

## Drafting and unresolved issues

Prepare a working copy of each selected precedent and populate all content
supported by the instruction table and approved drafting materials. Leave the
approved source unchanged.

When a fact or drafting decision is unresolved, insert
`[REVIEW REQUIRED – <missing fact or unresolved decision>]` at every affected
location. Do not hide a blank or choose an unsupported alternative by
inference.

Put `DRAFT – SOLICITOR REVIEW REQUIRED` inside every draft. If any review
marker remains, also put `PARTIAL DRAFT – UNRESOLVED ISSUES IDENTIFIED` inside
the draft and use the status `PARTIAL DRAFT – UNRESOLVED ISSUES`.

Return a drafting-issues register with one matching entry for every review
marker. Each entry records the document, location, missing fact or unresolved
decision, provenance, and the action required from the responsible solicitor.
Also return the instruction summary and a concise change summary.

## Result states

Use one state for each requested document:

- `DRAFT READY FOR SOLICITOR REVIEW` — the draft has no known unresolved fact
  or drafting decision, but still requires solicitor review;
- `PARTIAL DRAFT – UNRESOLVED ISSUES` — supported content was drafted and all
  unresolved matters are visible in the document and register;
- `BLOCKED – NO DRAFT PRODUCED` — the client, jurisdiction or document cannot
  be identified, or the required approved precedent is missing or unusable;
- `OUTSIDE SCOPE` — the request is outside the jurisdictional skill's express
  coverage.

Missing facts ordinarily lead to a partial draft, not a blocked result. The
responsible solicitor reviews the drafts, resolves marked issues and decides
whether each document may progress. Never describe a document as approved,
final, executable or ready to sign.
