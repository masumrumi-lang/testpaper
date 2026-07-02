import csv
import re

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    count = 0
    for idx, row in enumerate(reader):
        question = row['Question']
        # Let's search for roman numerals or multiple spaces or anything that needs cleanup
        if 'i.' in question or '(i)' in question or ' i ' in question or 'ii.' in question or '(ii)' in question:
            print(f"Row {idx+2} (Ch {row['Chapter']}):")
            print(f"  Q: {question}")
            count += 1
            if count >= 15:
                break
