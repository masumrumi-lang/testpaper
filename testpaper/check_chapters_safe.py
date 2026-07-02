import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
if bus2_idx != -1:
    print("Found bus2 at index:", bus2_idx)
    subj_start = content.find('{', bus2_idx)
    bracket = 0
    subj_end = -1
    for i in range(subj_start, len(content)):
        if content[i] == '{': bracket += 1
        elif content[i] == '}':
            bracket -= 1
            if bracket == 0:
                subj_end = i+1
                break
    bus2_block = content[subj_start:subj_end]
    
    chapters = re.findall(r'"(\d+)":\s*\{', bus2_block)
    print("Chapters list:", chapters)
    for chap in chapters:
        ch_match = re.search(r'"' + chap + r'":\s*\{', bus2_block)
        if ch_match:
            ch_start = ch_match.start()
            name_match = re.search(r'"chapterName"\s*:\s*"([^"]+)"', bus2_block[ch_start:])
            if name_match:
                print(f"Chapter {chap}: {name_match.group(1)}")
else:
    print("bus2 not found")
