<#
.SYNOPSIS
  Render HyperFrames projects one after another, level each to -14 LUFS, report duration and loudness.

.DESCRIPTION
  Takes pairs of <HyperFrames project dir> <output .mp4 path>. For each pair, in order:
    1. npx --yes hyperframes@<Version> render -o <out>_raw.mp4 -q <Quality>   (run inside the project dir)
    2. ffmpeg two-pass loudnorm I=-14 TP=-1.5 LRA=11, video stream copied, AAC 192k 48 kHz -> <out>.mp4
    3. deletes <out>_raw.mp4 (unless -KeepRaw)
    4. prints duration, integrated LUFS and true peak of <out>.mp4
  Renders run strictly one at a time: parallel renders starve the machine (~10 min per minute-long 1080p video).
  Run it as ONE background job and wait for it; don't start a second queue while one runs.
  -WhatIf prints the plan (paths, commands) and checks the inputs without rendering anything.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File _shared\tools\render_queue.ps1 -WhatIf `
    podcasts\x\episodes\E1\work\hyperframes\r1  podcasts\x\episodes\E1\output\final\X_E1_R1_9x16_v2.mp4 `
    podcasts\x\episodes\E1\work\hyperframes\r3  podcasts\x\episodes\E1\output\final\X_E1_R3_9x16_v2.mp4
