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
    
    for ch in ["9", "10", "11", "12"]:
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
            
            # Print keys inside this chapter block
            print(f"Chapter {ch} info:")
            # Find mcqData length, shortCQData length, fullCQData length or existence
            print("  chapterName:", re.search(r'"chapterName"\s*:\s*("[^"]*")', ch_block))
            print("  subjectName:", re.search(r'"subjectName"\s*:\s*("[^"]*")', ch_block))
            print("  shortCQData exists:", '"shortCQData"' in ch_block)
            print("  fullCQData exists:", '"fullCQData"' in ch_block)
            # Find number of MCQs inside mcqData
            mcq_start = ch_block.find('"mcqData"')
            if mcq_start != -1:
                # search for objects inside mcqData array
                arr_start = ch_block.index('[', mcq_start)
                # count matching brackets
                brac = 1
                k = arr_start + 1
                while k < len(ch_block) and brac > 0:
                    if ch_block[k] == '[': brac += 1
                    elif ch_block[k] == ']': brac -= 1
                    k += 1
                mcq_arr = ch_block[arr_start:k]
                mcq_count = len(re.findall(r'\{\s*"id"', mcq_arr))
                print(f"  mcqData count: {mcq_count}")
            
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
                fcq_count = len(re.findall(r'\{\s*"id"', fcq_arr))
                print(f"  fullCQData count: {fcq_count}")
            else:
                print("  fullCQData does not exist in this chapter block")
        else:
            print(f"Chapter {ch} not found")
else:
    print("bus1 not found")
