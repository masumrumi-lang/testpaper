import csv
import re

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'

rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        # Fix corrupted words from over-expansion
        for field in ['Level', 'Question', 'Options', 'Explanation']:
            row[field] = row[field].replace('Cumillamerce', 'Commerce')
            row[field] = row[field].replace('Jashoresore', 'Jashore')
            row[field] = row[field].replace('Chattogramtogram', 'Chattogram')
            row[field] = row[field].replace('Rajshahishahi', 'Rajshahi')
            row[field] = row[field].replace('Dinajpurajpur', 'Dinajpur')
            row[field] = row[field].replace('Barishalishal', 'Barishal')
            row[field] = row[field].replace('Sylhetlhet', 'Sylhet')

        # Fix "College Board" -> "College"
        if 'College Board' in row['Level']:
            row['Level'] = row['Level'].replace('College Board', 'College')
        if 'Secondary Board' in row['Level']:
             row['Level'] = row['Level'].replace('Secondary Board', 'Secondary')
             
        rows.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Final cleanup complete.")
