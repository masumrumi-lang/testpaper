<#
.SYNOPSIS
  extract_datajs.ps1 (v3)
  Reads data.js, converts JS object literal → JSON, writes per-subject files.

.NOTES
  v3 fixes:
  - String regex now also matches single-quoted JS strings ('...')
  - Template literals (`...`) replaced with a placeholder, then restored
  - Error preview now shows content around the actual parse error position
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ROOT       = 'c:\Users\BMTF\.antigravity\testpaper'
$DATA_FILE  = Join-Path $ROOT 'data.js'
$OUTPUT_DIR = Join-Path $ROOT 'static-data'
$LOG_FILE   = Join-Path $ROOT 'extract_datajs.log'

$log = [System.Collections.Generic.List[string]]::new()
function Log([string]$msg) { Write-Host $msg; $log.Add($msg) }
function Write-Log { $log | Set-Content -Path $LOG_FILE -Encoding UTF8 }

# ── STEP 1: Read ─────────────────────────────────────────────────────────────
Log ('=' * 65)
Log '  EXTRACT data.js → per-subject JSON  (PowerShell v3)'
Log ('=' * 65)

if (!(Test-Path $DATA_FILE)) {
    Log "[FATAL] data.js not found"; Write-Log; exit 1
}

Log "`n[STEP 1] Reading data.js ..."
$content = [System.IO.File]::ReadAllText($DATA_FILE, [System.Text.Encoding]::UTF8)
Log "         Size: $([math]::Round($content.Length/1MB,2)) MB ($($content.Length.ToString('N0')) chars)"

# ── STEP 2: Strip const declaration ──────────────────────────────────────────
Log "`n[STEP 2] Stripping const declaration ..."
$m0 = [regex]::Match($content, '(?s)const\s+testDatabase\s*=\s*(.*)')
if (!$m0.Success) { Log '[FATAL] Cannot find "const testDatabase ="'; Write-Log; exit 1 }
$jsObj = $m0.Groups[1].Value.TrimEnd()
if ($jsObj.EndsWith(';')) { $jsObj = $jsObj.Substring(0, $jsObj.Length - 1).TrimEnd() }
Log "         JS object: $([math]::Round($jsObj.Length/1MB,2)) MB"

# ── STEP 3: JS → JSON conversion ─────────────────────────────────────────────
# Strategy:
#   Pass 1: Walk through JS char-by-char tracking string state (double, single, template)
#           - double-quoted strings → passed through verbatim (already valid JSON strings)
#           - single-quoted strings → convert to double-quoted JSON strings
#           - template literals    → convert to double-quoted JSON strings (simple, no ${})
#           - in non-string code: quote bare identifier keys, strip trailing commas, undefined→null
Log "`n[STEP 3] Converting JS → JSON (v3 - full string-aware parser) ..."

$sb    = [System.Text.StringBuilder]::new($jsObj.Length + 300000)
$i     = 0
$len   = $jsObj.Length
$keyRe = [regex]::new('(?<!["\w])([a-zA-Z_$][a-zA-Z0-9_$]*)(\s*:)(?!:)')

# We process the JS in segments: collect non-string "code" segments and
# pass them through keyRe; emit string tokens verbatim (converted to double-quote).

$codeBuf = [System.Text.StringBuilder]::new(4096)

function FlushCode {
    if ($codeBuf.Length -eq 0) { return }
    $c = $codeBuf.ToString()
    $codeBuf.Clear() | Out-Null
    # Quote bare identifier keys
    $c = $keyRe.Replace($c, '"$1"$2')
    # undefined → null
    $c = $c -replace '\bundefined\b', 'null'
    [void]$sb.Append($c)
}

