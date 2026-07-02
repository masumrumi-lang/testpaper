import csv
import re

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader):
        q = row['Question']
        # Check if the question has ii. or (ii) and see if there is a question mark or text after the last roman item
        # Let's match iii. or (iii) or ii. or (ii) if iii/iii doesn't exist
        match = re.search(r'(?:iii\.|(iii)|iii,)(.*)', q, re.IGNORECASE)
        if not match:
            match = re.search(r'(?:ii\.|(ii)|ii,)(.*)', q, re.IGNORECASE)
            
        if match:
            suffix = match.group(2).strip()
            # If suffix contains words that look like a follow-up question
            if any(kw in suffix.lower() for kw in ['which', 'what', 'correct', 'suggest', 'statement']):
                print(f"Row {idx+2}: {q}")
                print(f"  Suffix: {suffix}")
                print("-" * 50)
                
