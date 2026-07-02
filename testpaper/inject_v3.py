import json
import os

def inject_v3():
    # Load extracted data
    with open('extracted_cq.json', 'r', encoding='utf-8') as f:
        cq_data = json.load(f)

    # Prepare the new CQ object
    new_cq = {
        "id": "acc2_ch4_cq1",
        "stem": cq_data["stimulus"], # Already has <br> from extract script
        "meta": "Dhaka Board · 2025",
        "type": "board",
        "questions": [
            {
                "label": "a",
                "text": cq_data["requirements"]["a"],
                "answer": cq_data["solutions"]["a"]
            },
            {
                "label": "b",
                "text": cq_data["requirements"]["b"],
                "answer": cq_data["solutions"]["b"]
            },
            {
                "label": "c",
                "text": cq_data["requirements"]["c"],
                "answer": cq_data["solutions"]["c"]
            }
        ]
    }

    acc2_data = {
        "4": {
            "subjectName": "Accounting 2nd Paper",
            "chapterName": "Chapter 4: Capital of Joint Stock Companies",
            "mcqData": [],
            "shortCQData": [],
            "fullCQData": [new_cq]
        }
    }

    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = '"acc2": {'
    start_idx = content.find(start_marker)
    
    if start_idx != -1:
        # Brace counting to find end of acc2 object
        brace_depth = 0
        i = start_idx + len(start_marker) - 1
        block_end = -1
        while i < len(content):
            if content[i] == '{':
                brace_depth += 1
            elif content[i] == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    block_end = i + 1
                    break
            i += 1
        
        if block_end != -1:
            acc2_js = json.dumps(acc2_data, indent=4, ensure_ascii=False)
            replacement = f'"acc2": {acc2_js}'
            new_content = content[:start_idx] + replacement + content[block_end:]
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully injected V3 (compact tables)")
        else:
            print("Could not find end of acc2 block")
    else:
        print("Could not find acc2 block")

if __name__ == "__main__":
    inject_v3()
