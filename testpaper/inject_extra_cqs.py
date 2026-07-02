import json
import re

def inject_extra_cqs():
    with open('c:/Users/BMTF/.antigravity/testpaper/finance1_extra_cqs.json', 'r', encoding='utf-8') as f:
        extra_cqs = json.load(f)
    
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapping of IDs to Chapters
    mapping = {
        "EX01": "3",
        "EX02": "7",
        "EX03": "8",
        "EX04": "9",
        "EX05": "5"
    }
    
    for cq in extra_cqs:
        chapter_num = mapping.get(cq['id'])
        if not chapter_num: continue
        
        print(f"Injecting extra CQ {cq['id']} into Chapter {chapter_num}...")
        
        # Find the fin1 block
        fin1_match = re.search(r'["\']fin1["\']:\s*\{', content)
        if not fin1_match:
            print("fin1 not found")
            return
        
        start = fin1_match.start()
        brace_count = 0
        fin1_end = -1
        for i in range(start, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    fin1_end = i + 1
                    break
        
        fin1_content = content[start:fin1_end]
        
        chapter_regex = r'["\']' + chapter_num + r'["\']:\s*\{'
        chapter_match = re.search(chapter_regex, fin1_content)
        
        if not chapter_match:
            print(f"Chapter {chapter_num} not found in fin1")
            continue
        
        ch_start = chapter_match.start()
        brace_count = 0
        ch_end = -1
        for i in range(ch_start, len(fin1_content)):
            if fin1_content[i] == '{':
                brace_count += 1
            elif fin1_content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    ch_end = i + 1
                    break
        
        chapter_content = fin1_content[ch_start:ch_end]
        
        # Inject into fullCQData
        # If fullCQData exists, append to the list
        full_cq_match = re.search(r'fullCQData:\s*\[', chapter_content)
        if full_cq_match:
            list_start = full_cq_match.end()
            # Find the closing bracket of the list
            brace_count = 1
            list_end = -1
            for i in range(list_start, len(chapter_content)):
                if chapter_content[i] == '[':
                    brace_count += 1
                elif chapter_content[i] == ']':
                    brace_count -= 1
                    if brace_count == 0:
                        list_end = i
                        break
            
            cq_json = json.dumps(cq, indent=20, ensure_ascii=False)
            if chapter_content[list_start:list_end].strip():
                # Add a comma if not empty
                new_list_content = chapter_content[list_start:list_end].rstrip() + ",\n" + cq_json + "\n                    ]"
            else:
                new_list_content = "\n" + cq_json + "\n                    ]"
            
            chapter_content = chapter_content[:list_start] + new_list_content + chapter_content[list_end+1:]
        
        # Inject into shortCQData (A and B parts)
        short_cq_a = {
            "id": cq['id'] + "A",
            "text": cq['questions'][0]['text'],
            "meta": "Knowledge · " + cq['meta'],
            "type": cq['type'],
            "answer": cq['questions'][0]['answer']
        }
        short_cq_b = {
            "id": cq['id'] + "B",
            "text": cq['questions'][1]['text'],
            "meta": "Comprehension · " + cq['meta'],
            "type": cq['type'],
            "answer": cq['questions'][1]['answer']
        }
        
        short_cq_match = re.search(r'shortCQData:\s*\[', chapter_content)
        if short_cq_match:
            list_start = short_cq_match.end()
            brace_count = 1
            list_end = -1
            for i in range(list_start, len(chapter_content)):
                if chapter_content[i] == '[':
                    brace_count += 1
                elif chapter_content[i] == ']':
                    brace_count -= 1
                    if brace_count == 0:
                        list_end = i
                        break
            
            short_json = json.dumps(short_cq_a, indent=20, ensure_ascii=False) + ",\n" + json.dumps(short_cq_b, indent=20, ensure_ascii=False)
            if chapter_content[list_start:list_end].strip():
                new_list_content = chapter_content[list_start:list_end].rstrip() + ",\n" + short_json + "\n                    ]"
            else:
                new_list_content = "\n" + short_json + "\n                    ]"
            
            chapter_content = chapter_content[:list_start] + new_list_content + chapter_content[list_end+1:]

        # Update fin1_content and main content
        fin1_content = fin1_content[:ch_start] + chapter_content + fin1_content[ch_end:]
        content = content[:start] + fin1_content + content[fin1_end:]
        
        # Re-search for fin1 because content size changed
        fin1_match = re.search(r'["\']fin1["\']:\s*\{', content)
        start = fin1_match.start()
        brace_count = 0
        fin1_end = -1
        for i in range(start, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    fin1_end = i + 1
                    break

    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Extra CQs injected successfully!")

if __name__ == "__main__":
    inject_extra_cqs()
