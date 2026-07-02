import os

file_path = r'c:\Users\BMTF\.antigravity\testpaper\data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '"fin1":' in line:
            print(f"FOUND fin1 at line {i+1}: {line.strip()}")
            # Check a few lines after to see the structure
            break
