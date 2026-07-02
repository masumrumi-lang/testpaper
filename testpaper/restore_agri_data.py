import json
import re

def restore():
    print("Loading correct Agriculture data...")
    with open('agr1_data.json', 'r', encoding='utf-8') as f:
        correct_data = json.load(f)

    # Filter to only include chapters 1 and 2 if needed, 
    # but the user said "fix it" and the file has 1-6. 
    # Usually it's better to restore everything if it's correct.
    # However, let's stick to what's expected. 
    # Actually, if I have 1-6, I'll restore 1-6. It's safer.
    
    print("Formatting Javascript object...")
    # Convert to JSON and then tweak for JS (optional, JSON is valid JS)
    # But we want it to look nice.
    js_object = json.dumps(correct_data, indent=4, ensure_ascii=False)
    
    # Prepend key
    new_block = '    "agr1": ' + js_object + ',\n\n'

    print("Reading data.js...")
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = '/* AGRI1_CHAPTER1_CQ_START */'
    end_marker = '"ict": {'

    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("Start marker not found! Trying fallback...")
        # Fallback: find "agr1": {
        start_pos = content.find('"agr1": {')
        if start_pos == -1:
            print("Could not find start point!")
            return
    else:
        # Keep the marker
        start_pos += len(start_marker)

    end_pos = content.find(end_marker)
    if end_pos == -1:
        print("End marker 'ict' not found!")
        return

    print(f"Replacing content from {start_pos} to {end_pos}...")
    
    final_content = content[:start_pos] + '\n' + new_block + '    ' + content[end_pos:]

    print("Writing restored data.js...")
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("Success!")

if __name__ == "__main__":
    restore()
