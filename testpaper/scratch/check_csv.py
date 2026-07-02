import csv
import json

file_path = 'Agri1_Ch2_CQ - Sheet1.csv'
questions = []

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        q_id = f"agr1_ch2_cq{i+1}"
        questions.append({
            "id": q_id,
            "stem": row.get('Stem', '').strip(),
            "image": row.get('Stem Image', '').strip()
        })

print(f"Total questions found: {len(questions)}")
for q in questions:
    print(f"{q['id']}: {q['stem'][:50]}... (Image: {q['image']})")
