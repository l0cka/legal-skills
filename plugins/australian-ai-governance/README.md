# Australian AI Governance

This plugin supplies six governed workflows for Australian AI governance:

- `configure-ai-governance-profile` creates a controlled organisational profile;
- `map-ai-regulatory-obligations` maps binding versus pending instruments for
  an AI use case;
- `assess-board-ai-oversight` issue-spots board and director-duty AI exposure;
- `check-ai-guidance-alignment` checks documentation against the voluntary
  guidance layers;
- `triage-government-ai-use-case` routes government AI use to the applicable
  jurisdictional assurance track; and
- `track-ai-regulatory-developments` monitors the pending-instrument
  watch-list.

## Boundary

Australia has no economy-wide AI Act. The workflows map obligations arising
from existing law, government-use policy and voluntary guidance, and they
label every layer: current, superseded, proposed or uncertain. A proposed
instrument — including the announced "Australian Standards for AI" — is a
watch item, never an obligation.

AI-privacy depth (privacy use-case assessment, automated-decision
transparency, APP analysis) belongs to the separately installed Australian
Privacy Cybersecurity plugin, and general board-process assessment to the
Australian Corporations Governance plugin; these skills route there rather
than duplicating them. EU AI Act exposure is flagged for specialist review,
not assessed. Court generative-AI practice directions are outside this
plugin.

The plugin is read-only. It does not certify compliance with any standard,
approve an AI deployment, lodge anything with a regulator or give final legal
advice. A responsible lawyer, privacy officer, company secretary or other
authorised reviewer must approve every consequential output.

## Sources

Controlling sources are the official publishers: legislation.gov.au and state
registers for legislation, courts and tribunals for decisions, and the
publishing regulator or agency (DISR/National AI Centre, OAIC, ASIC, APRA,
eSafety, DTA, state digital agencies) for guidance and policy. Trackers such
as policai.org are discovery indexes only — every lead is confirmed against
the named primary source before use.

The shared [source and control method](references/ai-governance-source-and-control-method.md)
defines the current-versus-superseded framework map, source hierarchy,
evidence states and human-review requirements. The
[profile schema](references/ai-governance-profile-schema.md) defines the
minimum organisation-controlled configuration.

## Permissions

No MCP server, app, hook or write action is bundled. The workflows may use
the separately installed Australian Legal Research plugin for read-only
verification of legislation and case citations. Users decide what documents
to provide and where to save any approved output.

## Licence

MIT. This is an original Australian workflow based on public official sources.
