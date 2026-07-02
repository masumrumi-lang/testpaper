import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
if bus2_idx != -1:
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
    print('Chapters in bus2:', re.findall(r'"(\d+)":\s*\{', bus2_block))
else:
    print('bus2 not found')
