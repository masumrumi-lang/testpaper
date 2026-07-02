import csv
import shutil
import os

path = 'BOM_1_CQ - Sheet1.csv'
backup = path + '.bak'

shutil.copy2(path, backup)
print(f'Backup created: {backup}')

seen = set()
deduped = []
removed_count = 0

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    deduped.append(header)
    for i, row in enumerate(reader, start=2):
        key = tuple(row)
        if key in seen:
            removed_count += 1
        else:
            seen.add(key)
            deduped.append(row)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(deduped)

print(f'Removed {removed_count} duplicate rows.')
print(f'New row count: {len(deduped) - 1}')
