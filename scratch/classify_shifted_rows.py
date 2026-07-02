import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')
csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for idx, row in enumerate(reader):
        row_num = idx + 2
        # If the row has less columns, skip
        if len(row) < 12:
            continue
            
        opt_d = row[9].strip()
        ans = row[10].strip()
        
        # Scenario 1: Option D contains a/b/c/d, and Correct Answer contains long text
        if opt_d.lower() in ['a', 'b', 'c', 'd'] and len(ans) > 1:
            print(f"Shift Type A on Row {row_num}:")
            print(f"  Question: {row[5][:80]}")
            print(f"  A: {row[6]}, B: {row[7]}, C: {row[8]}")
            print(f"  D (shifted): {row[9]}")
            print(f"  Ans (shifted): {row[10][:100]}")
            print("-" * 50)
            
        # Scenario 2: Correct Answer contains "Option A", "Option B", etc.
        elif any(ans.lower() == f"option {x}" for x in ['a', 'b', 'c', 'd']):
            pass # We already saw these in Row 906+
            
        # Let's count if there are other issues
