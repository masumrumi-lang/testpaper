import csv
import re

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'

rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        # Final cleanup of Level column
        level = row['Level']
        level = level.replace('Cumillailla', 'Cumilla')
        level = level.replace('Cumillamerce', 'Commerce')
        level = level.replace('Cumillam', 'Commerce') # Catch-all for Chattogram Cumillam Board
        level = level.replace('Chattogramtogram', 'Chattogram')
        
        # If it says "Board" but no year, add 2018
        if 'Board' in level and not re.search(r'\d{4}', level):
            level += " - 2018"
            
        row['Level'] = level
        rows.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Final Level normalization complete.")
