import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')
csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Bus2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("CSV Header:", header)
    
    rows_by_chapter = {}
    sample_rows = []
    
    # Check invalid correct answer rows in Business 2nd Paper CSV
    invalid_rows = []
    total_rows = 0
    for i, row in enumerate(reader):
        total_rows += 1
        if i < 3:
            sample_rows.append(row)
        ch = row[2].strip()
        rows_by_chapter[ch] = rows_by_chapter.get(ch, 0) + 1
        
        ans = row[10].strip()
        ans_lower = ans.lower()
        if ans_lower not in ['a', 'b', 'c', 'd']:
            # Capture invalid correct answer rows
            opt_d = row[9].strip() if len(row) > 9 else ''
            invalid_rows.append((i+2, ans, opt_d, row[5][:50]))

print(f"\nTotal rows in CSV: {total_rows}")
print("Rows by Chapter:", dict(sorted(rows_by_chapter.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 999)))

print("\nSample Rows:")
for idx, r in enumerate(sample_rows):
    print(f"Row {idx+2}: {r}")

print(f"\nTotal invalid Correct Answer rows: {len(invalid_rows)}")
for r in invalid_rows[:20]:
    print(f"Row {r[0]}: Correct Answer='{r[1]}', Option D='{r[2]}', Q='{r[3]}'")
