import csv
import json
import os
import sys

def sanitize(text):
    if not text:
        return ""
    # Normalize line endings and strip whitespace
    return text.replace('\r\n', '\n').strip()

def process():
    csv_path = 'Fin1_Ch5_CQ - Sheet1.csv'
    js_path = 'data.js'
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    full_cq_data = []
    short_cq_data = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, 1):
                # Validation: Skip if mandatory fields are missing
                stem = sanitize(row.get('Stem'))
                q_a = sanitize(row.get('Question_A'))
                ans_a = sanitize(row.get('Ans_A'))
                q_b = sanitize(row.get('Question_B'))
                ans_b = sanitize(row.get('Ans_B'))
                
                if not stem and not q_a:
                    continue # Empty row
                
                meta = f"{row.get('Level', '-')} · {row.get('Year', '-')}"
                q_type = row.get('Category', 'board').lower()
                
                # 1. Build Short CQ Data (Parts A and B) - Knowledge & Comprehension
                if q_a:
                    short_cq_data.append({
                        "id": f"fin1-ch5-short-a-{i:03}",
                        "text": q_a,
                        "answer": ans_a,
                        "meta": meta,
                        "type": q_type
                    })
                if q_b:
                    short_cq_data.append({
                        "id": f"fin1-ch5-short-b-{i:03}",
                        "text": q_b,
                        "answer": ans_b,
                        "meta": meta,
                        "type": q_type
                    })
                
                # 2. Build Full CQ Data
                full_cq_data.append({
                    "id": f"fin1-ch5-cq-{i:03}",
                    "stem": stem,
                    "meta": meta,
                    "type": q_type,
                    "questions": [
                        {"label": "a", "text": q_a, "answer": ans_a},
                        {"label": "b", "text": q_b, "answer": ans_b},
                        {"label": "c", "text": sanitize(row.get('Question_C')), "answer": sanitize(row.get('Ans_C'))},
                        {"label": "d", "text": sanitize(row.get('Question_D')), "answer": sanitize(row.get('Ans_D'))}
                    ]
                })

        print(f"Parsed {len(full_cq_data)} Full CQs and {len(short_cq_data)} Short CQs.")

        # Read data.js
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()

        # Marker-based replacement
        markers = [
            ("// === FIN1_CH5_SHORTCQ_START ===", "// === FIN1_CH5_SHORTCQ_END ===", short_cq_data),
            ("// === FIN1_CH5_FULLCQ_START ===", "// === FIN1_CH5_FULLCQ_END ===", full_cq_data)
        ]

        for start_m, end_m, new_data in markers:
            start_idx = js_content.find(start_m)
            end_idx = js_content.find(end_m)
            if start_idx == -1 or end_idx == -1:
                print(f"Error: Could not find markers {start_m} and {end_m} in data.js")
                return

            prefix = js_content[:start_idx + len(start_m)]
            suffix = js_content[end_idx:]
            
            # Generate JSON string
            json_str = json.dumps(new_data, ensure_ascii=False, indent=4)
            # Strip the outer [] if we are putting them inside an existing array structure
            # However, in my marker setup, I put markers INSIDE the brackets:
            # shortCQData: [
            # // === START ===
            # // === END ===
            # ]
            # So I should strip the outer brackets.
            inner_json = json_str.strip().strip('[]').strip()
            
            js_content = f"{prefix}\n{inner_json}\n{suffix}"

        # Write back to data.js
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
            
        print("SUCCESS: Data injected into data.js")
        
        # Final Syntax Validation
        import subprocess
        print("Running syntax validation...")
        result = subprocess.run(['node', '-c', 'data.js'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Syntax Validation: PASSED")
        else:
            print("Syntax Validation: FAILED")
            print(result.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    process()
