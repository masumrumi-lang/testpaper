import json
import os

def inject():
    # Load extracted data
    with open('extracted_cq.json', 'r', encoding='utf-8') as f:
        cq_data = json.load(f)

    # Prepare the new CQ object
    new_cq = {
        "id": "acc2_ch4_cq1",
        "stem": cq_data["stimulus"].replace("\n", "<br>"),
        "meta": "Dhaka Board · 2025",
        "type": "board",
        "questions": [
            {
                "label": "a",
                "text": cq_data["requirements"]["a"],
                "answer": cq_data["solutions"]["a"].replace("\n", "<br>")
            },
            {
                "label": "b",
                "text": cq_data["requirements"]["b"],
                "answer": cq_data["solutions"]["b"].replace("\n", "<br>")
            },
            {
                "label": "c",
                "text": cq_data["requirements"]["c"],
                "answer": cq_data["solutions"]["c"].replace("\n", "<br>")
            }
        ]
    }

    # Prepare the acc2 structure
    acc2_data = {
        "4": {
            "subjectName": "Accounting 2nd Paper",
            "chapterName": "Chapter 4: Capital of Joint Stock Companies",
            "mcqData": [],
            "cqData": [new_cq]
        }
    }

    # Convert to JS string (minimal formatting to match style)
    acc2_js = json.dumps({"acc2": acc2_data}, indent=4, ensure_ascii=False)
    # Remove outer braces to just get the "acc2": { ... } part
    acc2_js = acc2_js.strip()[1:-1].strip()

    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of acc1 or start of next subject
    # Or just insert before "ict": {
    target = '"ict": {'
    idx = content.find(target)
    
    if idx == -1:
        # Fallback to end of object before };
        idx = content.rfind('};')
        if idx == -1:
            print("Could not find insertion point")
            return

    # Insert acc2
    new_content = content[:idx] + acc2_js + ",\n\n    " + content[idx:]

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Injected acc2 chapter 4 cq1 successfully")

if __name__ == "__main__":
    inject()
