import csv

CSV_PATH = 'BUS1_CH9_10_11_12_CQ - Sheet1.csv'
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row_num, row in enumerate(reader, start=2):
        if row_num == 49:
            print(f"Row {row_num}:")
            print("Chapter:", row[2])
            print("Stem:", row[5])
            break
