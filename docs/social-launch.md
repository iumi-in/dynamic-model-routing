# Social launch copy

Attach `output/social/dynamic-model-routing-demo.mp4` directly to each post. The video includes narration and on-screen text; use the supplied alt text for accessibility.

## LinkedIn

I kept catching myself making the same small decision before every AI coding task: which model is “enough” for this job?

A typo, a dependency update, and an authorization change do not carry the same risk. Treating them the same wastes either compute or confidence.

So I turned the routing policy I was using into a free, open-source plugin: **Dynamic Model Routing**.

It works with Codex CLI and Claude Code CLI. It classifies work as Clerical, Routine, Sensitive, or Escalation, recommends the least expensive eligible model that clears the risk bar, preserves explicit model choices, and adds stronger checks as risk rises.

There is no proxy, extra API key, telemetry service, or runtime dependency.

The honest status: v0.1.1 is a pilot. Packaging and validation are complete, 17 regression tests pass, and CI is green on Windows, macOS, and Linux. Real native-worker behavior and savings still need independent evidence—and that is exactly what I am looking for now.

If you use Codex or Claude Code, try it on a real task and tell me where the policy helps or gets in your way:

https://github.com/iumi-in/dynamic-model-routing

What would you want a model router to optimize first: cost, speed, or confidence?

#OpenSource #AICoding #DeveloperTools #Codex #ClaudeCode

## X

I got tired of choosing a model for coding tasks. A typo and an auth change shouldn’t be treated the same.

So I built Dynamic Model Routing for Codex + Claude Code: risk-aware routing with explicit choices and checks.

Free + MIT:
https://github.com/iumi-in/dynamic-model-routing

### Optional first reply

v0.1.1 is an evidence-seeking pilot: 17 regression tests, green CI on Windows/macOS/Linux, no proxy, no telemetry, and no extra API keys. I’m looking for users to test native routing and report where it helps—or gets in the way.

## Video accessibility

**Alt text:** Animated 44-second demo of the open-source Dynamic Model Routing plugin. Dark navy slides show why coding tasks need different risk levels, Claude Code and Codex install commands, the four routes—Clerical, Routine, Sensitive, and Escalation—and the verified pilot status. The final slide links to the public GitHub repository.

**Voiceover transcript:** I kept making the same choice before every coding task: which model is enough? But a typo, a feature, and an authorization change carry very different risk. Dynamic Model Routing adds a simple risk-aware policy to Codex and Claude Code. For Claude Code, validate the plugin, load it for the session, and invoke the namespaced skill. For Codex, add the local marketplace, install the plugin, and ask for Advise mode. The router classifies work as clerical, routine, sensitive, or escalation, while preserving your explicit choice. The pilot has seventeen regression tests and green CI across Windows, macOS, and Linux. Version zero point one point one is free and MIT licensed. Try it, break it, and share the evidence on GitHub.
