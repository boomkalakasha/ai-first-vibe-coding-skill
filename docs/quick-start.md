# 60-second install and lifecycle

`DOCUMENTED_ONLY`: these are repository and package procedures. They do not prove that a particular coding-agent host has discovered, installed, or executed the Skill.

## Install

For a source checkout, place this repository in the skill directory configured by your host, then ask the host to reload its instructions. For Codex, the intended location is a directory named `ai-first-vibe-coding` under its configured skills directory; verify the live host configuration before copying files.

For a packaged candidate, validate and inspect it first:

```powershell
python scripts/validate.py
pwsh -NoProfile -File scripts/package.ps1 -Version 1.1.0
Get-Content dist\SHA256SUMS.txt
```

Extract the reviewed `.skill` only into the skill location selected by the host. Do not overwrite another Skill or assume a host supports `.skill` archives merely because this repository can build one.

## Upgrade

Record the current commit or tag, validate the incoming candidate, compare `dist/manifest.json` and `SHA256SUMS.txt`, then replace the host-selected Skill only through its documented upgrade method. Keep the previous reviewed source/tag available until the host has been manually verified.

## Rollback

Restore the previously recorded tag or source checkout, reload the host, and re-run the smallest known-good trigger or validation scenario. A repository rollback is not proof that a live host has reloaded the old instructions; report that host observation separately.

## Uninstall

Use the host's documented uninstall action. If it has no such action, remove only the exact skill directory chosen during installation after confirming its path and preserving any user-owned edits. Do not delete a broad skills root or another Skill as part of this procedure.
