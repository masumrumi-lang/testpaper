import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of keys matching "agr"
matches = re.findall(r'"(agr\w*)":', content)
print("Keys matching agr:", matches)

# Find top level keys
top_level_matches = []
for m in re.finditer(r'"(\w+)":\s*\{', content):
    start_pos = m.start()
    line_start = content.rfind('\n', 0, start_pos)
    prefix = content[line_start+1:start_pos]
    if len(prefix) == 4 and prefix.strip() == "":
        top_level_matches.append(m.group(1))
print("All top level keys:", top_level_matches)
