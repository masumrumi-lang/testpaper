import csv
import re
import json

def ensure_marks(text, mark):
    text = text.strip()
    if not text:
        return text
    if text.endswith(f"({mark})"):
        return text
    text = re.sub(r'\s*[\(\[-]?\s*\d\s*[\)\]]?$', '', text)
    return f"{text} ({mark})"

def process_and_inject_bom2():
    csv_path = 'Business Org & Mgmt 2 CQ - Sheet1.csv'
    db_path = 'data.js'
    
    bom2_data = {}
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        for row in reader:
            if len(row) < 14:
                continue
                
            year = row[0]
            subj = row[1]
            chapter_str = row[2]
            level = row[3]
            cat = row[4]
            stem = row[5]
            qa, qb, qc, qd = row[6], row[7], row[8], row[9]
            aa, ab, ac, ad = row[10], row[11], row[12], row[13]
            
            # The CSV might have chapter_str as "1" or "Chapter 1"
            ch_match = re.search(r'\d+', chapter_str)
            ch_id = ch_match.group(0) if ch_match else "1"
            
            if ch_id not in bom2_data:
                bom2_data[ch_id] = {
                    "chapterName": f"Chapter {ch_id}" if not "Chapter" in chapter_str else chapter_str,
                    "cqs": []
                }
            
            qa = ensure_marks(qa, 1)
            qb = ensure_marks(qb, 2)
            qc = ensure_marks(qc, 3)
            qd = ensure_marks(qd, 4)
            
            # Formatting
            if stem and not stem.startswith('<'): stem = f"<p>{stem}</p>"
            if aa and not aa.startswith('<'): aa = f"<p>{aa}</p>"
            if ab and not ab.startswith('<'): ab = f"<p>{ab}</p>"
            if ac and not ac.startswith('<'): ac = f"<p>{ac}</p>"
            if ad and not ad.startswith('<'): ad = f"<p>{ad}</p>"
            
            cq_obj = {
                "id": str(len(bom2_data[ch_id]["cqs"]) + 1).zfill(2),
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
            
            bom2_data[ch_id]["cqs"].append(cq_obj)

    with open(db_path, 'r', encoding='utf-8') as f:
        db_content = f.read()
    
    # We need to find bus2 or create it
    bus2_pattern = r'("bus2":\s*\{)'
    bus2_match = re.search(bus2_pattern, db_content)
    
    if bus2_match:
        start_pos = bus2_match.start()
        bracket_count = 0
        end_pos = -1
        for i in range(start_pos, len(db_content)):
            if db_content[i] == '{':
                bracket_count += 1
            elif db_content[i] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    end_pos = i + 1
                    break
        bus2_content = db_content[start_pos:end_pos]
        
        for ch_id, ch_data in bom2_data.items():
            cq_list = ch_data["cqs"]
            ch_pattern = rf'("{ch_id}":\s*\{{)'
            ch_match = re.search(ch_pattern, bus2_content)
            cq_json = json.dumps(cq_list, indent=4, ensure_ascii=False)
            
            if ch_match:
                ch_start = ch_match.start()
                ch_bracket_count = 0
                ch_end = -1
                for i in range(ch_start, len(bus2_content)):
                    if bus2_content[i] == '{':
                        ch_bracket_count += 1
                    elif bus2_content[i] == '}':
                        ch_bracket_count -= 1
                        if ch_bracket_count == 0:
                            ch_end = i + 1
                            break
                ch_content = bus2_content[ch_start:ch_end]
                new_ch_content = re.sub(r'("?)fullCQData("?)\s*:\s*\[.*?\]', f'"fullCQData": {cq_json}', ch_content, flags=re.DOTALL)
                bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
            else:
                ch_json = {
                    "subjectName": "Business 2nd Paper",
                    "chapterName": ch_data["chapterName"],
                    "mcqData": [],
                    "shortCQData": [],
                    "fullCQData": cq_list
                }
                ch_str = json.dumps(ch_json, indent=4, ensure_ascii=False)
                last_brace_idx = bus2_content.rfind('}')
                bus2_content = bus2_content[:last_brace_idx] + f',\n    "{ch_id}": {ch_str}\n' + bus2_content[last_brace_idx:]
                
        db_content = db_content[:start_pos] + bus2_content + db_content[end_pos:]
    else:
        # Create bus2 at the end of the file or before the last closing brace
        # db_content starts with const testDatabase = { and ends with }; or }
        print("Creating bus2 from scratch")
        bus2_json_obj = {}
        for ch_id, ch_data in bom2_data.items():
            bus2_json_obj[ch_id] = {
                "subjectName": "Business 2nd Paper",
                "chapterName": ch_data["chapterName"],
                "mcqData": [],
                "shortCQData": [],
                "fullCQData": ch_data["cqs"]
            }
        
        bus2_str = json.dumps(bus2_json_obj, indent=4, ensure_ascii=False)
        bus2_formatted = f'\n    "bus2": {bus2_str}\n'
        
        # Inject before the very last brace
        last_brace = db_content.rfind('}')
        if db_content[last_brace-1:last_brace].strip() == '':
            # find previous non empty character to see if we need a comma
            prev_comma = True
        else:
            prev_comma = False
            
        db_content = db_content[:last_brace].rstrip() + ',' + bus2_formatted + db_content[last_brace:]

    with open(db_path, 'w', encoding='utf-8') as f:
        f.write(db_content)

    print("Successfully injected BOM 2nd Paper CQ into data.js")

if __name__ == "__main__":
    process_and_inject_bom2()
