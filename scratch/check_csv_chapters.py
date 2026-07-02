import csv
from collections import Counter

CSV_PATH = 'BUS1_CH9_10_11_12_CQ - Sheet1.csv'
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    chapters = []
    for row in reader:
        if len(row) > 2:
            chapters.append(row[2].strip())

print(Counter(chapters))
