import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx != -1:
    start_brace = content.find('{', bus1_idx)
    brace_cnt = 1
    idx = start_brace + 1
    while idx < len(content) and brace_cnt > 0:
        c = content[idx]
        if c == '{': brace_cnt += 1
        elif c == '}': brace_cnt -= 1
        idx += 1
    bus1_block = content[start_brace:idx]
    
    # print all occurrences of "mcqData" in bus1_block and their surrounding content
    mcq_finds = [m.start() for m in re.finditer('"mcqData"', bus1_block)]
    print(f"Total mcqData occurrences in bus1: {len(mcq_finds)}")
    for i, pos in enumerate(mcq_finds):
        slice_txt = bus1_block[pos:pos+100]
        # count number of items in mcqData if it is followed by list
        # let's see how long the slice is or if it is empty list
        is_empty = "[]" in slice_txt
        print(f"Chapter occurrence {i+1}: empty={is_empty}, slice={repr(slice_txt[:60])}")
