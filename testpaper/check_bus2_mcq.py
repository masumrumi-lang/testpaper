import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2"')
if bus2_idx != -1:
    start_brace = content.find('{', bus2_idx)
    # find all "mcqData" in bus2
    # Find matching closing brace for bus2
    brace_cnt = 1
    idx = start_brace + 1
    while idx < len(content) and brace_cnt > 0:
        c = content[idx]
        if c == '{': brace_cnt += 1
        elif c == '}': brace_cnt -= 1
        idx += 1
    bus2_block = content[start_brace:idx]
    
    # print all occurrences of "mcqData" in bus2_block and their surrounding content
    mcq_finds = [m.start() for m in re.finditer('"mcqData"', bus2_block)]
    for i, pos in enumerate(mcq_finds):
        print(f"Occurrence {i+1} at index {pos}:")
        print(bus2_block[pos:pos+100])
