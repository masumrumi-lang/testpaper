import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
ch1 = '\n'.join(lines[1048:3350])

# Find all id patterns
ids = re.findall(r'id:\s*"(\d+)"', ch1)
print('IDs found:', ids)
print('Max:', max(ids, key=int) if ids else 'none')

# Count types
board_count = ch1.count('type: "board"')
college_count = ch1.count('type: "college"')
print(f'Board CQs: {board_count}, College CQs: {college_count}')

# Show last 5 lines before the chapter boundary
for i in range(3345, 3355):
    print(f'Line {i+1}: {lines[i].rstrip()}')
