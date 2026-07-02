import csv

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'
target_ids = range(855, 865)

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        if row_id in target_ids:
            print(f"--- Record {row_id} ---")
            print(f"Q: {row['Question']}")
            print(f"Opts: {row['Options']}")
            print(f"Ans: {row['Answer']}")
            print(f"Exp: {row['Explanation']}")
            print("-" * 20)
