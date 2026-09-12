---
name: dynamic-model-routing
description: "Route authorized coding tasks through native Codex or Claude Code model controls for verified quality, total cost, and completion time. Use for model selection, bounded escalation, delegation, or project routing setup; not an application's runtime AI router."
---

# Dynamic Model Routing

Optimize cost and elapsed time **to an accepted result**, subject to the project's quality requirements. A lower token price or a stronger model is not evidence that a change is correct. Preserve explicit model choices, budgets, execution holds, and required verification.

This pilot supports Codex CLI and Claude Code CLI. Read the matching host reference before resolving models or dispatching: [Codex](references/codex.md) or [Claude Code](references/claude-code.md). Identify the host from exposed runtime tools, not from filenames alone. For an unknown host, provide advice and state that its execution adapter is unverified. Native tools execute the decisions; this skill does not enforce a hard spending cap or control another client's session.

## Choose the requested mode

- **Advise:** Recommend routes for the supplied work; leave files and settings unchanged.
- **Apply:** Route already-authorized development, debugging or review through the procedure below. This does not require persistent configuration.
- **Configure:** When the request includes setting up persistent routing, use the matching host reference, then create or update the smallest project-specific configuration and policy. Preparing routing does not start a held implementation. Enumerate every created/changed setting and its rollback separately from plugin removal.

If the request is unclear, progress with advice or in-session routing within its existing scope. Ask only when an unresolved preference changes cost, authorization or the safe implementation.

## Resolve the project and eligible models

1. Identify the actual repository, applicable instructions, accepted plan, current task, dependencies and quality gates. Use existing handoff/decision records; do not import another project's stack, paths, workload or release constraints.
2. Read available model metadata and current session settings through the tools exposed by this client. If needed, inspect the installed CLI's help and model catalog. Verify changing availability, pricing and model guidance with the host/provider's official documentation. Inspect only relevant configuration fields; avoid credential files and full environment dumps.
3. Bind the four capability roles below to exact available model IDs or supported native aliases and supported reasoning efforts. Record when an alias can float; do not mistake it for an immutable model ID. Respect provider/account/data-handling constraints. A catalog entry proves identifier support, not account entitlement. Current successful calls or account-visible availability provide stronger evidence.
4. Resolve this map once per session and reuse it while facts remain current. Refresh after a model/pricing change, availability failure or new evidence of repeated rework. Do not hardcode a perpetual model ranking or assume similarly named models perform equivalently.

Use a balanced eligible model at moderate reasoning for ordinary coordination. Use a stronger coordinator when ambiguity, long context or cross-system judgment warrants it. Start workers at the lowest supported effort justified by their task; increasing effort on a small model does not establish equivalence to a larger model.

## Select a task route

Define the next dependency-ready outcome, owned files, acceptance check and available runtime evidence. Select the **highest applicable route**, including any escalation already triggered. Risk and uncertainty override patch size.

| Route | Capability role | Qualifying work | Review |
| --- | --- | --- | --- |
| Clerical | Lowest-cost adequate model, light reasoning | Fully specified documentation transformation or bounded evidence extraction; no change to runtime behavior, dependencies, contracts or sensitive invariants | Coordinator checks output and relevant existing validation |
| Routine | Balanced model, moderate reasoning | Approved design/contracts, ordinary UI, bounded logic, reproducible local fixes or test tooling without a sensitive invariant change | Spec and code-quality review appropriate to the scope; integration checks at feature boundaries |
| Sensitive | Strong model, deeper reasoning | Security/permissions, privacy, money, cryptography, deletion/export, persistence/recovery, concurrency, migrations, physical-system assumptions or ambiguous cross-system contracts | Independent capable review plus required boundary/failure/runtime checks |
| Escalation | Strongest eligible model suited to the unresolved problem | A reproducible difficult defect or conflicting critical findings that survived the bounded attempts below | Independent review of the resulting change and the original acceptance checks |

A one-line permission fix is Sensitive. Security-test changes can be Sensitive without production edits. UI that governs protected actions, disclosure or readiness inherits that risk. A large text transformation can remain Clerical. If risk is unclear, use a bounded strong-model analysis before implementation. Split mixed work only when the parts have independent acceptance checks and ownership.

Honor an explicit user's model selection within its stated scope. If it cannot meet a material requirement, explain the limitation rather than silently substituting another model. An unavailable user-pinned model keeps that branch pending unless the user explicitly permits fallback. A router-selected binding may use an eligible alternative that meets the route's capability floor; report the change. Quotas do not justify an unannounced capability downgrade.

