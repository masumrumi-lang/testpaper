import csv
import re

with open('Finance1 MCQ Database.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i > 1000: break # Just check first 1000 rows
        content = " ".join(row)
        if "<table>" in content or "|" in content or "Year |" in content:
            print(f"Row {i} has potential table: {row[5][:100]}...")
