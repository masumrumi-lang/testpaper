import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx == -1:
    print("bus1 not found in data.js")
else:
    # Find matching braces for bus1
    start_brace = content.find('{', bus1_idx)
    brace_cnt = 1
    idx = start_brace + 1
    while idx < len(content) and brace_cnt > 0:
        ch = content[idx]
        if ch == '{':
            brace_cnt += 1
        elif ch == '}':
            brace_cnt -= 1
        idx += 1
    bus1_block = content[start_brace:idx]
    
    # Let's see what chapter keys exist inside this block
    keys = re.findall(r'^\s*"(\d+)"\s*:', bus1_block, re.MULTILINE)
    print("Chapter keys in original bus1:", keys)
    
    # Let's inspect chapter 7 and 8 keys inside bus1 block
    for ch in ['7', '8']:
        ch_idx = bus1_block.find(f'"{ch}":')
        if ch_idx != -1:
            print(f"\n--- Chapter {ch} preview ---")
            print(bus1_block[ch_idx:ch_idx+400])
