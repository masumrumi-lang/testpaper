$content = Get-Content "data.js" -Raw
$content = $content.TrimEnd()

# Add the closing brackets
$content += @"
]
        }
    }
};
"@

Set-Content -Path "data.js" -Value $content
Write-Host "Fixed data.js ending."
