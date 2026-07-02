import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

print('=== Post-Injection Verification ===')
print(f'File size: {len(content):,} bytes')
print(f'Ends with }};: {content.rstrip().endswith("};")}\n')

bc = 0
bk = 0
for ch in content:
    if ch == '{': bc += 1
    elif ch == '}': bc -= 1
    elif ch == '[': bk += 1
    elif ch == ']': bk -= 1
print(f'Brace balance: {bc}')
print(f'Bracket balance: {bk}')

bus2_start = content.find('"bus2"')
bus2_section = content[bus2_start:]
ch2 = '"Chapter 2 : Principles of Management"' in bus2_section
ch3 = '"Chapter 3 : Planning"' in bus2_section
print(f'\nbus2 Chapter 2 present: {ch2}')
print(f'bus2 Chapter 3 present: {ch3}')

ch3_start = content.find('"Chapter 3 : Planning"')
ch3_block = content[ch3_start:ch3_start+500000]
id_matches = re.findall(r'"id"\s*:\s*"(\d+)"', ch3_block)
print(f'Chapter 3 CQ count: {len(id_matches)}')
if id_matches:
    print(f'ID range: {id_matches[0]} to {id_matches[-1]}')

print('\n=== ALL CHECKS PASSED ===' if bc == 0 and bk == 0 and ch2 and ch3 and len(id_matches) == 41 else '\n=== ISSUES DETECTED ===')
