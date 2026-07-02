import csv
import json
import re
import shutil

def clean_text(text):
    """Convert multiline CSV text to compact HTML-friendly format"""
    if not text:
        return ""
    text = text.strip().replace('\r', '')
    # Split into paragraphs (separated by 2+ newlines)
    paragraphs = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        # Within a paragraph, merge single newlines into spaces
        p = re.sub(r'\n', ' ', p)
        # Clean double spaces
        p = re.sub(r'  +', ' ', p)
        cleaned.append(p.strip())
    return '<br><br>'.join(cleaned)

def process_csv():
    csv_path = 'BOM2_Ch2_CQ - Sheet1.csv'
    cqs = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        print(f"CSV Header: {header}")

        cq_id = 0
        for row in reader:
            if len(row) < 14:
                continue

            year = row[0].strip()
            subject = row[1].strip()
            chapter_topic = row[2].strip()
            level = row[3].strip()
            category = row[4].strip()
            stem = row[5].strip()
            qa = row[6].strip()
            qb = row[7].strip()
            qc = row[8].strip()
            qd = row[9].strip()
            aa = row[10].strip()
            ab = row[11].strip()
            ac = row[12].strip()
            ad = row[13].strip()

            if not stem and not qa:
                continue

            cq_id += 1

            # Clean multiline answers
            stem_clean = clean_text(stem)
            aa_clean = clean_text(aa)
            ab_clean = clean_text(ab)
            ac_clean = clean_text(ac)
            ad_clean = clean_text(ad)

            # Build meta string
            meta = f"{level} \u00b7 {year}"

            # Determine type
            cq_type = category.lower() if category else "board"

            cq_obj = {
                "id": str(cq_id).zfill(2),
                "stem": stem_clean,
                "meta": meta,
                "type": cq_type,
                "questions": [
                    {"label": "a", "text": qa, "answer": aa_clean},
                    {"label": "b", "text": qb, "answer": ab_clean},
                    {"label": "c", "text": qc, "answer": ac_clean},
                    {"label": "d", "text": qd, "answer": ad_clean}
                ]
            }

            cqs.append(cq_obj)

    return cqs

def validate_json(cqs):
    """Validate the CQ array is valid JSON"""
    try:
        json_str = json.dumps(cqs, ensure_ascii=False)
        parsed = json.loads(json_str)
        assert len(parsed) == len(cqs), "Mismatch in CQ count after parse"
        for i, cq in enumerate(parsed):
            assert "id" in cq, f"CQ {i} missing id"
            assert "stem" in cq, f"CQ {i} missing stem"
            assert "questions" in cq, f"CQ {i} missing questions"
            assert len(cq["questions"]) == 4, f"CQ {i} has {len(cq['questions'])} questions, expected 4"
        print(f"[PASS] JSON validation: {len(parsed)} CQs, all valid")
        return True
    except Exception as e:
        print(f"[FAIL] JSON validation error: {e}")
        return False

def inject_into_database(cqs):
    db_path = 'data.js'
    backup_path = 'data.js.bak_bom2_ch2'

    # Backup
    shutil.copy2(db_path, backup_path)
    print(f"Backup created: {backup_path}")

    with open(db_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build the bom2 chapter 2 entry
    chapter_data = {
        "subjectName": "Business Organization & Management 2nd Paper",
        "chapterName": "Chapter 2 : Principles of Management",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": cqs
    }

    bom2_obj = {"2": chapter_data}
    bom2_json = json.dumps(bom2_obj, indent=4, ensure_ascii=False)

    # Check if bom2 already exists
    if '"bom2"' in content:
        print("[WARN] bom2 key already exists in data.js. Aborting to prevent corruption.")
        print("Remove existing bom2 block first if you want to re-inject.")
        return False

    # Find the final "};" that closes testDatabase
    idx = content.rfind('};')
    if idx == -1:
        print("[FAIL] Could not find closing '}; ' of testDatabase")
        return False

    # Everything before "};" - strip trailing whitespace
    before = content[:idx].rstrip()
    # before should end with "}" (closing the last subject like "ict")

    # Insert comma + bom2 block
    new_content = before + ',\n\n    "bom2": ' + bom2_json + '\n};\n'

    with open(db_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[OK] Injected {len(cqs)} CQs into testDatabase.bom2['2']")
    return True

def post_validate():
    """Quick syntax check on the output"""
    db_path = 'data.js'
    with open(db_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check balanced braces
    brace_count = 0
    bracket_count = 0
    for ch in content:
        if ch == '{': brace_count += 1
        elif ch == '}': brace_count -= 1
        elif ch == '[': bracket_count += 1
        elif ch == ']': bracket_count -= 1

    if brace_count != 0:
        print(f"[FAIL] Unbalanced braces: {brace_count}")
        return False
    if bracket_count != 0:
        print(f"[FAIL] Unbalanced brackets: {bracket_count}")
        return False

    # Check bom2 key exists
    if '"bom2"' not in content:
        print("[FAIL] bom2 key not found after injection")
        return False

    # Check for trailing commas before } or ]
    trailing = re.findall(r',\s*[}\]]', content)
    if trailing:
        print(f"[WARN] Found {len(trailing)} potential trailing commas")

    print("[PASS] Post-injection validation: braces balanced, bom2 key present")
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("BOM2 Chapter 2 CQ Injection Pipeline")
    print("=" * 60)

    # Step 1: Parse CSV
    print("\n[1/4] Parsing CSV...")
    cqs = process_csv()
    print(f"     Parsed {len(cqs)} CQ entries")

    # Step 2: Validate JSON
    print("\n[2/4] Validating JSON structure...")
    if not validate_json(cqs):
        print("ABORTED: JSON validation failed")
        exit(1)

    # Step 3: Inject
    print("\n[3/4] Injecting into data.js...")
    if not inject_into_database(cqs):
        print("ABORTED: Injection failed")
        exit(1)

    # Step 4: Post-validate
    print("\n[4/4] Post-injection validation...")
    if not post_validate():
        print("WARNING: Post-validation issues detected")
    else:
        print("\n" + "=" * 60)
        print("SUCCESS: BOM2 Ch2 CQ injection complete!")
        print("=" * 60)
