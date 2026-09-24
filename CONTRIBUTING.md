# Contributing

Contributions that make legal work more reliable, accessible, explainable, or
efficient are welcome.

## Add or change a plugin

1. Open an issue describing the jurisdiction, users, task, authoritative
   sources, expected output, and material risks.
2. Keep the canonical skill under its owning plugin and hand-edit only the
   canonical sources: `.claude-plugin/plugin.json`, `catalog.json`, and the
   per-skill provenance sentences in `skills.json`.
3. Run `python3 scripts/generate_registry.py` to regenerate the marketplace
   catalogs, Codex wrapper, and README regions in the same change.
4. Add focused tests for scripts and any rule that could silently change legal
   meaning.
5. Run `python3 scripts/validate_repository.py`,
   `python3 scripts/generate_registry.py --check`,
   `python3 -m unittest discover -s tests`, and `git diff --check`.

See [docs/adding-a-plugin.md](docs/adding-a-plugin.md) for the repository
contract.

## Repository layout

```text
legal-skills/
├── plugins/<plugin-name>/             # canonical plugin packages and skills
├── skills.json                        # per-skill provenance sentences
├── .claude-plugin/marketplace.json    # Claude marketplace (generated)
├── .agents/plugins/marketplace.json   # ChatGPT and Codex marketplace (generated)
├── scripts/                           # generator, validator, link checker
├── benchmarks/                        # with/without-plugin benchmark harness
└── docs/
```

Shared instructions have one canonical copy; the provider manifests wrap that
copy without creating different versions. External tools start in read-only
mode when practical, and write actions need clear approval boundaries.

## Testing

Every change must pass:

```bash
python3 scripts/validate_repository.py
python3 scripts/generate_registry.py --check
python3 -m unittest discover -s tests
git diff --check
```

Behavioural evals live under `plugins/<name>/evals/` (`claude plugin eval` is
in early access; CI only checks that the cases load). Each suite has a
happy-path case and at least one fail-closed case, so a prompt change that
makes a skill verify a fabricated citation, compute a date outside the script
or hand a help-seeker legal advice fails the run:

```bash
claude plugin eval plugins/australian-legal-research --allow-tools Bash WebFetch --no-publish
```

A weekly workflow runs `python3 scripts/check_links.py`, which probes every
URL cited under `plugins/` and fails on a dead link.

Benchmarks compare answers with and without the plugins (see
[benchmarks/README.md](benchmarks/README.md)). Keyed pass rates require the
skill's status vocabulary, so the false-verification rate and the rubric score
are the fair cross-arm comparisons:

```bash
python3 benchmarks/run.py --set citations --arm with,without --model opus
python3 benchmarks/score.py benchmarks/results/<timestamp>/
```

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
