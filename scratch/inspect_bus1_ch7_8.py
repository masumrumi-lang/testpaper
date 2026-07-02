import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx != -1:
    brace = 1
    i = content.index('{', bus1_idx)
    start_i = i
    i += 1
    while i < len(content) and brace > 0:
        if content[i] == '{': brace += 1
        elif content[i] == '}': brace -= 1
        i += 1
    bus1_block = content[start_i:i]
    
    for ch in ["7", "8"]:
        ch_key = f'"{ch}":'
        idx = bus1_block.find(ch_key)
        if idx != -1:
            # find the end of this chapter's block
            c_brace = 1
            j = bus1_block.index('{', idx)
            ch_start = j
            j += 1
            while j < len(bus1_block) and c_brace > 0:
                if bus1_block[j] == '{': c_brace += 1
                elif bus1_block[j] == '}': c_brace -= 1
                j += 1
            ch_block = bus1_block[ch_start:j]
            
            print(f"Chapter {ch} info:")
            # Find shortCQData length
            scq_start = ch_block.find('"shortCQData"')
            if scq_start != -1:
                arr_start = ch_block.index('[', scq_start)
                brac = 1
                k = arr_start + 1
                while k < len(ch_block) and brac > 0:
                    if ch_block[k] == '[': brac += 1
                    elif ch_block[k] == ']': brac -= 1
                    k += 1
                scq_arr = ch_block[arr_start:k]
                # count elements
                scq_count = scq_arr.count('"id"')
                print(f"  shortCQData count: {scq_count}")
            else:
                print("  shortCQData does not exist")
            
            fcq_start = ch_block.find('"fullCQData"')
            if fcq_start != -1:
                arr_start = ch_block.index('[', fcq_start)
                brac = 1
                k = arr_start + 1
                while k < len(ch_block) and brac > 0:
                    if ch_block[k] == '[': brac += 1
                    elif ch_block[k] == ']': brac -= 1
                    k += 1
                fcq_arr = ch_block[arr_start:k]
                fcq_count = fcq_arr.count('"id"')
                print(f"  fullCQData count: {fcq_count}")
            else:
                print("  fullCQData does not exist")
        else:
            print(f"Chapter {ch} not found")
else:
    print("bus1 not found")
