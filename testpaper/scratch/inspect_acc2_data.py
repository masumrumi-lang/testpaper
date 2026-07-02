import re
import json

with open("c:/Users/BMTF/.antigravity/testpaper/data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find acc2 block
# It starts at: "acc2": {
# and ends when the brackets match.
# But we can also use regular expressions or simple parsing.
match = re.search(r'"acc2"\s*:\s*\{', content)
if match:
    start_pos = match.start()
    print("Found acc2 at position:", start_pos)
    # let's extract some text around it
    print(content[start_pos:start_pos+1000])
else:
    print("acc2 not found in data.js")
