import json
import re

def surgical_inject():
    print("Starting surgical injection of Agriculture fullCQData...")
    
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Load the new data
    with open('agr1_ch1_data.json', 'r', encoding='utf-8') as f:
        ch1_cq = json.load(f)
    with open('agr1_ch2_data.json', 'r', encoding='utf-8') as f:
        ch2_cq = json.load(f)
    
    # Find the agr1 block
    agr1_match = re.search(r'"agr1":\s*{', content)
    if not agr1_match:
        print("Error: agr1 block not found in data.js")
        return
    
    agr1_start = agr1_match.start()
    
    def inject_to_chapter(subject_content, ch_num, cq_data):
        ch_key = f'"{ch_num}":'
        ch_start = subject_content.find(ch_key)
        if ch_start == -1:
            print(f"Error: Chapter {ch_num} not found in subject block")
            return subject_content
        
        # Find the end of mcqData or where we want to insert
        # We look for the closing brace of mcqData or just before the closing brace of the chapter object
        # The chapter object looks like: "1": { ... }
        # We find the matching closing brace for the chapter object
        brace_count = 0
        obj_start = subject_content.find('{', ch_start)
        if obj_start == -1: return subject_content
        
        obj_end = -1
        for i in range(obj_start, len(subject_content)):
            if subject_content[i] == '{':
                brace_count += 1
            elif subject_content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    obj_end = i
                    break
        
        if obj_end == -1:
            print(f"Error: Could not find closing brace for Chapter {ch_num}")
            return subject_content
            
        # Check if fullCQData already exists to avoid duplicates
        full_cq_key = '"fullCQData":'
        existing_pos = subject_content.find(full_cq_key, ch_start, obj_end)
        
        cq_json = json.dumps(cq_data, indent=12, ensure_ascii=False)
        
        if existing_pos != -1:
            print(f"Warning: fullCQData already exists for Chapter {ch_num}. Replacing...")
            # Find the end of the existing array
            array_start = subject_content.find('[', existing_pos)
            bracket_count = 0
            array_end = -1
            for i in range(array_start, len(subject_content)):
                if subject_content[i] == '[':
                    bracket_count += 1
                elif subject_content[i] == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        array_end = i + 1
                        break
            
            if array_end != -1:
                # Replace the existing array
                new_content = subject_content[:array_start] + cq_json + subject_content[array_end:]
                return new_content
            else:
                print(f"Error: Could not find end of existing fullCQData array for Chapter {ch_num}")
                return subject_content
        
        # If it doesn't exist, insert before the closing brace
        insertion = f',\n            "fullCQData": {cq_json}'
        new_content = subject_content[:obj_end] + insertion + subject_content[obj_end:]
        return new_content

    # Extract the agr1 block to operate on it safely
    # Find the end of the agr1 block
    brace_count = 0
    agr1_obj_start = content.find('{', agr1_start)
    agr1_obj_end = -1
    for i in range(agr1_obj_start, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                agr1_obj_end = i
                break
                
    if agr1_obj_end == -1:
        print("Error: Could not find closing brace for agr1 block")
        return

    agr1_block = content[agr1_start:agr1_obj_end+1]
    
    # Inject Chapter 1
    agr1_block = inject_to_chapter(agr1_block, "1", ch1_cq)
    # Inject Chapter 2
    agr1_block = inject_to_chapter(agr1_block, "2", ch2_cq)
    
    # Reassemble the file
    final_content = content[:agr1_start] + agr1_block + content[agr1_obj_end+1:]
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("Surgical injection complete. Verifying syntax...")

if __name__ == "__main__":
    surgical_inject()
