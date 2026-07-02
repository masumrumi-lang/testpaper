import csv
import json
import re
import os

def format_content(text):
    if not text: return ""
    
    # 1. Math & Formula Formatting
    formulas = ['PV', 'FV', 'WACC', 'NPV', 'IRR', 'EPS', 'EAT', 'EBT', 'ROI', 'ROE']
    for f in formulas:
        text = re.sub(rf'\$?{f}\$?', f'<code>{f}</code>', text)
    
    # 2. Currency Formatting
    text = re.sub(r'(\d+(?:,\d+)*(?:\.\d+)?)\s*TK', r'TK \1', text, flags=re.IGNORECASE)
    text = re.sub(r'TK\s*(\d+(?:,\d+)*(?:\.\d+)?)', r'TK \1', text, flags=re.IGNORECASE)
    
    # 3. Interest Rate Formatting
    text = re.sub(r'(\d+(?:\.\d+)?)\s*%', r'\1%', text)
    
    # 4. Table Detection
    if '|' in text or '\t' in text:
        lines = text.split('\n')
        table_html = '<div class="table-responsive my-3"><table class="w-full text-sm border-collapse border border-gray-200 dark:border-gray-700">'
        for line in lines:
            if not line.strip(): continue
            cells = [c.strip() for c in re.split(r'[|\t]', line) if c.strip()]
            if not cells: continue
            table_html += '<tr>'
            for cell in cells:
                table_html += f'<td class="border border-gray-200 dark:border-gray-700 p-2">{cell}</td>'
            table_html += '</tr>'
        table_html += '</table></div>'
        return table_html
    
    return text

def migrate():
    csv_path = 'Finance1 MCQ Database.csv'
    start_id = 3552
    
    questions_by_chapter = {}
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # Skip header
            
            for i, row in enumerate(reader):
                if not row: continue
                if len(row) < 11: # At least up to correct answer
                    print(f"Skipping row {i+2} (Length {len(row)}): {row}")
                    continue
                
                year = row[0].strip()
                chapter_str = row[2].strip()
                location = row[3].strip()
                category = row[4].strip().lower()
                question_text = row[5].strip()
                options = [row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip()]
                correct_letter = row[10].strip().lower()
                explanation_text = row[11].strip() if len(row) > 11 else ""
                
                correct_idx = ord(correct_letter) - ord('a') if correct_letter in 'abcd' else 0
                
                formatted_q = format_content(question_text)
                if not formatted_q.startswith('<div'):
                    formatted_q = f"<p>{formatted_q}</p>"
                
                formatted_exp = format_content(explanation_text)
                if not formatted_exp.startswith('<div'):
                    formatted_exp = f"<p>{formatted_exp}</p>"
                
                meta = f"{location} · {year}"
                
                ch_num = re.search(r'\d+', chapter_str)
                ch_id = ch_num.group() if ch_num else "0"
                if ch_id == "0":
                    print(f"Row {i+2} assigned to Chapter 0: {chapter_str}")
                
                q_obj = {
                    "text": formatted_q,
                    "meta": meta,
                    "type": category,
                    "options": options,
                    "correctAnswer": correct_idx,
                    "explanation": formatted_exp,
                    "year_val": int(year) if year.isdigit() else 0
                }
                
                if ch_id not in questions_by_chapter:
                    questions_by_chapter[ch_id] = []
                questions_by_chapter[ch_id].append(q_obj)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Sort and write files
    current_id = start_id
    summary = []
    
    # Remove chapter 0 if it's empty or garbage
    if "0" in questions_by_chapter and len(questions_by_chapter["0"]) < 5:
        print(f"Removing Chapter 0 with {len(questions_by_chapter['0'])} items.")
        del questions_by_chapter["0"]

    for ch_id in sorted(questions_by_chapter.keys(), key=int):
        questions_by_chapter[ch_id].sort(key=lambda x: x['year_val'], reverse=True)
        
        final_list = []
        for q in questions_by_chapter[ch_id]:
            q['id'] = current_id
            current_id += 1
            del q['year_val']
            final_list.append(q)
        
        js_filename = f"fin1_ch{ch_id}_mcq.js"
        with open(js_filename, 'w', encoding='utf-8') as js_file:
            js_file.write(f"const fin1_ch{ch_id}_mcq = ")
            json.dump(final_list, js_file, indent=4, ensure_ascii=False)
            js_file.write(";")
            
        summary.append(f"Chapter {ch_id}: {len(final_list)} questions added.")
        print(f"Generated {js_filename}")

    print("\nMigration Summary:")
    for line in summary:
        print(line)
    print(f"Total Questions: {current_id - start_id}")

if __name__ == "__main__":
    migrate()
