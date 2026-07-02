import os
import re

search_dir = r"c:\Users\BMTF\.antigravity\testpaper"
results = []

for root, dirs, files in os.walk(search_dir):
    # skip .git, .venv, etc.
    if any(p in root for p in [".git", ".venv", ".vs", "__pycache__"]):
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.py', '.json')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                matches_agr2 = re.findall(r'agr2', content, re.IGNORECASE)
                matches_agri2 = re.findall(r'agri2', content, re.IGNORECASE)
                if matches_agr2 or matches_agri2:
                    results.append((file, len(matches_agr2), len(matches_agri2)))
            except Exception as e:
                pass

for res in results:
    print(f"File: {res[0]} | 'agr2' matches: {res[1]} | 'agri2' matches: {res[2]}")
