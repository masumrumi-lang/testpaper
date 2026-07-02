import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
start_brace = content.find('{', bus1_idx)

def get_object_at_key(ch_key):
    key_pattern = f'"{ch_key}":'
    key_idx = content.find(key_pattern, start_brace)
    if key_idx == -1:
        return None
    obj_start = content.find('{', key_idx)
    brace_cnt = 1
    idx = obj_start + 1
    while idx < len(content) and brace_cnt > 0:
        c = content[idx]
        if c == '{': brace_cnt += 1
        elif c == '}': brace_cnt -= 1
        idx += 1
    return content[obj_start:idx]

for ch in ['7', '8']:
    obj = get_object_at_key(ch)
    if obj:
        print(f"=== Chapter {ch} tail ===")
        # Print the last 400 characters of the object
        print(obj[-400:])
