import json
import re

def inspect_agr1():
    try:
        with open('data.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find start of agr1
        match = re.search(r'"agr1":\s*{', content)
        if not match:
            print("agr1 not found")
            return
            
        start_index = match.start()
        
        # Look for chapters
        chapters = ["1", "2"]
        for ch in chapters:
            print(f"--- Chapter {ch} ---")
            ch_key = f'"{ch}":'
            ch_start = content.find(ch_key, start_index)
            if ch_start == -1:
                print(f"Chapter {ch} not found")
                continue
            
            # Find images array
            img_key = '"images":'
            img_start = content.find(img_key, ch_start)
            if img_start == -1:
                print(f"Images for Chapter {ch} not found")
                continue
            
            # Find fullCQData
            cq_key = '"fullCQData":'
            cq_start = content.find(cq_key, ch_start)
            
            # Print a chunk of fullCQData to see first question structure
            if cq_start != -1:
                print("First question structure:")
                print(content[cq_start:cq_start+1000])
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_agr1()
