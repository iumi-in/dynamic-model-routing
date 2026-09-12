"""Offline checks for this pilot's package contract; no routing execution."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "plugins/dynamic-model-routing"
MACHINE_PATH = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|/(?:home|Users|tmp|var)/|\\\\[^\s\\]+\\")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXPECTED_FILES = frozenset({
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "LICENSE",
    "skills/dynamic-model-routing/SKILL.md",
    "skills/dynamic-model-routing/agents/openai.yaml",
    "skills/dynamic-model-routing/references/claude-code.md",
    "skills/dynamic-model-routing/references/codex.md",
})
MANIFEST_KEYS = {
    "claude": frozenset({"name", "version", "description", "author", "license", "homepage", "repository"}),
    "codex": frozenset({"name", "version", "description", "author", "license", "skills", "interface"}),
}


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    if not root.is_dir():
        return ["Package directory is missing"]

    package_files = []
    for path in sorted(root.rglob("*")):
        label = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"Symbolic links are unsupported: {label}")
        elif path.is_file():
            package_files.append(path)
    present = {path.relative_to(root).as_posix() for path in package_files}
    for label in sorted(EXPECTED_FILES - present):
        errors.append(f"Missing package file: {label}")
    for label in sorted(present - EXPECTED_FILES):
        errors.append(f"Unexpected package file: {label}")

    def read(path):
        if not path.resolve().is_relative_to(root):
            errors.append(f"Path escapes package: {path.relative_to(root)}")
            return None
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {path.relative_to(root)}: {type(exc).__name__}")
            return None

    manifests = []
    for host in ("codex", "claude"):
        path = root / f".{host}-plugin/plugin.json"
        raw = read(path)
        if raw is None:
            continue
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            errors.append(f"Invalid JSON in {path.relative_to(root)}")
            continue
        if not isinstance(data, dict):
            errors.append(f"Manifest must be an object: {path.relative_to(root)}")
            continue
        manifests.append(data)
        unexpected_keys = sorted(set(data) - MANIFEST_KEYS[host])
        if unexpected_keys:
            errors.append(f"Unsupported {host} manifest fields: {', '.join(unexpected_keys)}")
        if data.get("name") != root.name:
            errors.append(f"{host} manifest name must match the package directory")
        version = data.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version):
            errors.append(f"{host} manifest requires a numeric semantic version")
        if not isinstance(data.get("description"), str) or not data["description"].strip():
            errors.append(f"{host} manifest requires a description")
        if "skills" in data and data["skills"] not in ("./skills/", "./skills", "skills"):
            errors.append(f"{host} skills must use the shared skills directory")
    if len(manifests) == 2 and manifests[0].get("version") != manifests[1].get("version"):
        errors.append("Host manifest versions differ")

    skill = root / "skills/dynamic-model-routing/SKILL.md"
    raw = read(skill)
    if raw is not None:
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", raw, re.S)
        fields = {}
        if match is None:
            errors.append("Skill requires closed frontmatter")
        else:
            # This package deliberately permits only two single-line metadata fields.
            for line in match[1].splitlines():
                key, separator, value = line.partition(":")
                if not separator or key not in {"name", "description"} or key in fields:
                    errors.append("Skill metadata must contain only name and description; no coordinator overrides")
                    continue
                try:
                    fields[key] = json.loads(value.strip()) if value.strip().startswith('"') else value.strip()
                except json.JSONDecodeError:
                    errors.append(f"Invalid skill metadata: {key}")
            if fields.get("name") != root.name:
                errors.append("Skill name must match the package")
            if not isinstance(fields.get("description"), str) or not fields["description"].strip():
                errors.append("Skill requires a description")
    for path in package_files:
        if path.suffix not in {".md", ".json", ".yaml", ".yml"}:
            continue
        raw = read(path)
        if raw is None:
            continue
        label = path.relative_to(root)
        if MACHINE_PATH.search(raw):
            errors.append(f"Machine-specific absolute path in {label}")
        if path.suffix != ".md":
            continue
        if re.search(r"(?m)^[ \t]{0,3}\[[^\]\n]+\]:", raw):
            errors.append(f"Reference-style definitions are unsupported in {label}; use inline links")
        for target in LINK.findall(raw):
            try:
                url = urlsplit(target)
                if url.scheme == "https" and url.netloc:
                    continue
                if target.startswith("#"):
                    continue
                if url.scheme or url.netloc:
                    errors.append(f"Unsupported reference in {label}: {target}")
                    continue
                local = Path(unquote(url.path).replace("\\", "/"))
                resolved = (path.parent / local).resolve()
                if local.is_absolute() or not resolved.is_relative_to(root):
                    errors.append(f"Reference escapes package in {label}: {target}")
                elif not resolved.is_file():
                    errors.append(f"Missing reference in {label}: {target}")
            except (OSError, ValueError):
                errors.append(f"Invalid reference in {label}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT)
    errors = validate(parser.parse_args().root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Package checks passed. Static validation does not prove native loading, routing behavior, or savings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