#>
[CmdletBinding(SupportsShouldProcess = $true, PositionalBinding = $false)]
param(
  [string]$Version = '0.8.217',
  [string]$Quality = 'delivery',
  [switch]$KeepRaw,
  [switch]$Overwrite,
  [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
  [string[]]$Pairs
)

$ErrorActionPreference = 'Continue'

function Resolve-Full([string]$p) {
  $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($p)
}

# Two-pass loudnorm (measure, then linear correction): single-pass lands ~0.5 LU off and can
# overshoot the true-peak ceiling (a single-pass deliverable measured -13.6 LUFS / -1.1 dBTP).
# Falls back to single-pass if the measurement can't be parsed. Video stream is copied.
function Invoke-Level([string]$src, [string]$dst) {
  $target = 'I=-14:TP=-1.5:LRA=11'
  $m = (& ffmpeg -hide_banner -nostats -i $src -vn -af "loudnorm=${target}:print_format=json" -f null - 2>&1 | ForEach-Object { "$_" }) -join "`n"
  $af = "loudnorm=$target"
  $js = [regex]::Match($m, '\{[^{}]*"input_i"[^{}]*\}')
  if ($js.Success) {
    $d = $js.Value | ConvertFrom-Json
    if ($d.input_i -ne '-inf') {
      $af = "loudnorm=${target}:measured_I=$($d.input_i):measured_TP=$($d.input_tp):measured_LRA=$($d.input_lra):measured_thresh=$($d.input_thresh):offset=$($d.target_offset):linear=true"
    }
  }
  & ffmpeg -hide_banner -loglevel error -y -i $src -c:v copy -af $af -ar 48000 -c:a aac -b:a 192k -movflags +faststart $dst 2>&1 | ForEach-Object { "$_" }
  return ($LASTEXITCODE -eq 0)
}

if ($env:RENDER_QUEUE_LEVEL_ONLY) {
  # Test hook: level an existing file without rendering. RENDER_QUEUE_LEVEL_ONLY="<in.mp4>|<out.mp4>"
  $src, $dst = $env:RENDER_QUEUE_LEVEL_ONLY -split '\|'
  if (Invoke-Level $src $dst) { 'levelled' } else { 'level failed'; exit 1 }
  exit 0
}

if (-not $Pairs -or ($Pairs.Count % 2) -ne 0) {
  Write-Error 'Give pairs: <project dir> <output.mp4> [<project dir> <output.mp4> ...]'
  exit 2
}

# Validate everything before the first (long) render starts.
$jobs = @()
$problems = 0
for ($i = 0; $i -lt $Pairs.Count; $i += 2) {
  $proj = Resolve-Full $Pairs[$i]
  $fin = Resolve-Full $Pairs[$i + 1]
  if (-not (Test-Path (Join-Path $proj 'index.html'))) { Write-Warning "no index.html in $proj"; $problems++ }
  if ([IO.Path]::GetExtension($fin) -ne '.mp4') { Write-Warning "output must be .mp4: $fin"; $problems++ }
  if ((Test-Path $fin) -and -not $Overwrite) {
    Write-Warning "$fin exists: move it to output/archive (or bump v<N>), or pass -Overwrite"
    if (-not $WhatIfPreference) { $problems++ }
  }
  $raw = Join-Path ([IO.Path]::GetDirectoryName($fin)) ([IO.Path]::GetFileNameWithoutExtension($fin) + '_raw.mp4')
  $jobs += [pscustomobject]@{ Proj = $proj; Raw = $raw; Fin = $fin }
}
if ($problems) { Write-Error "$problems problem(s) in the queue; nothing rendered."; exit 2 }

$results = @()
$n = 0
foreach ($j in $jobs) {
  $n++
  $tag = "[$n/$($jobs.Count)] $([IO.Path]::GetFileName($j.Fin))"
  $renderCmd = "npx --yes hyperframes@$Version render -o `"$($j.Raw)`" -q $Quality   (in $($j.Proj))"
  $levelCmd = "ffmpeg (measure, then) -i `"$($j.Raw)`" -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11:measured_*:linear=true -ar 48000 -c:a aac -b:a 192k -movflags +faststart `"$($j.Fin)`""

  if (-not $PSCmdlet.ShouldProcess($j.Fin, 'render + loudnorm')) {
    # -WhatIf: show the plan only.
    "$tag"
    "   render: $renderCmd"
    "   level : $levelCmd"
    if ($KeepRaw) { "   keep  : $($j.Raw)" } else { "   delete: $($j.Raw)" }
    continue
  }

  $outDir = [IO.Path]::GetDirectoryName($j.Fin)
  if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Force $outDir | Out-Null }

  "$tag rendering... $(Get-Date -Format HH:mm:ss)"
  Push-Location $j.Proj
  & npx --yes "hyperframes@$Version" render -o $j.Raw -q $Quality 2>&1 | ForEach-Object { "$_" } | Select-Object -Last 3
  $rc = $LASTEXITCODE
  Pop-Location
  if ($rc -ne 0 -or -not (Test-Path $j.Raw)) {
    "$tag RENDER FAILED (exit $rc); skipping"
    $results += [pscustomobject]@{ File = $j.Fin; Status = 'render failed'; Duration = ''; LUFS = ''; TruePeak = '' }
    continue
  }

  $ok = Invoke-Level $j.Raw $j.Fin
  if (-not $ok -or -not (Test-Path $j.Fin)) {
    "$tag LEVELLING FAILED; raw kept at $($j.Raw)"
    $results += [pscustomobject]@{ File = $j.Fin; Status = 'loudnorm failed'; Duration = ''; LUFS = ''; TruePeak = '' }
    continue
  }
  if (-not $KeepRaw) { Remove-Item -LiteralPath $j.Raw -Force -Confirm:$false }

  $dur = (& ffprobe -v error -show_entries format=duration -of csv=p=0 $j.Fin)
  $meter = (& ffmpeg -hide_banner -nostats -i $j.Fin -af 'ebur128=peak=true' -f null - 2>&1 | ForEach-Object { "$_" })
  $I = ($meter | Select-String '^\s+I:\s+(-?[\d.]+) LUFS' | Select-Object -Last 1).Matches.Groups[1].Value
  $P = ($meter | Select-String '^\s+Peak:\s+(-?[\d.]+) dBFS' | Select-Object -Last 1).Matches.Groups[1].Value
  "$tag done: duration=$dur s  I=$I LUFS  TP=$P dBTP"
  $results += [pscustomobject]@{ File = $j.Fin; Status = 'ok'; Duration = $dur; LUFS = $I; TruePeak = $P }
}

if ($results.Count) {
  ''
  $results | Format-Table -AutoSize | Out-String -Width 300
}
