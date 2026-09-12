# Dynamic Model Routing handoff

Updated: 2026-09-12. Phase: public `0.1.0` release preparation.

## Objective and scope

Publish an MIT-licensed, instruction-only dynamic model routing plugin for Codex CLI and Claude Code CLI. The package must preserve authorization, explicit model choices, sensitive capability floors, bounded escalation, independent review, and acceptance evidence.

Cursor and desktop-specific adapters remain deferred. The plugin does not provide a daemon, proxy, telemetry service, hard spending cap, or automatic coordinator switch.

## Current state

- Package source: `plugins/dynamic-model-routing`.
- Distribution archive: `output/plugins/dynamic-model-routing-0.1.0.zip`.
- Intended public repository: `https://github.com/iumi-in/dynamic-model-routing`.
- The user authorized a public GitHub repository and MIT release on 2026-09-12.
- This workspace began without Git metadata. The remaining local action is to initialize `main` and commit the final reviewed tree, then create the public repository, push, and read back the remote state.

## Verification

- `python -B scripts/validate.py` passes.
- `python -B -m unittest discover -s tests -v` passes 17 tests.
- `claude plugin validate ./plugins/dynamic-model-routing --strict` passes.
- The archive has seven contained entries and matches package source byte for byte.
- `python -B scripts/package.py` reproduces the checked-in archive byte for byte.
- The release validator rejects unexpected package files and trust-expanding manifest fields.
- Codex isolated installation/discovery/removal and Claude session loading passed previously.
- Authenticated native worker execution, effective-model identity, adoption, and savings remain unverified.

## Next action and release gate

Create and push the public GitHub repository, enable private vulnerability reporting when available, create the `v0.1.0` release with the ZIP asset, and confirm the public repository, release, license, and CI state by readback.

Do not claim Cursor support, desktop-specific verification, native worker identity, adoption, or savings until measured. Do not publish credentials, private prompts, source contents, or local machine paths.

## Risk and rollback

Public Git history and downloaded releases are externally visible and cannot be reliably recalled. Before pushing, inspect the complete staged tree for secrets and machine-specific data. Local rollback is deletion of the newly initialized `.git` metadata only before publication; remote rollback requires deleting or archiving the GitHub repository and does not remove existing clones.

No unrelated user-owned workspace changes are known. Agent platform: Codex desktop. Provider: OpenAI. Exact runtime model and effort: unknown because they are not exposed.
