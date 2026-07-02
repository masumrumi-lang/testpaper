import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx == -1:
    print("bus1 not found")
    exit(1)

# Find the start brace of bus1
bus1_start_brace = content.find('{', bus1_idx)

# Let's find matching closing brace of bus1
brace_cnt = 1
idx = bus1_start_brace + 1
while idx < len(content) and brace_cnt > 0:
    c = content[idx]
    if c == '{': brace_cnt += 1
    elif c == '}': brace_cnt -= 1
    idx += 1
bus1_end = idx

bus1_block = content[bus1_start_brace:bus1_end]

def get_chapter_span(ch_key):
    # Find '"ch_key":' inside bus1_block
    pattern = r'"' + ch_key + r'"\s*:\s*\{'
    match = re.search(pattern, bus1_block)
    if not match:
        return None
    
    # We found the start of the chapter object
    ch_start_in_bus1 = match.start()
    # The actual open brace index in bus1_block
    ch_open_brace = bus1_block.find('{', ch_start_in_bus1)
    
    # Trace the matching closing brace
    brace_cnt = 1
    idx = ch_open_brace + 1
    while idx < len(bus1_block) and brace_cnt > 0:
        c = bus1_block[idx]
        if c == '{': brace_cnt += 1
        elif c == '}': brace_cnt -= 1
        idx += 1
    
    # The span in data.js is (bus1_start_brace + match.start(), bus1_start_brace + idx)
    span_start = bus1_start_brace + match.start()
    span_end = bus1_start_brace + idx
    return span_start, span_end

for ch in ['7', '8']:
    span = get_chapter_span(ch)
    if span:
        print(f"Chapter {ch} span: {span[0]} to {span[1]}")
        # Print the first 50 chars and last 50 chars of the span
        ch_text = content[span[0]:span[1]]
        print(f"Start: {repr(ch_text[:50])}")
        print(f"End: {repr(ch_text[-50:])}")
    else:
        print(f"Chapter {ch} not found")
