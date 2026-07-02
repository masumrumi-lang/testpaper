import os
import re

html_files = [
    'index.html',
    'subjects.html',
    'chapters-acc1.html',
    'chapters-acc2.html',
    'chapters-agr1.html',
    'chapters-agr2.html',
    'chapters-bus1.html',
    'chapters-bus2.html',
    'chapters-fin1.html',
    'chapters-fin2.html',
    'chapters-ict.html',
    'chapters-ict-fixed.html',
    'chapters.html',
    'mcq.html',
    'cq.html'
]

mobile_sidebar_html = """
<!-- Mobile Sidebar Overlay -->
<div id="mobileOverlay" class="fixed inset-0 z-40 hidden transition-opacity duration-300"></div>

<!-- Mobile Sidebar -->
<aside id="mobileSidebar" class="fixed inset-y-0 left-0 z-50 w-72 bg-white dark:bg-gray-900 border-r border-gray-100 dark:border-gray-800 shadow-2xl lg:hidden">
    <div class="flex flex-col h-full">
        <div class="flex items-center justify-between p-4 border-b border-gray-100 dark:border-gray-800">
            <div class="h-[28px] relative text-blue-600 font-bold text-xl poppins">etest<span class="text-sky-500">paper</span></div>
            <button id="closeMobileMenuBtn" class="p-2 rounded-xl text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
        </div>
        <nav class="flex-1 overflow-y-auto p-4 space-y-1">
            <p class="px-3 pb-2 text-[10px] font-bold text-gray-400 uppercase tracking-widest poppins">Menu</p>
            <a class="noto flex items-center gap-3 px-4 py-3 rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50" href="index.html">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M3.75 6A2.25 2.25 0 0 1 6 3.75h2.25A2.25 2.25 0 0 1 10.5 6v2.25a2.25 2.25 0 0 1-2.25 2.25H6a2.25 2.25 0 0 1-2.25-2.25V6ZM3.75 15.75A2.25 2.25 0 0 1 6 13.5h2.25a2.25 2.25 0 0 1 2.25 2.25V18a2.25 2.25 0 0 1-2.25 2.25H6A2.25 2.25 0 0 1 3.75 18v-2.25ZM13.5 6a2.25 2.25 0 0 1 2.25-2.25H18A2.25 2.25 0 0 1 20.25 6v2.25A2.25 2.25 0 0 1 18 10.5h-2.25a2.25 2.25 0 0 1-2.25-2.25V6ZM13.5 15.75a2.25 2.25 0 0 1 2.25-2.25H18a2.25 2.25 0 0 1 2.25 2.25V18A2.25 2.25 0 0 1 18 20.25h-2.25A2.25 2.25 0 0 1 13.5 18v-2.25Z"/></svg>
                <span class="noto">ড্যাশবোর্ড</span>
            </a>
            <a class="noto flex items-center gap-3 px-4 py-3 rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800/50" href="subjects.html">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25"/></svg>
                <span class="noto">অধ্যায় ভিত্তিক প্রস্তুতি</span>
            </a>
        </nav>
        <div class="p-4 border-t border-gray-100 dark:border-gray-800">
            <button onclick="toggleDarkMode()" class="w-full flex items-center justify-center gap-2 py-2.5 rounded-xl bg-gray-100 dark:bg-gray-800 text-sm font-medium">
                <span class="noto">থিম পরিবর্তন</span>
            </button>
        </div>
    </div>
</aside>
"""

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename} - not found")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Global CSS
    if 'global.css' not in content:
        content = content.replace('</head>', '<link rel="stylesheet" href="global.css"></head>')

    # 2. Global JS
    if 'global.js' not in content:
        content = content.replace('</body>', '<script src="global.js"></script></body>')

    # 3. Mobile Sidebar (if it has a Sidebar)
    if 'mobileSidebar' not in content and ('<!-- Sidebar -->' in content or '<aside' in content):
        if '<!-- Sidebar -->' in content:
            content = content.replace('<!-- Sidebar -->', mobile_sidebar_html + '\n<!-- Sidebar -->')
        else:
            content = re.sub(r'(<aside)', mobile_sidebar_html + r'\1', content, 1)

    # 4. Mobile Menu Button ID
    if 'mobileMenuBtn' not in content:
        # Find the button in the header that has lg:hidden (common pattern)
        content = re.sub(r'(<button [^>]*class="[^"]*lg:hidden[^"]*")', r'\1 id="mobileMenuBtn"', content)
        # fallback for mcq/cq which have a different button structure
        if 'mobileMenuBtn' not in content:
            content = re.sub(r'(<button [^>]*type="button"[^>]*class="[^"]*p-1.5 [^"]*")', r'\1 id="mobileMenuBtn"', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in html_files:
    update_file(f)

# Update login.html separately
if os.path.exists('login.html'):
    with open('login.html', 'r', encoding='utf-8') as f:
        content = f.read()
    if 'global.css' not in content:
        content = content.replace('</head>', '<link rel="stylesheet" href="global.css"></head>')
    if 'global.js' not in content:
        content = content.replace('</body>', '<script src="global.js"></script></body>')
    with open('login.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated login.html")
