import csv

rows_to_check = [1231, 1329, 1355, 1476, 1629]
source_csv = 'finance1_mcq_IMPORT_READY.csv'

with open(source_csv, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        row_num = i + 1
        if row_num in rows_to_check:
            print(f"Row {row_num}: {row[5]}")
            print(f"Options: {row[6:10]}")
            print("---")
