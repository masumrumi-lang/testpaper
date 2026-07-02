import csv
import re
import os

def audit_finance_data():
    source_csv = 'finance1_mcq_IMPORT_READY.csv'
    
    errors = []
    boards = ['Dhaka', 'Rajshahi', 'Comilla', 'Chittagong', 'Sylhet', 'Barisal', 'Jessore', 'Dinajpur', 'Mymensingh', 'Madrasa', 'Technical']
    
    try:
        with open(source_csv, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            for i, row in enumerate(reader):
                row_num = i + 2
                if not row: continue
                
                # 1. Missing Values
                cols_to_check = {0: "Year", 3: "Board/College Name", 4: "Category", 10: "Answer", 11: "Explanation"}
                for col_idx, col_name in cols_to_check.items():
                    if len(row) <= col_idx or not row[col_idx].strip() or row[col_idx].strip() == '-':
                        errors.append(f"Row {row_num}: Missing {col_name}")
                
                if len(row) < 11:
                    errors.append(f"Row {row_num}: Incomplete row data")
                    continue

                year = row[0].strip()
                location = row[3].strip()
                category = row[4].strip()
                explanation = row[11].strip() if len(row) > 11 else ""
                options = row[6:10]

                # 2. Category Standardization
                if category.lower() not in ['board', 'college'] and category != '-':
                    errors.append(f"Row {row_num}: Invalid Category '{category}'")
                
                is_board_name = any(b.lower() in location.lower() for b in boards)
                if category.lower() == 'board' and not is_board_name:
                    if 'college' in location.lower() or 'school' in location.lower():
                        errors.append(f"Row {row_num}: Ambiguous Category - 'Board' assigned to '{location}'")
                elif category.lower() == 'college' and is_board_name:
                    errors.append(f"Row {row_num}: Ambiguous Category - 'College' assigned to '{location}'")

                # 3. Year Validation
                if year != '-':
                    if not re.match(r'^\d{4}$', year):
                        errors.append(f"Row {row_num}: Incorrect Year Format '{year}'")
                    else:
                        y_int = int(year)
                        if y_int < 2010 or y_int > 2026:
                            errors.append(f"Row {row_num}: Year out of range '{year}'")

                # 4. Calculation without numbers
                if "Calculation" in explanation:
                    has_digits = any(char.isdigit() for char in explanation)
                    has_formula = '<code>' in explanation or '$' in explanation or 'table' in explanation
                    if not (has_digits or has_formula):
                        errors.append(f"Row {row_num}: Explanation mentions 'Calculation' but has no numbers/formulas")
                
                # 5. Option Count
                if len(options) != 4:
                    errors.append(f"Row {row_num}: Incorrect Option Count ({len(options)})")
                else:
                    if any(not opt.strip() for opt in options):
                        errors.append(f"Row {row_num}: Missing Option Text")
                    clean_opts = [o.strip().lower() for o in options]
                    if len(set(clean_opts)) < 4:
                        errors.append(f"Row {row_num}: Duplicate Options found")

                # 6. Broken Characters
                broken_patterns = ['Ã', '©', 'â', '€', '™']
                content_all = "".join(row)
                for p in broken_patterns:
                    if p in content_all:
                        errors.append(f"Row {row_num}: Broken character '{p}' detected")
                        break

        # Output Results
        if not errors:
            print("Ready for Deployment")
        else:
            print("Error Summary:")
            for err in errors:
                print(err)
            print(f"\nTotal Errors Found: {len(errors)}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    audit_finance_data()
