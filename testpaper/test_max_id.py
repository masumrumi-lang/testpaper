import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

ids_with_quotes = re.findall(r'"id"\s*:\s*(\d+)', content)
ids_flexible = re.findall(r'"?id"?\s*:\s*(\d+)', content)

print("Ids with quotes count:", len(ids_with_quotes))
if ids_with_quotes:
    print("Max with quotes:", max(int(x) for x in ids_with_quotes))

print("Ids flexible count:", len(ids_flexible))
if ids_flexible:
    print("Max flexible:", max(int(x) for x in ids_flexible))
