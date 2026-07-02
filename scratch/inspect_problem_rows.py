import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')
csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for idx, row in enumerate(reader):
        row_num = idx + 2
        if row_num in range(580, 595) or row_num == 870:
            print(f"Row {row_num}:")
            for col_idx, val in enumerate(row):
                print(f"  Col {col_idx} ({header[col_idx] if col_idx < len(header) else 'OUT'}): {val}")
            print("-" * 50)
