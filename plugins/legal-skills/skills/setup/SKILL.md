---
name: setup
description: Set up Legal Skills for a practice. Asks role, jurisdictions and practice areas, drafts the profiles those areas need from the starter profiles, and saves them where you choose. Run by typing it; never approves a profile.
disable-model-invocation: true
---

# Setup

## Scope

A guided first run for a lawyer, practice or legal centre that has just
installed the plugin. It asks a few questions, works out which practice areas
need a profile, drafts each profile from
[../../references/starter-profiles.md](../../references/starter-profiles.md)
through that area's own `configure-*` skill, and offers to save the drafts as
files in a folder the user names. It runs only when the user types it. Use
`$help` to see what the plugin covers and `$start` to work on a matter.

Read [../../references/profile-guide.md](../../references/profile-guide.md)
before asking anything. It governs where profiles live, what happens without
one and who may approve one. Each area's schema and `configure-*` skill
govern the profile's content; this skill only sequences them.

## Workflow

1. Ask once, in one message, for:
   - the user's role (for example sole practitioner, lawyer in a firm,
     in-house counsel, community legal centre staff);
   - the Australian jurisdictions the practice works in;
   - the practice areas they want to use, offering the list in
     [../../references/skill-map.md](../../references/skill-map.md);
   - where profiles should be kept: a folder path the assistant can write to,
     or `no files` to have each draft shown for copying instead.
   Accept `unknown` for any answer. Do not ask for client names, matter facts
   or personal information.
2. Map each chosen area to its profile skill:

   | Practice area | Profile skill |
   | --- | --- |
   | Litigation deadlines | `$configure-litigation-deadline-profile` |
   | Employment and Fair Work | `$configure-employment-profile` |
   | Commercial drafting | `$configure-drafting-profile` |
   | Contract review | `$configure-review-playbook` |
   | Consumer and competition | `$configure-consumer-competition-profile` |
   | Corporations governance | `$configure-corporations-governance` |
   | AI governance | `$configure-ai-governance-profile` |
   | AML/CTF | `$configure-aml-ctf-practice-profile` |
   | Legal triage | `$configure-legal-triage` |

   Legal research, privacy and cybersecurity, work health and safety, estate
   planning, evidence workflows, the router and cognitive sparring need no
   profile. Say so for each one chosen, and say what the skill needs instead
   where it matters (estate planning runs only from the practice's own
   approved precedents).
3. Show the plan: the profiles to draft, in the order above, and the areas
   that need none. Ask the user to confirm or drop items before drafting.
4. For each confirmed profile, run its `configure-*` skill starting from the
   matching starter in `starter-profiles.md`. Replace every example value
   with the user's fact or `unknown`; never carry an example value into the
   draft. Ask only the questions that skill needs and the user has not
   already answered. Keep the status `draft` and leave approval fields blank
   unless the user, holding the authority, states their role and the date.
5. Save, if a folder was given.
   - List the file names first, one per profile with the version in the name
     (for example `employment-profile-v1.md`), and wait for the user to
     confirm. Write nothing before that confirmation.
   - Write only those files, only inside the named folder. Never overwrite an
     existing file: if the name is taken, propose the next version number.
   - If the host cannot write files, show each draft in full for the user to
     save and say so.
6. Report using the result contract.

## Result contract

```text
Setup: <role; jurisdictions; areas chosen>
Profiles:
  <area> — <profile skill>; status: draft | approved by <role> on <date>;
    saved: <path> | shown for copying | not drafted (<reason>)
No profile needed: <areas and what each needs instead>
Unknowns to resolve: <field; why it matters>
Next session: attach or point to the saved profile files, then type `$start`
  with a matter, or `$help`
```

## Fail closed

Never approve a profile, mark one approved without the user's own statement
of role and date, or treat silence as approval. Never invent a practice fact,
keep a starter example value, or read `unknown` as `no`. Never write a file
the user has not confirmed, write outside the named folder, overwrite a file
or store client or matter information. Where an area's `configure-*` skill
stops or returns `NOT READY`, record that result and move to the next area;
never work around it. This skill stores nothing between sessions; the saved
files are the only record.
