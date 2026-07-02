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

ch_match = re.search(r'"1":\s*\{', bus2_block)
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

full_match = re.search(r'fullCQData"?\s*:\s*\[', ch_block)
if full_match:
    print('found fullCQData')
    full_start = full_match.end() - 1
    arr_count = 0
    full_end = -1
    for i in range(full_start, len(ch_block)):
        if ch_block[i] == '[': arr_count += 1
        elif ch_block[i] == ']':
            arr_count -= 1
            if arr_count == 0:
                full_end = i + 1
                break
    full_cq_str = ch_block[full_start:full_end]
    print('full cq str length:', len(full_cq_str))
    
    label_matches = re.findall(r'"label"\s*:\s*"(a|b)"', full_cq_str)
    print('found labels:', len(label_matches))
    
    # Try the complex regex
    complex_matches = re.finditer(r'\{\s*"label"\s*:\s*"(a|b)"\s*,\s*"text"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*,\s*"answer"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*\}', full_cq_str, re.DOTALL)
    print('complex regex matches:', len(list(complex_matches)))
else:
    print('fullCQData not found')
