import re

try:
    with open('data.js.bak_bus2_ch3', 'r', encoding='utf-8') as f:
        content = f.read()
    print("Backup file read successfully.")
except Exception as e:
    print("Could not read backup file:", e)
    exit(1)

bus2_idx = content.find('"bus2":')
if bus2_idx != -1:
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
    print(f"Backup bus2 starts at {subj_start}, ends at {subj_end}")
    
    # Print chapters in backup bus2
    bus2_block = content[subj_start:subj_end]
    chapters = re.findall(r'"(\d+)":\s*\{', bus2_block)
    print("Backup chapters inside bus2:", chapters)
    
    # Print occurrences of "2": { in the whole backup file
    matches = list(re.finditer(r'"2"\s*:\s*\{', content))
    print(f"Found {len(matches)} occurrences of '\"2\": {{' in backup:")
    for m in matches:
        pos = m.start()
        line_start = content.rfind('\n', 0, pos)
        prefix = content[line_start+1:pos]
        name_match = re.search(r'"(subjectName|chapterName)"\s*:\s*"([^"]+)"', content[pos:])
        name = name_match.group(2) if name_match else "Unknown"
        print(f"  Pos: {pos}, Prefix: {repr(prefix)}, Name: {name}")
else:
    print("bus2 not found in backup")
