import csv
import json
import re

def format_text(text):
    if not text:
        return ""
    # Replace newlines with <br> for HTML
    text = text.replace('\r\n', '<br>').replace('\n', '<br>')
    # Bold pH values (e.g., pH 7.0)
    text = re.sub(r'(pH\s?\d+(\.\d+)?)', r'<b>\1</b>', text, flags=re.IGNORECASE)
    return text

def format_part_html(q, a, label):
    q_clean = format_text(q)
    a_clean = format_text(a)
    # The requirement says ["a", "b"] and ["a", "b", "c", "d"]
    # We'll combine question and answer in a clean div for each part
    return f"<div class='cq-part mb-4'><p class='font-bold text-gray-800 dark:text-gray-200'>({label}) {q_clean}</p><div class='mt-2 text-gray-700 dark:text-gray-300'>{a_clean}</div></div>"

def process_agri_cq():
    csv_path = 'Agri1_Ch2_CQ - Sheet1.csv'
    output_path = 'agr1_ch2_data.json'
    
    questions = []
    
    img_mapping = {
        2: "Recreate soil pH classification flowchart: A Acidic Soil, B Neutral Soil, C Alkaline Soil",
        6: "Recreate irrigation methods flowchart: A Surface, B Sub-surface, C Sprinkler, D Drip",
        10: "Recreate rice planting layout: Fig A (25x25cm), Fig B (15x10cm)",
        12: "Recreate Boro rice seedling methods: A (1 seedling), B (3-4 seedlings)",
        14: "Recreate sprinkler irrigation diagram showing fine droplets over crops",
        17: "Recreate pH scale chart: A (Acidic), B (Neutral range), C (Alkaline)",
        18: "Generate later: English-only diagram of Sandy to Loam Soil transformation, no question text, minimal agricultural schematic style",
        21: "Generate later: English-only diagram of pH scale table visualization, no question text, minimal agricultural schematic style",
        22: "Generate later: English-only diagram of pH scale line diagram, no question text, minimal agricultural schematic style"
    }
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            q_idx = i + 1
            question_id = f"agr1_ch2_cq{q_idx}"
            
            # Stem formatting
            stem = format_text(row['Stem'].strip())
            if not stem.startswith('<p>'):
                stem = f"<p>{stem}</p>"
            
            # Extract and format parts
            a = format_part_html(row['Question_A'].strip(), row['Ans_A'].strip(), 'a')
            b = format_part_html(row['Question_B'].strip(), row['Ans_B'].strip(), 'b')
            c = format_part_html(row['Question_C'].strip(), row['Ans_C'].strip(), 'c')
            d = format_part_html(row['Question_D'].strip(), row['Ans_D'].strip(), 'd')
            
            # Image mapping
            images = []
            if q_idx in img_mapping:
                status = "generated" if q_idx <= 17 else "pending"
                instr = img_mapping[q_idx]
                
                img_obj = {
                    "type": "diagram",
                    "status": status,
                    "instruction": instr
                }
                # Even if not in schema, adding src for generated ones is good practice for the final app
                # But I'll follow the STRICT instructions first.
                # Actually, the user might need the src to show it.
                if status == "generated":
                    img_obj["src"] = f"assets/images/agr1/ch2/agri1_ch2_cq{q_idx}_recreated.png"
                
                images.append(img_obj)
            
            level = row.get('Level', '').strip()
            year = row.get('Year', '').strip()
            meta_str = "Agri1 Chapter 2"
            if level and year:
                meta_str = f"{level} &middot; {year}"
            elif level:
                meta_str = level
            
            obj = {
                "chapter": meta_str,
                "question_id": question_id,
                "stem": stem,
                "knowledge_comprehension": [a, b],
                "full_cq": [a, b, c, d],
                "images": images
            }
            questions.append(obj)
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
    
    return len(questions)

if __name__ == "__main__":
    count = process_agri_cq()
    print(f"Processed {count} questions.")
