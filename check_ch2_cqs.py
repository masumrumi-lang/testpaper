import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

def get_block(start):
    bracket = 0
    end = -1
    for i in range(start, len(content)):
        if content[i] == '{': bracket += 1
        elif content[i] == '}':
            bracket -= 1
            if bracket == 0:
                end = i+1
                break
    return content[start:end]

block1 = get_block(4782371)
block2 = get_block(5209330)

print("Block 1 starts at 4782371, ends at 4996782, length:", len(block1))
print("Block 2 starts at 5209330, ends at 5428824, length:", len(block2))

# Count CQs in fullCQData
cqs1 = re.findall(r'"id"\s*:\s*"([^"]+)"', block1)
cqs2 = re.findall(r'"id"\s*:\s*"([^"]+)"', block2)

print(f"Block 1 CQ count: {len(cqs1)}, first few: {cqs1[:5]}, last few: {cqs1[-5:]}")
print(f"Block 2 CQ count: {len(cqs2)}, first few: {cqs2[:5]}, last few: {cqs2[-5:]}")
