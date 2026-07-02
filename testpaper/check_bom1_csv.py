import csv
import re
import os

def check_csv(filepath):
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            if len(header) != 12:
                errors.append(f"Header has {len(header)} columns, expected 12.")
            
            row_count = 1
            for row in reader:
                row_count += 1
                if len(row) != 12:
                    errors.append(f"Row {row_count} has {len(row)} columns, expected 12.")
                    continue
                
                year, subject, chapter, level, category, question, opt_a, opt_b, opt_c, opt_d, ans, explanation = row
                
                # Check for empty mandatory fields
                if not question.strip():
                    errors.append(f"Row {row_count}: Question is empty.")
                if not opt_a.strip() or not opt_b.strip() or not opt_c.strip() or not opt_d.strip():
                    errors.append(f"Row {row_count}: One or more options are empty.")
                
                # Check correct answer
                if ans.strip().lower() not in ['a', 'b', 'c', 'd']:
                    errors.append(f"Row {row_count}: Invalid correct answer '{ans}'.")
                
                # Check for unbalanced $ in question or explanation
                for field_name, field_val in [("Question", question), ("Explanation", explanation)]:
                    if field_val.count('$') % 2 != 0:
                        errors.append(f"Row {row_count}: Unbalanced '$' in {field_name}.")
                
                # Check for common LaTeX typos in fields
                for field_val in [question, explanation, opt_a, opt_b, opt_c, opt_d]:
                    if 'imes' in field_val and '\\times' not in field_val:
                        if not re.search(r'[a-zA-Z]times', field_val):
                             if re.search(r'(^|\s)imes', field_val):
                                 errors.append(f"Row {row_count}: Potential LaTeX typo 'imes' found.")

            print(f"Checked {row_count} rows.")
    except Exception as e:
        errors.append(f"File read error: {str(e)}")
    
    return errors

if __name__ == "__main__":
    filepath = r"c:\Users\BMTF\.antigravity\testpaper\B&M 1st Paper mcq - Sheet1.csv"
    errs = check_csv(filepath)
    if not errs:
        print("No errors found.")
    else:
        print(f"Found {len(errs)} potential errors:")
        for err in errs[:20]: # Show first 20
            print(f"- {err}")
        if len(errs) > 20:
            print(f"... and {len(errs)-20} more.")
