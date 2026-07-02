import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')
csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Bus2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    invalid_rows = []
    for idx, row in enumerate(reader):
        row_num = idx + 2
        ans = row['Correct Answer'].strip()
        ans_lower = ans.lower()
        if ans_lower not in ['a', 'b', 'c', 'd']:
            # Check if it's one of the option strings
            if ans_lower in ['option a', 'option b', 'option c', 'option d']:
                continue
            
            # Check if Option D is a/b/c/d (Shift Type A)
            opt_d = row['Option D'].strip().lower()
            if opt_d in ['a', 'b', 'c', 'd']:
                continue
                
            invalid_rows.append((row_num, ans, row['Option D'], row['Question'][:50]))

print(f"Total invalid rows not matched by general rules: {len(invalid_rows)}")
for r in invalid_rows[:50]:
    print(f"Row {r[0]}: Correct Answer='{r[1]}', Option D='{r[2]}', Q='{r[3]}'")
