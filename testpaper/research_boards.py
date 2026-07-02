import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')
input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'
target_ids = [701, 709, 721, 793, 818, 859, 893, 894, 1498]

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        if row_id in target_ids:
            print(f"Row {row_id}: {row['Question'][:60]}... | {row['Level']}")
