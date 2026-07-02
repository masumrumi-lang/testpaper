import json

data_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'

with open(data_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find "fin1":
start_idx = content.find('"fin1":')
if start_idx == -1:
    print("Could not find 'fin1' block")
    exit(1)

brace_count = 0
found_first_brace = False
end_idx = -1
for i in range(start_idx, len(content)):
    char = content[i]
    if char == '{':
        brace_count += 1
        found_first_brace = True
    elif char == '}':
        brace_count -= 1
        if found_first_brace and brace_count == 0:
            end_idx = i + 1
            break

fin1_block_str = content[start_idx:end_idx]
json_str = fin1_block_str.split(':', 1)[1].strip()
fin1_data = json.loads(json_str)

print("Chapter MCQs in data.js for fin1:")
for ch in sorted(fin1_data.keys(), key=int):
    ch_data = fin1_data[ch]
    mcq_data = ch_data.get('mcqData', [])
    print(f"Chapter {ch}: mcqData length = {len(mcq_data)}")
    if mcq_data:
        print(f"  Sample MCQ: {json.dumps(mcq_data[0], ensure_ascii=False, indent=2)}")
        break
