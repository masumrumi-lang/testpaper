import csv

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    shifted_count = 0
    for idx, row in enumerate(reader):
        row_num = idx + 2
        ans = row['Correct Answer'].strip().lower()
        # If Correct Answer is not one of a, b, c, d
        if ans not in ['a', 'b', 'c', 'd']:
            shifted_count += 1
            print(f"Shifted Row {row_num}:")
            print(f"  Option D: {row['Option D']}")
            print(f"  Correct Answer: {row['Correct Answer'][:100]}")
            print(f"  Explanation: {row['Explanation'][:100]}")
            print("-" * 50)
            
    print(f"Total shifted rows found: {shifted_count}")
