# Two-week routing pilot

The pilot tests whether this package improves real work compared with existing methods. It does not assume that automatic routing is useful, cheaper, or more reliable. These thresholds come from the project's research recommendation; they are proposed decisions, not industry benchmarks.

Recruit eight regular Codex or Claude Code users, including several who use both clients and some satisfied with native defaults. Obtain permission before contacting or collecting information from anyone. No participants have been recruited by this implementation.

Ask about one recent task: which model they selected, how often they switched, why a run failed, what repair took, and what they already do to control usage. First compare the supplied policy, native controls, and a close existing router. If a short instruction gives the same benefit, prefer sharing that instruction over maintaining extra integration.

## Trial procedure

1. Record client version, operating system, installation path, model bindings, and which runtime evidence is available. Do not record credentials, private prompts, or source contents.
2. Time unassisted setup and the first successful route. Mark setup blocked if native loading or required model identity cannot be established.
3. Select recurring task classes and stable acceptance checks before comparing results. Choose each class's primary metric in advance.
4. Run two weeks of real work. Target at least twenty comparable accepted-task observations across at least five participants; also record failed/abandoned tasks and their resource use so they do not disappear from the comparison.
5. Compare against the developer's normal model, native Auto/defaults where available, and a short manual policy. Include their existing router if used. Use equivalent fresh branches and vary order where practical; do not repeat production side effects for a benchmark.
6. Review actual outputs and acceptance evidence, including required independent checks. A model's confidence or a build alone is insufficient.

## Record per task

Use an existing handoff or a locally retained table with these fields:

```text
participant_alias, task_class, client_version, baseline_or_plugin,
route, requested_model_effort, effective_model_effort, identity_evidence,
attempts, first_pass, accepted, acceptance_evidence,
elapsed_seconds, human_switching_and_repair_seconds,
total_measured_cost_or_usage, measurement_basis, unavailable_fields
```

Count coordinator, workers, reviews, retries, and failed work associated with the task. Keep cost, elapsed time, and human intervention separate. Record unavailable measurements as unavailable. Subscription consumption is not automatically dollars saved, and concurrent account-wide usage is not task-local cost.

## Continue or stop

| Gate | Proposed threshold |
| --- | --- |
| Activation | At least 6 of 8 configure their first route within 10 minutes without author help |
| Repeat use | At least 5 return in week two on real tasks |
| Practical advantage | At least 3 of the minimum 5 retained users pass their preselected metric and guardrails |
| Integrity | No observed unauthorized substitution, out-of-scope action, or omitted required check |
| Add another host | At least 3 retained participants request it and can help verify it |

For a cost cohort, require at least 15% lower total measured cost or an agreed usage measure when costs are unavailable. For a workflow cohort, require at least 25% less hands-on switching and repair time. Preserve acceptance quality; median elapsed time may not worsen by more than 10%. Workflow-cohort measured cost may not worsen by more than 10%. An unavailable guardrail is unverified, not passed.

Zero observed failures in this small sample is not statistical proof of safety. If the package misses activation, simplify setup. If repeat use or practical benefit is absent, narrow the task class, contribute to an existing tool, or stop at the reference skill. Public release and expanded host claims depend on evidence, not completion of the code.

## Scenario checks before real work

Use [the scenarios](../tests/scenarios.json) in Advise mode first. They are synthetic decisions, not instructions to edit a project or make actual model calls. A reviewer compares answers with the expected outcomes and records per-case failures. Passing these cases does not prove native worker execution or economic benefit. Test a harmless native worker separately and record its requested and effective identity when available.
