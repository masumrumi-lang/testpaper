$data = Get-Content -Raw "data.js"

$part1 = Get-Content -Raw "acc1_ch1_part1.js"
$part1 = $part1.Substring($part1.IndexOf('[') + 1)
$part1 = $part1.Substring(0, $part1.LastIndexOf(']'))

$part2 = Get-Content -Raw "acc1_ch1_part2.js"
$part2 = $part2.Substring($part2.IndexOf('[') + 1)
$part2 = $part2.Substring(0, $part2.LastIndexOf(']'))

$part3 = Get-Content -Raw "acc1_ch1_part3.js"
$part3 = $part3.Substring($part3.IndexOf('[') + 1)
$part3 = $part3.Substring(0, $part3.LastIndexOf(']'))

$combined = $part1 + "," + $part2 + "," + $part3

$ictStartIndex = $data.IndexOf('    "ict": {')
if ($ictStartIndex -eq -1) {
    Write-Host "Error: Could not find ict block"
    exit 1
}

$ictBlock = $data.Substring($ictStartIndex)

$newContent = "const testDatabase = {`n" +
"    `"acc1`": {`n" +
"        `"1`": {`n" +
"            subjectName: `"Accounting 1st Paper`",`n" +
"            chapterName: `"Chapter 1 : Introduction to Accounting`",`n" +
"            mcqData: [" + $combined + "`n" +
"            ],`n" +
"            shortCQData: [],`n" +
"            fullCQData: []`n" +
"        }`n" +
"    },`n" +
$ictBlock

Set-Content -Path "data.js" -Value $newContent
Write-Host "Fixed data.js successfully."
