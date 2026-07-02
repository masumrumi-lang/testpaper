import csv
import re
import os
import json

def repair_math(text):
    if not text: return text
    text = re.sub(r'(\d|\)|\]|\})\s*\*\s*(\d|\(|\[|\{)', r'\1 \\times \2', text)
    text = re.sub(r'(?<!\\)imes', r'\\times', text)
    text = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', r'$$\1$$', text)
    text = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + m.group(1).replace('<code>', '').replace('</code>', '').replace('<b>', '').replace('</b>', '') + '$$', text)
    return text

def ensure_marks(text, mark):
    text = text.strip()
    if not text: return text
    if text.endswith(f"({mark})"): return text
    text = re.sub(r'\s*[\(\[-]?\s*\d\s*[\)\]]?$', '', text)
    return f"{text} ({mark})"

def rebuild_bus1():
    db_path = r"c:\Users\BMTF\.antigravity\testpaper\data.js"
    mcq_csv = r"c:\Users\BMTF\.antigravity\testpaper\B&M 1st Paper mcq - Sheet1.csv"
    cq_csv = r"c:\Users\BMTF\.antigravity\testpaper\Business Org & Mgmt 1 CQ - Sheet1.csv"
    
    bus1_data = {} # chapter_id -> dict
    
    # --- 1. Process MCQ ---
    with open(mcq_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) < 11: continue
            year, subj, chapter_str, level, cat, question = row[:6]
            opts = [row[6], row[7], row[8], row[9]]
            ans_str = row[10].strip().lower()
            explanation = row[11] if len(row) > 11 else ""
            
            if "&" in ans_str: ans_str = ans_str.split("&")[0].strip()
            ans_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
            ans_idx = ans_map.get(ans_str, 0)
            
            ch_match = re.search(r'Chapter (\d+)', chapter_str)
            ch_id = ch_match.group(1) if ch_match else "1"
            
            if ch_id not in bus1_data:
                bus1_data[ch_id] = {
                    "subjectName": "Business 1st Paper",
                    "chapterName": chapter_str,
                    "mcqData": [],
                    "shortCQData": [],
                    "fullCQData": []
                }
                
            question = repair_math(question)
            explanation = repair_math(explanation)
            opts = [repair_math(o) for o in opts]
            
            if not question.startswith('<'): question = f"<p>{question}</p>"
            if explanation and not explanation.startswith('<'): explanation = f"<p>{explanation}</p>"
            
            bus1_data[ch_id]["mcqData"].append({
                "id": len(bus1_data[ch_id]["mcqData"]) + 1,
                "text": question,
                "meta": f"{level} · {year}" if level != "N/A" else f"General Practice · {year}",
                "type": cat.lower(),
                "options": opts,
                "correctAnswer": ans_idx,
                "explanation": explanation
            })
            
    # --- 2. Process CQ ---
    with open(cq_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) < 14: continue
            year, subj, chapter_str, level, cat, stem = row[:6]
            qa, qb, qc, qd = row[6], row[7], row[8], row[9]
            aa, ab, ac, ad = row[10], row[11], row[12], row[13]
            
            ch_match = re.search(r'(\d+)', chapter_str)
            ch_id = str(int(ch_match.group(1))) if ch_match else "1"
            
            if ch_id not in bus1_data:
                bus1_data[ch_id] = {
                    "subjectName": "Business 1st Paper",
                    "chapterName": f"Chapter {ch_id}",
                    "mcqData": [],
                    "shortCQData": [],
                    "fullCQData": []
                }
                
            stem = repair_math(stem)
            qa = ensure_marks(repair_math(qa), 1)
            qb = ensure_marks(repair_math(qb), 2)
            qc = ensure_marks(repair_math(qc), 3)
            qd = ensure_marks(repair_math(qd), 4)
            aa, ab, ac, ad = repair_math(aa), repair_math(ab), repair_math(ac), repair_math(ad)
            
            if not stem.startswith('<'): stem = f"<p>{stem}</p>"
            if aa and not aa.startswith('<'): aa = f"<p>{aa}</p>"
            if ab and not ab.startswith('<'): ab = f"<p>{ab}</p>"
            if ac and not ac.startswith('<'): ac = f"<p>{ac}</p>"
            if ad and not ad.startswith('<'): ad = f"<p>{ad}</p>"
            
            cq_obj = {
                "id": str(len(bus1_data[ch_id]["fullCQData"]) + 1).zfill(2),
                "stem": stem,
                "meta": f"{level} · {year}" if level != "N/A" else f"General Practice · {year}",
                "type": cat.lower(),
                "questions": [
                    { "label": "a", "text": qa, "answer": aa },
                    { "label": "b", "text": qb, "answer": ab },
                    { "label": "c", "text": qc, "answer": ac },
                    { "label": "d", "text": qd, "answer": ad }
                ]
            }
            bus1_data[ch_id]["fullCQData"].append(cq_obj)
            
            # Populate shortCQData with Knowledge (a) and Comprehension (b)
            cq_number_str = cq_obj["id"]
            bus1_data[ch_id]["shortCQData"].append({
                "id": f"{cq_number_str}(a)",
                "text": qa,
                "answer": aa,
                "meta": cq_obj["meta"],
                "type": cq_obj["type"]
            })
            bus1_data[ch_id]["shortCQData"].append({
                "id": f"{cq_number_str}(b)",
                "text": qb,
                "answer": ab,
                "meta": cq_obj["meta"],
                "type": cq_obj["type"]
            })
            
    # --- 3. Clean and Inject into data.js ---
    with open(db_path, 'r', encoding='utf-8') as f:
        db_content = f.read()
        
    # Find the corrupted bus1 block
    bus1_idx = db_content.find(',\n    "bus1": {')
    if bus1_idx == -1:
        # Maybe without newline?
        bus1_idx = db_content.find(',"bus1": {')
        if bus1_idx == -1:
            bus1_idx = db_content.find('"bus1": {')
            # If we matched just "bus1": {, backtrack to previous comma if possible
            if bus1_idx != -1:
                comma_idx = db_content.rfind(',', 0, bus1_idx)
                if comma_idx != -1:
                    bus1_idx = comma_idx
    
    if bus1_idx != -1:
        # Truncate db_content right before bus1
        clean_db = db_content[:bus1_idx]
        print(f"Truncated corrupted bus1 at index {bus1_idx}")
    else:
        # If not found, just truncate before the last };
        last_brace = db_content.rfind('};')
        clean_db = db_content[:last_brace]
        print("bus1 not cleanly found. Truncating before end of testDatabase.")
        
    # Prepare the new bus1 json
    bus1_json = json.dumps(bus1_data, indent=4, ensure_ascii=False)
    
    # Construct final file
    final_db = clean_db + ',\n    "bus1": ' + bus1_json + '\n};\n'
    
    with open(db_path, 'w', encoding='utf-8') as f:
        f.write(final_db)
        
    print("Successfully rebuilt and injected clean bus1 data (MCQ & CQ) into data.js")

if __name__ == "__main__":
    rebuild_bus1()
