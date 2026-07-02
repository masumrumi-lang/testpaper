import json
import re

def inspect_data():
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find the Finance 1st Paper block
    # It might be double quoted or single quoted
    match = re.search(r'["\']Finance 1st Paper["\']:\s*\{', content)
    if not match:
        print("Finance 1st Paper not found")
        return

    # Extract some content after the match
    start = match.start()
    print(content[start:start+2000])

if __name__ == "__main__":
    inspect_data()
