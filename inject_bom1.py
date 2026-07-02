import csv
import re
import os
import json

def repair_math(text):
    if not text:
        return text
    
    # Standardize multiplication
    text = re.sub(r'(\d|\)|\]|\})\s*\*\s*(\d|\(|\[|\{)', r'\1 \\times \2', text)
    text = re.sub(r'(?<!\\)imes', r'\\times', text)
    
    # Strip HTML from inside math
    # First, wrap $...$ in $$...$$ if not already
    text = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', r'$$\1$$', text)
    
    # Remove HTML tags from inside $$...$$
    text = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + m.group(1).replace('<code>', '').replace('</code>', '').replace('<b>', '').replace('</b>', '') + '$$', text)
    
    return text

def process_and_inject():
    csv_path = r"c:\Users\BMTF\.antigravity\testpaper\B&M 1st Paper mcq - Sheet1.csv"
    db_path = r"c:\Users\BMTF\.antigravity\testpaper\data.js"
    
    bom_data = {} # chapter_id -> list of mcq
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        row_num = 1
        for row in reader:
            row_num += 1
            if len(row) < 11:
                continue
                
            year = row[0]
            subj = row[1]
            chapter_str = row[2]
            level = row[3]
            cat = row[4]
            question = row[5]
            opts = [row[6], row[7], row[8], row[9]]
            ans_str = row[10].strip().lower()
            explanation = row[11] if len(row) > 11 else ""
            
            # Fix duplicate correct answer (just in case)
            if "&" in ans_str:
                ans_str = ans_str.split("&")[0].strip()
                
            # Convert ans to index
            ans_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
            ans_idx = ans_map.get(ans_str, 0)
            
            # Extract chapter ID
            ch_match = re.search(r'Chapter (\d+)', chapter_str)
            ch_id = ch_match.group(1) if ch_match else "1"
            
            if ch_id not in bom_data:
                bom_data[ch_id] = {
                    "subjectName": "Business 1st Paper",
                    "chapterName": chapter_str,
                    "mcqData": []
                }
            
            # Repair math in all fields
            question = repair_math(question)
            explanation = repair_math(explanation)
            opts = [repair_math(o) for o in opts]
            
            # Wrap in <p> if not already
            if not question.startswith('<'): question = f"<p>{question}</p>"
            if explanation and not explanation.startswith('<'): explanation = f"<p>{explanation}</p>"
            
            bom_data[ch_id]["mcqData"].append({
                "id": len(bom_data[ch_id]["mcqData"]) + 1,
                "text": question,
                "meta": f"{level} · {year}" if level != "N/A" else f"General Practice · {year}",
                "type": cat.lower(),
                "options": opts,
                "correctAnswer": ans_idx,
                "explanation": explanation
            })

    # Prepare JS content
    new_bom_json = json.dumps(bom_data, indent=4, ensure_ascii=False)
    
    # Inject into data.js
    with open(db_path, 'r', encoding='utf-8') as f:
        db_content = f.read()
    
    # Check if bus1 already exists
    if '"bus1":' in db_content:
        # Replace existing
        pattern = r'("bus1":\s*\{)'
        match = re.search(pattern, db_content)
        if match:
            start_pos = match.start()
            
            # Find closing brace for bus1 object
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
            
            if end_pos != -1:
                db_content = db_content[:start_pos] + '"bus1": ' + new_bom_json + db_content[end_pos:]
            else:
                print("Could not find matching closing brace for bus1.")
                return
    else:
        # Append before the last };
        last_brace_idx = db_content.rfind('};')
        db_content = db_content[:last_brace_idx] + ',\n    "bus1": ' + new_bom_json + '\n' + db_content[last_brace_idx:]
    
    with open(db_path, 'w', encoding='utf-8') as f:
        f.write(db_content)
    
    print("Successfully repaired and injected Business 1st Paper MCQs into data.js")

if __name__ == "__main__":
    process_and_inject()
