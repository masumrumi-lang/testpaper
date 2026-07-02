import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract only the Chapter 6 block from bus2
bus2_idx = content.find('"bus2":')
ch6_idx = content.find('"6":', bus2_idx)

# Find the start of the object block after "6":
start_idx = content.find('{', ch6_idx)
bracket = 0
end_idx = -1
for i in range(start_idx, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            end_idx = i+1
            break

ch6_block = content[start_idx:end_idx]
print(f"Chapter 6 block length: {len(ch6_block)} characters")

# Let's count the number of main CQ IDs in this specific block
cq_ids = re.findall(r'"id"\s*:\s*"(\d+)"', ch6_block)
print(f"Number of CQs in Chapter 6: {len(cq_ids)}")
print(f"IDs: {cq_ids}")

# Verify structural parsing by wrapping in JSON
json_str = "{" + content[ch6_idx:end_idx] + "}"
try:
    data = json.loads(json_str)
    ch6_data = data["6"]
    print("\nParsed with JSON successfully!")
    print(f"Subject Name: {ch6_data.get('subjectName')}")
    print(f"Chapter Name: {ch6_data.get('chapterName')}")
    full_cqs = ch6_data.get('fullCQData', [])
    print(f"Total CQs in JSON: {len(full_cqs)}")
    if full_cqs:
        print("\nFirst CQ sample:")
        print(json.dumps(full_cqs[0], indent=2, ensure_ascii=False))
        print("\nLast CQ sample:")
        print(json.dumps(full_cqs[-1], indent=2, ensure_ascii=False))
except Exception as e:
    print("JSON Parsing Error:", e)
