# Dynamic model routing across coding platforms

Date: 2026-09-12. Status: approved for the narrowed CLI pilot by the user's instruction, "ok build as per your recommendations". The original six-surface proposal below remains a future direction.

## Approved pilot amendment

Build one self-contained native plugin for Codex CLI and Claude Code CLI, based on the supplied policy. Ship shared routing instructions, two host references, native manifests, portable offline validation, behavioral scenarios, and a short pilot guide. No API proxy, automated model ranking, fixed model pins, telemetry service, or global configuration changes. Cursor and desktop integration are deferred until the research report's repeat-use and host-demand gates justify them.

## Public release authorization

After implementation and audit, the user authorized publishing the pilot as an MIT-licensed public repository under `iumi-in` on 2026-09-12. This changes the distribution decision only; the pilot status, deferred surfaces, verification gaps, and prohibition on unsupported claims remain in force.

Installation and effective worker execution must be reported separately. Test local loading with the installed CLIs, then attempt a harmless bounded runtime check within existing permissions. Missing authentication, unsupported controls, or unavailable runtime identity remain explicit verification gates; do not invent success. Package/source checks alone do not establish routing quality or savings.

Use `plugins/dynamic-model-routing` as the distributable directory. Ordinary use needs no Python runtime; repository validation uses Python 3.11+ standard library. Native dispatch performs routing, with host-specific instructions discovered by the shared skill. The plugin never changes the coordinator model through prose. Author identity is "Dynamic Model Routing contributors"; use the MIT license for this freely reusable pilot, with no invented repository URL. No publishing or account/profile installation is authorized by this build.

## Purpose and proposed scope

Turn the user's dynamic-model-routing skill into one maintainable plugin source that works through Codex, Cursor, and Claude Code's supported desktop and CLI mechanisms. Optimize total effort, elapsed time, and cost to a verified result while preserving the original quality and authorization requirements.

The approved pilot uses native platform routing, following the research recommendation. The API-service alternative is outside this build.

Desktop means the Codex desktop coding surface, Cursor's editor/agent surface, and the Claude Desktop Code tab using local sessions. Standalone CLI support is a separate acceptance target. Cloud, SSH, WSL-specific desktop integration, generic Claude chat, and IDE extensions other than Cursor require separate capability evidence before being advertised.

## Foundation: preserve the user's policy

The canonical input is the user's `dynamic-model-routing/SKILL.md`, its `references/codex-setup.md`, and `agents/openai.yaml`. Source paths and hashes are recorded in the repository handoff. The installed originals remain untouched. The distributed plugin must be self-contained and must not reference those personal absolute paths.

Adapt the original skill's Codex-specific wording into shared policy, and move host-specific instructions into references. Retain the three modes: Advise leaves state unchanged; Apply routes already-authorized work; Configure prepares persistent project routing without starting held work.

Retain all four routes and their meaning:

| Route | Selection rule | Acceptance requirement |
| --- | --- | --- |
| Clerical | Lowest-cost adequate model for specified transformations or evidence extraction without sensitive behavior changes | Coordinator inspects output and applicable validation |
| Routine | Balanced eligible model for bounded work under understood contracts | Appropriate specification, code, and integration checks |
| Sensitive | Strong eligible model for sensitive invariants or ambiguous cross-system contracts | Independent capable review and boundary/failure/runtime evidence |
| Escalation | Strongest eligible model suited to the unresolved problem after bounded attempts | Independent review and original acceptance checks |

Risk outranks patch size. Preserve explicit model choices within their stated scope, execution holds, budgets, provider restrictions, and sensitive capability floors. An unavailable explicit choice is not permission to substitute. Preserve the two-unsuccessful-attempt default ceiling, immediate escalation for unsafe/repeated failures, bounded highest-route diagnosis, and reset to the normal route for unrelated work. Escalation within authorized scope is automatic; ask the user only when a real authorization or evidence boundary requires it.

## Approaches considered

