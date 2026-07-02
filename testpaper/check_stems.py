import re
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('"acc1":')
ch2_idx = content.find('"2":', start_idx)
ch3_idx = content.find('"3": {', ch2_idx)
ch2_content = content[ch2_idx:ch3_idx]

stems = re.findall(r'stem:\s*"(.*?)"', ch2_content)
for i, stem in enumerate(stems):
    print(f'CQ {i+1} stem: {stem[:50]}...')
