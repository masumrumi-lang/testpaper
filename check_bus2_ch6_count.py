import json
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

ch_match = re.search(r'"6":\s*\{', bus2_block)
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
    json_str = "{" + ch_block + "}"
    try:
        data = json.loads(json_str)
        ch6 = data.get("6", {})
        short_cqs = ch6.get("shortCQData", [])
        print(f"Loaded {len(short_cqs)} short CQs for Chapter 6.")
    except Exception as e:
        print("JSON Error:", e)
else:
    print('Chapter 6 not found')
