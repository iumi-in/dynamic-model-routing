# Contributing

Thanks for helping improve Dynamic Model Routing. Keep changes focused on the instruction-only Codex and Claude Code CLI pilot unless pilot evidence justifies another host or runtime component.

## Development

Python 3.11 or newer is sufficient. The plugin itself has no runtime dependency.

```text
python -B scripts/package.py
python -B scripts/validate.py
python -B -m unittest discover -s tests -v
claude plugin validate ./plugins/dynamic-model-routing --strict
```

The package contract intentionally permits only the seven files listed in `scripts/validate.py`. Propose hooks, MCP servers, executables, telemetry, credential access, global configuration, or new runtime dependencies in an issue before implementing them.

Pull requests should explain the user-visible behavior, include the smallest relevant regression check, preserve authorization and verification gates, and rebuild the ZIP when packaged source changes.
