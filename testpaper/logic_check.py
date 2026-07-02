import csv
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'
errors = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        # 1. Answer check
        ans = row['Answer'].strip().lower()
        if ans not in ['a', 'b', 'c', 'd']:
            errors.append(f"Row {row_id}: Invalid answer '{ans}'")
        
        # 2. Empty fields check
        for field in ['Subject', 'Chapter', 'Question', 'Options']:
            if not row[field].strip():
                errors.append(f"Row {row_id}: Empty field '{field}'")
        
        # 3. HTML Code check for tables
        if '|' in row['Question'] and not row['HTML_Code'].strip():
            errors.append(f"Row {row_id}: Missing HTML_Code for table")

print(f"Total rows scanned: {row_id}")
print(f"Total logical errors: {len(errors)}")
for e in errors[:20]: print(e)
