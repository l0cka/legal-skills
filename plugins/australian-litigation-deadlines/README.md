# Australian Litigation Deadlines

Every date this plugin produces is provisional until the responsible lawyer
confirms it. The plugin is not a diary, court-list or practice-management
system and says so in every output.

The plugin supplies six governed workflows for Australian civil litigation:

- `configure-litigation-deadline-profile` creates a controlled practice
  profile naming the jurisdictions practised in and the human confirmer;
- `map-limitation-periods` maps a described cause of action to candidate
  limitation periods across all nine Australian jurisdictions, flagging
  postponement and special regimes without resolving them;
- `compute-procedural-deadlines` computes candidate court deadlines with a
  bundled deterministic script — the model never performs date arithmetic;
- `map-tribunal-review-deadlines` maps and computes candidate tribunal and
  merits-review deadlines, with mandatory warnings for migration matters;
- `maintain-deadline-register` builds a source-linked deadline register for
  a matter with per-entry confirmation status; and
- `verify-deadline-basis` verifies computation-rule and holiday tables
  against official publishers and records an evidence fingerprint.

## Boundary

The plugin serves Australian legal practitioners running civil litigation,
in firms or in-house. Criminal procedure fails closed to human review in
every workflow. Foreign limitation law and cross-border choice-of-law
questions are flagged, never assessed.

Date arithmetic is script-only: the bundled `compute_deadline.py` performs
every computation from evidence-gated JSON rule tables, and any period the
tables cannot express — court-fixed dates, "as soon as practicable",
periods counted backwards from a future event — is identified but never
computed. Computation activates for a rule-table entry only after it is
verified against the official publisher through `verify-deadline-basis`.
The shipped tables carry the initial verification of 2026-08-14: the
Federal Court, NSW court, Queensland court, ART, NCAT, QCAT and Victorian
defence rules are verified and compute. FCR r 1.61(5) is expressed as a declared excluded
range (24 December to 14 January not counted) and r 1.61(3) as a
short-period threshold that fails calendar-day rules of 5 days or less
closed; where rolling a last day would enter the excluded range, the
unsettled interaction of r 1.61(4) and (5) makes the script refuse rather
than choose a reading. The Victorian appearance rule stays pending because
the operative time is stated in the writ itself, and VCAT ships no general
period rule because none exists in the Act or Rules — the enabling
enactment always fixes it. The Queensland UCPR has no time-reckoning rule
of its own — the Acts Interpretation Act 1954 s 38 governs through the
Statutory Instruments Act 1992 bridge, and the Queensland holiday table is
Brisbane-area based, with district show holidays and the Christmas Eve
part-day holiday recorded as caveats. Holiday tables for NSW, Victoria and
Queensland ship verified against the official government publications
listed in each table.

The plugin never determines when a cause of action accrued, when a fact
became discoverable, or whether an extension of time would be granted —
those are the responsible lawyer's calls, recorded as inputs. Computed
coverage: the federal courts, the Supreme, District/County and Magistrates
or Local Courts of every State and Territory, and the ART, NCAT, QCAT and
VCAT; steps without a verified table entry receive identify-only
output naming the governing rule. Migration-review outputs always carry a non-extendable and
jurisdictional-deadline warning with a specialist-review flag.

Point-in-time verification of Acts routes to the separately installed
Australian Legal Research plugin. Court rules sit outside that plugin's
scope by design, so this plugin carries its own court-rules source method.

## Sources

Controlling sources are the official publishers: legislation.gov.au,
legislation.nsw.gov.au, legislation.vic.gov.au, legislation.qld.gov.au and
the other jurisdictions' official legislation sites for Limitation Acts, Interpretation Acts, court
rules and tribunal Acts; court and tribunal websites for practice notes and
registry arrangements; and the official government public-holiday
publications named in each holiday table. Commentary and firm
limitation-period tables are discovery material only.

The shared [source and control method](references/litigation-deadlines-source-and-control-method.md)
defines the source hierarchy, evidence states, the script-only arithmetic
rule and human-confirmation requirements. The
[deadline profile schema](references/deadline-profile-schema.md) defines the
minimum practice-controlled configuration. The
[computation-rule tables](references/computation-rules/) and
[holiday tables](references/holidays/) are the only inputs the computation
script accepts.

## Permissions

No MCP server, app, hook or write action is bundled. The bundled Python
script reads only the JSON tables in this plugin and the input the user
supplies. The workflows may use the separately installed Australian Legal
Research plugin for read-only verification of Acts. Users decide what
documents to provide and where to save any approved output.

## Licence

MIT. This is an original Australian workflow based on public official sources.
