import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
if bus2_idx == -1:
    print("Could not find 'bus2' in data.js")
    exit(1)

# Find the end of bus2 block
subj_start = content.find('{', bus2_idx)
bracket = 0
subj_end = -1
for i in range(subj_start, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            subj_end = i+1
            break

print(f"bus2 block starts at {subj_start}, ends at {subj_end}")
bus2_block = content[subj_start:subj_end]

# Let's search for any keys in bus2_block using a regex
# Keys are formatted like "1": {, "2": {, "3": {, etc. at 8-space indentation or 4-space indentation
matches = list(re.finditer(r'"(\d+)":\s*\{', bus2_block))
print(f"Found {len(matches)} chapter key matches inside bus2:")
for m in matches:
    rel_start = m.start()
    abs_start = subj_start + rel_start
    # Let's find the chapterName
    name_match = re.search(r'"chapterName"\s*:\s*"([^"]+)"', bus2_block[rel_start:])
    if name_match:
        name = name_match.group(1)
    else:
        name = "Unknown"
    print(f"  Key {m.group(1)} absolute start {abs_start}, ChapterName: {name}")
