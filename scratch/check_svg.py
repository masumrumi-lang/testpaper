import csv

CSV_PATH = 'BUS1_CH9_10_11_12_CQ - Sheet1.csv'
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    found_svg = False
    for row_num, row in enumerate(reader, start=2):
        for col_idx, val in enumerate(row):
            if '<svg' in val or 'svg' in val.lower():
                print(f"Row {row_num}, Column {col_idx} ({header[col_idx]}): contains SVG/svg")
                found_svg = True
    if not found_svg:
        print("No SVG/svg found in CSV")
