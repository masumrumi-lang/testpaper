import csv
import json
import os
import re

# Configuration
SOURCE_CSV = 'acc1_mcq_IMPORT_READY.csv'
STARTING_ID = 188  # Continuing from Chapter 8's last ID (187)
CHAPTER_MAPPING = {
    "Chapter 2 : Books of Accounts": "2",
    "Chapter 3 : Bank Reconciliation Statement": "3",
    "Chapter 4 : Trial Balance": "4",
    "Chapter 5 : Accounting Principles (Out of Short Syllabus)": "5",
    "Chapter 6 : Accounting for Receivables (Out of Short Syllabus)": "6",
    "Chapter 7 : Work Sheet": "7",
    "Chapter 9 : Financial Statements": "9",
    "Chapter 10 : Single Entry System (Out of Short Syllabus)": "10"
}

def generate_js_content(var_name, data):
    return f"const {var_name} = {json.dumps(data, indent=4)};"

def main():
    if not os.path.exists(SOURCE_CSV):
        print(f"Error: {SOURCE_CSV} not found.")
        return

    questions_by_chapter = {}
    current_id = STARTING_ID

    with open(SOURCE_CSV, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Cleanup and validation
            q_text = row.get('q_text', '').strip()
            html_code = row.get('HTML_Code', '').strip()
            
            # Combine text and HTML if present
            full_text = f"<p>{q_text}</p>"
            if html_code:
                full_text += html_code
            
            # Validation for null/undefined
            if not q_text:
                print(f"Warning: Empty question text at row {reader.line_num}. Skipping.")
                continue
            
            options = [
                row.get('opt_a', '').strip(),
                row.get('opt_b', '').strip(),
                row.get('opt_c', '').strip(),
                row.get('opt_d', '').strip()
            ]
            
            if any(not opt for opt in options):
                 print(f"Warning: Empty option at row {reader.line_num}. Question: {q_text[:50]}...")

            # Map Answer (a, b, c, d) to (0, 1, 2, 3)
            answer_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
            correct_answer = answer_map.get(row.get('Answer', '').lower(), 0)

            # Create the JS object
            obj = {
                "id": current_id,
                "text": full_text,
                "meta": row.get('Type', '').strip(),
                "type": row.get('Category', '').strip().lower(),
                "options": options,
                "correctAnswer": correct_answer,
                "explanation": f"<p>{row.get('Explanation', '').strip()}</p>" if row.get('Explanation') else ""
            }

            chapter = row.get('Chapter')
            if chapter not in questions_by_chapter:
                questions_by_chapter[chapter] = []
            
            questions_by_chapter[chapter].append(obj)
            current_id += 1

    # Generate individual JS files
    generated_files = []
    for chapter_name, questions in questions_by_chapter.items():
        ch_idx = CHAPTER_MAPPING.get(chapter_name)
        if not ch_idx:
            # Fallback for unexpected chapter names
            match = re.search(r'Chapter\s*(\d+)', chapter_name)
            ch_idx = match.group(1) if match else "unknown"
        
        filename = f"acc1_ch{ch_idx}_mcq.js"
        var_name = f"acc1_ch{ch_idx}_mcq"
        
        with open(filename, 'w', encoding='utf-8') as f_out:
            f_out.write(generate_js_content(var_name, questions))
        
        generated_files.append((ch_idx, filename, var_name, chapter_name))
        print(f"Generated {filename} with {len(questions)} questions.")

    print(f"\nTotal questions imported: {current_id - STARTING_ID}")
    
    # Update rebuild_data.ps1
    update_rebuild_script(generated_files)

def update_rebuild_script(generated_files):
    ps_path = 'rebuild_data.ps1'
    if not os.path.exists(ps_path):
        print(f"Error: {ps_path} not found.")
        return

    with open(ps_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add file reading logic
    # We'll insert after the existing MCQ variables
    insert_point = content.find('$mcq8Combined =')
    if insert_point != -1:
        # Find the next newline after the next line
        next_line_end = content.find('\n', insert_point)
        next_line_end = content.find('\n', next_line_end + 1)
        
        new_reads = "\n"
        for ch_idx, filename, var_name, _ in generated_files:
            new_reads += f'${var_name} = Get-ArrayContent "{filename}"\n'
        
        content = content[:next_line_end+1] + new_reads + content[next_line_end+1:]

    # 2. Update the testDatabase assembly
    # This is trickier. I'll replace the entire "acc1" block in the template string.
    
    acc1_block = '    "acc1": {\n'
    # Keep Chapter 1
    acc1_block += '        "1": {\n            subjectName: "Accounting 1st Paper",\n            chapterName: "Chapter 1 : Introduction to Accounting",\n            mcqData: [\n$mcqCombined\n            ],\n            shortCQData: [\n$shortCombined\n            ],\n            fullCQData: [\n$fullCQCombined\n            ]\n        },\n'
    
    # Add new chapters
    sorted_files = sorted(generated_files, key=lambda x: int(x[0]) if x[0].isdigit() else 999)
    for ch_idx, filename, var_name, chapter_name in sorted_files:
        if ch_idx == "8": continue # We handle 8 separately or overwrite it? 
        # Actually Chapter 8 is already in the script. I'll include it in the loop if it's there.
        
        acc1_block += f'        "{ch_idx}": {{\n            subjectName: "Accounting 1st Paper",\n            chapterName: "{chapter_name}",\n            mcqData: [\n${var_name}\n            ],\n            shortCQData: [],\n            fullCQData: []\n        }},\n'
    
    # Keep Chapter 8 (since it has fullCQ)
    # Wait, if Chapter 8 was in the CSV, I would have filtered it.
    # So I should keep the existing Chapter 8 definition if it's not in my new list.
    if not any(f[0] == "8" for f in generated_files):
         acc1_block += '        "8": {\n            subjectName: "Accounting 1st Paper",\n            chapterName: "Chapter 8 : Accounting for Tangible and Intangible Assets",\n            mcqData: [\n$mcq8Combined\n            ],\n            shortCQData: [],\n            fullCQData: [\n$fullCQ8Combined\n            ]\n        }\n'

    acc1_block += '    },'

    # Regex to find the "acc1" block in the $newData heredoc
    # It ends with }, followed by a newline and $ictBlock
    pattern = r'"acc1": \{.*?\n\s+\},\s*(?=\$ictBlock)'
    content = re.sub(pattern, acc1_block + '\n', content, flags=re.DOTALL)

    with open(ps_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("rebuild_data.ps1 updated.")

if __name__ == "__main__":
    main()
