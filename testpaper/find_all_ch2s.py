import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all occurrences of "2": { or similar
matches = list(re.finditer(r'"2"\s*:\s*\{', content))
print(f"Found {len(matches)} occurrences of '\"2\": {{' in data.js:")
for m in matches:
    pos = m.start()
    line_start = content.rfind('\n', 0, pos)
    prefix = content[line_start+1:pos]
    # find subject Name or chapterName inside this block
    name_match = re.search(r'"(subjectName|chapterName)"\s*:\s*"([^"]+)"', content[pos:])
    name = name_match.group(2) if name_match else "Unknown"
    print(f"  Pos: {pos}, Prefix: {repr(prefix)}, Name: {name}")
