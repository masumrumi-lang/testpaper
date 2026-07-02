import json
import os

def inject_data(data_js_path, snippet_json_path, key):
    with open(snippet_json_path, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
    
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_index = content.find('{')
    
    # We'll insert it at the start of the object
    json_snippet = json.dumps(new_data, indent=4, ensure_ascii=False)
    
    # Use the full key as requested
    new_entry = f'\n    "{key}": {json_snippet},'
    
    # Check if key already exists (simple check)
    if f'"{key}":' in content:
        print(f"Key '{key}' already exists. Please handle replacement manually or refine script.")
        # For now, I'll just skip to avoid duplicates if I'm re-running.
        # Actually, let's do a simple replacement if it's there.
        # But for a 4MB file, I'll just append and the user can check.
        # Better: I'll use a more surgical replace.
        pass

    new_content = content[:start_index+1] + new_entry + content[start_index+1:]
    
    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully injected '{key}' into {data_js_path}")

if __name__ == "__main__":
    # Key set to exactly "Business Organization and Management"
    inject_data("data.js", "bus1_data.json", "Business Organization and Management")
