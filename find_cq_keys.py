import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

keys = set(re.findall(r'\"?([a-zA-Z0-9_]*CQData[a-zA-Z0-9_]*)\"?\s*:', content))
print(list(keys))
