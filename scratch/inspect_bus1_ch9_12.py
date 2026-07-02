import re
import json

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find testDatabase
match = re.search(r'(=)\s*(\{.*?\})\s*;?\s*$', content.strip(), re.DOTALL)
if not match:
    # Let's search for var database = or window.database = or testDatabase = or just find '{'
    match = re.search(r'(=)\s*(\{.*?\})', content, re.DOTALL)

if match:
    data = json.loads(match.group(2))
    bus1 = data.get("bus1", {})
    for ch in ["9", "10", "11", "12"]:
        if ch in bus1:
            ch_data = bus1[ch]
            print(f"Chapter {ch}:")
            print(f"  subjectName: {ch_data.get('subjectName')}")
            print(f"  chapterName: {ch_data.get('chapterName')}")
            print(f"  mcqData count: {len(ch_data.get('mcqData', []))}")
            print(f"  shortCQData count: {len(ch_data.get('shortCQData', []))}")
            print(f"  fullCQData count: {len(ch_data.get('fullCQData', []))}")
        else:
            print(f"Chapter {ch} not in bus1")
else:
    print("Could not parse data.js")
