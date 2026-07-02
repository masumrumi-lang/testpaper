import csv
import json
import os
import sys

def sanitize(text):
    if not text:
        return ""
    return text.replace('\r\n', '\n').strip()

def process():
    csv_path = 'Fin1_Ch2_CQ - Sheet1.csv'
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
                if not row.get('Stem') or not row.get('Question_A'):
                    print(f"Skipping row {i+1} due to missing data.")
                    continue
                
                meta = f"{row.get('Level', '-')} · {row.get('Year', '-')}"
                q_type = row.get('Category', 'board').lower()
                
                # 1. Build Short CQ Data (Parts A and B)
                # Part A
                short_cq_data.append({
                    "id": f"fin1-ch2-short-a-{i:03}",
                    "text": sanitize(row.get('Question_A')),
                    "answer": sanitize(row.get('Ans_A')),
                    "meta": meta,
                    "type": q_type
                })
                # Part B
                short_cq_data.append({
                    "id": f"fin1-ch2-short-b-{i:03}",
                    "text": sanitize(row.get('Question_B')),
                    "answer": sanitize(row.get('Ans_B')),
                    "meta": meta,
                    "type": q_type
                })
                
                # 2. Build Full CQ Data
                full_cq_data.append({
                    "id": f"fin1-ch2-cq-{i:03}",
                    "stem": sanitize(row.get('Stem')),
                    "meta": meta,
                    "type": q_type,
                    "questions": [
                        {"label": "a", "text": sanitize(row.get('Question_A')), "answer": sanitize(row.get('Ans_A'))},
                        {"label": "b", "text": sanitize(row.get('Question_B')), "answer": sanitize(row.get('Ans_B'))},
                        {"label": "c", "text": sanitize(row.get('Question_C')), "answer": sanitize(row.get('Ans_C'))},
                        {"label": "d", "text": sanitize(row.get('Question_D')), "answer": sanitize(row.get('Ans_D'))}
                    ]
                })

        print(f"Parsed {len(full_cq_data)} Full CQs and {len(short_cq_data)} Short CQs.")

        # Read data.js
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()

        # Marker-based replacement for Short CQ
        short_start_marker = "// === FIN1_CH2_SHORTCQ_START ==="
        short_end_marker = "// === FIN1_CH2_SHORTCQ_END ==="
        
        # Marker-based replacement for Full CQ
        full_start_marker = "// === FIN1_CH2_FULLCQ_START ==="
        full_end_marker = "// === FIN1_CH2_FULLCQ_END ==="

        def replace_between(content, start_m, end_m, new_data):
            start_idx = content.find(start_m)
            end_idx = content.find(end_m)
            if start_idx == -1 or end_idx == -1:
                return None
            
            # Keep the markers themselves
            prefix = content[:start_idx + len(start_m)]
            suffix = content[end_idx:]
            
            # Generate JSON string
            json_str = json.dumps(new_data, ensure_ascii=False, indent=4)
            # Remove the outer [ and ] because they are already in the data.js arrays
            # Wait, actually it's easier to just replace the whole array content if I'm replacing EVERYTHING.
            # But the user said "Replace ONLY inside markers".
            # If the markers are INSIDE the brackets, I should strip the outer brackets of the JSON string.
            inner_json = json_str.strip().strip('[]').strip()
            
            return f"{prefix}\n{inner_json}\n{suffix}"

        # Update Short CQ
        js_content = replace_between(js_content, short_start_marker, short_end_marker, short_cq_data)
        if js_content is None:
            print("Error: Could not find Short CQ markers in data.js")
            return

        # Update Full CQ
        js_content = replace_between(js_content, full_start_marker, full_end_marker, full_cq_data)
        if js_content is None:
            print("Error: Could not find Full CQ markers in data.js")
            return

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
