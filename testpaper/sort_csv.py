import csv
import re

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_COMPLETE_FINAL.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_SORTED.csv'

def get_chapter_num(chapter_str):
    match = re.search(r'Chapter\s*(\d+)', chapter_str, re.IGNORECASE)
    return int(match.group(1)) if match else 999

def get_year(level_str):
    match = re.search(r'(\d{4})', level_str)
    return int(match.group(1)) if match else 0

rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Sort by Chapter (Ascending) and then Year (Descending/Newest first)
# User said "Sort by Board Year", usually newest first is better, but I'll stick to ascending unless specified.
# Let's do Year Ascending for organization.
rows.sort(key=lambda x: (get_chapter_num(x['Chapter']), get_year(x['Level'])))

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Sorted {len(rows)} rows by Chapter and Year.")
print(f"Saved to {output_file}")
