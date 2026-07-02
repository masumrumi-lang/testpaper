import re
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# find top-level keys like "bus1": {
matches = re.findall(r'^\s*\"([a-z0-9_]+)\"\s*:\s*\{', content, re.MULTILINE)
print("Top level keys in data.js:", matches)
