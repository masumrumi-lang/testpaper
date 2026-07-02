import csv
import json
import re
import os
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_ch3_5_7_8_12_13_14_cq - Sheet1.csv'
data_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'
backup_path = data_js_path + '.bak_fin2_new_chapters'

chapter_names_mapping = {
    "3": "Chapter 3: Commercial Bank",
    "5": "Chapter 5: Negotiable Instruments",
    "7": "Chapter 7: Source and Use of Bank Funds",
    "8": "Chapter 8: Foreign Exchange and Foreign Currency",
    "12": "Chapter 12: Marine Insurance",
    "13": "Chapter 13: Fire Insurance",
    "14": "Chapter 14: Miscellaneous Insurance"
}

def clean_text(text):
    if not text: return ""
    return text.strip()

# 1. Read existing data.js
print("Reading data.js...")
with open(data_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Extract existing fin2 block
start_idx = content.find('"fin2":')
if start_idx == -1:
    start_idx = content.find("'fin2':")
if start_idx == -1:
    print("FAILED: Could not find fin2 block start in data.js")
    sys.exit(1)

# Read brackets to locate the exact end of the block
brace_count = 0
found_first_brace = False
end_idx = -1
for i in range(start_idx, len(content)):
    char = content[i]
    if char == '{':
        brace_count += 1
        found_first_brace = True
    elif char == '}':
        brace_count -= 1
        if found_first_brace and brace_count == 0:
            end_idx = i + 1
            break

if end_idx == -1:
    print("FAILED: Could not find matching end brace for fin2 in data.js")
    sys.exit(1)

fin2_block_str = content[start_idx:end_idx]
json_str = fin2_block_str.split(':', 1)[1].strip()

try:
    fin2_data = json.loads(json_str)
    print("Successfully parsed existing fin2 data from data.js.")
except Exception as e:
    print("FAILED: Could not parse existing fin2 block as JSON:", e)
    sys.exit(1)

# 3. Parse and transform CSV data
print("Parsing CSV data...")
new_chapters = {}
injected_log = []

with open(csv_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        ch_num = clean_text(row['Chapter'])
        
        # Verify it's one of our target chapters
        if ch_num not in chapter_names_mapping:
            print(f"Warning: Chapter '{ch_num}' is not in the target chapters. Skipping.")
            continue
            
        if ch_num not in new_chapters:
            new_chapters[ch_num] = {
                "subjectName": "Finance 2nd Paper",
                "chapterName": chapter_names_mapping[ch_num],
                "mcqData": [],
                "shortCQData": [],
                "fullCQData": []
            }
        
        cq_id = f"fin2-ch{ch_num}-cq-{i:03d}"
        injected_log.append(f"Chapter {ch_num} CQ {i:03d}: {cq_id}")
        
        # Short CQ Data
        new_chapters[ch_num]["shortCQData"].append({
            "id": cq_id,
            "category": "Knowledge",
            "question": clean_text(row['Question_A']),
            "answer": clean_text(row['Ans_A'])
        })
        new_chapters[ch_num]["shortCQData"].append({
            "id": cq_id + "-b",
            "category": "Comprehension",
            "question": clean_text(row['Question_B']),
            "answer": clean_text(row['Ans_B'])
        })
        
        # Full CQ Data
        meta = f"{row['Level']} · {row['Year']}"
        q_type = row['Category'].lower() if row['Category'] else "board"
        
        full_cq = {
            "id": cq_id,
            "stem": clean_text(row['Stem']),
            "stemImage": "",
            "meta": meta,
            "type": q_type,
            "questions": [
                {"label": "a", "text": clean_text(row['Question_A']), "answer": clean_text(row['Ans_A'])},
                {"label": "b", "text": clean_text(row['Question_B']), "answer": clean_text(row['Ans_B'])},
                {"label": "c", "text": clean_text(row['Question_C']), "answer": clean_text(row['Ans_C'])},
                {"label": "d", "text": clean_text(row['Question_D']), "answer": clean_text(row['Ans_D'])}
            ]
        }
        new_chapters[ch_num]["fullCQData"].append(full_cq)

print(f"Transformed CSV. Total records processed: {len(injected_log)}")

# 4. Merge new chapters into existing fin2 data
print("Merging new chapters...")
for ch_num, ch_data in new_chapters.items():
    if ch_num in fin2_data:
        print(f"Warning: Chapter {ch_num} already exists in existing fin2. Overwriting.")
    fin2_data[ch_num] = ch_data

# Sort fin2_data by chapter number (key) numerically
sorted_fin2_data = {str(k): fin2_data[str(k)] for k in sorted(map(int, fin2_data.keys()))}

# 5. Format merged data to match the original style
# We use json.dumps with 8-spaces indentation
formatted_fin2_json = json.dumps(sorted_fin2_data, ensure_ascii=False, indent=8)

# The original has "fin2": { ... }
# Let's align the block properly.
# The original block has structure like:
# "fin2": {
#         "1": {
#                 ...
#         }
# },
# Let's indent each line of the json string by 8 spaces or keep it as formatted by json.dumps but prefixed with proper tabs.
# Let's inspect how the original JSON block formatting looks:
# In the original, the first line is `"fin2": {`
# The nested lines are indented. Let's format the new block to:
#     "fin2": <formatted_fin2_json>,
# Wait, let's make sure the lines are indented nicely to match standard JS formatting.
# The formatted JSON will have 8 spaces for indent.
# We want the lines of formatted_fin2_json (except the first one) to align properly.
# Actually, if we just do:
# The content after the fin2 block already has a comma, so we must NOT add one here.
# Check what follows end_idx to be safe:
after_block = content[end_idx:end_idx+10].strip()
if after_block.startswith(','):
    # Already has a comma — don't add one
    new_fin2_block_str = f'"fin2": {formatted_fin2_json}'
else:
    # No comma — add one
    new_fin2_block_str = f'"fin2": {formatted_fin2_json},'

print(f"After-block chars: {repr(content[end_idx:end_idx+10])}")

# Let's replace the old block with the new block in data.js
new_content = content[:start_idx] + new_fin2_block_str + content[end_idx:]

# 6. Safety check: write to a temp file and run node syntax validation
temp_path = data_js_path + '_temp.js'
print("Writing test output to temp file...")
with open(temp_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Running syntax validation with node -c...")
try:
    subprocess.run(['node', '-c', temp_path], check=True, capture_output=True, text=True)
    print("Syntax check PASSED successfully!")
except subprocess.CalledProcessError as e:
    print("SYNTAX ERROR IN GENERATED JS FILE:")
    print(e.stderr)
    os.remove(temp_path)
    sys.exit(1)
finally:
    if os.path.exists(temp_path) and not os.path.exists(backup_path): # clean up if we didn't move it yet
         pass


# 7. Finalize: Backup and Move
if not os.path.exists(backup_path):
    shutil.copy2(data_js_path, backup_path)
    print(f"Created backup of data.js at {backup_path}")

shutil.move(temp_path, data_js_path)
print("SUCCESS: Injected new chapters successfully into data.js!")
