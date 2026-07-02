import re

with open("c:/Users/BMTF/.antigravity/testpaper/data.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'"fin2"\s*:\s*\{', content)
if match:
    start_pos = match.end() - 1
    brace_count = 0
    end_pos = -1
    for idx in range(start_pos, len(content)):
        char = content[idx]
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = idx + 1
                break
    if end_pos != -1:
        fin2_str = content[start_pos:end_pos]
        sub_keys = re.findall(r'"(\w+)"\s*:\s*\{', fin2_str)
        print("Sub keys under fin2:", sorted(sub_keys, key=lambda x: int(x) if x.isdigit() else 999))
