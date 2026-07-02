import csv

CSV_PATH = 'BUS2_CH9_CH10_CQ - Sheet1.csv'

with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("CSV Header:", header)
    
    chapters = set()
    rows_count = 0
    for i, row in enumerate(reader):
        rows_count += 1
        if len(row) > 2:
            chapters.add(row[2].strip())
        if i < 5:
            print(f"Row {i+2}: Chapter='{row[2]}' Stem length={len(row[5]) if len(row) > 5 else 0}")
            
    print(f"Total rows: {rows_count}")
    print("Chapters found:", chapters)
