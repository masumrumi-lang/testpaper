import os

def extract_block(text, start_pos):
    # Find the start { after start_pos
    brace_start = text.find('{', start_pos)
    if brace_start == -1: return None, -1
    
    level = 1
    pos = brace_start + 1
    while level > 0 and pos < len(text):
        if text[pos] == '{': level += 1
        elif text[pos] == '}': level -= 1
        pos += 1
    
    return text[brace_start:pos], pos

def robust_rebuild():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find "1": {
    c1_key_pos = content.find('"1": {')
    if c1_key_pos == -1: 
        print("C1 not found")
        return
    c1_obj, _ = extract_block(content, c1_key_pos)
    
    # Find "2": {
    c2_key_pos = content.find('"2": {')
    if c2_key_pos == -1: 
        print("C2 not found")
        return
    c2_obj, _ = extract_block(content, c2_key_pos)
    
    if not c1_obj or not c2_obj: 
        print("Extraction failed")
        return
    
    start_marker = '/* AGRI1_CHAPTER1_CQ_START */'
    ict_key = '"ict": {'
    
    start_pos = content.find(start_marker)
    ict_pos = content.find(ict_key)
    
    if start_pos == -1 or ict_pos == -1:
        print("Markers not found")
        return
        
    new_agr1 = f'    "agr1": {{\n        "1": {c1_obj},\n        "2": {c2_obj}\n    }},\n'
    
    final_content = content[:start_pos] + start_marker + '\n' + new_agr1 + '    ' + content[ict_pos:]
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Robustly rebuilt agr1 block")

robust_rebuild()
