import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProductDocumentationTests(unittest.TestCase):
    def test_readmes_and_brand_docs_use_theme_compatible_watermark(self):
        for name in ("README.md", "README.zh-CN.md"):
            source = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("assets/brand/watermark-auto.svg", source, name)
            self.assertNotIn("assets/brand/watermark-dark.svg", source, name)

        asset = ROOT / "assets" / "brand" / "watermark-auto.svg"
        docs_asset = ROOT / "docs" / "assets" / "brand" / "watermark-auto.svg"
        self.assertTrue(asset.is_file())
        self.assertTrue(docs_asset.is_file())
        self.assertEqual(asset.read_bytes(), docs_asset.read_bytes())
        source = asset.read_text(encoding="utf-8")
        self.assertIn("@media (prefers-color-scheme: dark)", source)
        self.assertRegex(source, r'<text[^>]*class="wordmark"[^>]*stroke-width="3"')
        self.assertIn("watermark-auto.svg", (ROOT / "docs" / "brand.md").read_text(encoding="utf-8"))

    def test_bilingual_install_lifecycle_docs_are_present_and_truthful(self):
        english = (ROOT / "docs" / "quick-start.md").read_text(encoding="utf-8")
        chinese = (ROOT / "docs" / "quick-start.zh-CN.md").read_text(encoding="utf-8")
        for source, heading in ((english, "# 60-second install and lifecycle"), (chinese, "# 60 秒安装与生命周期")):
            self.assertIn(heading, source)
            for word in ("install", "upgrade", "rollback", "uninstall") if source is english else ("安装", "升级", "回滚", "卸载"):
                self.assertIn(word, source)
            self.assertIn("DOCUMENTED_ONLY", source)

    def test_skill_hands_public_productization_to_the_optional_governance_skill(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("icarus-open-source-governance", skill)
        self.assertIn("not a claimed host installation", skill)

    def test_readmes_link_release_status_and_keep_brand_optional(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("GitHub Releases", english)
        self.assertIn("a tag alone is not proof", english)
        self.assertIn("GitHub Releases", chinese)
        self.assertIn("仅创建标签不能证明", chinese)
        self.assertIn("optional BOOMKALAKASHA", english)
        self.assertIn("可选的 BOOMKALAKASHA", chinese)

    def test_security_policy_does_not_invent_a_response_sla(self):
        security = (ROOT / "SECURITY.md").read_text(encoding="utf-8").lower()
        self.assertNotIn("seven days", security)
        self.assertIn("does not promise", security)

    def test_release_workflow_passes_a_real_semver_value_to_clean_release_packaging(self):
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(encoding="utf-8")
        self.assertIn('$version = $env:TAG_NAME.TrimStart("v")', workflow)
        self.assertIn("-Release -Version $version", workflow)


if __name__ == "__main__":
    unittest.main()
