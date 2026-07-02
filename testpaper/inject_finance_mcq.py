import json
import re
import os
import sys

def inject(js_file, chapter_id, chapter_name):
    db_file = r"c:\Users\BMTF\.antigravity\testpaper\data.js"
    
    if not os.path.exists(js_file) or not os.path.exists(db_file):
        print(f"Files not found: {js_file}, {db_file}")
        return

    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    start_idx = js_content.find('[')
    end_idx = js_content.rfind(']') + 1
    new_mcq_data = js_content[start_idx:end_idx]
    
    with open(db_file, 'r', encoding='utf-8') as f:
        db_content = f.read()
    
    # Escape quotes in chapter name for regex
    escaped_chapter_name = re.escape(chapter_name)
    pattern = rf'("{chapter_id}":\s*{{\s*subjectName:\s*"Finance 1st Paper",\s*chapterName:\s*"{escaped_chapter_name}",\s*mcqData:\s*)\['
    
    match = re.search(pattern, db_content)
    if not match:
        print(f"Could not find Chapter {chapter_id} ({chapter_name}) in data.js")
        return
    
    start_pos = match.end() - 1
    
    bracket_count = 0
    end_pos = -1
    for i in range(start_pos, len(db_content)):
        if db_content[i] == '[':
            bracket_count += 1
        elif db_content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_pos = i + 1
                break
    
    if end_pos == -1:
        print("Could not find closing bracket for mcqData")
        return
    
    new_db_content = db_content[:start_pos] + new_mcq_data + db_content[end_pos:]
    
    with open(db_file, 'w', encoding='utf-8') as f:
        f.write(new_db_content)
    
    print(f"Successfully injected Chapter {chapter_id} MCQ data into data.js")

if __name__ == "__main__":
    if len(sys.argv) > 3:
        inject(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python inject_finance_mcq.py <js_file> <chapter_id> <chapter_name>")
