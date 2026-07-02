import json
import re

def inject_agri_cq():
    with open('agr1_ch2_data.json', 'r', encoding='utf-8') as f:
        new_questions = json.load(f)
    
    # Structure for Chapter 2
    ch2_data = {
        "subjectName": "Agriculture 1st Paper",
        "chapterName": "Chapter 2 : Agricultural Water Management and Soil Properties",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": new_questions
    }
    
    # Generate the JS string for the Chapter 2 object
    # We want it to be nicely formatted
    ch2_json_str = json.dumps(ch2_data, indent=24, ensure_ascii=False)
    # Adjusting indentation to match the file (roughly)
    ch2_json_str = ch2_json_str.replace(' ' * 24, '\t\t\t')
    
    ch2_entry = f'\n\t\t"2": {ch2_json_str},'
    
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    marker = '/* AGRI1_CHAPTER1_CQ_END */'
    marker_line_idx = -1
    for i, line in enumerate(lines):
        if marker in line:
            marker_line_idx = i
            break
            
    if marker_line_idx == -1:
        print("Marker not found!")
        return

    # We want to insert before the marker, but after the last closing brace of Chapter 1
    # Line 66911 was "        },"
    # Marker was at 66912
    # So we insert at marker_line_idx
    
    lines.insert(marker_line_idx, ch2_entry + '\n')
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("Injection successful.")

if __name__ == "__main__":
    inject_agri_cq()
