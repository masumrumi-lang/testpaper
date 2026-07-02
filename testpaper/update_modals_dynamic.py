import os
import glob
import re

modal_html_new = """
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
    
    document.getElementById('mcqLink').href = `mcq.html?subject=${subjectId}&chapter=${chapterId}`;
    document.getElementById('cqLink').href = `cq.html?subject=${subjectId}&chapter=${chapterId}`;
    
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
"""

files = glob.glob("c:/Users/BMTF/.antigravity/testpaper/chapters-*.html")

for fpath in files:
    filename = os.path.basename(fpath)
    subject_id = filename.replace("chapters-", "").replace(".html", "")
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the old modal block if it exists
    if "<!-- Question Type Modal -->" in content:
        content = re.sub(r'<!-- Question Type Modal -->.*?</script>', modal_html_new, content, flags=re.DOTALL)
    else:
        # If it doesn't exist, append it before </body>
        content = content.replace("</body>", modal_html_new + "\n</body>")
        
    # Now, find all openQuestionModal('...') and replace them with openQuestionModal('...', 'subjectId', chapterId)
    # The trick is that we need to assign chapterId = 1, 2, 3 incrementally.
    # OR we can parse the chapter name from the HTML.
    
    # Let's find the subject name first
    match = re.search(r'<h2 class="[^"]*">([^—]+)\s*—', content)
    subject_name = "Subject"
    if match:
        subject_name = match.group(1).strip()
        
    # Some cards might have `href="mcq.html"`, some might have `onclick="...openQuestionModal('...')"`.
    # Let's unify them.
    
    # We will use regex to find each card, and its chapter number
    # A card starts with `<div class="transition-opacity duration-300 opacity-100 visible">`
    cards = re.split(r'<!-- Chapter (.*?) -->', content)
    
    new_content = cards[0]
    
    for i in range(1, len(cards), 2):
        chapter_identifier = cards[i]
        card_html = cards[i+1]
        
        # Extract chapter number, it might be '1', '2', or 'Extra'
        chapter_id = chapter_identifier.strip()
        
        # Replace href="mcq.html" with onclick
        card_html = re.sub(
            r'href="mcq\.html"',
            f'href="#" onclick="event.preventDefault(); openQuestionModal(\'{subject_name}\', \'{subject_id}\', \'{chapter_id}\');"',
            card_html
        )
        
        # Replace old openQuestionModal('Subject') with the new one
        card_html = re.sub(
            r'onclick="event\.preventDefault\(\);\s*openQuestionModal\(\'([^\']+)\'\);"([^>]*)>',
            f'onclick="event.preventDefault(); openQuestionModal(\'\\1\', \'{subject_id}\', \'{chapter_id}\');"\\2>',
            card_html
        )
        
        new_content += f'<!-- Chapter {chapter_identifier} -->' + card_html
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Updated {fpath}")

print("Done updating modals.")
