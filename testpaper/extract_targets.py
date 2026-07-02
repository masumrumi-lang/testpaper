import csv
import sys

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'
target_ids = [4, 8, 16, 21, 25, 27, 30, 32, 38, 42, 43, 50, 51, 54, 56, 70, 84, 93, 102, 106, 125, 143, 147, 159, 163, 168, 173, 174, 185, 187, 189, 190, 192, 201, 202, 213, 219, 223, 233, 236, 245, 281, 303, 304, 306]

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        if row_id in target_ids:
            print(f"ID: {row_id} | Chapter: {row['Chapter']} | Level: {row['Level']} | Category: {row['Category']}")
            print(f"Q: {row['Question']}")
            print(f"Opts: {row['Options']}")
            print(f"Ans: {row['Answer']}")
            print("-" * 30)
