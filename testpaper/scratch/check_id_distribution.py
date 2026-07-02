import re

with open("c:/Users/BMTF/.antigravity/testpaper/data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "mcqData" and extract its block, then find its numeric IDs.
# Also search for "fullCQData" and find its numeric IDs.
mcq_numeric_ids = []
cq_numeric_ids = []

# Let's find all blocks of mcqData: [ ... ]
for match in re.finditer(r'"mcqData"\s*:\s*\[', content):
    start_pos = match.end() - 1
    brace_count = 0
    end_pos = -1
    for idx in range(start_pos, len(content)):
        char = content[idx]
        if char == '[':
            brace_count += 1
        elif char == ']':
            brace_count -= 1
            if brace_count == 0:
                end_pos = idx + 1
                break
    if end_pos != -1:
        block = content[start_pos:end_pos]
        mcq_numeric_ids.extend([int(x) for x in re.findall(r'"id"\s*:\s*(\d+)', block)])

for match in re.finditer(r'"fullCQData"\s*:\s*\[', content):
    start_pos = match.end() - 1
    brace_count = 0
    end_pos = -1
    for idx in range(start_pos, len(content)):
        char = content[idx]
        if char == '[':
            brace_count += 1
        elif char == ']':
            brace_count -= 1
            if brace_count == 0:
                end_pos = idx + 1
                break
    if end_pos != -1:
        block = content[start_pos:end_pos]
        cq_numeric_ids.extend([int(x) for x in re.findall(r'"id"\s*:\s*(\d+)', block)])

print("Numeric IDs in mcqData:", len(mcq_numeric_ids), "max:", max(mcq_numeric_ids) if mcq_numeric_ids else None)
print("Numeric IDs in fullCQData:", len(cq_numeric_ids), "max:", max(cq_numeric_ids) if cq_numeric_ids else None)
