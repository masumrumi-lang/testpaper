import re
import json

with open("c:/Users/BMTF/.antigravity/testpaper/data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's locate "acc2" object in data.js
# We can find where it starts and match the curly braces to parse it or see all the keys.
match = re.search(r'"acc2"\s*:\s*\{', content)
if match:
    start_pos = match.end() - 1  # include {
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
        acc2_str = content[start_pos:end_pos]
        # Let's find all keys inside this object
        # Since it is JS, it might be: "2": { ...
        # Let's find matches of '"(\w+)"\s*:\s*\{'
        sub_keys = re.findall(r'"(\w+)"\s*:\s*\{', acc2_str)
        print("Sub keys found under acc2:", sub_keys)
        
        # Let's inspect each key's subjectName and chapterName if they exist.
        for sk in sorted(sub_keys, key=lambda x: int(x) if x.isdigit() else 999):
            # Find the chapterName for this key
            sk_pattern = rf'"{sk}"\s*:\s*\{{.*?"chapterName"\s*:\s*"(.*?)"'
            sk_match = re.search(sk_pattern, acc2_str, re.DOTALL)
            if sk_match:
                print(f"Key '{sk}': {sk_match.group(1)}")
            else:
                print(f"Key '{sk}': Name not matched")
    else:
        print("Couldn't find matching closing brace for acc2")
else:
    print("acc2 key not found")
