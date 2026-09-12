# Pilot verification evidence

Date: 12 September 2026. Platform: Windows, Codex desktop host. Exact root inference model/effort is not exposed in execution results. Native CLI versions checked: Codex `0.153.4`; Claude Code `2.1.247`.

## Observed results

| Layer | Result | What this establishes |
| --- | --- | --- |
| Repository validator | Passed | Manifest/skill consistency, required files, contained inline Markdown references, no coordinator metadata override or detected machine path |
| Validator regression suite | 17 tests passed | Actual malformed/missing/escaping package inputs are rejected, release contents are bounded, the archive is reproducible, and valid input stays unchanged |
| Official Codex plugin validator | Passed | Authoring schema and skill metadata accepted by the installed plugin-creator validator |
| Official skill quick validator | Passed | Packaged skill metadata accepted |
| Claude native strict validation | Passed | The installed CLI accepted the Claude plugin manifest |
| Claude session loading | Passed | `dynamic-model-routing@inline`, scope `session`, enabled `true`, exact source directory, no plugin errors |
| Codex isolated installation | Passed | Plugin `dynamic-model-routing@personal`, version `0.1.0`, installed and enabled in a disposable workspace profile |
| Codex prompt discovery | Passed | The packaged skill's distinct description appeared in native rendered model input |
| Codex removal | Passed | Plugin and test marketplace removed; final disposable-profile marketplace list was empty |
| Distribution archive | Passed | Seven ZIP entries match the source package byte for byte and pass ZIP integrity checking |
| Synthetic policy scenarios | 12/12 expected decisions matched | A separate agent consumed the skill and case prompts; root compared its answers with the expected outcomes |
| Claude live Advise invocation | Blocked | Native result: `Not logged in`; zero API tokens/cost reported; no model response or worker |
| Codex live execution | Unverified | Disposable profile's `codex login status` returned `Not logged in`; no credentials were copied into it |
| Native worker identity and routing | Unverified | No authenticated CLI worker run has completed |
| Cost/quality savings and retention | Not measured | No participant trial or benchmark has run |

These layers are intentionally separate. A manifest accepted by a parser is not proof that native execution preserves a model pin. An advisory scenario is not an actual worker run.

## Commands and boundaries

The portable authoring checks were run with the available Python 3.12 runtime:

```text
python -B -m unittest discover -s tests -v
python -B scripts/validate.py
claude plugin validate ./plugins/dynamic-model-routing --strict
claude --plugin-dir ./plugins/dynamic-model-routing plugin list --json
```

Only the matching plugin row from Claude's list was inspected for reporting; a full inventory can include unrelated configuration and should not be published.

The official plugin-creator and skill-creator validation scripts initially lacked PyYAML. Pinned PyYAML `6.0.3` was installed into a temporary authoring directory, used to run both official scripts successfully, and is not a plugin or repository runtime dependency. The portable checks require no third-party module.

Codex did not auto-discover the repository catalog in the sandboxed, non-Git workspace. A per-plugin enabled override alone also did not install the package. The working verification used a child process with its own disposable `CODEX_HOME`, leaving the parent's profile selection untouched. No authentication files were copied. The native operations were:

```text
codex plugin add dynamic-model-routing@personal --json
codex plugin list --json --marketplace personal
codex debug prompt-input "Use $dynamic-model-routing in Advise mode."
codex login status
```

The first three commands also received transient `marketplaces.personal.source` set to the absolute checkout directory and `marketplaces.personal.source_type="local"`. This resolved the source without registering it in the normal user profile. The installed cache and configuration stayed under the disposable workspace directory. The native prompt output was captured as UTF-8 and checked without publishing its full contents.

The Claude live check explicitly loaded the package, selected `sonnet`, used plan permissions, limited available tools to `Read,Skill`, capped API budget at `$0.25`, disabled session persistence, and requested only classification of a synthetic one-line cross-tenant authorization defect. It returned `Not logged in` before inference. No login, credential changes, global plugin installation, or policy bypass was performed to overcome that boundary.

## Remaining native smoke check

In an authenticated consuming CLI after installation:

1. Invoke the plugin explicitly. Ask for Advise on a one-line authorization fix; expect Sensitive and independent boundary review requirements.
2. Ask for one native worker, read-only, to alphabetize the supplied words `pear, apple, orange`. Permit no file writes, commands, network tools, or further delegation. Confirm the native model map before selecting a worker; do not use invented fixture names.
3. Require `apple, orange, pear` and record the dispatch identifier, requested model/effort, effective settings from native runtime evidence when exposed, and the checked output. A worker repeating its own requested model is not independent identity evidence.
4. Run the pin/unavailable/effort/fallback scenarios from `tests/scenarios.json` as simulations. They must not trigger actual inaccessible-model retries or protected operations.
5. End the Claude session or remove the test Codex installation. Inspect any consuming-project Configure changes separately; do not erase unrelated user edits.

If runtime identity is unavailable, record that limitation and do not count an explicit-pin or sensitive-floor requirement as passed. This smoke check does not establish cost savings or safe behavior on other platforms.

## Review trail

Independent source review found an ambiguity inherited from the original policy: unavailable explicit selections could be treated as allowing fallback unless separately forbidden. The pilot now distinguishes router-selected defaults from user pins and keeps an unavailable pin pending unless the user permits fallback. A dedicated scenario covers the user saying only "Use model X".

A separate Codex-hosted agent was requested at `gpt-5.6-sol`, medium reasoning, to read the shared skill and host reference and consume only case IDs/prompts, without the expected fields. It returned all 12 decisions. Root compared them with the expected outcomes: all matched the intended routes and constraints, including the pin/fallback distinction, unsupported effort, implementation hold, and unknown usage. This is a synthetic instruction-following check through the available agent tool, not a Codex CLI or Claude Code worker smoke test. The actual execution model was not independently exposed.

The validator's first implementation falsely recognized the end of `https:/` as a Windows drive prefix. The valid-package and HTTPS-reference tests caught that; a boundary-aware pattern corrected it, and all 12 tests passed. The initial test suite also failed before the validator existed, establishing the missing implementation gate.

Final independent review found that reference-style Markdown definitions bypassed the inline-link check. A new regression failed on that case before the fix. The deliberately small package format now rejects reference definitions and requires inline links. The validator is not a general Markdown security scanner.

A later public-release audit found that valid hooks or other executable components could pass the repository validator and that the ZIP was outside the tested boundary. The validator now enforces the exact seven-file instruction-only package and supported manifest fields. Regression checks also bind the distribution archive to those validated source bytes, reproduce it deterministically, and pin the marketplace to the intended local package. All 17 tests pass.

The scoped re-review confirmed the fix and found no new consequential issues. Final spec/quality verdict: pass for the narrowed pilot, with authenticated native worker execution explicitly unverified.

Native source references: [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins), [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference), [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference). Local command output, not documentation alone, supports the passed rows above.
