$utf8 = [System.Text.Encoding]::UTF8

$files = Get-ChildItem -Path . -Filter "chapters*.html"
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8)

    # The mangled text might exist
    $mangled1 = "à¦ªà§ à¦°à¦¶à§ à¦¨à§‡à¦° à¦§à¦°à¦¨ à¦¨à¦¿à¦°à§ à¦¬à¦¾à¦šà¦¨ à¦•à¦°à§ à¦¨"
    $mangled2 = "à¦¬à¦¹à§ à¦¨à¦¿à¦°à§ à¦¬à¦¾à¦šà¦¨à§€"
    $mangled3 = "à¦¸à§ƒà¦œà¦¨à¦¶à§€à¦²"
    
    $correct1 = "প্রশ্নের ধরন নির্বাচন করুন"
    $correct2 = "বহুনির্বাচনী"
    $correct3 = "সৃজনশীল"

    $updated = $content.Replace($mangled1, $correct1).Replace($mangled2, $correct2).Replace($mangled3, $correct3)
    
    if ($content -ne $updated) {
        [System.IO.File]::WriteAllText($file.FullName, $updated, $utf8)
        Write-Host "Fixed $($file.Name)"
    }
}
Write-Host "Done"
