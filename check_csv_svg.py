import csv
import re

CSV_PATH = 'BUS_2_CH4_CQ - Sheet1.csv'

with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for row_idx, row in enumerate(reader, start=2):
        stem = row[5]
        if "<svg" in stem:
            print(f"Row {row_idx} contains SVG!")
            # Check for double newlines in stem
            double_newlines = re.findall(r'\n\s*\n', stem)
            print(f"  Double newlines count: {len(double_newlines)}")
            
            # Print first 200 chars and last 200 chars of stem
            print("  First 150 chars of stem:")
            print(repr(stem[:150]))
            print("  Last 150 chars of stem:")
            print(repr(stem[-150:]))
