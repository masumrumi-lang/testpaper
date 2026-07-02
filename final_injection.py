import csv
import re

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_COMPLETE_FINAL.csv'

rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row_id, row in enumerate(reader, start=1):
        # Preservation Rule: Skip Ch 1 and 8
        if 'Chapter 1' in row['Chapter'] or 'Chapter 8' in row['Chapter']:
            rows.append(row)
            continue
            
        # 1. Data Injection for Row 536
        if row_id == 536:
            row['Question'] = (
                "Mr. Rahat is a furniture trader. He purchased furniture worth 3,00,000 TK from 'Star Furniture' "
                "at a 10% discount but mistakenly debited the Furniture Account. He took a table worth 3,000 TK "
                "for business use and sold half of the purchased goods for 1,50,000 TK, incurring 600 TK in transport costs. "
                "\n\nQ: What type of accounting error was committed in Mr. Rahat's books?"
            )
            row['Options'] = "a) Clerical Error\nb) Error of Principle\nc) Compensating Error\nd) Error of Omission"
            row['Answer'] = "b" # Purchased goods (inventory) debited to Asset (Furniture) is an Error of Principle
            row['Level'] = "Chattogram Board - 2022"
            row['HTML_Code'] = f'<div style="padding: 10px; border: 1px solid #ddd; background: #f9f9f9;">{row["Question"]}</div>'
            print("Injected data for Row 536.")

        # 2. Data Injection for Row 1351
        elif row_id == 1351:
            row['Question'] = (
                "Mr. Dalton purchased a machine for 60,000 TK. Transport and installation costs were 5,000 TK and "
                "3,000 TK respectively. At the end of the year, 10% depreciation was charged. Due to a defect, "
                "the machine was sold for 72,000 TK. \n\nQ: What is the amount of Revenue Expenditure?"
            )
            row['Options'] = "a) 6,000 TK\nb) 6,500 TK\nc) 6,800 TK\nd) 8,000 TK"
            # Revenue Expenditure is the Depreciation. 
            # Cost = 60,000 + 5,000 + 3,000 = 68,000. 10% of 68,000 = 6,800.
            row['Answer'] = "c"
            row['Level'] = "Barishal Board - 2019"
            row['HTML_Code'] = f'<div style="padding: 10px; border: 1px solid #ddd; background: #f9f9f9;">{row["Question"]}</div>'
            print("Injected data for Row 1351.")

        rows.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Final injection complete. Total rows: {len(rows)}")
print(f"Saved to {output_file}")
