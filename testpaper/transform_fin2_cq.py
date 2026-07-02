import csv
import json
import re

csv_path = r'c:\Users\BMTF\.antigravity\testpaper\Fin2_Ch_2_4_9_10_CQ - Sheet1.csv'

def clean_text(text):
    if not text: return ""
    # Normalize line breaks
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # Escape quotes for JS string if needed, but json.dumps handles this
    return text.strip()

def extract_chapter_num(chapter_str):
    match = re.search(r'Chapter (\d+)', chapter_str)
    return match.group(1) if match else "unknown"

chapters = {}

with open(csv_path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        ch_num = extract_chapter_num(row['Chapter'])
        if ch_num not in chapters:
            chapters[ch_num] = {
                "subjectName": row['Subject'],
                "chapterName": row['Chapter'],
                "mcqData": [],
                "shortCQData": [],
                "fullCQData": []
            }
        
        cq_id = f"fin2-ch{ch_num}-cq-{i:03d}"
        
        # 1. Short CQ Data (Knowledge & Comprehension)
        chapters[ch_num]["shortCQData"].append({
            "id": cq_id,
            "category": "Knowledge",
            "question": clean_text(row['Question_A']),
            "answer": clean_text(row['Ans_A'])
        })
        chapters[ch_num]["shortCQData"].append({
            "id": cq_id + "-b",
            "category": "Comprehension",
            "question": clean_text(row['Question_B']),
            "answer": clean_text(row['Ans_B'])
        })
        
        # 2. Full CQ Data
        meta = f"{row['Level']} · {row['Year']}"
        q_type = row['Category'].lower() if row['Category'] else "board"
        
        full_cq = {
            "id": cq_id,
            "stem": clean_text(row['Stem']),
            "stemImage": "",
            "meta": meta,
            "type": q_type,
            "questions": [
                {"label": "a", "text": clean_text(row['Question_A']), "answer": clean_text(row['Ans_A'])},
                {"label": "b", "text": clean_text(row['Question_B']), "answer": clean_text(row['Ans_B'])},
                {"label": "c", "text": clean_text(row['Question_C']), "answer": clean_text(row['Ans_C'])},
                {"label": "d", "text": clean_text(row['Question_D']), "answer": clean_text(row['Ans_D'])}
            ]
        }
        chapters[ch_num]["fullCQData"].append(full_cq)

# Print summary
for ch, data in chapters.items():
    print(f"Chapter {ch}: {len(data['fullCQData'])} records")
