import csv
file_path = 'Agri1_Ch2_CQ - Sheet1.csv'
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        print(f"{i+1}: {row.get('Stem', '')[:100]}")
