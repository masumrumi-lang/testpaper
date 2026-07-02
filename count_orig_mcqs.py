import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
start_brace = content.find('{', bus1_idx)

# Find the end of bus1
brace_cnt = 1
idx = start_brace + 1
while idx < len(content) and brace_cnt > 0:
    c = content[idx]
    if c == '{': brace_cnt += 1
    elif c == '}': brace_cnt -= 1
    idx += 1
bus1_block = content[start_brace:idx]

for ch in ['7', '8']:
    pattern = r'"' + ch + r'"\s*:\s*\{'
    match = re.search(pattern, bus1_block)
    if match:
        ch_start = match.start()
        # Find matching close brace
        ch_open = bus1_block.find('{', ch_start)
        brace = 1
        i = ch_open + 1
        while i < len(bus1_block) and brace > 0:
            if bus1_block[i] == '{': brace += 1
            elif bus1_block[i] == '}': brace -= 1
            i += 1
        ch_block = bus1_block[ch_start:i]
        
        # count occurrences of "id" under mcqData
        mcq_start = ch_block.find('"mcqData"')
        if mcq_start != -1:
            # Let's count how many "id": occur
            # but wait, let's be specific to avoid counting ids inside other places (there are no other keys in the original chapter object)
            mcq_ids = re.findall(r'"id"\s*:\s*\d+', ch_block[mcq_start:])
            print(f"Original Chapter {ch} has {len(mcq_ids)} MCQs")
