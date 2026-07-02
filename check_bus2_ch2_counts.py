import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
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

ch_match = re.search(r'"2":\s*\{', bus2_block)
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

short_match = re.search(r'"shortCQData"\s*:\s*\[', ch_block)
if short_match:
    s_start = short_match.end() - 1
    s_bracket = 0
    s_end = -1
    for i in range(s_start, len(ch_block)):
        if ch_block[i] == '[': s_bracket += 1
        elif ch_block[i] == ']':
            s_bracket -= 1
            if s_bracket == 0:
                s_end = i+1
                break
    short_str = ch_block[s_start:s_end]
    print('shortCQ count:', len(re.findall(r'"id"', short_str)))
else:
    print('shortCQData not found')

full_match = re.search(r'"fullCQData"\s*:\s*\[', ch_block)
if full_match:
    f_start = full_match.end() - 1
    f_bracket = 0
    f_end = -1
    for i in range(f_start, len(ch_block)):
        if ch_block[i] == '[': f_bracket += 1
        elif ch_block[i] == ']':
            f_bracket -= 1
            if f_bracket == 0:
                f_end = i+1
                break
    full_str = ch_block[f_start:f_end]
    print('fullCQ count:', len(re.findall(r'"stem"', full_str)))
else:
    print('fullCQData not found')
