import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find subject-level keys (indented 8 spaces like:         "acc1": {)
matches = re.findall(r'^\s{4,10}"([a-z][a-z0-9_]*)"\s*:\s*\{', content, re.MULTILINE)

seen = set()
unique = []
for m in matches:
    if m not in seen:
        seen.add(m)
        unique.append(m)

print("Subject keys in testDatabase:")
for k in unique:
    print(f"  - {k}")
