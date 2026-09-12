# Dynamic Model Routing handoff

Updated: 2026-09-12. Phase: public `0.1.1` pilot released.

## Objective and scope

Publish an MIT-licensed, instruction-only dynamic model routing plugin for Codex CLI and Claude Code CLI. The package preserves authorization, explicit model choices, sensitive capability floors, bounded escalation, independent review, and acceptance evidence.

Cursor and desktop-specific adapters remain deferred. The plugin does not provide a daemon, proxy, telemetry service, hard spending cap, or automatic coordinator switch.

## Current state

- Public repository: `https://github.com/iumi-in/dynamic-model-routing`.
- Default branch: `main`.
- Latest release: `https://github.com/iumi-in/dynamic-model-routing/releases/tag/v0.1.1`.
- Release commit: `69ca925c1e346300c0ab64441b7c66d35c3b165c`.
- Distribution archive: `output/plugins/dynamic-model-routing-0.1.1.zip`.
- Archive SHA-256: `9AC11AFEE8CCBFC2B26D5475C65D1B34F58B807F10A4D7FC10690FDDF83AD7E2`.
- Issues and private vulnerability reporting are enabled; the wiki is disabled.
- GitHub reports 100% community-profile health after adding the conduct policy, issue forms, and pull-request template.
- The repository is pinned on the `iumi-in` profile and has ten relevant discovery topics.
- Starter issues `#1` and `#2` invite independent Codex/Linux and Claude Code/macOS verification.
- `assets/social-preview.jpg` is committed and referenced by the README. Uploading it as GitHub's link-preview image still requires an authenticated repository-settings browser session.
- The original `v0.1.0` tag is preserved. Its attached ZIP was replaced with the corrected portable archive, and `v0.1.1` is the maintained additive patch release.

## Verification

- `python -B scripts/validate.py` passes.
- `python -B -m unittest discover -s tests -v` passes 17 tests.
- `claude plugin validate ./plugins/dynamic-model-routing --strict` passes.
- The archive has seven contained entries and matches package source byte for byte.
- `python -B scripts/package.py` reproduces the checked-in archive byte for byte.
- GitHub Actions run `34692122950` passes on Linux, macOS, and Windows for release commit `69ca925`.
- GitHub Actions run `34693076367` passes on Linux, macOS, and Windows for community-foundation commit `65f6813`.
- The release validator rejects unexpected package files and trust-expanding manifest fields.
- Codex isolated installation/discovery/removal and Claude session loading passed previously.
- Authenticated native worker execution, effective-model identity, adoption, and savings remain unverified.

## Next action

Upload `assets/social-preview.jpg` under GitHub repository Settings → General → Social preview when an authenticated browser session is available. Then run the documented two-week pilot and record native worker identity, route overrides, acceptance failures, latency, and cost evidence. Do not claim Cursor support, desktop-specific verification, native worker identity, adoption, or savings until measured.

## Risk and rollback

Public Git history and downloaded releases are externally visible and cannot be reliably recalled. A faulty future release should be deprecated and replaced by an additive patch release. The repository can be archived, but existing clones and downloads remain outside the maintainer's control.

No unrelated user-owned workspace changes are known. Agent platform: Codex desktop. Provider: OpenAI. Exact runtime model and effort: unknown because they are not exposed.
