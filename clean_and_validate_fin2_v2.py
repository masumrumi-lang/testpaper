import csv
import os

file_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_Ch_2_4_9_10_CQ - Sheet1.csv'

# Read all lines
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Clean all lines: remove trailing comma and whitespace
cleaned_lines = []
for line in lines:
    l = line.strip()
    if l.endswith(','):
        l = l[:-1]
    cleaned_lines.append(l + '\n')

# Now remove the specific rows (26 and 137 are already gone if I run this on the current file, 
# but wait, I should run it on the BACKUP to be safe and reproducible).
backup_path = file_path + '.bak'
with open(backup_path, 'r', encoding='utf-8') as f:
    orig_lines = f.readlines()

# 1. Clean all lines from trailing commas
final_lines = []
for line in orig_lines:
    l = line.strip()
    if l.endswith(','):
        l = l[:-1]
    final_lines.append(l + '\n')

# 2. Remove specified rows
rows_to_remove = [26, 137]
output_lines = []
removed_details = []
for i, line in enumerate(final_lines, start=1):
    if i in rows_to_remove:
        removed_details.append(f"Row {i}: {line[:50]}...")
        continue
    output_lines.append(line)

# 3. Write back
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.writelines(output_lines)

print(f"Updated row count: {len(output_lines)}")
print("Removed Rows:")
for r in removed_details:
    print(f" - {r}")

# 4. Final Validation
print("\n--- FINAL VALIDATION ---")
errors = []
try:
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        expected_cols = len(header)
        for i, row in enumerate(reader, start=2):
            if len(row) != expected_cols:
                errors.append(f"Row {i}: Column count mismatch (Expected {expected_cols}, got {len(row)})")
            
            # Check for specific known errors
            if "Monalisa" in row[5] and "Chapter 2" in row[2]:
                errors.append(f"Row {i}: Chapter mismatch (Monalisa in Chapter 2)")

    # Comprehensive Duplicate Check (Category, Stem, Question_A)
    import collections
    seen = collections.defaultdict(list)
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            # Check if all columns exist
            key = (row.get('Category',''), row.get('Stem','')[:100], row.get('Question_A',''))
            seen[key].append(i)
    
    for key, line_nums in seen.items():
        if len(line_nums) > 1:
            # Check if it's actually an exact duplicate (checking all columns)
            # We'll just report it as a potential duplicate for now
            errors.append(f"Duplicate/Variation found in rows {line_nums}: {key[2]}")

except Exception as e:
    errors.append(f"Critical Error: {str(e)}")

if not errors:
    print("SUCCESS: File is clean and valid.")
else:
    print("Remaining Issues:")
    for err in errors:
        print(f" - {err}")
