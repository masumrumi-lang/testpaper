import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx != -1:
    start_brace = content.find('{', bus1_idx)
    # let's locate "7": and "8": inside bus1 block
    # Find matching closing brace for each
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
            print(f"=== Chapter {ch} fully ===")
            # Print structure, length, and check if fullCQData exists
            print(f"Length: {len(obj)} characters")
            # Let's search if fullCQData exists and what it looks like
            fullcq_idx = obj.find('"fullCQData"')
            shortcq_idx = obj.find('"shortCQData"')
            mcq_idx = obj.find('"mcqData"')
            print(f"mcqData idx: {mcq_idx}, shortCQData idx: {shortcq_idx}, fullCQData idx: {fullcq_idx}")
            # Print the text where fullCQData starts to the end of the object
            if fullcq_idx != -1:
                print("fullCQData preview:")
                print(obj[fullcq_idx:fullcq_idx+300])
            else:
                # print first 300 chars of the chapter object
                print("First 300 chars:")
                print(obj[:300])
