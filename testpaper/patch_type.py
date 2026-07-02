import json
import csv

def patch_type():
    csv_path = 'Agri1_Ch2_CQ - Sheet1.csv'
    json_path = 'agr1_ch2_data.json'
    
    # Read CSV
    type_dict = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            q_id = f"agr1_ch2_cq{i+1}"
            category = row.get('Category', '').strip().lower()
            if category == 'college':
                type_dict[q_id] = 'college'
            else:
                type_dict[q_id] = 'board'
                
    # Update JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for q in data:
        qid = q.get('question_id')
        if qid in type_dict:
            q['type'] = type_dict[qid]
            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    patch_type()
    print("Patched type in agr1_ch2_data.json")
