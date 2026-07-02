import os

def final_repair():
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    # We will identify the problematic lines by their content and proximity to markers
    for i, line in enumerate(lines):
        # 1. Remove the premature closure of testDatabase (if any)
        # 2. Fix the closure of Chapter 2 and Subject agr1
        
        # If we see a line that is JUST "}," at the very start (indent 0)
        # between Chapter 2 and ICT, it's likely the error.
        if i > 66000 and line.strip() == '},' and not line.startswith(' '):
             # This is a premature closure at indent 0
             # We should probably indent it if it was meant for Chapter 2
             new_lines.append('        },\n')
             continue
             
        new_lines.append(line)

    # Ensure the transition to ICT is clean
    # "agr1": {
    #   "1": { ... },
    #   "2": { ... }
    # },
    # "ict": { ... }
    
    # I'll just write a fresh tail for the file starting from Chapter 1's end
    
    # Actually, I'll just use a simpler approach: 
    # Remove all "}," lines that are at indent 0 between agr1 and ict.
    
    # Let's try this:
    with open('data.js', 'r', encoding='utf-8') as f:
        full_text = f.read()
    
    import re
    # Find the area between agr1 and ict
    pattern = re.compile(r'("agr1":\s*\{.*?)("ict":\s*\{)', re.DOTALL)
    match = pattern.search(full_text)
    if match:
        block = match.group(1)
        # Remove any line that is exactly "}," at indent 0
        fixed_block = re.sub(r'\n\},\n', r'\n', block)
        # Ensure it ends with exactly one "    },\n"
        fixed_block = fixed_block.strip()
        if not fixed_block.endswith('}'):
             # Find last } and ensure it's closed
             pass
        fixed_block += '\n    },\n'
        
        new_text = full_text[:match.start(1)] + fixed_block + full_text[match.start(2):]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Surgically repaired data.js")

final_repair()
