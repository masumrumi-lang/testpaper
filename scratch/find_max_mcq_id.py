import re

data_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'

with open(data_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all occurrences of "id": <number> inside MCQ blocks
# MCQs have: "id": <number>
# Or we can just find all "id": \d+
ids = [int(x) for x in re.findall(r'"id"\s*:\s*(\d+)', content)]

if ids:
    print(f"Max MCQ integer ID: {max(ids)}")
    print(f"Min MCQ integer ID: {min(ids)}")
    print(f"Total MCQ integer IDs found: {len(ids)}")
else:
    print("No integer IDs found.")
