import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')
ch_match = re.search(r'("1":\s*\{)', c[idx_bus2:])
ch_start = idx_bus2 + ch_match.start()

bracket_count = 0
ch_end = -1
for i in range(ch_start, len(c)):
    if c[i] == '{':
        bracket_count += 1
    elif c[i] == '}':
        bracket_count -= 1
        if bracket_count == 0:
            ch_end = i + 1
            break

ch_content = c[ch_start:ch_end]

array_start = ch_content.find('"fullCQData":')
array_start = ch_content.find('[', array_start)
array_bracket_count = 0
array_end = -1
for i in range(array_start, len(ch_content)):
    if ch_content[i] == '[':
        array_bracket_count += 1
    elif ch_content[i] == ']':
        array_bracket_count -= 1
        if array_bracket_count == 0:
            array_end = i + 1
            break

cqs = json.loads(ch_content[array_start:array_end])
print(f"Max ID in Chapter 1: {max(int(cq['id']) for cq in cqs if cq['id'].isdigit())}")
print(f"Total CQs in Chapter 1: {len(cqs)}")
