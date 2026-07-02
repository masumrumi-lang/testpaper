import re

with open("data.js", "r", encoding="utf-8") as f:
    content = f.read(5000) # Check first 5000 chars

# Look for patterns like "key": {
keys = re.findall(r'"([^"]+)":\s*\{', content)
print("Keys found in first 5000 chars:", keys)

# Check middle/end
with open("data.js", "r", encoding="utf-8") as f:
    f.seek(100000)
    content = f.read(5000)
keys = re.findall(r'"([^"]+)":\s*\{', content)
print("Keys found around 100k:", keys)
