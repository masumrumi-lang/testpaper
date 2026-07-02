import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find top-level subject keys in testDatabase
# Look for patterns like  "acc1": {  or  "fin1": {
pattern = re.compile(r'^\s{4,10}"([a-zA-Z0-9_]+)"\s*:\s*\{', re.MULTILINE)
keys = []
for m in pattern.finditer(content):
    key = m.group(1)
    # Only add if it looks like a subject key (not a chapter number)
    if not key.isdigit():
        if key not in keys:
            keys.append(key)
            print(f"  Found key: '{key}' at line offset {content[:m.start()].count(chr(10))+1}")

print(f"\nAll top-level subject keys: {keys}")
print(f"Total: {len(keys)}")
print(f"\n'bus1' present: {'bus1' in keys}")
print(f"'bus2' present: {'bus2' in keys}")
