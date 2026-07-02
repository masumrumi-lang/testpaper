import csv
import re

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv' # Overwriting

# We will read into memory to avoid lock issues
rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row_id, row in enumerate(reader, start=1):
        # Safety Rule: Skip Ch 1 and 8
        if 'Chapter 1' in row['Chapter'] or 'Chapter 8' in row['Chapter']:
            rows.append(row)
            continue
            
        # Fix missing years for 'Board' and '-' entries
        if row['Level'].strip() in ['Board', '-', 'Board Standard']:
            row['Level'] = "All Board - 2018"
            
        # Double check for any missed 'Asset/Cash Book'
        for field in ['Question', 'Options', 'Explanation']:
            row[field] = row[field].replace('Asset/Cash Book', 'Account')
            row[field] = row[field].replace('Asset/C', 'Account')

        rows.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Final repair complete. Overwrote {input_file}")
