import csv
import os
import time

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'
temp_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY_temp.csv'

rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row_id, row in enumerate(reader, start=1):
        if row_id == 859:
            row['Options'] = "a) 4,000 b) 6,000 c) 9,750 d) 10,000"
            row['Answer'] = "b"
        elif row_id == 1388:
            row['Options'] = "a) Stock\nb) Receivables\nc) Cash\nd) Prepaid Insurance"
            row['Answer'] = "a"
        rows.append(row)

with open(temp_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Attempt to replace the original file
# We might need multiple attempts if there's a lock
max_attempts = 5
for i in range(max_attempts):
    try:
        if os.path.exists(input_file):
            os.remove(input_file)
        os.rename(temp_file, input_file)
        print("Successfully updated the file.")
        break
    except PermissionError:
        print(f"Attempt {i+1} failed: Permission denied. Retrying...")
        time.sleep(1)
else:
    print("Failed to replace the original file after several attempts.")
    print(f"The fixed data is saved in: {temp_file}")
