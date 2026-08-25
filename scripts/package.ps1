[CmdletBinding()]
param(
    [string]$Version,
    [switch]$Release
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$repositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if ([string]::IsNullOrWhiteSpace($Version)) {
    $match = Select-String -Path (Join-Path $repositoryRoot 'SKILL.md') -Pattern '^  version: "(.+)"$'
    $Version = $match.Matches.Groups[1].Value
}
if ($Version -notmatch '^\d+\.\d+\.\d+(?:-(?:alpha|beta|rc)\.\d+)?$') {
    throw "Version must be SemVer without the v prefix: $Version"
}

$distRoot = Join-Path $repositoryRoot 'dist'
$stageRoot = Join-Path $distRoot 'stage'
$skillName = 'ai-first-vibe-coding.skill'
$zipName = "ai-first-vibe-coding-$Version.zip"
$skillPath = Join-Path $distRoot $skillName
$zipPath = Join-Path $distRoot $zipName
$manifestPath = Join-Path $distRoot 'manifest.json'
$sumsPath = Join-Path $distRoot 'SHA256SUMS.txt'
$includes = @(
    'SKILL.md', 'README.md', 'README.zh-CN.md', 'CHANGELOG.md', 'LICENSE', 'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md', 'SECURITY.md', 'SUPPORT.md', 'compatibility.md', 'AGENTS.md',
    'assets', 'docs', 'references', 'templates', 'evals', 'scripts', '.github'
)

$isDirty = [bool](git -C $repositoryRoot status --porcelain)
if ($Release -and $isDirty) {
    throw 'Release packaging requires a clean working tree.'
}

New-Item -ItemType Directory -Force -Path $distRoot | Out-Null
if (Test-Path -LiteralPath $stageRoot) {
    Remove-Item -LiteralPath $stageRoot -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $stageRoot | Out-Null

foreach ($entry in $includes) {
    $source = Join-Path $repositoryRoot $entry
    if (-not (Test-Path -LiteralPath $source)) {
        throw "Required package source is missing: $entry"
    }
    if ((Get-Item -LiteralPath $source).PSIsContainer) {
        Get-ChildItem -LiteralPath $source -File -Recurse -Force |
            Where-Object { $_.FullName -notmatch '[\\/](__pycache__|dist|target)[\\/]' } |
            ForEach-Object {
                $relative = [IO.Path]::GetRelativePath($repositoryRoot, $_.FullName)
                $target = Join-Path $stageRoot $relative
                New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
                Copy-Item -LiteralPath $_.FullName -Destination $target -Force
            }
    } else {
        Copy-Item -LiteralPath $source -Destination (Join-Path $stageRoot $entry) -Force
    }
}

Remove-Item -LiteralPath $skillPath, $zipPath -Force -ErrorAction SilentlyContinue
$stageEntries = Get-ChildItem -LiteralPath $stageRoot -Force | ForEach-Object { $_.FullName }
Compress-Archive -Path $stageEntries -DestinationPath $skillPath -CompressionLevel Optimal
Compress-Archive -Path $stageEntries -DestinationPath $zipPath -CompressionLevel Optimal

$artifacts = @($zipPath, $skillPath) | ForEach-Object {
    [ordered]@{
        name = [IO.Path]::GetFileName($_)
        sha256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLowerInvariant()
    }
}
$stagedFiles = Get-ChildItem -LiteralPath $stageRoot -File -Recurse | Sort-Object FullName | ForEach-Object {
    [ordered]@{
        path = [IO.Path]::GetRelativePath($stageRoot, $_.FullName).Replace('\', '/')
        sha256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    }
}
$manifest = [ordered]@{
    schemaVersion = 1
    version = $Version
    sourceCommit = (git -C $repositoryRoot rev-parse HEAD).Trim()
    sourceTree = $(if ($isDirty) { 'dirty' } else { 'clean' })
    artifacts = $artifacts
    stagedFiles = $stagedFiles
}
$manifest | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $manifestPath -Encoding utf8NoBOM
($artifacts | ForEach-Object { "{0}  {1}" -f $_.sha256, $_.name }) | Set-Content -LiteralPath $sumsPath -Encoding utf8NoBOM

Write-Output "PASS: staged $($stagedFiles.Count) file(s) once"
Write-Output "PASS: created $zipName and $skillName from the same staged tree"
Write-Output 'PASS: wrote manifest.json and SHA256SUMS.txt'
