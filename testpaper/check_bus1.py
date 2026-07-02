import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Find how many "7": entries exist inside bus1
bus1_start = c.find('"bus1"')
# Find the end of bus1 block
brace = 0
i = c.index('{', bus1_start)
start_i = i
brace = 1
i += 1
while i < len(c) and brace > 0:
    if c[i] == '{': brace += 1
    elif c[i] == '}': brace -= 1
    i += 1
bus1_end = i

bus1_block = c[start_i:bus1_end]
print(f"bus1 block length: {len(bus1_block)} chars")

# Count chapter keys inside bus1
ch_keys = re.findall(r'"(\d+)"\s*:', bus1_block[:500])
print(f"Chapter keys found in bus1 first 500 chars: {ch_keys}")

# Count all chapter keys
all_ch_keys = re.findall(r'^\s+"(\d+)"\s*:', bus1_block, re.MULTILINE)
print(f"All chapter-level keys: {all_ch_keys}")

# Count fullCQData occurrences
fcq_count = bus1_block.count('"fullCQData"')
print(f"fullCQData occurrences in bus1: {fcq_count}")

# Check for duplicate "7" entries  
ch7_count = len(re.findall(r'^\s+"7"\s*:', bus1_block, re.MULTILINE))
ch8_count = len(re.findall(r'^\s+"8"\s*:', bus1_block, re.MULTILINE))
print(f'Chapter "7" entries: {ch7_count}')
print(f'Chapter "8" entries: {ch8_count}')

# Count CQ ids in Ch7 section
ch7_start = bus1_block.find('"Chapter 7 : State Owned Business"')
if ch7_start >= 0:
    ch7_section = bus1_block[ch7_start:ch7_start+500000]
    ch7_ids = re.findall(r'"id"\s*:\s*"(\d+)"', ch7_section)
    print(f"Ch7 CQ ids: {ch7_ids[:10]}... total: {len(ch7_ids)}")
