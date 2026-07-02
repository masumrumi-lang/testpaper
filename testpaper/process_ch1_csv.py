import csv
import json
import os
import re

def process_ch1_csv():
    csv_file = 'Agri1_Ch1_CQ - Sheet1.csv'
    output_file = 'agr1_ch1_data.json'
    
    questions = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            q_id = f"agr1_ch1_cq{i}"
            
            stem = row['Stem'].replace('\n', '<br>')
            if not stem.startswith('<p>'):
                stem = f"<p>{stem}</p>"
            
            # Extract image if present
            images = []
            stem_image = row.get('Stem Image', '')
            if stem_image and stem_image != 'NA':
                # Map to relative path
                image_filename = f"agri1_ch1_cq{i}.png"
                image_path = f"assets/images/agr1/ch1/{image_filename}"
                images.append({
                    "type": "diagram",
                    "status": "restored",
                    "instruction": f"Restore diagram for CQ {i}",
                    "src": image_path
                })
            
            # Questions and Answers
            qa = {
                'a': (row['Question_A'], row['Ans_A']),
                'b': (row['Question_B'], row['Ans_B']),
                'c': (row['Question_C'], row['Ans_C']),
                'd': (row['Question_D'], row['Ans_D'])
            }
            
            # Format answers as HTML
            def format_qa(label, q, a):
                return f"<div class='cq-part mb-4'><p class='font-bold text-gray-800 dark:text-gray-200'>({label}) {q}</p><div class='mt-2 text-gray-700 dark:text-gray-300'>{a.replace('\\n', '<br>').replace('\n', '<br>')}</div></div>"

            knowledge_comprehension = [
                format_qa('a', qa['a'][0], qa['a'][1]),
                format_qa('b', qa['b'][0], qa['b'][1])
            ]
            
            full_cq = [
                format_qa('a', qa['a'][0], qa['a'][1]),
                format_qa('b', qa['b'][0], qa['b'][1]),
                format_qa('c', qa['c'][0], qa['c'][1]),
                format_qa('d', qa['d'][0], qa['d'][1])
            ]
            
            questions.append({
                "chapter": "Agri1 Chapter 1",
                "question_id": q_id,
                "stem": stem,
                "knowledge_comprehension": knowledge_comprehension,
                "full_cq": full_cq,
                "images": images
            })
            
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
    
    print(f"Processed {len(questions)} questions into {output_file}")

if __name__ == "__main__":
    process_ch1_csv()