## Execute without multiplying work

If the active model is adequate and already holds the context, complete a small task locally when dispatch would cost more. A model cannot change its own active inference model merely by declaring a new route.

Use subagents for bounded independent implementation, evidence extraction or review when execution is authorized, delegation is permitted, and useful local work can continue. Dispatch explicitly with the chosen model and reasoning where supported. If the tool cannot select models, report that limitation and use supported session controls; do not claim an automatic switch.

Select a worker through the native tool schema actually exposed to this session. Do not invent a model or effort argument, silently inherit an expensive model, or launch a different coding CLI as an adapter workaround. If effort selection is unavailable, record it as unavailable and use a verified adequate model without claiming an effort value. An unsupported user-required setting or an unestablished sensitive capability floor keeps that branch pending. Distinguish the requested route, dispatch acceptance, effective model/effort evidence, and acceptance checks. Native fallback is not proof that an explicit pin was honored.

Each assignment includes the task/plan anchor, repository/worktree/revision, acceptance criteria, owned files, relevant constraints and source pointers, checks, prior failed attempts, and read-only or write scope. Pass only useful context, preserving all controlling constraints. Return concise findings, changes, real checks and remaining gates.

Start with modest concurrency, normally one worker or two independent workers. Respect stricter platform/project limits. Workers should not recursively delegate by default. Use isolated worktrees for concurrent writes; otherwise serialize all writers, including the coordinator. Review a frozen revision or patch. Honor any stricter existing review workflow without duplicating completed review work.

Batch independent reads and checks; reuse tools and context for the same problem. Run focused validation before broader checkpoints. Keep every required acceptance check while removing redundant work. Standard service is the cost-conscious default; paid speed tiers are a separate tradeoff to use only within the user's urgency and spending authorization.

## Escalate with evidence

An attempt is a concrete diagnosis, a relevant change or experiment, and its observed result. An intentionally failing regression test is not a failed implementation attempt.

- After a failed attempt, inspect the result. Permit one targeted correction at the same route when new evidence supports it. Repeated identical failure, unsafe assumptions or newly discovered sensitive scope escalates immediately. Two unsuccessful attempts on the same cause is the default ceiling, not permission to repeat blindly.
- Escalate Clerical to Routine for ordinary logic or directly to Sensitive for sensitive scope. Escalate Routine to Sensitive and unresolved Sensitive reasoning to Escalation. Pass the reproduction and failed approaches forward.
- Give the highest route a bounded diagnosis and falsifiable next experiment. If it fails to resolve the uncertainty, record the missing evidence and stop speculative retries on that branch. Continue independent authorized work; revisit when new evidence arrives.
- Missing tools, credentials, access, hardware or an upstream outage are prerequisite failures. Resolve them within existing authorization or state the exact gate; a larger model cannot supply missing evidence.
- Return to the normal route for the next unrelated task. Extra reasoning and premium models are responses to demonstrated need, not permanent escalation.

## Accept, measure and adapt

The coordinator inspects the actual diff and verification output. Reviewer agreement, a successful build, or model confidence alone does not establish acceptance. Preserve project-specific tests, accessibility, data integrity and release gates. Distinguish synthetic evidence from checks needing real hardware or external systems. A review is independent only when the reviewer inspects source/evidence separately from the implementation context; if unavailable, disclose that limitation.

For sustained work, append a compact record to the existing task handoff:

`task/class | route | requested model/effort | effective model/effort and evidence | attempts | elapsed | first-pass result | material findings | acceptance evidence | total usage if exposed | next gate`

Measure total coordinator, worker, review and retry cost per accepted task. Record unknown usage as unavailable; concurrent account-wide usage is not task-local cost. Without measurements, label rankings and savings as estimates. Do not invent a quota for cheap-model usage or claim guaranteed optimal cost, speed or quality.

Reassess comparable task classes after a small observed sample, for example five accepted tasks. Repeated escalation suggests a higher starting route. An escaped security/data-integrity defect triggers immediate reassessment and a stronger route pending diagnosis. A consistently successful Routine class may trial lower effort on one comparable bounded task, keeping review and acceptance unchanged; reverse that trial if it fails. These are operating heuristics, not statistical proof. Sensitive capability floors do not decrease automatically.

## Completion

Report the effective route, what was executed/configured, actual checks and remaining limitations. For configuration, distinguish files saved, native settings read back, worker dispatch verified, and cost/quality benchmarked. Do not present one as proof of another. Applying this skill never authorizes credit purchases, account changes, deployment, commits, or work outside the user's task.
