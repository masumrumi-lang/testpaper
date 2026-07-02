import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx != -1:
    # Find the end of bus1 block
    brace = 1
    i = content.index('{', bus1_idx)
    start_i = i
    i += 1
    while i < len(content) and brace > 0:
        if content[i] == '{': brace += 1
        elif content[i] == '}': brace -= 1
        i += 1
    bus1_block = content[start_i:i]
    
    for ch in ["9", "10", "11", "12"]:
        ch_key = f'"{ch}":'
        idx = bus1_block.find(ch_key)
        if idx != -1:
            # find chapter block
            c_brace = 1
            j = bus1_block.index('{', idx)
            ch_start = j
            j += 1
            while j < len(bus1_block) and c_brace > 0:
                if bus1_block[j] == '{': c_brace += 1
                elif bus1_block[j] == '}': c_brace -= 1
                j += 1
            ch_block = bus1_block[ch_start:j]
            
            # find mcqData
            mcq_match = re.search(r'"mcqData"\s*:\s*\[', ch_block)
            if not mcq_match:
                mcq_match = re.search(r'mcqData\s*:\s*\[', ch_block)
            
            if mcq_match:
                mcq_start = mcq_match.end() - 1 # starts at '['
                # find matching bracket
                brac = 1
                k = mcq_start + 1
                while k < len(ch_block) and brac > 0:
                    if ch_block[k] == '[': brac += 1
                    elif ch_block[k] == ']': brac -= 1
                    k += 1
                mcq_raw_str = ch_block[mcq_start:k]
                print(f"Chapter {ch}: extracted mcqData raw string length = {len(mcq_raw_str)}")
                print(f"First 100 chars: {mcq_raw_str[:100]}")
                print(f"Last 100 chars: {mcq_raw_str[-100:]}")
            else:
                print(f"Chapter {ch}: mcqData not found")
        else:
            print(f"Chapter {ch}: key not found")
else:
    print("bus1 not found")
