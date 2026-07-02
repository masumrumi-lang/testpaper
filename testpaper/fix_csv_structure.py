import csv
import os

file_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_Ch_2_4_9_10_CQ - Sheet1.csv'

# Read using csv module to properly handle quoted fields
with open(file_path, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f))

header = reader[0]
data = reader[1:]

print(f"Total rows (incl. header): {len(reader)}")

fixed_rows = []
for i, row in enumerate(reader):
    if len(row) > 14:
        print(f"Row {i+1} has {len(row)} columns. Merging last columns...")
        # Merge columns from index 13 onwards into index 13 (Ans_D)
        # Ans_D starts at index 13 (0-indexed)
        new_row = row[:13]
        merged_ans_d = " ".join(row[13:]).strip()
        new_row.append(merged_ans_d)
        fixed_rows.append(new_row)
        print(f"Fixed Row {i+1}: {new_row[0]}, {new_row[1]}, ... [Merged Ans_D]")
    elif len(row) < 14 and len(row) > 0:
        print(f"Row {i+1} has only {len(row)} columns. Padding with empty strings...")
        new_row = row + [""] * (14 - len(row))
        fixed_rows.append(new_row)
    else:
        fixed_rows.append(row)

# Final check
final_errors = []
for i, row in enumerate(fixed_rows):
    if len(row) != 14:
        final_errors.append(f"Row {i+1} still has {len(row)} columns.")

if not final_errors:
    # Write back using proper CSV quoting
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(fixed_rows)
    print("\nSUCCESS: All rows now have exactly 14 columns.")
else:
    print("\nFAILED: Some rows are still incorrect:")
    for err in final_errors:
        print(err)

# Validation check
print("\n--- POST-FIX VALIDATION ---")
try:
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        row_count = 0
        for i, row in enumerate(reader, start=2):
            row_count += 1
            # Check for empty mandatory fields
            if not row.get('Stem') or not row.get('Ans_D'):
                print(f"Warning: Row {i} has empty mandatory fields.")
        print(f"Validated {row_count} data rows.")
except Exception as e:
    print(f"Validation Error: {str(e)}")
