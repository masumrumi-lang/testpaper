$data = Get-Content -Raw "data.js"

$part1 = Get-Content -Raw "shortCQ_part1.js"
$part1 = $part1.Substring($part1.IndexOf('[') + 1)
$part1 = $part1.Substring(0, $part1.LastIndexOf(']'))

$part2 = Get-Content -Raw "shortCQ_part2.js"
$part2 = $part2.Substring($part2.IndexOf('[') + 1)
$part2 = $part2.Substring(0, $part2.LastIndexOf(']'))

$combined = "[$part1,$part2]"

$data = $data -replace '(?s)shortCQData:\s*\[\s*\],', "shortCQData: $combined,"

Set-Content -Path "data.js" -Value $data
Write-Host "Injected shortCQData successfully."
