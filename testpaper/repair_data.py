import os

def repair_data_js():
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # We want to find the area between agr1 start and ict start
    # and fix the braces.
    
    agr1_start = -1
    ict_start = -1
    for i, line in enumerate(lines):
        if '"agr1": {' in line:
            agr1_start = i
        if '"ict": {' in line:
            ict_start = i
            break
            
    if agr1_start == -1 or ict_start == -1:
        print("Could not find blocks.")
        return

    # Extract the lines for agr1
    agr1_lines = lines[agr1_start:ict_start]
    
    # We need to find the erroneous closing braces at indent 0
    # and fix them.
    
    new_lines = lines[:agr1_start]
    
    # Process agr1 lines
    # We'll just re-indent them properly or just fix the obvious ones.
    
    # Actually, a better way:
    # 1. Find "2": {
    # 2. Find its closing brace (currently at indent 0)
    # 3. Indent it.
    
    # Let's just do a simple replacement for the problematic block we saw
    fixed_agr1 = []
    for line in agr1_lines:
        if line.strip() == '},' and not line.startswith(' '):
            # This is likely the misplaced brace at 67396
            fixed_agr1.append('        },\n')
        elif line.strip() == '},' and line.startswith('    '):
             # This is the one at 67399
             fixed_agr1.append('    },\n')
        else:
            fixed_agr1.append(line)
            
    # Also ensure there is a comma before ict
    if not fixed_agr1[-1].strip().endswith(','):
        if fixed_agr1[-1].strip() == '}':
            fixed_agr1[-1] = fixed_agr1[-1].replace('}', '},')
            
    new_lines.extend(fixed_agr1)
    new_lines.extend(lines[ict_start:])
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Repaired data.js")

if __name__ == "__main__":
    repair_data_js()
