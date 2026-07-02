import csv
import json
import re

def clean_html(text):
    if not text:
        return ""
    text = text.replace('\n', '<br>')
    return text.strip()

def process_cq_csv(file_path):
    chapters = {}
    
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chapter_str = row['Chapter'].strip()
            chapter_num_match = re.search(r'\d+', chapter_str)
            chapter_id = str(int(chapter_num_match.group())) if chapter_num_match else "1"
            
            if chapter_id not in chapters:
                chapters[chapter_id] = {
                    "subjectName": "Business 2nd Paper", # Default
                    "chapterName": f"Chapter {chapter_id}",
                    "mcqData": [],
                    "shortCQData": [],
                    "fullCQData": []
                }
            
            year = row['Year'].strip()
            level = row['Level'].strip()
            category = row['Category'].strip().lower()
            
            meta = f"{level} · {year}"
            q_type = category if category else "board"
            
            cq_id = str(len(chapters[chapter_id]["fullCQData"]) + 1).zfill(2)
            
            questions = []
            for label in ['A', 'B', 'C', 'D']:
                q_text = row.get(f'Question_{label}', '').strip()
                a_text = row.get(f'Ans_{label}', '').strip()
                if q_text:
                    questions.append({
                        "label": label.lower(),
                        "text": q_text,
                        "answer": a_text.replace('\n', '<br>')
                    })
            
            full_cq = {
                "id": cq_id,
                "stem": clean_html(row['Stem']),
                "meta": meta,
                "type": q_type,
                "questions": questions
            }
            chapters[chapter_id]["fullCQData"].append(full_cq)
            
            if row.get('Question_A'):
                chapters[chapter_id]["shortCQData"].append({
                    "id": f"{cq_id}A",
                    "text": row['Question_A'].strip(),
                    "meta": f"Knowledge · {meta}",
                    "type": q_type,
                    "answer": row['Ans_A'].strip().replace('\n', '<br>')
                })
            
            if row.get('Question_B'):
                chapters[chapter_id]["shortCQData"].append({
                    "id": f"{cq_id}B",
                    "text": row['Question_B'].strip(),
                    "meta": f"Comprehension · {meta}",
                    "type": q_type,
                    "answer": row['Ans_B'].strip().replace('\n', '<br>')
                })
                
    return chapters

if __name__ == "__main__":
    input_file = "Business Org & Mgmt 2 CQ - Sheet1.csv"
    data = process_cq_csv(input_file)
    
    with open("bus2_cq_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Processing complete.")
    for ch, d in data.items():
        print(f"Chapter {ch}: {len(d['fullCQData'])} Full CQs, {len(d['shortCQData'])} Short CQs")
