import re

with open("c:/Users/BMTF/.antigravity/testpaper/data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find all occurrences of "mcqData" and parse the block
# Let's find all instances of '"id": <number>' in data.js
# Or more specifically, within any "mcqData" array.
# Let's search using regex:
matches = re.findall(r'"id"\s*:\s*(\d+)', content)
if matches:
    ids = [int(m) for m in matches]
    print("Total MCQ IDs found in data.js:", len(ids))
    print("Max MCQ ID found in data.js:", max(ids))
    print("Min MCQ ID found in data.js:", min(ids))
else:
    print("No numeric IDs found.")
