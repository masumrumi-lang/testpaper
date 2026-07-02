$dataJSPath = "data.js"
$ictBlock = ""

try {
    $currentData = Get-Content -Path $dataJSPath -Raw -Encoding UTF8
    $idx = $currentData.IndexOf("`"ict`": {")
    if ($idx -eq -1) {
        $idx = $currentData.IndexOf("'ict': {")
    }
    
    if ($idx -ge 0) {
        $ictBlock = $currentData.Substring($idx)
        # Fix the junk at the end of ict block
        $endIdx = $ictBlock.IndexOf("};")
        if ($endIdx -ge 0) {
            $ictBlock = $ictBlock.Substring(0, $endIdx + 2)
        }
    }
} catch {}

function Get-ArrayContent($filename) {
    if (Test-Path $filename) {
        $content = Get-Content -Path $filename -Raw -Encoding UTF8
        $start = $content.IndexOf('[') + 1
        $end = $content.LastIndexOf(']')
        if ($start -gt 0 -and $end -gt $start) {
            return $content.Substring($start, $end - $start).Trim()
        }
    }
    return ""
}

$mcq1 = Get-ArrayContent "acc1_ch1_part1.js"
$mcq2 = Get-ArrayContent "acc1_ch1_part2.js"
$mcq3 = Get-ArrayContent "acc1_ch1_part3.js"
$mcqArr = @()
if ($mcq1) { $mcqArr += $mcq1 }
if ($mcq2) { $mcqArr += $mcq2 }
if ($mcq3) { $mcqArr += $mcq3 }
$mcqCombined = $mcqArr -join ",`n"

$mcq8_1 = Get-ArrayContent "acc1_ch8_mcq_part1.js"
$mcq8_board1 = Get-ArrayContent "acc1_ch8_mcq_board_part1.js"
$mcq8_board2 = Get-ArrayContent "acc1_ch8_mcq_board_part2.js"
$mcq8_board3 = Get-ArrayContent "acc1_ch8_mcq_board_part3.js"
$mcq8_board4 = Get-ArrayContent "acc1_ch8_mcq_board_part4.js"
$mcq8_board5 = Get-ArrayContent "acc1_ch8_mcq_board_part5.js"
$mcq8_board6 = Get-ArrayContent "acc1_ch8_mcq_board_part6.js"
$mcq8_board7 = Get-ArrayContent "acc1_ch8_mcq_board_part7.js"
$mcq8Arr = @()
if ($mcq8_1) { $mcq8Arr += $mcq8_1 }
if ($mcq8_board1) { $mcq8Arr += $mcq8_board1 }
if ($mcq8_board2) { $mcq8Arr += $mcq8_board2 }
if ($mcq8_board3) { $mcq8Arr += $mcq8_board3 }
if ($mcq8_board4) { $mcq8Arr += $mcq8_board4 }
if ($mcq8_board5) { $mcq8Arr += $mcq8_board5 }
if ($mcq8_board6) { $mcq8Arr += $mcq8_board6 }
if ($mcq8_board7) { $mcq8Arr += $mcq8_board7 }
$mcq8Combined = $mcq8Arr -join ",`n"


$acc1_ch2_mcq = Get-ArrayContent "acc1_ch2_mcq.js"
$acc1_ch3_mcq = Get-ArrayContent "acc1_ch3_mcq.js"
$acc1_ch4_mcq = Get-ArrayContent "acc1_ch4_mcq.js"
$acc1_ch5_mcq = Get-ArrayContent "acc1_ch5_mcq.js"
$acc1_ch6_mcq = Get-ArrayContent "acc1_ch6_mcq.js"
$acc1_ch7_mcq = Get-ArrayContent "acc1_ch7_mcq.js"
$acc1_ch9_mcq = Get-ArrayContent "acc1_ch9_mcq.js"
$acc1_ch10_mcq = Get-ArrayContent "acc1_ch10_mcq.js"

$fin1_ch1_mcq = Get-ArrayContent "fin1_ch1_mcq.js"
$fin1_ch2_mcq = Get-ArrayContent "fin1_ch2_mcq.js"
$fin1_ch3_mcq = Get-ArrayContent "fin1_ch3_mcq.js"
$fin1_ch4_mcq = Get-ArrayContent "fin1_ch4_mcq.js"
$fin1_ch5_mcq = Get-ArrayContent "fin1_ch5_mcq.js"
$fin1_ch6_mcq = Get-ArrayContent "fin1_ch6_mcq.js"
$fin1_ch7_mcq = Get-ArrayContent "fin1_ch7_mcq.js"
$fin1_ch8_mcq = Get-ArrayContent "fin1_ch8_mcq.js"
$fin1_ch9_mcq = Get-ArrayContent "fin1_ch9_mcq.js"

$short1 = Get-ArrayContent "shortCQ_part1.js"
$short2 = Get-ArrayContent "shortCQ_part2.js"
$shortArr = @()
if ($short1) { $shortArr += $short1 }
if ($short2) { $shortArr += $short2 }
$shortCombined = $shortArr -join ",`n"

$fullCQ_college1 = Get-ArrayContent "fullCQ_part1.js"
$fullCQ_college2 = Get-ArrayContent "fullCQ_part2.js"
$fullCQ_board1 = Get-ArrayContent "fullCQ_board_part1.js"

$fullArr = @()
if ($fullCQ_college1) { $fullArr += $fullCQ_college1 }
if ($fullCQ_college2) { $fullArr += $fullCQ_college2 }
if ($fullCQ_board1) { $fullArr += $fullCQ_board1 }
$fullCQCombined = $fullArr -join ",`n"

$fullCQ8_college1 = Get-ArrayContent "acc1_ch8_fullcq_college_part1.js"
$fullCQ8_college2 = Get-ArrayContent "acc1_ch8_fullcq_college_part2.js"
$fullCQ8_board1 = Get-ArrayContent "acc1_ch8_fullcq_board_part1.js"
$fullCQ8Arr = @()
if ($fullCQ8_college1) { $fullCQ8Arr += $fullCQ8_college1 }
if ($fullCQ8_college2) { $fullCQ8Arr += $fullCQ8_college2 }
if ($fullCQ8_board1) { $fullCQ8Arr += $fullCQ8_board1 }
$fullCQ8Combined = $fullCQ8Arr -join ",`n"

if ($ictBlock -eq "") {
    $ictBlock = @"
    "ict": {
        "1": {
            subjectName: "ICT",
            chapterName: "Chapter 1 : Information and Communication Technology",
            mcqData: [],
            shortCQData: [],
            fullCQData: []
        }
    }
};
"@
}

$newData = @"
const testDatabase = {
        "acc1": {
        "1": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 1 : Introduction to Accounting",
            mcqData: [
$mcqCombined
            ],
            shortCQData: [
$shortCombined
            ],
            fullCQData: [
$fullCQCombined
            ]
        },
        "2": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 2 : Books of Accounts",
            mcqData: [
$acc1_ch2_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "3": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 3 : Bank Reconciliation Statement",
            mcqData: [
$acc1_ch3_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "4": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 4 : Trial Balance",
            mcqData: [
$acc1_ch4_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "5": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 5 : Accounting Principles (Out of Short Syllabus)",
            mcqData: [
$acc1_ch5_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "6": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 6 : Accounting for Receivables (Out of Short Syllabus)",
            mcqData: [
$acc1_ch6_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "7": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 7 : Work Sheet",
            mcqData: [
$acc1_ch7_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "9": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 9 : Financial Statements",
            mcqData: [
$acc1_ch9_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "10": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 10 : Single Entry System (Out of Short Syllabus)",
            mcqData: [
$acc1_ch10_mcq
            ],
            shortCQData: [],
            fullCQData: []
        },
        "8": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 8 : Accounting for Tangible and Intangible Assets",
            mcqData: [
$mcq8Combined
            ],
            shortCQData: [],
            fullCQData: [
$fullCQ8Combined
            ]
        }
    },
    "fin1": {
        "1": { subjectName: "Finance 1st Paper", chapterName: "Chapter 1 : Introduction to Finance", mcqData: [$fin1_ch1_mcq], shortCQData: [], fullCQData: [] },
        "2": { subjectName: "Finance 1st Paper", chapterName: "Chapter 2 : Environment of Business Finance", mcqData: [$fin1_ch2_mcq], shortCQData: [], fullCQData: [] },
        "3": { subjectName: "Finance 1st Paper", chapterName: "Chapter 3 : Time Value of Money", mcqData: [$fin1_ch3_mcq], shortCQData: [], fullCQData: [] },
        "4": { subjectName: "Finance 1st Paper", chapterName: "Chapter 4 : Financial Analysis", mcqData: [$fin1_ch4_mcq], shortCQData: [], fullCQData: [] },
        "5": { subjectName: "Finance 1st Paper", chapterName: "Chapter 5 : Short-term Finance", mcqData: [$fin1_ch5_mcq], shortCQData: [], fullCQData: [] },
        "6": { subjectName: "Finance 1st Paper", chapterName: "Chapter 6 : Long-term Finance", mcqData: [$fin1_ch6_mcq], shortCQData: [], fullCQData: [] },
        "7": { subjectName: "Finance 1st Paper", chapterName: "Chapter 7 : Cost of Capital", mcqData: [$fin1_ch7_mcq], shortCQData: [], fullCQData: [] },
        "8": { subjectName: "Finance 1st Paper", chapterName: "Chapter 8 : Capital Budgeting", mcqData: [$fin1_ch8_mcq], shortCQData: [], fullCQData: [] },
        "9": { subjectName: "Finance 1st Paper", chapterName: "Chapter 9 : Risk and Return", mcqData: [$fin1_ch9_mcq], shortCQData: [], fullCQData: [] }
    },
$ictBlock
"@

[IO.File]::WriteAllText((Join-Path (Get-Location) "data.js"), $newData, [System.Text.Encoding]::UTF8)
Write-Host "data.js rebuilt successfully, syntax junk fixed."
