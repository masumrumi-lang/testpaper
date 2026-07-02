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

    for chap in ['1', '2', '6']:
        ch_match = re.search(r'"' + chap + r'":\s*\{', bus2_block)
        if ch_match:
            ch_start = ch_match.start()
            ch_bracket = 0
            ch_end = -1
            for i in range(ch_start, len(bus2_block)):
                if bus2_block[i] == '{': ch_bracket += 1
                elif bus2_block[i] == '}':
                    ch_bracket -= 1
                    if ch_bracket == 0:
                        ch_end = i+1
                        break
            ch_block = bus2_block[ch_start:ch_end]
            print(f'Keys in bus2 chapter {chap}:', re.findall(r'(\w+Data)\s*:', ch_block))
        else:
            print(f'Chapter {chap} not found in bus2')
