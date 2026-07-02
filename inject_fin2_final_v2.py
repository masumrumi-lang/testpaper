import csv
import json
import re
import os
import shutil
import subprocess

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_Ch_2_4_9_10_CQ - Sheet1.csv'
data_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'
backup_path = data_js_path + '.bak_fin2'

def clean_text(text):
    if not text: return ""
    return text.strip()

def extract_chapter_num(chapter_str):
    match = re.search(r'Chapter (\d+)', chapter_str)
    return match.group(1) if match else "unknown"

# 1. Transform Data
chapters = {}
injected_log = []

with open(csv_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        ch_num = extract_chapter_num(row['Chapter'])
        if ch_num not in chapters:
            chapters[ch_num] = {
                "subjectName": row['Subject'],
                "chapterName": row['Chapter'],
                "mcqData": [],
                "shortCQData": [],
                "fullCQData": []
            }
        
        cq_id = f"fin2-ch{ch_num}-cq-{i:03d}"
        injected_log.append(f"Injected: {cq_id} (Chapter {ch_num})")
        
        # Short CQ Data
        chapters[ch_num]["shortCQData"].append({
            "id": cq_id,
            "category": "Knowledge",
            "question": clean_text(row['Question_A']),
            "answer": clean_text(row['Ans_A'])
        })
        chapters[ch_num]["shortCQData"].append({
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
        chapters[ch_num]["fullCQData"].append(full_cq)

# 2. Generate JS Fragment
fin2_js = "    \"fin2\": " + json.dumps(chapters, ensure_ascii=False, indent=8) + ","

# 3. Read data.js and find insertion point
with open(data_js_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

insert_idx = -1
for i, line in enumerate(lines):
    if '"ict":' in line:
        insert_idx = i
        break

if insert_idx == -1:
    for i in range(len(lines) - 1, -1, -1):
        if '};' in lines[i]:
            insert_idx = i
            break

if insert_idx == -1:
    print("FAILED: Could not find insertion point in data.js")
    exit(1)

new_lines = lines[:insert_idx] + [fin2_js + "\n"] + lines[insert_idx:]

# 4. Safety Validation
temp_js_path = r'c:\Users\BMTF\.antigravity\testpaper\data_test.js'
with open(temp_js_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Validating syntax with node -c...")
try:
    result = subprocess.run(['node', '-c', temp_js_path], capture_output=True, text=True, check=True)
    print("Syntax check passed.")
except subprocess.CalledProcessError as e:
    print("SYNTAX ERROR IN GENERATED JS:")
    print(e.stderr)
    os.remove(temp_js_path)
    exit(1)

# 5. Finalize Injection
if not os.path.exists(backup_path):
    shutil.copy2(data_js_path, backup_path)
    print(f"Backup created at {backup_path}")

shutil.move(temp_js_path, data_js_path)
print("Injection successful.")

# Print Log
for entry in injected_log:
    print(entry)

print(f"\nTOTAL RECORDS INJECTED: {len(injected_log)}")
