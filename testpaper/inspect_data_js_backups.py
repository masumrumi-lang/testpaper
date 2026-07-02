import os
import re

backups = [f for f in os.listdir('.') if f.startswith('data.js.bak')]
print("Found backups:", backups)

for b in backups:
    try:
        with open(b, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"\n--- BACKUP {b} ---")
        bus2_idx = content.find('"bus2":')
        if bus2_idx == -1:
            print("  'bus2' not found")
            continue
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
        print(f"  Starts at {subj_start}, ends at {subj_end}")
        bus2_block = content[subj_start:subj_end]
        chapters = re.findall(r'"(\d+)":\s*\{', bus2_block)
        print("  Chapters inside bus2 block:", chapters)
        # Check if there is another "2" or other keys after bus2 ends
        after_block = content[subj_end:subj_end+500]
        print("  After block (first 150 chars):", repr(after_block[:150]))
    except Exception as e:
        print(f"  Error reading {b}: {e}")
