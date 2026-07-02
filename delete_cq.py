import os
import re

def delete_cq():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the acc2 block
    # Since it was the only thing in acc2, we can just remove the acc2 section
    start_marker = '"acc2": {'
    start_idx = content.find(start_marker)
    
    if start_idx != -1:
        # Brace counting to find end of acc2 object
        brace_depth = 0
        i = start_idx + len(start_marker) - 1
        block_end = -1
        while i < len(content):
            if content[i] == '{':
                brace_depth += 1
            elif content[i] == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    block_end = i + 1
                    break
            i += 1
        
        if block_end != -1:
            # Check for trailing comma
            if block_end < len(content) and content[block_end] == ',':
                block_end += 1
            
            # Check for leading comma if it was the last one (but it's usually not)
            # Actually, let's just remove the block and clean up surrounding whitespace
            new_content = content[:start_idx].rstrip() + content[block_end:]
            
            # Clean up potential double commas or empty lines
            new_content = re.sub(r',\s*,', ',', new_content)
            
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully deleted acc2_ch4_cq1 (and acc2 block)")
        else:
            print("Could not find end of acc2 block")
    else:
        print("Could not find acc2 block")

if __name__ == "__main__":
    delete_cq()
