"""Exercise the package validator's release boundary using real file mutations."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate.py"
PACKAGE_SCRIPT = ROOT / "scripts/package.py"
PACKAGE = ROOT / "plugins/dynamic-model-routing"
ARCHIVE = ROOT / "output/plugins/dynamic-model-routing-0.1.1.zip"
MARKETPLACE = ROOT / ".agents/plugins/marketplace.json"


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.is_file(), "The package validator has not been implemented")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / PACKAGE.name
        shutil.copytree(PACKAGE, self.root)
        spec = importlib.util.spec_from_file_location("pilot_validate", SCRIPT)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def errors(self):
        return self.module.validate(self.root)

    def change_manifest(self, host, key, value):
        path = self.root / f".{host}-plugin/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data[key] = value
        path.write_text(json.dumps(data), encoding="utf-8")

    def append_link(self, target):
        path = self.root / "skills/dynamic-model-routing/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write(f"\n[Reference]({target})\n")

    def test_valid_package_passes_without_changing_files(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual([], self.errors())
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_rejects_host_identity_and_version_mismatch(self):
        for key, value in [("name", "wrong-plugin"), ("version", "0.2.0")]:
            with self.subTest(key=key):
                self.change_manifest("claude", key, value)
                self.assertTrue(self.errors())
                self.change_manifest("claude", key, PACKAGE.name if key == "name" else "0.1.1")

    def test_rejects_non_object_or_malformed_manifest(self):
        path = self.root / ".claude-plugin/plugin.json"
        for content in ["null", "[]", "{broken", '{"name": null}']:
            with self.subTest(content=content):
                path.write_text(content, encoding="utf-8")
                self.assertTrue(self.errors())

    def test_rejects_missing_skill(self):
        (self.root / "skills/dynamic-model-routing/SKILL.md").unlink()
        self.assertTrue(self.errors())

    def test_rejects_missing_local_reference(self):
        self.append_link("references/missing.md")
        self.assertTrue(self.errors())

    def test_rejects_reference_outside_package_even_when_it_exists(self):
        (self.root.parent / "outside.md").write_text("private", encoding="utf-8")
        self.append_link("../../../outside.md")
        self.assertTrue(self.errors())

    def test_rejects_encoded_path_traversal(self):
        self.append_link("%2e%2e/%2e%2e/%2e%2e/outside.md")
        self.assertTrue(self.errors())

    def test_rejects_unsupported_reference_style_links(self):
        path = self.root / "skills/dynamic-model-routing/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n[setup][host]\n\n[host]: ../../../outside.md\n")
        self.assertTrue(self.errors())

    def test_rejects_unsupported_or_external_skill_directory(self):
        self.change_manifest("codex", "skills", "../outside/")
        self.assertTrue(self.errors())

    def test_rejects_unexpected_components_and_manifest_fields(self):
        hooks = self.root / "hooks"
        hooks.mkdir()
        (hooks / "hooks.json").write_text('{"hooks": {}}', encoding="utf-8")
        self.assertIn("Unexpected package file: hooks/hooks.json", self.errors())
        shutil.rmtree(hooks)
        self.change_manifest("claude", "hooks", "./hooks/hooks.json")
        self.assertIn("Unsupported claude manifest fields: hooks", self.errors())

    def test_rejects_accidental_coordinator_override(self):
        path = self.root / "skills/dynamic-model-routing/SKILL.md"
        original = path.read_text(encoding="utf-8")
        for setting in ['model: "premium"', 'effort: "high"', 'context: "fork"']:
            with self.subTest(setting=setting):
                path.write_text(original.replace("---\n", "---\n" + setting + "\n", 1), encoding="utf-8")
                self.assertTrue(self.errors())

    def test_rejects_machine_specific_paths(self):
        path = self.root / "notes.md"
        for machine_path in [r"C:\Users\someone\secret", "/home/someone/private", "/Users/someone/private"]:
            with self.subTest(path=machine_path):
                path.write_text(machine_path, encoding="utf-8")
                self.assertTrue(self.errors())

    def test_allows_https_and_local_anchors(self):
        self.append_link("https://example.org/docs#native")
        self.append_link("#completion")
        self.assertEqual([], self.errors())

    def test_cli_reports_failure_and_success_without_traceback(self):
        success = subprocess.run([sys.executable, "-B", str(SCRIPT), str(self.root)], capture_output=True, text=True)
        self.assertEqual(0, success.returncode, success.stderr)
        (self.root / ".claude-plugin/plugin.json").write_text("null", encoding="utf-8")
        failure = subprocess.run([sys.executable, "-B", str(SCRIPT), str(self.root)], capture_output=True, text=True)
        self.assertEqual(1, failure.returncode)
        self.assertIn("ERROR:", failure.stderr)
        self.assertNotIn("Traceback", failure.stderr)

    def test_distribution_archive_matches_validated_source(self):
        self.assertTrue(ARCHIVE.is_file())
        with zipfile.ZipFile(ARCHIVE) as archive:
            names = archive.namelist()
            self.assertEqual(sorted(self.module.EXPECTED_FILES), sorted(names))
            self.assertEqual(len(names), len(set(names)), "Archive contains duplicate paths")
            self.assertIsNone(archive.testzip())
            for name in names:
                self.assertEqual((PACKAGE / name).read_bytes(), archive.read(name), name)

    def test_distribution_archive_is_reproducible(self):
        output = Path(self.temp.name) / "rebuilt.zip"
        result = subprocess.run(
            [sys.executable, "-B", str(PACKAGE_SCRIPT), str(PACKAGE), str(output)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(ARCHIVE.read_bytes(), output.read_bytes())

    def test_marketplace_targets_only_the_local_package(self):
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        self.assertEqual("personal", data.get("name"))
        self.assertEqual(1, len(data.get("plugins", [])))
        plugin = data["plugins"][0]
        self.assertEqual("dynamic-model-routing", plugin.get("name"))
        self.assertEqual({"source": "local", "path": "./plugins/dynamic-model-routing"}, plugin.get("source"))


if __name__ == "__main__":
    unittest.main()
