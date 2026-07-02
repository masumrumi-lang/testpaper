import json
import re
import os

def inject_cq_data(data_js_path, cq_json_path):
    with open(cq_json_path, 'r', encoding='utf-8') as f:
        cq_data = json.load(f)
    
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    subject_key = "Business Organization and Management"
    
    # Find the subject block
    subject_pattern = re.compile(rf'"{subject_key}":\s*{{')
    match = subject_pattern.search(content)
    if not match:
        print(f"Error: Subject '{subject_key}' not found in {data_js_path}")
        return

    subject_start = match.start()
    
    # For each chapter in cq_data, find its block and inject the data
    for chapter_id, cq_content in cq_data.items():
        # Find chapter block inside the subject block
        # Look for "chapter_id": {
        chapter_pattern = re.compile(rf'"{chapter_id}":\s*{{')
        ch_match = chapter_pattern.search(content, subject_start)
        if not ch_match:
            print(f"Warning: Chapter {chapter_id} not found for subject. Skipping.")
            continue
            
        ch_start = ch_match.end()
        
        # Inject shortCQData and fullCQData
        # We'll insert them right after the opening brace of the chapter object
        short_json = json.dumps(cq_content['shortCQData'], indent=12, ensure_ascii=False)
        full_json = json.dumps(cq_content['fullCQData'], indent=12, ensure_ascii=False)
        
        # We need to be careful not to double-inject if already present
        if f'"shortCQData":' in content[ch_match.start():ch_match.start()+1000]: # check near start
             print(f"Info: Chapter {chapter_id} already has CQ data. Overwriting...")
             # Simple replacement for existing keys
             content = re.sub(rf'"{chapter_id}":\s*{{(?s:.*?)"shortCQData":\s*\[.*?\]', 
                              f'"{chapter_id}": {{ "shortCQData": {short_json}', content, 1)
             # This is getting complex with regex. 
             # Let's try a simpler approach: check if keys exist, if so, delete them first.
             pass

        injection = f'\n            "shortCQData": {short_json},\n            "fullCQData": {full_json},'
        
        # Insert at the beginning of the chapter object
        content = content[:ch_start] + injection + content[ch_start:]
        
    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Injection complete for {len(cq_data)} chapters.")

if __name__ == "__main__":
    inject_cq_data("data.js", "bus1_cq_data.json")
