import os

def seal_agri_block():
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 1. Add Chapter 2 end marker
    # 2. Ensure agr1 block is closed before ict
    
    ict_line_idx = -1
    for i, line in enumerate(lines):
        if '"ict":' in line:
            ict_line_idx = i
            break
    
    if ict_line_idx == -1:
        print("Could not find 'ict' block start.")
        return

    # Check for closing brace of agr1
    # It should be at lines[ict_line_idx - 1] or similar
    # In my last view, it was:
    # 67397:     /* AGRI1_CHAPTER1_CQ_END */
    # 67398: 
    # 67399: "ict": {
    
    # We want it to be:
    # },
    # /* AGRI1_CHAPTER2_CQ_END */
    # 
    # "ict": {
    
    # Let's remove the misplaced Chapter 1 end marker if it's there
    marker_1_end = '/* AGRI1_CHAPTER1_CQ_END */'
    marker_2_end = '/* AGRI1_CHAPTER2_CQ_END */'
    
    new_lines = []
    for line in lines:
        if marker_1_end in line:
            # We'll re-place it correctly later or just keep it if it's in the right place
            # Actually, let's just leave it and add the new ones.
            new_lines.append(line)
        else:
            new_lines.append(line)
            
    # Find insertion point: after the closing brace of "2":
    # My injection added:
    # "2": { ... },
    # So we need to find that closing brace.
    
    # Re-read and find the "2": block end
    # Actually, it's easier to just find the 'ict' line and insert before it.
    
    # We want:
    #     },
    #     /* AGRI1_CHAPTER2_CQ_END */
    # 
    # "ict": {
    
    # Find where "2": ends. It's the last "}," before "ict"
    insertion_idx = -1
    for i in range(ict_line_idx - 1, 0, -1):
        if '},' in lines[i]:
            insertion_idx = i + 1
            break
            
    if insertion_idx != -1:
        # Check if there is already a closing brace for the parent object
        # If the indentation of lines[insertion_idx-1] is for "2":, then it's not the parent.
        # "2": is at level 2. Parent "agr1" is at level 1.
        
        # Let's just insert the closing brace and markers.
        seal = [
            '    },\n',
            f'    {marker_2_end}\n',
            '\n'
        ]
        
        # Check if we already have a brace
        if '}' in lines[ict_line_idx - 1]:
             # Maybe it's already sealed?
             pass
        else:
             for s in reversed(seal):
                 lines.insert(ict_line_idx, s)
                 
        with open('data.js', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Sealed agr1 block.")
    else:
        print("Could not find insertion point.")

if __name__ == "__main__":
    seal_agri_block()
