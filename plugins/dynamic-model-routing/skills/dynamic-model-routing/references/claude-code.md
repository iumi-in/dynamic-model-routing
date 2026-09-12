# Claude Code CLI adapter

Use this reference with the shared skill. Resolve the eligible model map once per session. Do not assume similarly named effort settings have identical effects across vendors.

## Discover and dispatch

Inspect `claude --help`, the native model picker, and the exposed Agent tool schema. Native aliases can change meaning by provider, account, or release. Record the binding and date; do not ship an assumed permanent ranking or treat help examples as entitlement.

Delegate through the native Agent tool with a model argument only if that session supports it. Give the worker bounded scope, owned files, acceptance criteria, relevant project instructions, prior failures, and no recursive delegation. Do not assume the coordinator's skill was inherited. Keep review independently read-only, and serialize writers without separate worktrees.

Select effort only through a supported native argument or an authorized native role. If the tool has no effort control, report it as unavailable. Do not invent an Agent-tool field or pin the shared skill's `model`, `effort`, or `context`: those fields can change the coordinator/turn behavior and defeat dynamic choice.

Model precedence varies by version. The author's inspected 2.1.247 predates the documented 2.1.251 precedence change; a configured subagent-model override can defeat a per-call choice. Account policies, aliases, and fallback can also affect execution. Read only relevant nonsecret settings when permitted. Preserve a user pin or capability floor if the actual choice cannot be established.

## Configure only when requested

Prefer an existing project routing document or a small section in project-owned instructions. Do not alter a reusable CLAUDE.md template or global settings. If recurring worker roles are useful, verify the installed custom-agent schema and create only the needed `.claude/agents/*.md` definitions. Select supported model/effort fields from observed metadata, pass controlling policy to each role, and narrow reviewers' tools where supported.

Do not install a hook, override permission mode, change trust, set authentication variables, or rewrite the user's model settings as a routing shortcut. Configuration creates no permission to start held implementation.

## Verify and recover

Use `/agents` to inspect role discovery where available and `/tasks` to inspect running/recent worker model details. A model string in a prompt or a worker's own assertion is not native runtime proof. Record requested model/effort, dispatch evidence, effective settings if exposed, attempts, and acceptance checks separately.

When runtime identity is unavailable, say so. If a required pin or sensitive floor cannot be verified, keep that branch pending; continue independent authorized work. Provider access failures need access resolution, not repeated premium-model retries. A model switch need not restore shared subscription capacity or lower the subscription bill.

Session-only loading through `--plugin-dir` ends when that invocation ends. Configure changes in a consuming project remain and must have an explicit separate rollback list. Preserve later user edits during removal.

## Official references

- [Plugins and component discovery](https://code.claude.com/docs/en/plugins-reference)
- [Custom subagents and model precedence](https://code.claude.com/docs/en/subagents)
- [Model configuration](https://code.claude.com/docs/en/model-config)
- [Skills and native metadata](https://code.claude.com/docs/en/skills)
