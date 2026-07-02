import csv
import sys

# Set encoding to utf-8 for console output
sys.stdout.reconfigure(encoding='utf-8')

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_v3_EXPANDED.csv'
target_ids = [309, 403, 408, 490, 507, 536, 627, 1351]

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        if row_id in target_ids:
            print(f"--- Row {row_id} ---")
            print(f"Q: {row['Question']}")
            print(f"Opts: {row['Options']}")
            print(f"Ans: {row['Answer']}")
            print(f"Level: {row['Level']}")
            print(f"Exp: {row['Explanation']}")
            print("-" * 30)
