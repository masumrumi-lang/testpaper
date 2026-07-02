import re
import os

def check_chapters():
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'["\']fin1["\']:\s*\{', content)
    if not match:
        print("fin1 not found")
        return
    
    start = match.start()
    # Find the end of the fin1 block by matching braces
    brace_count = 0
    end = -1
    for i in range(start, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break
    
    fin1_content = content[start:end]
    
    # Check for keys "1", "2", "3" etc inside fin1_content
    chapters = re.findall(r'["\'](\d+)["\']:\s*\{', fin1_content)
    print(f"Chapters in fin1: {chapters}")

if __name__ == "__main__":
    check_chapters()
