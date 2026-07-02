import difflib

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

# Let's compare them
# We can print some specific diffs or count the occurrences of differences
# Let's find first difference
lines1 = block1.splitlines()
lines2 = block2.splitlines()

print(f"Block 1 has {len(lines1)} lines, Block 2 has {len(lines2)} lines")

diff_count = 0
for idx, (l1, l2) in enumerate(zip(lines1, lines2)):
    if l1.strip() != l2.strip():
        print(f"Diff at line {idx+1}:")
        print(f"  B1: {repr(l1)}")
        print(f"  B2: {repr(l2)}")
        diff_count += 1
        if diff_count >= 10:
            break
