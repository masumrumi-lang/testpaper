import os
import re

def delete_cq():
    file_path = 'data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the specific CQ entry
    cq_id = '"id": "acc2_ch4_cq1"'
    start_idx = content.find(cq_id)
    
    if start_idx == -1:
        # Try single quotes
        cq_id = "'id': 'acc2_ch4_cq1'"
        start_idx = content.find(cq_id)
        if start_idx == -1:
            print("CQ entry not found")
            return

    # Move back to the start of the object {
    obj_start = content.rfind('{', 0, start_idx)
    if obj_start == -1:
        print("Could not find start of CQ object")
        return

    # Use brace counting to find the end of the object }
    brace_depth = 0
    obj_end = -1
    for i in range(obj_start, len(content)):
        if content[i] == '{':
            brace_depth += 1
        elif content[i] == '}':
            brace_depth -= 1
            if brace_depth == 0:
                obj_end = i + 1
                break
    
    if obj_end == -1:
        print("Could not find end of CQ object")
        return

    # Handle commas
    # Look ahead for a comma
    final_end = obj_end
    while final_end < len(content) and content[final_end].isspace():
        final_end += 1
    if final_end < len(content) and content[final_end] == ',':
        final_end += 1
    else:
        # Look behind for a comma if it was the last element
        # Actually, if it's the only element, removing it from [ ... ] is easy
        pass

    # Replacement
    new_content = content[:obj_start] + content[final_end:]
    
    # Clean up potentially broken array like [ , ] or empty lines
    new_content = re.sub(r'\[\s*,\s*', '[', new_content)
    new_content = re.sub(r',\s*\]', ']', new_content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully deleted {cq_id} and cleaned up structure.")

if __name__ == "__main__":
    delete_cq()
