# Australian Corporations Governance

This plugin supplies five governed workflows for companies registered under
the *Corporations Act 2001* (Cth):

- `configure-corporations-governance` creates a controlled governance profile;
- `assess-director-duties-governance` issue-spots decision-process risks;
- `prepare-board-decision-record` drafts controlled board materials;
- `review-corporations-governance-framework` reviews governance controls; and
- `maintain-corporations-governance-calendar` creates a source-linked calendar.

## Boundary

The core workflow covers proprietary and public companies governed by the
*Corporations Act 2001* (Cth). Listed entities, APRA-regulated institutions,
registered charities, Aboriginal and Torres Strait Islander corporations,
managed schemes and foreign bodies require separate or additional regimes.
The skills identify those overlays and stop where they are decisive.

The plugin is read-only. It does not approve corporate action, give final
legal advice, file with a regulator, send notices, execute resolutions or
invent what occurred at a meeting. A responsible lawyer, company secretary or
other authorised reviewer must approve every consequential output.

## Sources

The controlling statutory source is the official Federal Register of
Legislation. ASIC material is regulator guidance, not a substitute for the
Act. Organisation-supplied constitutions, replaceable-rule mappings,
shareholder arrangements, delegations and policies control internal process
only after their status and version are confirmed.

The shared [source and control method](references/governance-source-and-control-method.md)
defines source hierarchy, overlay routing, evidence states and human-review
requirements. The [profile schema](references/governance-profile-schema.md)
defines the minimum organisation-controlled configuration.

## Permissions

No MCP server, app, hook or write action is bundled. The workflows may use the
separately installed Australian Legislation plugin for read-only verification
of Commonwealth legislation. Users decide what documents to provide and where
to save any approved output.

## Licence

MIT. This is an original Australian workflow based on public official sources.