| Approach | Benefit | Cost or limitation |
| --- | --- | --- |
| Shared skill with native platform adapters — recommended | Closest to the original skill; uses existing clients, model controls, permissions, and subscriptions | Capability and effective-model reporting differ across clients |
| Portable advice-only skill | Very small and broadly reusable | Recommendations alone do not deliver model-aware execution |
| Executable router exposed through MCP or CLI | Can own deterministic dispatch, retries, and accounting for work it launches | Adds runtime, credential, provider, context-transfer, and billing responsibilities; does not by itself control a host's active inference |

Choose the first approach for version one. Add a separate execution service only if the user requires independently enforced dispatch/budgets or provider execution that native clients cannot supply. That would be a distinct architecture decision, not a silent fallback.

## Packaging and component boundaries

Maintain one plugin directory with a shared `skills/dynamic-model-routing/SKILL.md`, relative references for Codex, Cursor, and Claude Code, and minimal platform manifests. The proposed manifests are `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, and `.claude-plugin/plugin.json`. Each should discover the same shared skill. Native package validation and loading must confirm this layout before release; manifest coexistence is not yet runtime-tested.

The shared skill owns classification, capability floors, bounded escalation, acceptance, and measurement. Each platform reference owns model discovery, native dispatch/configuration, precedence, verification, and rollback for that client. Do not duplicate routing policy in three independent implementations.

Configure may create the smallest project-owned policy and useful native worker/reviewer roles after discovering eligible settings. Four logical routes do not require four permanently pinned workers. Where direct model selection is supported, use it. Where a native role definition is required, create only the needed project roles and verify discovery before claiming activation. Worker instructions must carry the necessary policy; do not assume inheritance of the coordinator skill.

Include installation/activation instructions and a small package validator plus routing scenarios. Add marketplace metadata only where the documented installation path requires it. No daemon, network proxy, global startup hook, dashboard, or new runtime dependency is needed for the proposed first release.

## Platform evidence and adapter behavior

The following mechanisms were checked against official documentation on 2026-09-12. These are documentation findings, not plugin smoke-test results.

| Target | Supported mechanism to use | Boundary to preserve |
| --- | --- | --- |
| Codex desktop | Native plugin skills and exposed subagent dispatch | A declared route does not change the active coordinator model |
| Codex CLI | Plugin support; explicit worker model/effort or custom TOML roles | Check installed help, configuration precedence, and loaded settings |
| Cursor editor | Cursor Plugin; custom subagent `model` setting | Host plan/admin rules can substitute a different model |
| Cursor CLI | Documented skills/rules, subagents, `/plugin`, and `/model` controls | Verify component loading and actual dispatch separately from editor support |
| Claude Code desktop | Claude Code plugin in local Code sessions; native subagents | Desktop is interactive; CLI scripting cannot be a required integration path |
| Claude Code CLI | Plugin skills and subagent model/effort controls | Model precedence and fallback vary by version and settings |

Codex's installed CLI is 0.153.4. Help and the bundled catalog were read successfully, and an installed plugin confirms the `.codex-plugin` layout. Its custom agent configuration may override explicit dispatch values. Official references: [plugins](https://learn.chatgpt.com/docs/plugins), [building plugins](https://learn.chatgpt.com/docs/build-plugins), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Cursor's native format can package skills, rules, and agents; its portable Agent Plugin format packages skills and MCP. Subagents are documented in editor and CLI, with explicit IDs or inheritance. Do not treat a configured ID as proof of execution: plan and administrator restrictions may cause fallback. No automatic coordinator-switch mechanism was established by this research; use documented user controls when needed. References: [plugin format](https://cursor.com/docs/reference/plugins), [subagents](https://cursor.com/docs/subagents), [CLI controls](https://cursor.com/docs/cli/reference/slash-commands).

Claude Code's skill `model` frontmatter can override the model for the remainder of a turn; plain prose cannot. Omit that override from the shared coordinator skill by default to preserve the user's session selection. Prefer model-aware subagent dispatch. The docs distinguish precedence before and after version 2.1.251; the installed CLI is 2.1.247, so verify its actual precedence. References: [skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/subagents), [plugin format](https://code.claude.com/docs/en/plugins-reference).

Claude Desktop Code shares configuration with CLI but has no `--print` equivalent. Its plugin browser supports local sessions; the current docs exclude plugins in Desktop WSL sessions and require a different installation path for cloud. These exclusions do not imply that a standalone CLI inside WSL lacks plugins. Reference: [Desktop](https://code.claude.com/docs/en/desktop).

## Execution and failure flow

1. Read the authorized task, project instructions, dependencies, owned files, and acceptance criteria.
2. Identify the host and available capabilities through exposed tools/help. Record unavailable or ambiguous capabilities rather than guessing.
3. Resolve eligible model IDs/aliases and supported efforts once for the session. An installed catalog is weaker evidence than account-visible availability or successful execution. Use dated, evidence-backed role bindings; do not ship a perpetual model ranking or equate effort labels across vendors.
4. Classify the next dependency-ready outcome using the highest applicable risk route. Preserve the current coordinator where adequate and dispatch would add overhead.
5. For a useful worker, dispatch with the verified native mechanism, bounded scope, relevant context, and acceptance criteria. Serialize writers unless each has an isolated worktree. Keep review independent and read-only.
6. Inspect actual artifacts and native runtime evidence. Track requested model/effort separately from effective settings; record unknowns explicitly.
7. Escalate from observed failure evidence within the original attempt limits, then accept only after the required checks. Report total work including review and retries when usage is exposed.

Unsupported dispatch, missing entitlement, or unavailable model evidence must produce an explicit limitation. Continue locally only when the active model is adequate and permitted. Never claim that an unverified selection satisfies an explicit pin or sensitive capability floor. If that floor cannot be established, keep the affected branch pending and identify the required native selection or evidence; continue independent authorized work.

Native routing is agent-directed policy, not a deterministic enforcement engine. The plugin can preserve checks and report native fallbacks; it cannot guarantee that a platform never substitutes models or enforce a hard monetary cap without suitable host support. Unknown task-local cost stays unavailable, and account-wide quota changes are not attributed to this task.

## Configuration, data, and rollback

Installation makes the skill available; it does not authorize rewriting every project or enabling routing globally. Apply can work within the current session. Configure creates or updates only explicitly scoped project policy and native role settings, preserving existing instructions and permissions. Automatic skill discovery remains available unless the user requests explicit-only invocation.

Use existing task handoff records for sustained routing evidence. Record task, route, requested/effective model and effort, attempts, elapsed time, findings, acceptance evidence, and usage if exposed. Do not collect credentials, full environments, prompts, or source contents for telemetry. No plugin-owned external telemetry endpoint is proposed.

Rollback disables/removes the plugin and restores only routing-owned project changes after checking for subsequent edits. Uninstalling a plugin may not remove configuration created by Configure; the setup report must enumerate that separate rollback unit. Preserve global settings and unrelated user work.

## Verification and release criteria

Offline package checks must verify parseable manifests, consistent identity/version, skill discovery, required metadata, contained relative references, and absence of machine-specific paths. Use the lightest installed/native validation mechanism; no new test framework is required.

Behavioral evaluation must exercise actual skill invocation with cases for a clerical transformation, a routine fix, a one-line sensitive change, an explicit model pin, an unavailable model, unsupported effort, missing dispatch capability, host fallback, two failed attempts, a held implementation, and unknown usage. Required outcomes come from the original skill. Static keyword checks alone do not prove routing behavior.

For each of the six target surfaces, separately record package installation/loading, skill visibility, a harmless routed worker returning a bounded artifact, requested/effective model evidence where exposed, and rollback. Native syntax validation is not proof of activation; a worker smoke test is not a quality or cost benchmark. Mark blocked surfaces as unverified rather than advertising them as tested.

No implementation or plugin tests have run yet. Codex and Claude CLI read-only discovery succeeded; Cursor was not found on PATH. Desktop and Cursor verification availability remains to be established during the approved implementation work.

## Approval decision

The user approved the narrower research recommendation and requested implementation. Apply the pilot amendment above; the three-adapter/six-surface release is deferred. No commit, installation into a user's profile, publication, or deployment is implied by this approval.
