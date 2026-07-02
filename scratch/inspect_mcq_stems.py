import csv

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for idx, row in enumerate(reader):
        if idx in range(2, 10):
            print(f"Row {idx+2}:")
            print(f"  Q: {row[5]}")
            print(f"  A: {row[6]}, B: {row[7]}, C: {row[8]}, D: {row[9]}")
            print(f"  Ans: {row[10]}")
            print(f"  Explanation: {row[11][:100]}")
