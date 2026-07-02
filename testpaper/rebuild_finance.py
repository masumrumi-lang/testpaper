import csv
import json
import re
import os
import shutil

def clean_text(text):
    if not text:
        return ""
    # Fix common LaTeX commands that might have lost their backslash
    # Note: In Python string for JSON, we want \\command
    text = text.replace('rac{', '\\\\frac{')
    text = text.replace('beta', '\\\\beta')
    text = text.replace('alpha', '\\\\alpha')
    text = text.replace('gamma', '\\\\gamma')
    text = text.replace('times', '\\\\times')
    text = text.replace('sigma', '\\\\sigma')
    text = text.replace('rho', '\\\\rho')
    text = text.replace('mu', '\\\\mu')
    
    # Fix the "1. Data:" etc. if they exist to the cleaner format
    text = re.sub(r'\d+\.\s*Data:', 'Data:', text)
    text = re.sub(r'\d+\.\s*Formula:', 'Formula:', text)
    text = re.sub(r'\d+\.\s*Calculation:', 'Calculation:', text)
    
    # Replace newlines with <br><br>
    text = text.replace('\n', '<br><br>')
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    return text.strip()

def rebuild():
    # 1. Restore data.js from backup
    data_js = 'c:/Users/BMTF/.antigravity/testpaper/data.js'
    backup = 'c:/Users/BMTF/.antigravity/testpaper/data.js.bak_cq'
    if os.path.exists(backup):
        shutil.copy(backup, data_js)
        print("Restored data.js from backup.")
    else:
        print("Backup not found, proceeding with current data.js (might cause duplicates if not careful)")

    # 2. Process CSV
    csv_path = 'c:/Users/BMTF/.antigravity/testpaper/Finance1 CQ - Sheet5.csv'
    chapters_data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            chapter = row['Chapter']
            if chapter not in chapters_data:
                chapters_data[chapter] = {'shortCQData': [], 'fullCQData': []}
            
            count = len(chapters_data[chapter]['fullCQData']) + 1
            id_base = f"{count:02d}"
            meta = f"{row['Category']} · {row['Year']}"
            q_type = row['Level'].lower()
            
            full_cq = {
                "id": id_base,
                "stem": clean_text(row['Stem']),
                "meta": meta,
                "type": q_type,
                "questions": [
                    {"label": "a", "text": f"(a) {row['Question_A']}", "answer": clean_text(row['Ans_A'])},
                    {"label": "b", "text": f"(b) {row['Question_B']}", "answer": clean_text(row['Ans_B'])},
                    {"label": "c", "text": f"(c) {row['Question_C']}", "answer": clean_text(row['Ans_C'])},
                    {"label": "d", "text": f"(d) {row['Question_D']}", "answer": clean_text(row['Ans_D'])}
                ]
            }
            chapters_data[chapter]['fullCQData'].append(full_cq)
            
            short_cq_a = {
                "id": id_base + "A",
                "text": f"(a) {row['Question_A']}",
                "meta": f"Knowledge · {meta}",
                "type": q_type,
                "answer": clean_text(row['Ans_A'])
            }
            short_cq_b = {
                "id": id_base + "B",
                "text": f"(b) {row['Question_B']}",
                "meta": f"Comprehension · {meta}",
                "type": q_type,
                "answer": clean_text(row['Ans_B'])
            }
            chapters_data[chapter]['shortCQData'].append(short_cq_a)
            chapters_data[chapter]['shortCQData'].append(short_cq_b)

    # 3. Add Extra CQs
    with open('c:/Users/BMTF/.antigravity/testpaper/finance1_extra_cqs.json', 'r', encoding='utf-8') as f:
        extra_cqs = json.load(f)
    
    # Mapping for extra CQs (IDs EX01, etc.)
    extra_mapping = {"EX01": "3", "EX02": "7", "EX03": "8", "EX04": "9", "EX05": "5"}
    
    for cq in extra_cqs:
        ch = extra_mapping.get(cq['id'])
        if ch:
            if ch not in chapters_data:
                chapters_data[ch] = {'shortCQData': [], 'fullCQData': []}
            chapters_data[ch]['fullCQData'].append(cq)
            # Add short versions for extra CQs
            chapters_data[ch]['shortCQData'].append({
                "id": cq['id'] + "A",
                "text": cq['questions'][0]['text'],
                "meta": "Knowledge · " + cq['meta'],
                "type": cq['type'],
                "answer": cq['questions'][0]['answer']
            })
            chapters_data[ch]['shortCQData'].append({
                "id": cq['id'] + "B",
                "text": cq['questions'][1]['text'],
                "meta": "Comprehension · " + cq['meta'],
                "type": cq['type'],
                "answer": cq['questions'][1]['answer']
            })

    # 4. Inject into data.js
    with open(data_js, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for chapter_num, data in chapters_data.items():
        print(f"Processing Chapter {chapter_num}...")
        fin1_match = re.search(r'["\']fin1["\']:\s*\{', content)
        if not fin1_match: continue
        
        start = fin1_match.start()
        brace_count = 0
        fin1_end = -1
        for i in range(start, len(content)):
            if content[i] == '{': brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    fin1_end = i + 1
                    break
        
        fin1_content = content[start:fin1_end]
        ch_regex = r'["\']' + chapter_num + r'["\']:\s*\{'
        ch_match = re.search(ch_regex, fin1_content)
        
        if not ch_match: continue
        
        ch_start = ch_match.start()
        brace_count = 0
        ch_end = -1
        for i in range(ch_start, len(fin1_content)):
            if fin1_content[i] == '{': brace_count += 1
            elif fin1_content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    ch_end = i + 1
                    break
        
        ch_content = fin1_content[ch_start:ch_end]
        
        # Replace empty arrays
        # Note: We use json.dumps with ensure_ascii=False to preserve Bengali characters
        # And we need to be careful with double backslashes for the final JS file
        short_json = json.dumps(data['shortCQData'], indent=16, ensure_ascii=False)
        full_json = json.dumps(data['fullCQData'], indent=16, ensure_ascii=False)
        
        # We need to ensure that the backslashes in the JSON are preserved for JS
        # json.dumps already adds them if they are in the string
        
        ch_content = re.sub(r'shortCQData:\s*\[\s*\]', f'shortCQData: {short_json}', ch_content)
        ch_content = re.sub(r'fullCQData:\s*\[\s*\]', f'fullCQData: {full_json}', ch_content)
        
        fin1_content = fin1_content[:ch_start] + ch_content + fin1_content[ch_end:]
        content = content[:start] + fin1_content + content[fin1_end:]

    with open(data_js, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Rebuild and injection complete with fixed math formatting!")

if __name__ == "__main__":
    rebuild()
