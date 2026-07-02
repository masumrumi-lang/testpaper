import csv

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    print("CSV Header:", header)
    
    # Let's count rows per chapter or show some rows
    rows_by_chapter = {}
    sample_rows = []
    
    for i, row in enumerate(reader):
        if i < 5:
            sample_rows.append(row)
        # Assuming chapter or similar column is there. Let's print the first row details
        if i == 0:
            for idx, val in enumerate(row):
                print(f"Col {idx}: {header[idx]} = {val[:50] if val else ''}")
        
        # Let's count by chapter
        # Find chapter column index. Let's find which column contains chapter name or number.
        # Often it is named "Chapter" or "chapter" or "Subject" or similar.
        # Let's print the entire first row to be sure.

print("\nSample Rows:")
for idx, row in enumerate(sample_rows):
    print(f"Row {idx+1}: {row}")
