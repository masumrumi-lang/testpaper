import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
if bus2_idx == -1:
    print("Could not find 'bus2' in data.js")
    exit(1)

print("Found 'bus2' at index:", bus2_idx)

# Let's find where the bus2 block ends
subj_start = content.find('{', bus2_idx)
bracket = 0
subj_end = -1
for i in range(subj_start, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            subj_end = i+1
            break

bus2_block = content[subj_start:subj_end]
print("Length of bus2 block:", len(bus2_block))

# Find all keys under bus2
chapters = re.findall(r'"(\d+)":\s*\{', bus2_block)
print("Chapters:", chapters)

# For each chapter, find its closing brace in the main content
for chap in chapters:
    ch_match = re.search(r'"' + chap + r'":\s*\{', bus2_block)
    if ch_match:
        ch_start = subj_start + ch_match.start()
        ch_bracket = 0
        ch_end = -1
        for i in range(ch_start, len(content)):
            if content[i] == '{': ch_bracket += 1
            elif content[i] == '}':
                ch_bracket -= 1
                if ch_bracket == 0:
                    ch_end = i+1
                    break
        print(f"Chapter {chap} starts at {ch_start}, ends at {ch_end}")
        # Print the last 40 chars of Chapter block and first 40 chars after it
        print(f"  Last 40 chars of Chapter {chap}: {repr(content[ch_end-40:ch_end])}")
        print(f"  First 40 chars after Chapter {chap}: {repr(content[ch_end:ch_end+40])}")

# Let's print the end of the entire bus2 block (around subj_end)
print(f"bus2 block ends at {subj_end}")
print(f"  Last 60 chars of bus2 block: {repr(content[subj_end-60:subj_end])}")
print(f"  First 60 chars after bus2 block: {repr(content[subj_end:subj_end+60])}")