while ($i -lt $len) {
    $ch = $jsObj[$i]

    if ($ch -eq '"') {
        # Double-quoted string — pass through verbatim
        FlushCode
        $i++
        [void]$sb.Append('"')
        while ($i -lt $len) {
            $c = $jsObj[$i]
            if ($c -eq '\') {
                # escape sequence
                [void]$sb.Append($c)
                $i++
                if ($i -lt $len) { [void]$sb.Append($jsObj[$i]); $i++ }
            } elseif ($c -eq '"') {
                [void]$sb.Append('"')
                $i++
                break
            } else {
                [void]$sb.Append($c)
                $i++
            }
        }
    } elseif ($ch -eq "'") {
        # Single-quoted JS string → convert to double-quoted JSON string
        FlushCode
        $i++
        [void]$sb.Append('"')
        while ($i -lt $len) {
            $c = $jsObj[$i]
            if ($c -eq '\') {
                $i++
                if ($i -lt $len) {
                    $nc = $jsObj[$i]
                    if ($nc -eq "'") { [void]$sb.Append("'"); $i++ }    # \' → '
                    else { [void]$sb.Append('\'); [void]$sb.Append($nc); $i++ }
                }
            } elseif ($c -eq '"') {
                # bare double-quote inside single-quoted string → escape it
                [void]$sb.Append('\"')
                $i++
            } elseif ($c -eq "'") {
                [void]$sb.Append('"')
                $i++
                break
            } else {
                [void]$sb.Append($c)
                $i++
            }
        }
    } elseif ($ch -eq '`') {
        # Template literal — convert to double-quoted string (assume no ${} expressions)
        FlushCode
        $i++
        [void]$sb.Append('"')
        while ($i -lt $len) {
            $c = $jsObj[$i]
            if ($c -eq '\') {
                $i++
                if ($i -lt $len) { [void]$sb.Append('\'); [void]$sb.Append($jsObj[$i]); $i++ }
            } elseif ($c -eq '"') {
                [void]$sb.Append('\"'); $i++
            } elseif ($c -eq '`') {
                [void]$sb.Append('"'); $i++; break
            } else {
                [void]$sb.Append($c); $i++
            }
        }
    } elseif ($ch -eq '/' -and ($i + 1) -lt $len -and $jsObj[$i+1] -eq '/') {
        # Line comment — skip to end of line
        FlushCode
        while ($i -lt $len -and $jsObj[$i] -ne "`n") { $i++ }
    } elseif ($ch -eq '/' -and ($i + 1) -lt $len -and $jsObj[$i+1] -eq '*') {
        # Block comment — skip to */
        FlushCode
        $i += 2
        while ($i -lt ($len - 1) -and !($jsObj[$i] -eq '*' -and $jsObj[$i+1] -eq '/')) { $i++ }
        $i += 2
    } else {
        [void]$codeBuf.Append($ch)
        $i++
    }
}
FlushCode

$jsonStr = $sb.ToString()

# Strip trailing commas: ,} or ,]
$jsonStr = [regex]::Replace($jsonStr, ',(\s*[}\]])', '$1')

Log "         JSON string: $([math]::Round($jsonStr.Length/1MB,2)) MB"

# ── STEP 4: Parse JSON ────────────────────────────────────────────────────────
Log "`n[STEP 4] Parsing JSON ..."
try {
    $testDatabase = $jsonStr | ConvertFrom-Json -ErrorAction Stop
} catch {
    $errMsg = $_.ToString()
    Log "[FATAL] JSON parse error: $errMsg"

    # Try to find error position from message
    $posMatch = [regex]::Match($errMsg, 'position (\d+)')
    if ($posMatch.Success) {
        $pos = [int]$posMatch.Groups[1].Value
        $start = [math]::Max(0, $pos - 200)
        $end   = [math]::Min($jsonStr.Length, $pos + 200)
        $ctx   = $jsonStr.Substring($start, $end - $start)
        Log "         Context around pos $pos :"
        Log $ctx
        $ctx | Set-Content (Join-Path $ROOT 'extract_bad_json_ps.tmp') -Encoding UTF8
    } else {
        $jsonStr.Substring(0, [math]::Min(5000, $jsonStr.Length)) | Set-Content (Join-Path $ROOT 'extract_bad_json_ps.tmp') -Encoding UTF8
    }
    Write-Log; exit 1
}

$subjectIds = $testDatabase.PSObject.Properties.Name
Log "         Subjects found: $($subjectIds -join ', ')"
Log "         Total: $($subjectIds.Count) subjects"

# ── STEP 5: Create output directory ───────────────────────────────────────────
Log "`n[STEP 5] Creating static-data/ ..."
New-Item -ItemType Directory -Force -Path $OUTPUT_DIR | Out-Null
Log "         OK: $OUTPUT_DIR"

# ── STEP 6: Write per-subject JSON files ──────────────────────────────────────
Log "`n[STEP 6] Writing subject files ..."
$manifest      = [ordered]@{ subjects = [ordered]@{} }
$totalChapters = 0

foreach ($sid in $subjectIds) {
    $subjectData = $testDatabase.$sid
    $chapters    = @($subjectData.PSObject.Properties.Name)

    $subjectName = $sid
    foreach ($ch in $chapters) {
        $chObj = $subjectData.$ch
        if ($chObj -and $chObj.PSObject.Properties['subjectName']) {
            $subjectName = $chObj.subjectName; break
        }
    }

    $outPath     = Join-Path $OUTPUT_DIR "$sid.json"
    $subjectJson = $subjectData | ConvertTo-Json -Depth 100
    [System.IO.File]::WriteAllText($outPath, $subjectJson, [System.Text.Encoding]::UTF8)

    $sizeKB = [math]::Round((Get-Item $outPath).Length / 1KB, 0)
    Log "  ✓ $($sid.PadRight(8))  $($chapters.Count) ch  → $outPath ($sizeKB KB)"

    $manifest.subjects[$sid] = [ordered]@{
        name     = $subjectName
        chapters = $chapters
        file     = "static-data/$sid.json"
    }
    $totalChapters += @($chapters).Count
}

# ── STEP 7: Write manifest.json ───────────────────────────────────────────────
Log "`n[STEP 7] Writing manifest.json ..."
$manifestPath = Join-Path $OUTPUT_DIR 'manifest.json'
$manifest | ConvertTo-Json -Depth 10 | Set-Content -Path $manifestPath -Encoding UTF8
Log "         Subjects: $($subjectIds.Count),  Chapters: $totalChapters"

# ── STEP 8: Validate ──────────────────────────────────────────────────────────
Log "`n[STEP 8] Validating ..."
$errors = 0
foreach ($sid in $subjectIds) {
    $p = Join-Path $OUTPUT_DIR "$sid.json"
    try {
        $parsed = Get-Content $p -Raw | ConvertFrom-Json -ErrorAction Stop
        if (!$parsed) { Log "  ✗ $sid : empty"; $errors++ } else { Log "  ✓ $sid : OK" }
    } catch { Log "  ✗ $sid : $_"; $errors++ }
}

Log ("`n" + ('=' * 65))
Log "  DONE — Subjects: $($subjectIds.Count),  Chapters: $totalChapters"
Log "  Output : $OUTPUT_DIR\"
Log ('=' * 65)
Write-Log
exit $(if ($errors -gt 0) { 1 } else { 0 })
