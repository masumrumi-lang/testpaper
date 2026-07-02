import csv
import json

CSV_PATH = '../Acc2_ch1_cq - Sheet1.csv'

with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print("Fields:", reader.fieldnames)
    rows = list(reader)
    print("Total rows:", len(rows))
    for i, row in enumerate(rows[:5]):
        print(f"\n--- Row {i+1} ---")
        print("Stem:", repr(row.get('Stem'))[:300])
        print("Ans_A:", repr(row.get('Ans_A'))[:100])
        print("Ans_B:", repr(row.get('Ans_B'))[:100])
        print("Ans_C:", repr(row.get('Ans_C'))[:100])
