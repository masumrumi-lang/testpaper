import re

def check_syntax(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if '"ict": {' in line:
            print(f"Line {i+1}: {line.strip()}")
            print(f"Line {i}: {lines[i-1].strip()}")
            print(f"Line {i-1}: {lines[i-2].strip()}")
            break

check_syntax(r"c:\Users\BMTF\.antigravity\testpaper\data.js")
