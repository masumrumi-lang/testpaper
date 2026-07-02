import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
if bus1_idx != -1:
    print("Found 'bus1' at", bus1_idx)
    # let's print 1000 characters from there
    print(content[bus1_idx:bus1_idx+1000])
else:
    print("'bus1' not found")
