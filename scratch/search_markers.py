import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# find all occurrences of comments containing "fin1" or "FIN1"
comments = re.findall(r'//.*', content)
fin1_comments = [c for c in comments if 'fin1' in c.lower() or 'cq' in c.lower()]
print(f"Total comments matching fin1/cq: {len(fin1_comments)}")
for c in fin1_comments[:50]:
    print(c)
