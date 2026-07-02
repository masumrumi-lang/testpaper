import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx != -1:
    # Find closing brace of bus1
    brace = 1
    i = content.index('{', bus1_idx)
    start_i = i
    i += 1
    while i < len(content) and brace > 0:
        if content[i] == '{': brace += 1
        elif content[i] == '}': brace -= 1
        i += 1
    bus1_block = content[start_i:i]
    
    # search for chapter blocks
    for ch in ["9", "10", "11", "12"]:
        ch_key = f'"{ch}":'
        idx = bus1_block.find(ch_key)
        if idx != -1:
            print(f"Found {ch_key} inside bus1:")
            print(bus1_block[idx:idx+400])
        else:
            print(f"{ch_key} NOT found inside bus1")
else:
    print("'bus1' not found")
