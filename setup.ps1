# One-time setup after cloning: installs the HyperFrames skills, the Python packages, and checks the tools.
# Run from the repo root:  powershell -ExecutionPolicy Bypass -File setup.ps1

$root = $PSScriptRoot
Set-Location $root

function Test-Tool($name, $cmd, $hint) {
    try {
        $v = & $cmd[0] $cmd[1..($cmd.Length - 1)] 2>&1 | Select-Object -First 1
        Write-Host "ok    $name  $v"
        return $true
    } catch {
        Write-Host "NEED  $name  ($hint)"
        return $false
    }
}

$node = Test-Tool "node"   @("node", "--version")    "https://nodejs.org (LTS); HyperFrames runs via npx"
Test-Tool "ffmpeg" @("ffmpeg", "-version")   "winget install Gyan.FFmpeg" | Out-Null
$py = Test-Tool "python" @("python", "--version")  "winget install Python.Python.3.11"

# HyperFrames skills (hyperframes, hyperframes-cli, hyperframes-registry, media-use, figma, ...) into .claude/skills
if ($node) {
    if (Test-Path (Join-Path $root ".claude\skills\hyperframes")) {
        Write-Host "ok    HyperFrames skills already installed"
    } else {
        Write-Host "...   installing HyperFrames skills"
        npx --yes skills add heygen-com/hyperframes
    }
}

if ($py) {
    Write-Host "...   installing Python packages"
    python -m pip install -r (Join-Path $root "requirements.txt") --quiet
}

Write-Host ""
Write-Host "Next: copy memory\*.md into Claude's memory folder for this project (see README, 'Memory')."
