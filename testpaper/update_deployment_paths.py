import os
import re

root_dir = r'c:\Users\BMTF\.antigravity\testpaper'
html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

replacements = [
    (r'href=["\']global\.css["\']', 'href="assets/css/global.css"'),
    (r'src=["\']global\.js["\']', 'src="assets/js/global.js"'),
    (r'src=["\']data\.js["\']', 'src="data/data.js"'),
    (r'src=["\']openrouter\.js["\']', 'src="assets/js/openrouter.js"')
]

for html_file in html_files:
    file_path = os.path.join(root_dir, html_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated paths in {html_file}")
    else:
        print(f"No path changes needed in {html_file}")
