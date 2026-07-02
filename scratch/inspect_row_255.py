import csv

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for idx, row in enumerate(reader):
        # Row number in 1-based indexing for reader (where header is 1) is idx + 2
        row_num = idx + 2
        if row_num in range(250, 260):
            print(f"Row {row_num}: length={len(row)}")
            for col_idx, val in enumerate(row):
                print(f"  Col {col_idx} ({header[col_idx] if col_idx < len(header) else 'OUT'}): {val[:100]}")
            print("-" * 50)
