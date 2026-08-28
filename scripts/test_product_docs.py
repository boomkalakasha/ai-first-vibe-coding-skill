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
            self.assertIn("scripts/package.ps1 -Version 1.2.2", source)

    def test_skill_hands_public_productization_to_the_optional_governance_skill(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("icarus-open-source-governance", skill)
        self.assertIn("not a claimed host installation", skill)

    def test_readmes_link_release_status_and_keep_brand_optional(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        for source in (english, chinese):
            self.assertIn("<!-- icarus-release-fact: dynamic -->", source)
            self.assertIn("https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/latest", source)
            self.assertIn("https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases", source)
        self.assertNotIn("latest public stable release is", english.lower())
        self.assertNotIn("最新公开稳定版是", chinese)
        self.assertIn("a tag alone is not proof", english)
        self.assertIn("仅创建标签不能证明", chinese)
        self.assertIn("optional BOOMKALAKASHA", english)
        self.assertIn("可选的 BOOMKALAKASHA", chinese)

    def test_readmes_show_an_illustrative_execution_outcome_after_quick_start(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertLess(english.index("## What you get"), english.index("## What makes it useful"))
        self.assertIn("Illustrative outcome", english)
        self.assertIn("P1: 0 open", english)
        self.assertLess(chinese.index("## 你会得到什么"), chinese.index("## 核心亮点"))
        self.assertIn("示意结果", chinese)
        self.assertIn("P1：0 个未关闭", chinese)

    def test_readmes_lead_with_bilingual_value_proposition_and_companions(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("Let AI divide the work; let evidence earn the release.", english)
        self.assertIn("Within clear boundaries", english)
        self.assertIn("https://github.com/boomkalakasha/icarus-ai-spring-scaffold", english)
        self.assertIn("https://github.com/boomkalakasha/icarus-open-source-governance-skill", english)
        self.assertIn("让 AI 自主分工，把交付交给证据验收。", chinese)
        self.assertIn("在明确授权边界内", chinese)
        self.assertIn("https://github.com/boomkalakasha/icarus-ai-spring-scaffold", chinese)
        self.assertIn("https://github.com/boomkalakasha/icarus-open-source-governance-skill", chinese)

    def test_readmes_explain_core_features_and_first_task_path(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        for source, markers in (
            (
                english,
                (
                    "## At a glance",
                    "Turn a fuzzy goal into an executable plan",
                    "Split a long task across agents",
                    "Know whether a change is really ready",
                    "1. Install or point your agent host",
                    "execution ledger",
                ),
            ),
            (
                chinese,
                (
                    "## 一眼看懂：它能帮你做什么",
                    "把模糊目标变成可执行计划",
                    "把长任务交给多个 Agent",
                    "判断改动是否真的可以放行",
                    "1. 让 Agent 宿主读取",
                    "执行台账",
                ),
            ),
        ):
            for marker in markers:
                self.assertIn(marker, source, marker)

    def test_readmes_offer_a_simple_install_and_link_the_public_operation_guide(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        guide = (ROOT / "docs" / "ai-operation-guide.md").read_text(encoding="utf-8")
        guide_zh = (ROOT / "docs" / "ai-operation-guide.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("git clone --depth 1", english)
        self.assertIn("git clone --depth 1", chinese)
        self.assertIn("docs/ai-operation-guide.md", english)
        self.assertIn("docs/ai-operation-guide.zh-CN.md", chinese)
        for source, markers in (
            (guide, ("## Scope before action", "## Evidence before claims", "## Parallel work without overload", "## Privacy and public collaboration", "optional companion documentation", "not auto-loaded")),
            (guide_zh, ("## 先定范围再行动", "## 先拿证据再下结论", "## 并行工作不能超载", "## 隐私与公开协作", "可选的配套文档", "不会自动加载")),
        ):
            for marker in markers:
                self.assertIn(marker, source, marker)

    def test_security_policy_does_not_invent_a_response_sla(self):
        security = (ROOT / "SECURITY.md").read_text(encoding="utf-8").lower()
        self.assertNotIn("seven days", security)
        self.assertIn("does not promise", security)

    def test_release_workflow_passes_a_real_semver_value_to_clean_release_packaging(self):
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(encoding="utf-8")
        self.assertIn('$version = $env:TAG_NAME.TrimStart("v")', workflow)
        self.assertIn("-Release -Version $version", workflow)
        self.assertIn(
            "icarus-open-source-governance-skill/actions/release-doc-sync@"
            "12999d05ccc73800b5d6c49b709e2f09e8303519",
            workflow,
        )
        self.assertIn("steps.release-metadata.outputs.version", workflow)
        self.assertIn("'^v\\d+\\.\\d+\\.\\d+$'", workflow)
        self.assertNotIn("alpha|beta|rc", workflow)
        self.assertIn('draft_url="$(' , workflow)
        self.assertIn('gh release create "${TAG_NAME}"', workflow)
        self.assertIn("gh api --paginate --slurp", workflow)
        self.assertIn('release.get("html_url") == os.environ["DRAFT_URL"]', workflow)
        self.assertIn('release.get("tag_name") != os.environ["EXPECTED_TAG"]', workflow)
        self.assertIn('release.get("assets", [])', workflow)
        self.assertIn("$GITHUB_STEP_SUMMARY", workflow)

    def test_changelog_records_the_v112_brand_fix(self):
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("## [1.2.1] - 2026-08-28", changelog)
        self.assertIn("theme-compatible BOOMKALAKASHA watermark", changelog)

    def test_skill_declares_the_v122_release_version(self):
        self.assertIn('version: "1.2.2"', (ROOT / "SKILL.md").read_text(encoding="utf-8"))

    def test_skill_exposes_tiered_model_and_context_drift_controls(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for marker in (
            "主动评估多 Agent 协作",
            "分层模型执行与长上下文防漂移",
            "references/multi-model-orchestration.md",
            "P0/P1",
        ):
            self.assertIn(marker, skill)
        for relative in (
            "references/git-branch-policy.md",
            "references/multi-model-orchestration.md",
            "templates/business-write-path-inventory.md",
            "templates/handoff.md",
            "templates/iteration-manifest.md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
