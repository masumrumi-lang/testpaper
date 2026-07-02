import csv
import re
import collections
import os

FILE_PATH = r'c:\Users\BMTF\OneDrive\Documents\Rumi\testpaper\BOM_1_CQ - Sheet1.csv'

def validate_bom_cq(path):
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return

    errors = []
    rows = []
    
    print(f"--- Auditing: {os.path.basename(path)} ---")

    try:
        with open(path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
            except StopIteration:
                print("Error: CSV file is empty.")
                return

            expected_cols = len(header)
            print(f"Expected columns: {expected_cols}")

            for i, row in enumerate(reader, start=2):
                # 1. Structural Check: Column Count
                if len(row) != expected_cols:
                    errors.append({
                        "row": i,
                        "type": "Malformed Row",
                        "desc": f"Found {len(row)} columns instead of {expected_cols}."
                    })
                rows.append((i, row))

    except UnicodeDecodeError:
        print("Critical Error: File encoding is not UTF-8.")
        return

    # Map headers to indices
    col_map = {name.strip(): idx for idx, name in enumerate(header)}
    
    # 2. Duplicate Detection
    seen_stems = collections.defaultdict(list)
    
    for i, row in rows:
        # 3. Mandatory Field Validation
        mandatory_fields = ['Year', 'Subject', 'Chapter', 'Stem', 'Question_A', 'Ans_A']
        for field in mandatory_fields:
            if field in col_map:
                val = row[col_map[field]].strip() if col_map[field] < len(row) else ""
                if not val:
                    errors.append({
                        "row": i,
                        "type": "Missing Data",
                        "desc": f"Mandatory field '{field}' is empty."
                    })

        # 4. Logical Consistency (Question vs Answer Pairs)
        for part in ['A', 'B', 'C', 'D']:
            q_key = f'Question_{part}'
            a_key = f'Ans_{part}'
            
            if q_key in col_map and a_key in col_map:
                q_val = row[col_map[q_key]].strip() if col_map[q_key] < len(row) else ""
                a_val = row[col_map[a_key]].strip() if col_map[a_key] < len(row) else ""
                
                if q_val and not a_val:
                    errors.append({"row": i, "type": "Logic Error", "desc": f"{q_key} exists but {a_key} is missing."})
                elif a_val and not q_val:
                    errors.append({"row": i, "type": "Logic Error", "desc": f"{a_key} exists but {q_key} is missing."})

        # 5. Year Format Check
        if 'Year' in col_map:
            year_val = row[col_map['Year']].strip() if col_map['Year'] < len(row) else ""
            if year_val and not re.match(r'^\d{4}$', year_val):
                errors.append({
                    "row": i,
                    "type": "Format Error",
                    "desc": f"Invalid Year format: '{year_val}' (Expected YYYY)."
                })

        # Collect data for Duplicate Check (Category + Stem prefix)
        stem_idx = col_map.get('Stem')
        cat_idx = col_map.get('Category')
        if stem_idx is not None:
            stem_content = row[stem_idx].strip()[:100]
            cat_content = row[cat_idx].strip() if cat_idx is not None else ""
            key = (cat_content, stem_content)
            seen_stems[key].append(i)

    # Report Duplicates
    for key, line_nums in seen_stems.items():
        if len(line_nums) > 1:
            errors.append({
                "row": line_nums,
                "type": "Duplicate",
                "desc": f"Potential duplicate stem found in rows {line_nums}."
            })

    # Output Results
    if not errors:
        print("Success: No errors detected in BOM_1_CQ.")
    else:
        print(f"Detected {len(errors)} issues:")
        for err in errors:
            print(f"[{err['type']}] Row {err['row']}: {err['desc']}")

if __name__ == "__main__":
    validate_bom_cq(FILE_PATH)