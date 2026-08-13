# Commonwealth Legislation

Two provenance-first workflows for checking Commonwealth Acts and registered
instruments against the official Federal Register of Legislation.

## Skills

`check-commonwealth-legislation` identifies the official title, Title ID,
status and applicable point-in-time compilation. It surfaces commencement,
unincorporated-amendment, future-change and rectification issues rather than
collapsing them into an unsupported "current" label.

The bundled `frl_lookup.py` helper uses the Register's free, keyless API for
bounded metadata retrieval. The skill still requires inspection of the
official pages and relevant legislation before a result can be verified.

`trace-commonwealth-legislative-change` compares a named provision across two
dates or compilations, inventories every intervening compilation, and traces a
verified textual change through amendment and commencement material. It keeps
net text, intervening events, commencement, incorporation and legal operation
as separate findings.

Its bundled `frl_change_trace.py` helper retrieves endpoint and transition
metadata without claiming that a compilation reason affected the requested
provision. The skill requires confirmation from official texts and endnotes.

## Scope

Version 0.2 covers Commonwealth Acts and registered legislative and notifiable
instruments. Change traces are limited to 10 expressly identified provisions
per run. The plugin does not cover State or Territory law, Bills, court
deadlines, case treatment, legal interpretation, transitional operation,
application to facts or advice.
