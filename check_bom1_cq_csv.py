import csv
import re

def check_csv(filepath):
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            if len(header) != 14:
                errors.append(f"Header has {len(header)} columns, expected 14.")
            
            row_count = 1
            for row in reader:
                row_count += 1
                if len(row) < 14:
                    errors.append(f"Row {row_count} has {len(row)} columns, expected at least 14.")
                    continue
                
                year, subject, chapter, level, category, stem, qa, qb, qc, qd, aa, ab, ac, ad = row[:14]
                
                # Check for empty mandatory fields
                if not stem.strip():
                    errors.append(f"Row {row_count}: Stem is empty.")
                if not qa.strip() or not qb.strip() or not qc.strip() or not qd.strip():
                    errors.append(f"Row {row_count}: One or more questions (A/B/C/D) are empty.")
                if not aa.strip() or not ab.strip() or not ac.strip() or not ad.strip():
                    errors.append(f"Row {row_count}: One or more answers (A/B/C/D) are empty.")
                
                # Check for unbalanced $ in stem or answers
                for field_name, field_val in [("Stem", stem), ("Ans A", aa), ("Ans B", ab), ("Ans C", ac), ("Ans D", ad)]:
                    if field_val.count('$') % 2 != 0:
                        errors.append(f"Row {row_count}: Unbalanced '$' in {field_name}.")
                
            print(f"Checked {row_count} rows.")
    except Exception as e:
        errors.append(f"File read error: {str(e)}")
    
    return errors

if __name__ == "__main__":
    filepath = r"c:\Users\BMTF\.antigravity\testpaper\Business Org & Mgmt 1 CQ - Sheet1.csv"
    errs = check_csv(filepath)
    if not errs:
        print("No errors found.")
    else:
        print(f"Found {len(errs)} potential errors:")
        for err in errs[:20]:
            print(f"- {err}")
        if len(errs) > 20:
            print(f"... and {len(errs)-20} more.")
