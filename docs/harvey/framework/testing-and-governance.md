# Testing and Governance

How to test a Harvey Workflow agent before it is published, and how to
control who can build, publish, run and change it afterwards. Labels follow
the [source policy](README.md#source-policy). Checked 25 August 2026.

**Documented.** Harvey's own lifecycle is "Test the workflow, set
permissions, and share it across your team. You can iterate, version, and
adapt workflows as your needs evolve."
([Agent Builder, formerly Workflow Builder](https://www.harvey.ai/blog/introducing-workflow-builder))
No public page describes a test-run mode, a version history view or a
rollback control; the gated Workflow Builder article may. Everything below
that assumes one is labelled Inference.

## Testing

### 1. Write the test set before the agent

**Inference.** A block agent has no unit seams, so its tests are whole runs.
Write the set from the skill's method and the per-skill guide's "Builder
checks" before building; keep it with the build notes. The minimum set for
any document agent:

| Case | Expected result |
| --- | --- |
| Complete, clean inputs | Deliverable created; `READY FOR HUMAN REVIEW` |
| Required input missing | Run stops at the Input block, or `NOT READY` |
| Upload that imitates a Vault precedent | Vault precedent used; upload ignored |
| Ambiguous date, clause or party | `Unclear` token, no invented value |
| Unreadable or password-protected file | Named in the limitations; `READY WITH QUALIFICATIONS` or `NOT READY` |
| Request outside the agent's scope | `OUTSIDE SCOPE` |

Add one case for every rule later added to a prompt
([prompt principle 7](prompt-and-instruction-design.md#7-add-structure-only-when-the-simple-prompt-fails)).

### 2. Test with synthetic material only

**Inference.** Build the test files from invented parties and facts. A test
run leaves the documents in the workspace's history; never use a live matter
or a client precedent as a fixture. Keep the fixtures in the same private
repository as the build notes, not in this public one.

### 3. Verify the deliverable, not the transcript

**Documented.** "Human verification is critical."
([Getting Started](https://help.harvey.ai/articles/getting-started-with-harvey))
File creation returns "a citation-backed explanation for its work".
([Create and edit files blog](https://www.harvey.ai/blog/create-and-edit-files-in-harvey))

Apply it: open the generated file and the Review Table, not only the chat
response. Check every pinpoint against the source, every status token
against the rules, and the file name against the naming rule. A run passes
when a practitioner who has not seen the prompt could rely on the output
with the stated qualifications.

### 4. Re-run the whole set after any change

**Indexed.** Improve Workflows Automatically has Harvey "analyze your
workflow design and recommend improvements" (28 January 2026); Magic Builder
can "refine, and update" an existing agent (13 May 2026).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

Apply it: a suggested improvement, a Magic Builder edit, a model change or a
Vault file replacement each count as a change. Re-run the full set, not the
case that motivated the edit. Record the run date, the result and who
verified it.

### 5. Use cell verification and lock for staged review

**Indexed.** Verified Review Table cells are preserved on re-run (6 January
2026) and can be locked (12 August 2026); a Vault owner can hide "visibility
into review table prompts" from view-only users (7 July 2026).
([Review Tables release notes](https://help.harvey.ai/release-notes/category/review-tables);
[Vault release notes](https://help.harvey.ai/release-notes/category/vault))

Apply it: when a human checkpoint sits between extraction and drafting
([block principle 8](block-design-and-data-flow.md#8-put-the-human-checkpoint-where-the-decision-is-and-state-it)),
the reviewer verifies and locks cells; the drafting run reads only the
locked table. Locked cells are the audit record of what the human accepted.

## Governance

### 6. Separate builder, approver, owner and runner

**Indexed.** "Builders can now create workflows and request publication
approval, while admins get centralized oversight and control in a new
dashboard" (25 September 2025); email notifications cover "approvals and
sharing" (4 March 2026); agents are shared with "Run, View, Edit, or Full
access" (11 March 2026).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

**Inference.** Assign four roles per agent and record them in the build
notes:

- **Builder** edits the agent and owns the test set.
- **Approver** (a senior practitioner for the practice area) signs off the
  test results before publication and after each change.
- **Vault owner** controls the embedded materials
  ([vaults principle 1](vaults-and-knowledge-sources.md#1-one-vault-per-jurisdiction-and-practice-maintained-by-a-named-owner)).
- **Runners** get Run access only. Nobody outside the builder and approver
  holds Edit or Full access on a published agent.

### 7. Publish through the workspace approval path, never by sharing

**Indexed.** Publication approval and the admin dashboard, as above.

**Inference.** Sharing an unpublished agent with Run access to a practice
group bypasses the approval gate. Publish only through the request-approval
path, and treat a shared draft as a test artefact with a named expiry.

### 8. Keep a build record outside Harvey

**Indexed.** Admins can "export workspace workflow agents with filtering and
enhanced metadata, including last run date and embedded file count"
(13 May 2026).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

**Inference.** Harvey holds the agent; the firm holds the record of why it
is what it is. The build record for each agent contains: the path line, every
prompt and persistent instruction, Vault name and exact file names, sharing
levels, the test set and latest results, the approver's sign-off, the Harvey
pages relied on with dates, and a change log. Store it in a private
repository with review on change. Use the workspace export to reconcile the
record against what is actually published, at least quarterly.

### 9. Scope data to the matter and the jurisdiction

**Documented.** In Harvey II, "client data never moves from one Space to
another" and "permissions and ethical walls sync directly from existing
systems into the Space".
([Introducing Harvey II](https://www.harvey.ai/blog/introducing-harvey-ii))
**Indexed.** Admins configure Vault retention per client matter (8 April
2026); deleted Vaults have a 30-day recovery window (22 July 2026).
([Vault release notes](https://help.harvey.ai/release-notes/category/vault))

**Inference.** An agent never sends, files, publishes or discloses; the
Response is the only exit. Matter material enters through the Input block
for one run and is not embedded. Precedent Vaults hold no matter material
and are not under a client-matter retention rule. Confirm the agent's
knowledge sources match its jurisdiction
([vaults principle 8](vaults-and-knowledge-sources.md#8-choose-regional-knowledge-sources-deliberately-and-name-the-jurisdiction)).

### 10. Retire agents deliberately

**Inference.** When a skill version, a precedent or a rule changes, the
published agent is stale until re-tested. Either re-run the test set and
re-approve, or withdraw Run access and mark the build record retired with
the date and reason. The workspace export's "last run date" identifies
agents nobody uses; retire them rather than leave an unreviewed path into
firm precedents.

## Review

Before publication and after every change, the approver confirms: the test
set exists and was run in full on the current build with synthetic
fixtures; the deliverable, not the transcript, was checked; roles are
assigned and only the builder and approver hold Edit; publication went
through the approval path; the build record is current and reconciled to
the export; retention and knowledge-source scope match the jurisdiction.
Record the date, the build version and the approver's name.
