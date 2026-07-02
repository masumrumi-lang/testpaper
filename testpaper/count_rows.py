import csv
with open('Finance1 MCQ Database.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(f"Total rows produced by csv.reader: {len(rows)}")
