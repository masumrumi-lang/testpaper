import json
import csv

def patch_meta():
    csv_path = 'Agri1_Ch2_CQ - Sheet1.csv'
    json_path = 'agr1_ch2_data.json'
    
    # Read CSV
    meta_dict = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            q_id = f"agr1_ch2_cq{i+1}"
            level = row.get('Level', '').strip()
            year = row.get('Year', '').strip()
            if level and year:
                meta_dict[q_id] = f"{level} &middot; {year}"
            elif level:
                meta_dict[q_id] = level
                
    # Update JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for q in data:
        qid = q.get('question_id')
        if qid in meta_dict:
            q['chapter'] = meta_dict[qid]
            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    patch_meta()
    print("Patched metadata in agr1_ch2_data.json")
