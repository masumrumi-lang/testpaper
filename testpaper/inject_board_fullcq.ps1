$data = Get-Content -Raw "data.js"

$part1 = Get-Content -Raw "fullCQ_board_part1.js"
$part1 = $part1.Substring($part1.IndexOf('[') + 1)
$part1 = $part1.Substring(0, $part1.LastIndexOf(']')).Trim()

$part2 = Get-Content -Raw "fullCQ_board_part2.js"
$part2 = $part2.Substring($part2.IndexOf('[') + 1)
$part2 = $part2.Substring(0, $part2.LastIndexOf(']')).Trim()

$part3 = Get-Content -Raw "fullCQ_board_part3.js"
$part3 = $part3.Substring($part3.IndexOf('[') + 1)
$part3 = $part3.Substring(0, $part3.LastIndexOf(']')).Trim()

$part4 = Get-Content -Raw "fullCQ_board_part4.js"
$part4 = $part4.Substring($part4.IndexOf('[') + 1)
$part4 = $part4.Substring(0, $part4.LastIndexOf(']')).Trim()

$combined = $part1 + ",`n" + $part2 + ",`n" + $part3 + ",`n" + $part4

# Find '"acc1":', then 'chapterName: "Chapter 1', then 'fullCQ: ['
$idxSubject = $data.IndexOf("`"acc1`":")
if ($idxSubject -eq -1) { $idxSubject = $data.IndexOf("'acc1':") }

$idxChapter = $data.IndexOf('Chapter 1', $idxSubject)
$idxFullCQ = $data.IndexOf('fullCQ: [', $idxChapter)

if ($idxSubject -eq -1 -or $idxChapter -eq -1 -or $idxFullCQ -eq -1) {
    Write-Output "Failed to find injection point."
    exit 1
}

# Find the end of the fullCQ array by counting brackets
$count = 1
$pos = $idxFullCQ + 9
while ($count -gt 0 -and $pos -lt $data.Length) {
    if ($data[$pos] -eq '[') { $count++ }
    elseif ($data[$pos] -eq ']') { $count-- }
    $pos++
}

$injectPos = $pos - 1

# Get the content inside fullCQ to check if it's empty
$contentInside = $data.Substring($idxFullCQ + 9, $injectPos - ($idxFullCQ + 9)).Trim()
$comma = if ($contentInside.Length -gt 0) { ",`n" } else { "`n" }

$newData = $data.Substring(0, $injectPos) + $comma + $combined + "`n    " + $data.Substring($injectPos)

Set-Content -Path "data.js" -Value $newData -NoNewline
Write-Output "Injected successfully."
