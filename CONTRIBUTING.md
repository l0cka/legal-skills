# Contributing

Contributions that make legal work more reliable, accessible, explainable, or
efficient are welcome.

## Add or change a plugin

1. Open an issue describing the jurisdiction, users, task, authoritative
   sources, expected output, and material risks.
2. Keep the canonical skill under its owning plugin and add paired Claude and
   Codex manifests.
3. Update both marketplace catalogs and `skills.json` in the same change.
4. Add focused tests for scripts and any rule that could silently change legal
   meaning.
5. Run `python3 scripts/validate_repository.py` and `git diff --check`.

See [docs/adding-a-plugin.md](docs/adding-a-plugin.md) for the repository
contract.

## Public-content boundary

Do not submit client or matter information, privileged or confidential
material, personal data, credentials, private infrastructure details, or
third-party material that cannot lawfully be redistributed.

## Legal reliability

A contribution should identify its jurisdiction and source basis, distinguish
law from workflow guidance, state important limits, and preserve a meaningful
human-review point for consequential outputs. A plugin must not promise legal
correctness or describe itself as a substitute for legal advice.

## Licence

By contributing, you agree that your contribution is licensed under the MIT
Licence that applies to this repository. You must identify third-party material
and its separate licence or usage conditions.
