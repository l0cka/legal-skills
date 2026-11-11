# Privacy

Legal Skills is a set of instruction files<!-- ai-tool:code --> and small helper scripts<!-- /ai-tool:code --> that run
inside your AI assistant<!-- ai-tool:code --> (Claude Cowork, Claude Code, ChatGPT Work or Codex)<!-- /ai-tool:code -->.
The author does not operate any server for it.

## What the plugin collects

Nothing. The plugin has no telemetry, analytics, accounts, cookies or remote
storage, and it sends nothing to the author.

## What leaves your machine

- **Your conversation.** The documents and facts you give the assistant are
  processed by the assistant's provider under that provider's terms and
  privacy policy, as they would be without the plugin.
- **Official-source lookups.** Research skills ask the assistant to read
  official publishers, such as legislation registers, courts, tribunals and
  regulators, through the host app's web tools.
<!-- ai-tool:code -->
- **Federal Register helpers.** Two scripts,
  `skills/check-commonwealth-legislation/scripts/frl_lookup.py` and
  `skills/trace-commonwealth-legislative-change/scripts/frl_change_trace.py`,
  send read-only HTTPS GET requests to `api.prod.legislation.gov.au`. Each
  request carries only a title search phrase, a Federal Register Title ID and
  dates. No other bundled script makes a network request.
<!-- /ai-tool:code -->

The research skills tell the assistant never to send confidential facts in
public searches.

## What the plugin stores

Skills write files only when you ask for a deliverable, such as a Word
document index or a draft, and only where your assistant saves files. The
plugin keeps no memory between sessions.

## Contact

Raise privacy questions in
[GitHub issues](https://github.com/l0cka/legal-skills/issues), or report a
privacy or security problem privately through
[GitHub security advisories](https://github.com/l0cka/legal-skills/security/advisories/new).
