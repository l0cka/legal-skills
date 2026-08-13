# Australian Legislation

This plugin verifies legislation against the official Commonwealth, State and
Territory publishers. It combines the existing Commonwealth and NSW workflows
with dedicated checkers for Victoria, Queensland, Western Australia, South
Australia, Tasmania, the ACT and the Northern Territory.

The skills establish title identity, point-in-time version, commencement,
currency and official-source provenance. The Commonwealth change-tracing skill
also follows compilations, amendments and commencement across a date range.

Every State and Territory checker follows the same workflow, result contract
and fail-closed rule, defined once in
[references/point-in-time-method.md](references/point-in-time-method.md). Each
checker supplies only its jurisdiction-specific facts: the official publisher,
the local timezone and the local name for a consolidated version.

Every check fails closed when official evidence is unavailable or incomplete.
Case law, Bills, interpretation, application and final legal advice are outside
scope unless a skill expressly states otherwise.
