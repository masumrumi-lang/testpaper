import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2"')
if bus2_idx != -1:
    start_brace = content.find('{', bus2_idx)
    
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
            print(f"=== Bus2 Chapter {ch} ===")
            print(f"Length: {len(obj)}")
            mcq_idx = obj.find('"mcqData"')
            fcq_idx = obj.find('"fullCQData"')
            # Print first 200 chars and end of object
            print("First 200 chars:", repr(obj[:200]))
            if mcq_idx != -1:
                print("mcqData slice:", repr(obj[mcq_idx:mcq_idx+100]))
            if fcq_idx != -1:
                print("fullCQData slice:", repr(obj[fcq_idx:fcq_idx+100]))
