import json
import re

def inject_new_subject(data_js_path, cq_json_path, subject_key):
    with open(cq_json_path, 'r', encoding='utf-8') as f:
        cq_data = json.load(f)
    
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Format the new subject data
    subject_json = json.dumps(cq_data, indent=8, ensure_ascii=False)
    new_entry = f'\n    "{subject_key}": {subject_json},'
    
    # Find the start of testDatabase
    match = re.search(r'const testDatabase = \{', content)
    if not match:
        print("Error: testDatabase not found")
        return
        
    insert_pos = match.end()
    
    new_content = content[:insert_pos] + new_entry + content[insert_pos:]
    
    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Subject '{subject_key}' injected successfully.")

if __name__ == "__main__":
    inject_new_subject("data.js", "bus2_cq_data.json", "Business 2nd Paper")
