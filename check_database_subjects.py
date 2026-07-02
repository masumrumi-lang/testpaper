import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all keys at the root of testDatabase
# testDatabase is defined as "var testDatabase = {" or "const testDatabase = {" or similar
# Let's find the top-level keys (e.g. "acc1", "acc2", etc.)
matches = list(re.finditer(r'"(\w+)":\s*\{', content))
for m in matches:
    # check if this key is at the root level of testDatabase
    # To check if it's top-level, we can check its indentation
    # Let's see the characters before it
    start_pos = m.start()
    line_start = content.rfind('\n', 0, start_pos)
    prefix = content[line_start+1:start_pos]
    if len(prefix) == 4 and prefix.strip() == "":
        print(f"Top-level key: {m.group(1)} at index {m.start()} with prefix: {repr(prefix)}")
