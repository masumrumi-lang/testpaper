import csv

CSV_PATH = 'BUS1_CH9_10_11_12_CQ - Sheet1.csv'
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header columns:", header)
    for i in range(3):
        try:
            row = next(reader)
            print(f"Row {i+1}:")
            for j, val in enumerate(row):
                # Print index, header name, and truncated value
                col_name = header[j] if j < len(header) else f"Col{j}"
                print(f"  {j}. {col_name}: {val[:80]}...")
        except StopIteration:
            break
