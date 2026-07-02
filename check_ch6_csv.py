import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

CSV_PATH = 'BUS2_CH6_CQ - Sheet1.csv'

with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print("Headers:")
    for idx, h in enumerate(headers):
        print(f"  {idx}: {h}")
        
    print("\nFirst row:")
    try:
        first_row = next(reader)
        for idx, val in enumerate(first_row):
            print(f"  {idx}: {val[:100]}...")
    except StopIteration:
        print("Empty file!")
