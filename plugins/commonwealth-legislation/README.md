# Commonwealth Legislation

One provenance-first workflow for checking Commonwealth Acts and registered
instruments against the official Federal Register of Legislation.

## Skill

`check-commonwealth-legislation` identifies the official title, Title ID,
status and applicable point-in-time compilation. It surfaces commencement,
unincorporated-amendment, future-change and rectification issues rather than
collapsing them into an unsupported "current" label.

The bundled `frl_lookup.py` helper uses the Register's free, keyless API for
bounded metadata retrieval. The skill still requires inspection of the
official pages and relevant legislation before a result can be verified.

## Scope

Version 0.1 covers Commonwealth Acts and registered legislative and notifiable
instruments. It does not cover State or Territory law, Bills, court deadlines,
case treatment, legal interpretation or advice.
