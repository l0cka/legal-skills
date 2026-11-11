# Profile guide

Ten skills create a profile: a short, controlled record of facts about the
practice, employer, company or centre that the other skills in that practice
area run against. This guide says how to get one quickly, where to keep it
and what happens without one. Each area's own schema and method document
still govern its content.

## Fastest path to a usable profile

1. Open the matching starter in [starter-profiles.md](starter-profiles.md)
   and ask the `configure-*` skill to fill it from what you tell it. Every
   starter value is a fictional example. Replace each one or mark it
   `unknown`; `unknown` is a valid answer and is never read as `no`.
2. Read the draft. The assistant can only ever set status `draft`.
3. Approve it yourself if you hold the authority. Approval is a human act:
   state your role and the date, and the skill records them as supplied by
   you. A sole practitioner or principal can do this in the same session.
   Nothing is approved by silence or by the assistant.
4. Save the approved profile where the practice keeps controlled documents,
   and reuse it. The plugin stores nothing between sessions.

## Where to keep a profile

Keep each profile as its own file, named so the version is visible, for
example `employment-profile-v3.md`. Keep it somewhere the assistant can read
at the start of a session:

| How you work | A workable home for the file |
| --- | --- |
| An assistant with project or working folders | A folder in the project you open for the client or practice |
| An assistant with per-project file storage | That project's files |
| A code editor workspace | A folder in the workspace, kept out of any public repository |
| A chat without files | Paste or attach the profile at the start of the session |

These are suggestions. The practice's document management system remains the
system of record, and the copy the assistant reads should be exported from
it. At the start of a session, attach or point to the file. The skill
records the profile's identifier, version, status and as-at date in its
output, so a reviewer can see which profile a result relied on.

Never put client names, matter facts, personal information or privileged
advice in a profile. A profile describes the organisation, by role and
document identifier.

## Working without an approved profile

Areas differ, because in some of them the approved profile is itself the
safeguard.

| Practice area | Without an approved profile |
| --- | --- |
| Employment and Fair Work | The mapping and review skills proceed on stated assumptions, labelled as such |
| Work health and safety | The duty map proceeds on stated assumptions and never blocks on a missing profile |
| Commercial drafting | Drafting proceeds from explicit instructions; missing choices become marked gaps in a partial draft |
| Contract review | A missing playbook prevents a complete comparison; clearly labelled issue spotting is still permitted |
| Consumer and competition | Unknown facts stay unknown and are never read as `no`; each skill states what it could not assess |
| Litigation deadlines | Dates are computed only by the deterministic computation step, and every candidate date needs a named confirmer before reliance |
| Corporations governance | Consequential governance work returns `NOT READY` until the profile and governing documents are identified |
| AI governance | Obligation mapping requires an approved profile and records any gap |
| AML/CTF | The mapping and review skills require an approved practice profile |
| Legal triage | No triage pathway is named without the centre's approved profile |

This table summarises the skills as written; each skill's own text governs.
Where a skill proceeds without an approved profile, it names each
assumption. Where a skill stops, the quickest fix is the path above, not a
workaround.

## Changing a profile

Record every change as a new version with its approver. A retired or draft
profile is not an approved one. If fresh instructions conflict with the
profile, the skill records the departure for human review and does not
rewrite the profile.
