import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/BMTF/.antigravity/testpaper/data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's locate the full acc2 object.
# To parse it cleanly, we can find the "acc2": { part, and then parse the JS object.
# Let's write a quick JS-like parser or use python regex to find the chapter IDs.
# E.g. find "acc2": { ...
# and then find all sub-keys like "2": {, "4": {, etc.
# Let's search for the pattern of chapter declarations under acc2:
# "acc2": {
#     "2": { ...
#     "4": { ...

acc2_match = re.search(r'"acc2"\s*:\s*\{', content)
if not acc2_match:
    print("Could not find acc2 key in data.js")
    sys.exit(1)

start_idx = acc2_match.end()
# Let's find matches of '"(\d+)"\s*:\s*\{' within the acc2 object.
# We will read until we hit the end of the acc2 object (which is the closing brace of acc2).
# Let's find brackets.
brace_count = 1
idx = start_idx
acc2_content = ""
while idx < len(content) and brace_count > 0:
    char = content[idx]
    if char == '{':
        brace_count += 1
    elif char == '}':
        brace_count -= 1
    acc2_content += char
    idx += 1

print("Length of acc2 content:", len(acc2_content))

# Now let's find all keys (chapters) in acc2_content
chapters = re.findall(r'"(\d+)"\s*:\s*\{', acc2_content)
print("Chapters found in acc2:", chapters)

# For each chapter, let's find the chapterName
for ch in chapters:
    ch_match = re.search(rf'"{ch}"\s*:\s*\{{.*?"chapterName"\s*:\s*"(.*?)",', acc2_content, re.DOTALL)
    if ch_match:
        print(f"Chapter {ch}: {ch_match.group(1)}")
    else:
        print(f"Chapter {ch}: Name not found with regex")
