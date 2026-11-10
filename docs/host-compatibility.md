# Host compatibility

Legal Skills ships the same skills to Claude (Cowork and Claude Code),
ChatGPT (Work and Codex) and Cursor. What a skill can do still depends on
the host: whether its web tool can read an official publisher, whether it
can run the bundled Python helpers and whether it can create a Word file.
This page holds the smoke set that checks those things and the results
recorded so far.

A skill that cannot read a publisher returns `UNVERIFIABLE`. That is the
correct result, not a fault, and it tells the lawyer to check by hand. The
smoke set shows in advance where that will happen.

## Smoke set

Run each prompt in a fresh session with the plugin installed and no other
legal plugin. Record `pass`, `fail` or `blocked`, the date, the host and its
version, and the model. `blocked` means the host could not reach the source
or run the tool and the skill said so.

| # | Checks | Prompt | Pass when |
| --- | --- | --- | --- |
| S1 | A skill triggers without being named | `Is Love v Commonwealth [2020] HCA 3 a real case?` | The reply follows the citation workflow and leads with a status such as `VERIFIED` or `UNVERIFIABLE`, not an answer from memory |
| S2 | High Court website | `Use verify-hca-judgment to verify this citation: Love v Commonwealth of Australia [2020] HCA 3.` | `VERIFIED` with an `hcourt.gov.au` URL and decision date 11 February 2020 |
| S3 | Federal Register of Legislation | `Is the Privacy Act 1988 (Cth) current, and which compilation applied on 1 January 2024?` | `VERIFIED` naming Title ID `C2004A03712` and Register ID `C2023C00347` |
| S4 | NSW Caselaw | `Use verify-nsw-judgment to verify this citation: State of New South Wales v McLaughlin [2024] NSWCA 137.` | `VERIFIED` with a `caselaw.nsw.gov.au` URL and decision date 4 June 2024 |
| S5 | Queensland Judgments | `Use verify-qld-judgment to verify this citation: R v Peter [2023] QCA 1.` | `VERIFIED` or `VERIFIED WITH QUALIFICATIONS`, naming the three appellants and a `queenslandjudgments.com.au` URL |
| S6 | Federal Court (expects a bot challenge) | `Use verify-federal-judgment to verify this citation: [2026] FCA 196.` | `VERIFIED` through a browser the user operates, or `UNVERIFIABLE` with the manual search path. A guess is a fail |
| S7 | A court's practice note PDF | `Use check-court-ai-protocol. I am filing an affidavit in the Supreme Court of New South Wales that an AI tool helped draft.` | Names Practice Note SC Gen 23 from a `supremecourt.nsw.gov.au` URL opened in the session, and does not clear the affidavit |
| S8 | Bundled Python helper | `A statement of claim in the Supreme Court of New South Wales was served on our client on Monday 2 March 2026. When is the defence due?` | Candidate date 30 March 2026 under UCPR r 14.3, produced by `compute_deadline.py`. A date with no script run is a fail |
| S9 | Word output | `Use build-document-index on these two documents.` with two short documents attached | A `.docx` file is produced, or the skill returns `NOT READY` because the host cannot create one |
| S10 | A typed command | `/legal-skills:help` (Claude), `$help` (ChatGPT, Codex) or `/help` (Cursor), then `What should I run for a data breach?` in a new session without typing a command | The first lists the practice areas and the four commands. The second does not start `setup`, `start`, `check-citations` or `help` |

S2 to S4 and S8 reuse cases from `benchmarks/keyed/`, so their expected
answers were read at the publisher or produced by the script.

## Results

| Check | Claude Code | Claude Cowork | ChatGPT Work | Codex | Cursor |
| --- | --- | --- | --- | --- | --- |
| S1 Trigger | not tested | not tested | not tested | not tested | not tested |
| S2 High Court | blocked (1) | not tested | not tested | not tested | not tested |
| S3 Federal Register | not tested | not tested | not tested | not tested | not tested |
| S4 NSW Caselaw | not tested | not tested | not tested | not tested | not tested |
| S5 Queensland Judgments | not tested | not tested | not tested | not tested | not tested |
| S6 Federal Court | not tested | not tested | not tested | not tested | not tested |
| S7 Practice note | not tested | not tested | not tested | not tested | not tested |
| S8 Python helper | pass (2) | not tested | not tested | not tested | not tested |
| S9 Word output | not tested | not tested | not tested | not tested | not tested |
| S10 Typed command | not tested | not tested | not tested | not tested | not tested |

(1) 9 November 2026, Claude Code in a cloud container whose network policy
blocks the publishers, Sonnet 5.5. Three High Court citations from the keyed
set each returned `UNVERIFIABLE` and named the blocked host. The skill
behaved correctly; the environment could not reach the source. This is not a
finding about Claude Code on a lawyer's own machine.

(2) 9 November 2026, same environment and model. The whole keyed deadlines
set (40 cases, one run, plugin loaded) scored 36 of 40 with no forbidden
status. Every case that expected a computed date produced it through
`compute_deadline.py`. Three of the four misses were out-of-scope questions
(a criminal appeal, a contested service date and an English claim) where
the model answered from memory and did its own date arithmetic in place of
returning `OUTSIDE SCOPE` or `NOT READY`; two of those failed the same way
on the commit before this page was added, in two runs each. The fourth
(`dl-vcat-001`) gave the right `NOT READY` answer but did not run the
script, which its key requires.

Fill a cell only from a run you made. Give the date, host version and model
in a numbered note, as above.

## Publisher reachability seen while building the registers

These are single observations of whether a hosted web-fetch tool could read
a page, made on 9 November 2026 while building the court AI protocol
register and the Queensland verifier. They are leads for where a skill may
return `UNVERIFIABLE`, not test results for any host.

| Publisher | Observation |
| --- | --- |
| `queenslandjudgments.com.au` | Home page and a decision page were read |
| `fedcourt.gov.au` practice notes | Read |
| `supremecourt.nsw.gov.au`, `lec.nsw.gov.au`, `districtcourt.nsw.gov.au`, `localcourt.nsw.gov.au`, `ncat.nsw.gov.au`, `pi.nsw.gov.au` | Practice note PDFs and pages were read |
| `supremecourt.vic.gov.au` | A practice note page was read; the page on where judgments are published was refused |
| `courts.qld.gov.au`, `qcat.qld.gov.au` | Practice direction PDFs were read; one guideline PDF was refused |
| `supremecourt.wa.gov.au`, `art.gov.au`, `fwc.gov.au`, `courts.sa.gov.au` | Read |
| `fcfcoa.gov.au` | A practice direction PDF was refused by the site's robots rules |
| `countycourt.vic.gov.au` | Returned a script-only page with no text |
| `austlii.edu.au`, `sclqld.org.au` | Refused |

## What each host is documented to support

| Host | Skill listing budget | Runs bundled scripts | Typed-only skills |
| --- | --- | --- | --- |
| Claude Code | 1% of the model's context window; descriptions are dropped past it | Yes | `disable-model-invocation: true`; the description is left out of the listing |
| Codex | 2% of the context window, or 8,000 characters when unknown; descriptions are shortened first, then skills omitted | Yes | `policy.allow_implicit_invocation: false` in `agents/openai.yaml` |
| Cursor | Not stated | Yes | `disable-model-invocation: true` |

Read on 9 November 2026 from the hosts' own skills documentation. The plugin
keeps each description to 260 characters and the listing to 26,000
characters, enforced by `scripts/validate_repository.py`. On a model with a
200,000-token window that is still more than Claude Code's stated 1%, so
some descriptions may be dropped there. Every skill name is always listed.
