$modalHtmlNew = @"
<!-- Question Type Modal -->
<div id="questionTypeModal" class="fixed inset-0 z-50 hidden items-center justify-center">
  <!-- Backdrop -->
  <div class="fixed inset-0 bg-gray-900/40 backdrop-blur-sm transition-opacity" onclick="closeQuestionModal()"></div>
  
  <!-- Modal Content -->
  <div class="relative w-[340px] max-w-[90%] rounded-3xl bg-white dark:bg-gray-900 p-6 shadow-2xl transition-all transform scale-95 opacity-0 duration-200" id="modalContent">
    <button onclick="closeQuestionModal()" class="absolute right-4 top-4 rounded-full p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 dark:hover:bg-gray-800 dark:hover:text-gray-300 transition-colors">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>
    
    <div class="mb-5">
      <h3 class="noto text-lg font-semibold text-gray-900 dark:text-white">প্রশ্নের ধরন নির্বাচন করুন</h3>
      <p class="poppins text-sm text-gray-500 dark:text-gray-400 mt-0.5" id="modalSubjectName">Subject Name</p>
    </div>

    <div class="space-y-3">
      <!-- MCQ Button -->
      <a href="#" id="mcqLink" class="flex items-center gap-4 rounded-2xl border border-gray-100 dark:border-gray-800 p-4 transition-all hover:border-sky-400 hover:bg-sky-50/50 hover:shadow-md dark:hover:border-sky-500/50 dark:hover:bg-sky-900/20 group">
        <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-sky-50 text-sky-500 dark:bg-sky-500/10 group-hover:scale-110 transition-transform">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V18.75m-7.5-10.5h6.375c.621 0 1.125.504 1.125 1.125v9.375m-8.25-3l1.5 1.5 3-3.75" />
          </svg>
        </div>
        <div>
          <h4 class="poppins font-semibold text-gray-800 dark:text-gray-200">MCQ</h4>
          <p class="noto text-xs text-gray-500 dark:text-gray-400">বহুনির্বাচনী</p>
        </div>
      </a>

      <!-- CQ Button -->
      <a href="#" id="cqLink" class="flex items-center gap-4 rounded-2xl border border-gray-100 dark:border-gray-800 p-4 transition-all hover:border-amber-400 hover:bg-amber-50/50 hover:shadow-md dark:hover:border-amber-500/50 dark:hover:bg-amber-900/20 group">
        <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-amber-50 text-amber-500 dark:bg-amber-500/10 group-hover:scale-110 transition-transform">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
          </svg>
        </div>
        <div>
          <h4 class="poppins font-semibold text-gray-800 dark:text-gray-200">CQ</h4>
          <p class="noto text-xs text-gray-500 dark:text-gray-400">সৃজনশীল</p>
        </div>
      </a>
    </div>
  </div>
</div>

<script>
  function openQuestionModal(subjectName, subjectId, chapterId) {
    const modal = document.getElementById('questionTypeModal');
    const modalContent = document.getElementById('modalContent');
    if(subjectName) {
      document.getElementById('modalSubjectName').innerText = subjectName;
    }
    
    document.getElementById('mcqLink').href = 'mcq.html?subject=' + subjectId + '&chapter=' + chapterId;
    document.getElementById('cqLink').href = 'cq.html?subject=' + subjectId + '&chapter=' + chapterId;
    
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    
    // Animate in
    setTimeout(() => {
      modalContent.classList.remove('scale-95', 'opacity-0');
      modalContent.classList.add('scale-100', 'opacity-100');
    }, 10);
  }

  function closeQuestionModal() {
    const modal = document.getElementById('questionTypeModal');
    const modalContent = document.getElementById('modalContent');
    
    // Animate out
    modalContent.classList.remove('scale-100', 'opacity-100');
    modalContent.classList.add('scale-95', 'opacity-0');
    
    setTimeout(() => {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }, 200);
  }
</script>
"@

$files = Get-ChildItem -Path . -Filter "chapters*.html"
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    $subjectId = "ict"
    if ($file.Name -match 'chapters-(.*?)\.html') {
        $subjectId = $matches[1]
    }

    # Replace old modal block
    if ($content -match '<!-- Question Type Modal -->') {
        $content = $content -replace '(?s)<!-- Question Type Modal -->.*?</script>', $modalHtmlNew
    } else {
        $content = $content -replace '</body>', "$modalHtmlNew`n</body>"
    }

    # Extract subject name
    $subjectName = "Subject"
    if ($content -match '<h2[^>]*>([^—]+)\s*—') {
        $subjectName = $matches[1].Trim()
    }

    # Regex to match each chapter card block
    # It starts with <!-- Chapter <id> --> and ends at </a>\s*</div>
    $content = [regex]::Replace($content, '(?s)<!-- Chapter (.*?) -->.*?</a>\s*</div>', {
        param($match)
        $chapterNum = $match.Groups[1].Value
        $cardContent = $match.Value
        
        $chapterId = if ($chapterNum.Trim() -eq 'Extra') { 'extra' } else { $chapterNum.Trim() }

        # Replace href="mcq.html" or href="#"
        $cardContent = $cardContent -replace 'href="[^"]*"', 'href="#"'
        # Remove existing onclick if any
        $cardContent = $cardContent -replace 'onclick="[^"]*"', ''

        # Insert new onclick
        $cardContent = $cardContent -replace '(<a[^>]*?)>', "`$1 onclick=`"event.preventDefault(); openQuestionModal('$subjectName', '$subjectId', '$chapterId');`">"
        
        return $cardContent
    })

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
    Write-Host "Updated $($file.Name)"
}
Write-Host "All links and modals fixed!"
