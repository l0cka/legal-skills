<!-- GENERATED FILE - do not edit. Built from plugins/ by
     scripts/generate_registry.py -->

# Legal Skills (all)

`legal-skills-all` installs every Legal Skills workflow at once: sixty-one
skills from eleven plugins. It is a generated copy of each plugin's `skills/`
and `references/` trees, so every skill behaves exactly as it does in its own
plugin, with the same sources, result contract and human-review gates.

Install either this bundle or the individual plugins, not both: installing
both loads every skill twice.

## Install

```bash
# Codex or ChatGPT Work: one plugin from the .agents marketplace
codex plugin marketplace add l0cka/legal-skills
codex plugin add legal-skills-all@legal-skills

# Or copy the skills straight into an .agents directory
# (~/.agents for your user, or .agents at a project root)
git clone --depth 1 https://github.com/l0cka/legal-skills.git
mkdir -p ~/.agents
cp -R legal-skills/bundles/legal-skills-all/skills legal-skills/bundles/legal-skills-all/references ~/.agents/
```

Copying into `.agents/` needs both trees: the skills link to shared files at
`../../references/`. Copy again to update.

## Included plugins

- [**Australian AI
  Governance**](../../plugins/australian-ai-governance/README.md) 0.1.2, law
  checked 2026-08-26: `assess-board-ai-oversight`,
  `check-ai-guidance-alignment`, `configure-ai-governance-profile`,
  `map-ai-regulatory-obligations`, `track-ai-regulatory-developments`,
  `triage-government-ai-use-case`
- [**Australian AML/CTF**](../../plugins/australian-aml-ctf/README.md) 0.1.2,
  law checked 2026-08-26: `configure-aml-ctf-practice-profile`,
  `map-designated-services`, `map-reporting-obligations`,
  `review-aml-ctf-program`, `track-aml-ctf-developments`
- [**Australian Corporations
  Governance**](../../plugins/australian-corporations-governance/README.md)
  0.1.2, law checked 2026-08-26: `assess-director-duties-governance`,
  `configure-corporations-governance`,
  `maintain-corporations-governance-calendar`,
  `prepare-board-decision-record`, `review-corporations-governance-framework`
- [**Australian Employment & Fair
  Work**](../../plugins/australian-employment-fair-work/README.md) 0.1.1, law
  checked 2026-08-26: `assess-termination-exposure`,
  `configure-employment-profile`, `map-fair-work-obligations`,
  `review-workplace-policy`, `track-fair-work-developments`
- [**Australian Estate
  Planning**](../../plugins/australian-estate-planning/README.md) 0.5.1, law
  checked 2026-08-26: `assemble-nsw-estate-documents`,
  `assemble-qld-estate-documents`, `assemble-vic-estate-documents`
- [**Australian Legal
  Research**](../../plugins/australian-legal-research/README.md) 0.1.1, law
  checked 2026-08-26: `check-act-legislation`,
  `check-commonwealth-legislation`, `check-northern-territory-legislation`,
  `check-nsw-legislation`, `check-queensland-legislation`,
  `check-south-australia-legislation`, `check-tasmania-legislation`,
  `check-victoria-legislation`, `check-western-australia-legislation`,
  `format-aglc4-citations`, `route-case-citation`,
  `trace-commonwealth-legislative-change`, `verify-case-quote`,
  `verify-federal-judgment`, `verify-hca-judgment`, `verify-nsw-judgment`
- [**Australian Litigation
  Deadlines**](../../plugins/australian-litigation-deadlines/README.md) 0.3.1,
  law checked 2026-08-26: `compute-procedural-deadlines`,
  `configure-litigation-deadline-profile`, `maintain-deadline-register`,
  `map-limitation-periods`, `map-tribunal-review-deadlines`,
  `verify-deadline-basis`
- [**Australian Privacy &
  Cybersecurity**](../../plugins/australian-privacy-cybersecurity/README.md)
  0.3.3, law checked 2026-08-26: `assess-ai-privacy-cybersecurity-use-case`,
  `assess-australian-data-breach`, `assess-australian-privacy-issues`,
  `assess-automated-decision-transparency`, `assess-statutory-privacy-tort`,
  `check-australian-privacy-principles`,
  `map-australian-cyber-incident-obligations`,
  `route-australian-privacy-jurisdiction`
- [**Legal Evidence
  Workflows**](../../plugins/legal-evidence-workflows/README.md) 0.2.0, law
  checked 2026-08-26: `build-document-index`, `build-evidence-chronology`,
  `build-privilege-log`, `map-evidence-inconsistencies`
- [**Legal Triage**](../../plugins/legal-triage/README.md) 0.1.2, law checked
  2026-08-26: `configure-legal-triage`, `triage-legal-enquiry`
- [**Legal Workflow Router**](../../plugins/legal-workflow-router/README.md)
  0.2.0, law checked 2026-08-26: `route-legal-fact-pattern`

## Before you rely on it

Every skill prepares work for a lawyer or other qualified person to check and
approve. None of them gives legal advice or replaces professional judgment.
Each plugin's README states its jurisdiction, sources and currency limits.

Licence: MIT. See [LICENSE](../../LICENSE).
