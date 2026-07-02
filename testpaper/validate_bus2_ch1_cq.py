import csv
import re
import collections
import os

FILE_PATH = r'BUS_2_CH1_CQ - ch1.csv'

MANDATORY_FIELDS = ['Year', 'Subject', 'Chapter', 'Stem', 'Question_A', 'Ans_A']


def validate_csv(path):
    if not os.path.exists(path):
        print(f'Error: {path} not found')
        return 1

    errors = []
    duplicates = collections.defaultdict(list)
    with open(path, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            print('Error: CSV is empty')
            return 1

        col_map = {name.strip(): idx for idx, name in enumerate(header)}
        expected_cols = len(header)

        for row_no, row in enumerate(reader, start=2):
            if len(row) != expected_cols:
                errors.append((row_no, 'ColumnCount', f'Expected {expected_cols} columns, found {len(row)}'))

            for field in MANDATORY_FIELDS:
                idx = col_map.get(field)
                if idx is None:
                    errors.append((row_no, 'HeaderMissing', f'Missing expected header {field}'))
                    continue
                val = row[idx].strip() if idx < len(row) else ''
                if not val:
                    errors.append((row_no, 'MissingMandatory', f'{field} is empty'))

            # Check question-answer pairing
            for part in ['A', 'B', 'C', 'D']:
                q_key = f'Question_{part}'
                a_key = f'Ans_{part}'
                q_idx = col_map.get(q_key)
                a_idx = col_map.get(a_key)
                q_val = row[q_idx].strip() if q_idx is not None and q_idx < len(row) else ''
                a_val = row[a_idx].strip() if a_idx is not None and a_idx < len(row) else ''
                if q_val and not a_val:
                    errors.append((row_no, 'Logic', f'{q_key} present but {a_key} missing'))
                if a_val and not q_val:
                    errors.append((row_no, 'Logic', f'{a_key} present but {q_key} missing'))

            year_idx = col_map.get('Year')
            if year_idx is not None and year_idx < len(row):
                year = row[year_idx].strip()
                if year and not re.match(r'^\d{4}$', year):
                    errors.append((row_no, 'YearFormat', f'Year value {year} is not YYYY'))

            stem_idx = col_map.get('Stem')
            cat_idx = col_map.get('Category')
            stem = row[stem_idx].strip() if stem_idx is not None and stem_idx < len(row) else ''
            cat = row[cat_idx].strip() if cat_idx is not None and cat_idx < len(row) else ''
            key = (cat, stem[:150])
            duplicates[key].append(row_no)

    dup_errors = [(rows, 'DuplicateStem', f'Duplicate stem found in rows {rows}') for rows in duplicates.values() if len(rows) > 1]

    if errors or dup_errors:
        print(f'Detected {len(errors) + len(dup_errors)} problems:')
        for row_no, etype, desc in errors:
            print(f'Row {row_no}: [{etype}] {desc}')
        for rows, etype, desc in dup_errors:
            print(f'Rows {rows}: [{etype}] {desc}')
        return 1

    print('Success: No issues found in BUS_2_CH1_CQ - ch1.csv')
    return 0


if __name__ == '__main__':
    exit(validate_csv(FILE_PATH))
