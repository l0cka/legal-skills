# Security policy

## Reporting a vulnerability

Report suspected vulnerabilities privately through GitHub's
[private vulnerability reporting](https://github.com/l0cka/legal-skills/security/advisories/new)
for this repository. Do not open a public issue for a security report.

Include the affected plugin or skill, the repository state you tested, and
reproduction steps. You should receive an acknowledgement within seven days.

## Scope

This repository publishes instruction files and small offline helper scripts.
Reports of most interest:

- Helper scripts that could be induced to contact a non-official endpoint or
  to execute untrusted input.
- Skill instructions that could cause an agent to leak client or matter
  information, or to bypass a stated human-review or fail-closed boundary.
- Supply-chain issues in the CI workflow or validation tooling.

## Data boundary

Never include client information, matter information, credentials, privileged
material, or confidential firm content in a report. Reproduce issues with
synthetic data only.
