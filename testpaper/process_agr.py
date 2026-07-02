import csv
import json
import re

def format_text(text):
    if not text:
        return ""
    
    # 1. Italicize scientific names
    species = [
        "Oryza sativa", "Labeo rohita", "Anabaena azollae", "Trichoderma harzianum",
        "Catla catla", "Cirrhinus cirrhosus", "Tenualosa ilisha", "Azolla pinnata",
        "Corchorus capsularis", "Corchorus olitorius", "Triticum aestivum",
        "Saccharum officinarum", "Gossypium herbaceum", "Brassica napus",
        "Lens culinaris", "Cicer arietinum", "Ipomoea batatas", "Solanum tuberosum",
        "Zea mays", "Rhizobium", "Azolla", "Chondrichthyes", "Pythium", "Fusarium", "Anabaena"
    ]
    for s in species:
        # Use regex to avoid double wrapping or partial matches
        text = re.sub(rf'\b{s}\b', f'<i>{s}</i>', text, flags=re.IGNORECASE)

    # 2. Unit Standardization: Celsius
    text = text.replace("Celsius", "°C")
    text = re.sub(r'(\d+)\s*(degree\s*C|deg\s*C|°\s*C|C\s+)', r'\1°C ', text)

    # 3. Bold soil pH
    text = re.sub(r'\b(pH\s*\d+\.?\d*)\b', r'<b>\1</b>', text)

    # 4. Chemical Formulas (Subscripts via KaTeX)
    def chem_sub(m):
        formula = m.group(0)
        # Add underscores before numbers if they follow letters or parentheses
        formatted = re.sub(r'([A-Za-z)])(\d+)', r'\1_\2', formula)
        return f'${formatted}$'

    # Match common agricultural formulas
    chem_regex = r'\b(CO\(NH2\)2|Ca\(H2PO4\)2|KCl|K2SO4|CaSO4|CaCO3|NH4NO3|H2O|P2O5|SiO2|CaO|NH4|NO3|PO4)\b'
    text = re.sub(chem_regex, chem_sub, text)

    # Special handling for hydrates and dots
    text = text.replace(" . H2O", " \\cdot H_2O")
    text = text.replace(" . 2H2O", " \\cdot 2H_2O")
    
    # Common names mapping
    chem_map = {
        "TSP": r"TSP ($Ca(H_2PO_4)_2 \cdot H_2O$)",
        "MOP": r"MOP ($KCl$)",
        "DAP": r"DAP ($(NH_4)_2HPO_4$)",
        "Urea": r"Urea ($CO(NH_2)_2$)",
        "Gypsum": r"Gypsum ($CaSO_4 \cdot 2H_2O$)"
    }
    for k, v in chem_map.items():
        if k in text and "$" not in text[text.find(k):text.find(k)+5]:
             text = text.replace(k, v)

    # Wrap in <p> if not already
    if not text.startswith("<p>") and not text.startswith("<div"):
        text = f"<p>{text}</p>"
    
    return text
def process_csv(file_path):
    database = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) < 11: continue
            
            # Better shift detection
            # Correct Answer should be exactly one of 'a', 'b', 'c', 'd'
            # Check row[10] (standard) and row[9] (shifted)
            
            if row[9].strip().lower() in ['a', 'b', 'c', 'd'] and len(row[10].strip()) > 1:
                is_shifted = True
            elif row[10].strip().lower() in ['a', 'b', 'c', 'd']:
                is_shifted = False
            else:
                # Ambiguous or error, default to non-shifted but log it
                is_shifted = False
            
            if is_shifted:
                q_text = row[5]
                opt_a = row[6]
                opt_b = row[7]
                opt_c = row[8]
                opt_d = "i, ii & iii" 
                correct_ans_raw = row[9]
                explanation_raw = row[10]
            else:
                q_text = row[5]
                opt_a = row[6]
                opt_b = row[7]
                opt_c = row[8]
                opt_d = row[9]
                correct_ans_raw = row[10]
                explanation_raw = row[11] if len(row) > 11 else ""

            chapter_str = row[2].replace("Chapter ", "").strip()
            chapter_num = chapter_str
            
            if chapter_num not in database:
                database[chapter_num] = {
                    "subjectName": "Agriculture 1st Paper",
                    "chapterName": f"Chapter {chapter_num}",
                    "mcqData": []
                }
            
            chapter_names = {
                "1": "Agriculture of Bangladesh",
                "2": "Land Related Agricultural Technology",
                "3": "Special Production Related Agricultural Technology",
                "4": "Agriculture and Climate",
                "5": "Field and Horticultural Crop Production",
                "6": "Processing and Preservation of Fruits and Vegetables"
            }
            database[chapter_num]["chapterName"] = f"Chapter {chapter_num} : " + chapter_names.get(chapter_num, f"Chapter {chapter_num}")

            # Metadata Patch
            year = row[0]
            level = row[3]
            if year == "N/A":
                meta = f"{level} · General Practice"
            else:
                meta = f"{level} · {year}"
            
            clean_ans = correct_ans_raw.strip().lower()
            if len(clean_ans) == 1 and 'a' <= clean_ans <= 'd':
                correct_ans_idx = ord(clean_ans) - ord('a')
            else:
                # Fallback or search in the string
                if 'a' in clean_ans[:2]: correct_ans_idx = 0
                elif 'b' in clean_ans[:2]: correct_ans_idx = 1
                elif 'c' in clean_ans[:2]: correct_ans_idx = 2
                elif 'd' in clean_ans[:2]: correct_ans_idx = 3
                else: correct_ans_idx = 0

            mcq = {
                "id": len(database[chapter_num]["mcqData"]) + 1,
                "text": format_text(q_text),
                "meta": meta,
                "type": row[4].lower(),
                "options": [opt_a, opt_b, opt_c, opt_d],
                "correctAnswer": correct_ans_idx,
                "explanation": format_text(explanation_raw)
            }
            database[chapter_num]["mcqData"].append(mcq)
    
    return database

def update_data_js(new_data):
    js_path = 'c:/Users/BMTF/.antigravity/testpaper/data.js'
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the testDatabase object
    # We want to insert "agr1": { ... } into the testDatabase object
    # Since it's a large file, we can use a more surgical approach or rewrite the part.
    
    # Let's convert new_data to JSON string
    new_data_json = json.dumps(new_data, indent=4, ensure_ascii=False)
    
    # Check if agr1 already exists
    if '"agr1":' in content:
        # Replace existing agr1
        # This is tricky with regex if it's nested. 
        # Simpler: load the whole thing as JS if possible? No, it's 2MB.
        # Let's use a marker or just replace the whole section.
        pass
    
    # Alternative: use a separate file for agr1 data or append to data.js
    # But the app expects testDatabase.agr1
    
    # For now, let's just create a separate file and tell the user to include it, 
    # OR try to append it to the testDatabase object.
    
    # Let's try to find where testDatabase ends or where to insert.
    # It starts with const testDatabase = {
    
    # I'll just write the agr1 part to a new file and then use a python script to merge.
    with open('agr1_data.json', 'w', encoding='utf-8') as f:
        f.write(new_data_json)

if __name__ == "__main__":
    data = process_csv('c:/Users/BMTF/.antigravity/testpaper/agriculture1_FINAL_CLEANED.csv')
    update_data_js(data)
    print("Processed and saved to agr1_data.json")
