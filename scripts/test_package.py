import hashlib
import json
import subprocess
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


class PackageContractTests(unittest.TestCase):
    def run_package(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["pwsh", "-NoProfile", "-File", str(ROOT / "scripts" / "package.ps1"), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_dot_prefixed_package_entries_are_read_with_force_on_unix(self):
        source = (ROOT / "scripts" / "package.ps1").read_text(encoding="utf-8")
        self.assertIn("Get-Item -LiteralPath $source -Force", source)

    def test_release_workflow_uploads_only_named_files(self):
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(encoding="utf-8")
        self.assertNotIn("dist/* --verify-tag", workflow)
        self.assertIn('"dist/ai-first-vibe-coding-${version}.zip"', workflow)
        self.assertIn("dist/ai-first-vibe-coding.skill", workflow)
        self.assertIn("dist/manifest.json", workflow)
        self.assertIn("dist/SHA256SUMS.txt", workflow)

    def test_one_staged_tree_produces_manifested_zip_skill_and_checksums(self):
        result = self.run_package("-Version", "1.2.3")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        manifest = json.loads((DIST / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual("1.2.3", manifest["version"])
        self.assertIn(manifest["sourceTree"], {"clean", "dirty"})
        archives = [DIST / item["name"] for item in manifest["artifacts"]]
        self.assertEqual(
            {"ai-first-vibe-coding-1.2.3.zip", "ai-first-vibe-coding.skill"},
            {path.name for path in archives},
        )
        entries = []
        for archive_path in archives:
            self.assertTrue(archive_path.is_file(), archive_path)
            with zipfile.ZipFile(archive_path) as archive:
                entries.append(sorted(archive.namelist()))
        self.assertEqual(entries[0], entries[1])
        self.assertTrue(
            {
                "SKILL.md",
                "docs/quick-start.md",
                "docs/quick-start.zh-CN.md",
                "assets/brand/watermark-dark.svg",
                "assets/brand/watermark-auto.svg",
                "docs/assets/brand/avatar.png",
            }.issubset(set(entries[0]))
        )
        for artifact, archive_path in zip(manifest["artifacts"], archives):
            self.assertEqual(hashlib.sha256(archive_path.read_bytes()).hexdigest(), artifact["sha256"])
        self.assertEqual(
            {f"{item['sha256']}  {item['name']}" for item in manifest["artifacts"]},
            set((DIST / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()),
        )

    def test_release_mode_refuses_a_dirty_worktree(self):
        probe = ROOT / ".package-release-dirty-probe"
        probe.write_text("test-owned untracked probe\n", encoding="utf-8")
        try:
            result = self.run_package("-Release", "-Version", "1.2.3")
            self.assertNotEqual(0, result.returncode)
            self.assertIn("clean working tree", result.stdout + result.stderr)
        finally:
            probe.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
