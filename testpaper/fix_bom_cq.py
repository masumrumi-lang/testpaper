import json
import re

def fix_cq_injection():
    db_path = r"c:\Users\BMTF\.antigravity\testpaper\data.js"
    csv_path = r"c:\Users\BMTF\.antigravity\testpaper\Business Org & Mgmt 1 CQ - Sheet1.csv"
    
    # 1. First re-parse the CQs because we need the data
    import csv
    bom_data = {}
    
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
        
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) < 14: continue
            year, subj, chapter_str, level, cat, stem = row[:6]
            qa, qb, qc, qd = row[6], row[7], row[8], row[9]
            aa, ab, ac, ad = row[10], row[11], row[12], row[13]
            
            ch_match = re.search(r'Chapter (\d+)', chapter_str)
            ch_id = ch_match.group(1) if ch_match else "1"
            
            if ch_id not in bom_data:
                bom_data[ch_id] = []
                
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
                "id": str(len(bom_data[ch_id]) + 1).zfill(2),
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
            bom_data[ch_id].append(cq_obj)
            
    # 2. Inject
    with open(db_path, 'r', encoding='utf-8') as f:
        db_content = f.read()
        
    bus1_pattern = r'("bus1":\s*\{)'
    bus1_match = re.search(bus1_pattern, db_content)
    start_pos = bus1_match.start()
    
    bracket_count = 0
    end_pos = -1
    for i in range(start_pos, len(db_content)):
        if db_content[i] == '{': bracket_count += 1
        elif db_content[i] == '}':
            bracket_count -= 1
            if bracket_count == 0:
                end_pos = i + 1
                break
                
    bus1_content = db_content[start_pos:end_pos]
    
    for ch_id, cq_list in bom_data.items():
        ch_pattern = rf'("{ch_id}":\s*\{{)'
        ch_match = re.search(ch_pattern, bus1_content)
        cq_json = json.dumps(cq_list, indent=4, ensure_ascii=False)
        
        if ch_match:
            ch_start = ch_match.start()
            ch_bracket_count = 0
            ch_end = -1
            for i in range(ch_start, len(bus1_content)):
                if bus1_content[i] == '{': ch_bracket_count += 1
                elif bus1_content[i] == '}':
                    ch_bracket_count -= 1
                    if ch_bracket_count == 0:
                        ch_end = i + 1
                        break
            
            ch_content = bus1_content[ch_start:ch_end]
            
            if '"fullCQData"' in ch_content:
                # If it somehow exists, replace it
                new_ch_content = re.sub(r'"fullCQData"\s*:\s*\[.*?\]', f'"fullCQData": {cq_json}', ch_content, flags=re.DOTALL)
            else:
                # Append before the last brace of the chapter
                last_brace_idx = ch_content.rfind('}')
                new_ch_content = ch_content[:last_brace_idx] + f',\n        "shortCQData": [],\n        "fullCQData": {cq_json}\n    ' + ch_content[last_brace_idx:]
                
            bus1_content = bus1_content[:ch_start] + new_ch_content + bus1_content[ch_end:]

    db_content = db_content[:start_pos] + bus1_content + db_content[end_pos:]
    
    with open(db_path, 'w', encoding='utf-8') as f:
        f.write(db_content)
        
    print("Injected fullCQData successfully!")

if __name__ == "__main__":
    fix_cq_injection()
