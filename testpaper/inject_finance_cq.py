import csv
import json
import re
import os

def clean_text(text):
    if not text:
        return ""
    # Replace newlines with <br><br>
    text = text.replace('\n', '<br><br>')
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    return text.strip()

def process_csv():
    csv_path = 'c:/Users/BMTF/.antigravity/testpaper/Finance1 CQ - Sheet5.csv'
    chapters_data = {}

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            chapter = row['Chapter']
            if chapter not in chapters_data:
                chapters_data[chapter] = {'shortCQData': [], 'fullCQData': []}
            
            # Count how many we already have for this chapter to generate ID
            count = len(chapters_data[chapter]['fullCQData']) + 1
            id_base = f"{count:02d}"
            
            meta = f"{row['Category']} · {row['Year']}"
            q_type = row['Level'].lower()
            
            # Full CQ
            full_cq = {
                "id": id_base,
                "stem": clean_text(row['Stem']),
                "meta": meta,
                "type": q_type,
                "questions": [
                    {"label": "a", "text": f"(a) {row['Question_A']}", "answer": clean_text(row['Ans_A'])},
                    {"label": "b", "text": f"(b) {row['Question_B']}", "answer": clean_text(row['Ans_B'])},
                    {"label": "c", "text": f"(c) {row['Question_C']}", "answer": clean_text(row['Ans_C'])},
                    {"label": "d", "text": f"(d) {row['Question_D']}", "answer": clean_text(row['Ans_D'])}
                ]
            }
            chapters_data[chapter]['fullCQData'].append(full_cq)
            
            # Short CQ A
            short_cq_a = {
                "id": id_base + "A",
                "text": f"(a) {row['Question_A']}",
                "meta": f"Knowledge · {meta}",
                "type": q_type,
                "answer": clean_text(row['Ans_A'])
            }
            # Short CQ B
            short_cq_b = {
                "id": id_base + "B",
                "text": f"(b) {row['Question_B']}",
                "meta": f"Comprehension · {meta}",
                "type": q_type,
                "answer": clean_text(row['Ans_B'])
            }
            chapters_data[chapter]['shortCQData'].append(short_cq_a)
            chapters_data[chapter]['shortCQData'].append(short_cq_b)
            
    return chapters_data

def inject_data(chapters_data):
    data_js_path = 'c:/Users/BMTF/.antigravity/testpaper/data.js'
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for chapter_num, data in chapters_data.items():
        print(f"Injecting Chapter {chapter_num}...")
        
        # Find the fin1 block
        fin1_match = re.search(r'["\']fin1["\']:\s*\{', content)
        if not fin1_match:
            print("fin1 not found in data.js")
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
        
        chapter_start_in_fin1 = chapter_match.start()
        brace_count = 0
        chapter_end_in_fin1 = -1
        for i in range(chapter_start_in_fin1, len(fin1_content)):
            if fin1_content[i] == '{':
                brace_count += 1
            elif fin1_content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    chapter_end_in_fin1 = i + 1
                    break
        
        chapter_content = fin1_content[chapter_start_in_fin1:chapter_end_in_fin1]
        
        # Format the JSON strings
        short_cq_json = json.dumps(data['shortCQData'], indent=4, ensure_ascii=False)
        full_cq_json = json.dumps(data['fullCQData'], indent=4, ensure_ascii=False)
        
        # Helper to indent the JSON
        def indent_block(json_str, spaces):
            lines = json_str.split('\n')
            return '\n'.join([' ' * spaces + line for line in lines])
        
        # Check if shortCQData exists in chapter_content
        if 'shortCQData' in chapter_content:
            # Replace existing shortCQData
            # Note: This is a bit tricky with regex if it's empty or has data.
            # But we know it's currently empty: shortCQData: []
            chapter_content = re.sub(r'shortCQData:\s*\[\s*\]', f'shortCQData: {json.dumps(data["shortCQData"], indent=16, ensure_ascii=False)}', chapter_content)
        else:
            # Append before the last brace
            last_brace = chapter_content.rfind('}')
            chapter_content = chapter_content[:last_brace] + f', shortCQData: {json.dumps(data["shortCQData"], indent=16, ensure_ascii=False)}' + chapter_content[last_brace:]

        if 'fullCQData' in chapter_content:
            chapter_content = re.sub(r'fullCQData:\s*\[\s*\]', f'fullCQData: {json.dumps(data["fullCQData"], indent=16, ensure_ascii=False)}', chapter_content)
        else:
            last_brace = chapter_content.rfind('}')
            chapter_content = chapter_content[:last_brace] + f', fullCQData: {json.dumps(data["fullCQData"], indent=16, ensure_ascii=False)}' + chapter_content[last_brace:]
            
        # Update fin1_content
        fin1_content = fin1_content[:chapter_start_in_fin1] + chapter_content + fin1_content[chapter_end_in_fin1:]
        
        # Update the main content
        content = content[:start] + fin1_content + content[fin1_end:]
        
        # Re-search for fin1 for next chapter since content changed
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

    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injection complete!")

if __name__ == "__main__":
    chapters_data = process_csv()
    inject_data(chapters_data)
