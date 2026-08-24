param(
    [string]$Version
)

$ErrorActionPreference = "Stop"
$repositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
if ([string]::IsNullOrWhiteSpace($Version)) {
    $match = Select-String -Path (Join-Path $repositoryRoot "SKILL.md") -Pattern '^  version: "(.+)"$'
    $Version = $match.Matches.Groups[1].Value
}
if ($Version -notmatch '^\d+\.\d+\.\d+(?:-(?:alpha|beta|rc)\.\d+)?$') {
    throw "Version must be SemVer without the v prefix: $Version"
}
$distRoot = Join-Path $repositoryRoot "dist"
$archiveName = "ai-first-vibe-coding-skill-v$Version.zip"
$archivePath = Join-Path $distRoot $archiveName
$checksumPath = "$archivePath.sha256"

New-Item -ItemType Directory -Force -Path $distRoot | Out-Null

foreach ($target in @($archivePath, $checksumPath)) {
    $resolvedParent = (Resolve-Path (Split-Path -Parent $target)).Path
    if ($resolvedParent -ne $distRoot) {
        throw "Refusing to replace a file outside dist: $target"
    }
    if (Test-Path -LiteralPath $target) {
        Remove-Item -LiteralPath $target -Force
    }
}

$items = @(
    (Join-Path $repositoryRoot "SKILL.md"),
    (Join-Path $repositoryRoot "LICENSE"),
    (Join-Path $repositoryRoot "README.md"),
    (Join-Path $repositoryRoot "README.zh-CN.md"),
    (Join-Path $repositoryRoot "compatibility.md"),
    (Join-Path $repositoryRoot "references"),
    (Join-Path $repositoryRoot "templates"),
    (Join-Path $repositoryRoot "evals")
)

Compress-Archive -Path $items -DestinationPath $archivePath -CompressionLevel Optimal
$hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $archivePath).Hash.ToLowerInvariant()
Set-Content -LiteralPath $checksumPath -Value "$hash  $archiveName" -Encoding utf8NoBOM
Write-Output $archivePath
Write-Output $checksumPath
