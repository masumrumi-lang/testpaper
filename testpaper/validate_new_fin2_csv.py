import csv
import re
import collections
import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_ch3_5_7_8_12_13_14_cq - Sheet1.csv'

def validate_csv(path):
    errors = []
    rows = []
    
    try:
        with open(path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            expected_cols = len(header)
            
            for i, row in enumerate(reader, start=2):
                if len(row) != expected_cols:
                    errors.append({
                        "row": i,
                        "type": "Malformed Row",
                        "desc": f"Expected {expected_cols} columns, but found {len(row)}.",
                        "data": row
                    })
                rows.append((i, row))
    except UnicodeDecodeError as e:
        errors.append({
            "row": "N/A",
            "type": "Encoding Error",
            "desc": f"File is not valid UTF-8. Error: {str(e)}"
        })
        return errors, []
    except Exception as e:
        errors.append({
            "row": "N/A",
            "type": "File Read Error",
            "desc": str(e)
        })
        return errors, []

    col_map = {name: idx for idx, name in enumerate(header)}
    seen_stems = collections.defaultdict(list)
    
    for i, row in rows:
        # Check all headers map
        for col_name, col_idx in col_map.items():
            if not col_name: continue
            val = row[col_idx].strip() if col_idx < len(row) else ""
            
            if not val:
                if col_name in ['Year', 'Subject', 'Chapter', 'Level', 'Category', 'Stem']:
                    errors.append({
                        "row": i,
                        "type": "Missing Value",
                        "desc": f"Column '{col_name}' is empty."
                    })
                elif col_name.startswith('Question_') or col_name.startswith('Ans_'):
                     errors.append({
                        "row": i,
                        "type": "Missing Value",
                        "desc": f"Question/Answer column '{col_name}' is empty."
                    })

        # Year validation
        year_val = row[col_map['Year']].strip() if 'Year' in col_map else ""
        # Let's see if year format is OK, or sometimes it's e.g. "2023" or "2022" or "2019" or list of years
        
        chapter_val = row[col_map['Chapter']].strip() if 'Chapter' in col_map else ""
        if chapter_val and not chapter_val.startswith('Chapter'):
            errors.append({
                "row": i,
                "type": "Inconsistent Formatting",
                "desc": f"Chapter field '{chapter_val}' should start with 'Chapter'."
            })

        # Questions vs Answers consistency
        for char in ['A', 'B', 'C', 'D']:
            q_col = f'Question_{char}'
            a_col = f'Ans_{char}'
            q_val = row[col_map[q_col]].strip() if q_col in col_map else ""
            a_val = row[col_map[a_col]].strip() if a_col in col_map else ""
            
            if q_val and not a_val:
                errors.append({
                    "row": i,
                    "type": "Logical Inconsistency",
                    "desc": f"Question_{char} is present but Ans_{char} is missing."
                })
            elif a_val and not q_val:
                  errors.append({
                    "row": i,
                    "type": "Logical Inconsistency",
                    "desc": f"Ans_{char} is present but Question_{char} is missing."
                })

        stem_val = row[col_map['Stem']].strip() if 'Stem' in col_map else ""
        cat_val = row[col_map['Category']].strip() if 'Category' in col_map else ""
        key = (cat_val, stem_val[:100])
        seen_stems[key].append(i)

    return errors, rows

errors, rows = validate_csv(file_path)
if not errors:
    print("No errors detected.")
else:
    print(f"Detected {len(errors)} potential issues:\n")
    for err in errors:
        row_info = f"Row {err['row']}" if not isinstance(err['row'], list) else f"Rows {err['row']}"
        print(f"[{err['type']}] {row_info}: {err['desc']}")
