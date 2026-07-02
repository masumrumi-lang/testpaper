import csv
import os

file_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_Ch_2_4_9_10_CQ - Sheet1.csv'
backup_path = file_path + '.bak'

# 1. Create Backup
if not os.path.exists(backup_path):
    import shutil
    shutil.copy2(file_path, backup_path)
    print(f"Created backup at {backup_path}")

# 2. Perform Cleaning
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original line count: {len(lines)}")

# Fix header (Row 1)
header = lines[0].strip()
if header.endswith(','):
    header = header[:-1]
    lines[0] = header + '\n'
    print("Fixed header trailing comma.")

# Remove Row 26 and 137 (1-indexed)
# Note: Row 26 is index 25, Row 137 is index 136
rows_to_remove = [26, 137]
new_lines = []
removed_details = []

for i, line in enumerate(lines, start=1):
    if i in rows_to_remove:
        removed_details.append(f"Row {i}: {line[:50]}...")
        continue
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.writelines(new_lines)

print(f"Updated line count: {len(new_lines)}")
print("Removed Rows:")
for r in removed_details:
    print(f" - {r}")

# 3. Post-Cleaning Validation
print("\n--- POST-CLEANING VALIDATION ---")
errors = []

try:
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        expected_cols = len(header)
        
        for i, row in enumerate(reader, start=2):
            # Check column count
            if len(row) != expected_cols:
                errors.append(f"Row {i}: Column count mismatch (Expected {expected_cols}, got {len(row)})")
            
            # Check Chapter Mismatch for the Monalisa stem specifically
            # We already removed row 137, but let's check if any other Central Bank rows have E-banking questions.
            chapter = row[2]
            stem = row[5]
            if "Chapter 2" in chapter and "Monalisa" in stem:
                 errors.append(f"Row {i}: Potential chapter mismatch found (Monalisa stem in Chapter 2)")
            
            # Check if Row 26 or 137 content somehow survived
            if "Udayan Bank PLC" in stem and i == 26: # Row 26 was Udayan Bank related? No, Row 26 was Sylhet Board duplicate.
                pass 

    # Re-run duplicate check on (Category, Stem, Question_A)
    # Using full Question_A to differentiate valid shared stems
    import collections
    seen = collections.defaultdict(list)
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            key = (row['Category'], row['Stem'][:100], row['Question_A'])
            seen[key].append(i)
    
    for key, line_nums in seen.items():
        if len(line_nums) > 1:
            errors.append(f"Duplicate entry found in rows {line_nums}: {key[2]}")

except Exception as e:
    errors.append(f"Critical Validation Error: {str(e)}")

if not errors:
    print("All validations passed. The CSV is now clean and consistent.")
else:
    print("Issues found during validation:")
    for err in errors:
        print(f" - {err}")
