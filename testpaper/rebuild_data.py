import os

def clean_rebuild():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Identify the start of agr1 and start of ict
    start_marker = '/* AGRI1_CHAPTER1_CQ_START */'
    end_marker = '"ict": {'
    
    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker)
    
    if start_pos == -1 or end_pos == -1:
        print("Markers not found")
        return
        
    # We want to keep everything before start_marker
    # and everything from end_marker onwards.
    # In between, we want a clean agr1 block.
    
    # Let's extract the current agr1 content to salvage it
    agr1_raw = content[start_pos:end_pos]
    
    # Now, let's try to extract Chapter 1 and Chapter 2 separately
    # and re-assemble them.
    
    # Or better yet, just fix the braces in the block we have
    # I suspect there's an extra brace at the end of Chapter 1
    
    import re
    # Remove the premature closure of agr1 if it exists
    # It would look like "    }," followed by a marker or "2":
    fixed_agr1 = re.sub(r'\},\s*/\* AGRI1_CHAPTER1_CQ_END \*/', r'},', agr1_raw)
    
    # Actually, I'll just look for any level-0 braces and indent them
    # and then ensure there is exactly one level-0 brace at the end.
    
    lines = agr1_raw.splitlines()
    balanced_lines = []
    level = 0
    for line in lines:
        stripped = line.strip()
        # Simple heuristic: if it's a closing brace and it's at indent 0, it's likely wrong
        if stripped == '},' and not line.startswith(' '):
            balanced_lines.append('        ' + stripped)
        elif stripped == '}' and not line.startswith(' '):
            balanced_lines.append('        ' + stripped)
        else:
            balanced_lines.append(line)
            
    # Now assemble a clean block
    new_agr1_block = '\n'.join(balanced_lines)
    # Ensure it ends with exactly one closure for agr1
    new_agr1_block = new_agr1_block.rstrip()
    if not new_agr1_block.endswith(','):
        new_agr1_block += ','
    if not new_agr1_block.endswith('    },\n'):
         # Add it if missing
         pass
    
    # Actually, I'll just force the structure:
    # /* START */
    # "agr1": {
    #    "1": { ... },
    #    "2": { ... }
    # },
    
    # I'll just use a more reliable way:
    # 1. Find all content for "1": { ... }
    # 2. Find all content for "2": { ... }
    # 3. Wrap them in "agr1": { ... }
    
    c1_match = re.search(r'("1":\s*\{.*?\n\s*\})', content, re.DOTALL)
    c2_match = re.search(r'("2":\s*\{.*?\n\s*\})', content, re.DOTALL)
    
    if c1_match and c2_match:
        c1_text = c1_match.group(1)
        c2_text = c2_match.group(1)
        
        new_agr1 = f'    "agr1": {{\n        {c1_text},\n        {c2_text}\n    }},\n'
        
        # Replace the whole area
        final_content = content[:start_pos] + start_marker + '\n' + new_agr1 + '\n    ' + content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        print("Cleanly rebuilt agr1 block")

clean_rebuild()
