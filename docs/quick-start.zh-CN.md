# 60 秒安装与生命周期

`DOCUMENTED_ONLY`：以下是仓库与打包流程，不能证明某个 coding-agent 宿主已经发现、安装或执行了该 Skill。

## 安装

对于源码 checkout，将本仓库放入宿主配置的 Skill 目录，再让宿主重载说明。对 Codex，目标目录名是其已配置 skills 目录下的 `ai-first-vibe-coding`；复制前必须核对当前宿主配置。

对于打包候选，先验证并检查：

```powershell
python scripts/validate.py
pwsh -NoProfile -File scripts/package.ps1 -Version 1.2.2
Get-Content dist\SHA256SUMS.txt
```

只将已审核的 `.skill` 解压到宿主选定的位置。仓库能生成 `.skill` 不代表任意宿主都支持该归档，也不要覆盖其他 Skill。

## 升级

记录当前 commit 或 tag，验证新候选，比较 `dist/manifest.json` 与 `SHA256SUMS.txt`，再按宿主文档的升级方式替换 Skill。保留上一份已审核的源码/tag，直到人工确认宿主已载入新指令。

## 回滚

恢复已记录的上一 tag 或源码 checkout，重载宿主，并运行最小已知可用 trigger 或验证场景。仓库回滚不等于宿主已重载旧指令，应单独报告宿主观察结果。

## 卸载

优先使用宿主文档中的卸载动作。若没有该动作，确认精确安装目录并保留用户改动后，只删除该 Skill 目录。不要删除宽泛的 skills 根目录或其他 Skill。
