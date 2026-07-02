"""
Bus2 Chapter 3 CQ Injection Pipeline
=====================================
Parses Bus2_Ch3_CQ - Sheet1.csv and injects into testDatabase.bus2["3"]
"""
import csv
import json
import re
import shutil
import os

CSV_PATH = 'Bus2_Ch3_CQ - Sheet1.csv'
DB_PATH = 'data.js'
BACKUP_PATH = 'data.js.bak_bus2_ch3'

# ─── Text Cleaning ───────────────────────────────────────────────────

def clean_answer(text):
    """Convert multiline CSV answer text to HTML-safe format."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    # Normalize literal \\n to actual newlines first
    text = text.replace('\\n', '\n')
    # Remove \r
    text = text.replace('\r', '')
    # Split into paragraphs (double newline)
    paragraphs = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        # Merge single newlines within a paragraph into spaces
        p = re.sub(r'\n', ' ', p)
        # Clean multiple spaces
        p = re.sub(r'  +', ' ', p)
        cleaned.append(p.strip())
    return '<br><br>'.join(cleaned)


def clean_question(text):
    """Clean question text (simpler, usually single line)."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', ' ')
    text = text.replace('\r', '').replace('\n', ' ')
    text = re.sub(r'  +', ' ', text)
    return text.strip()


def clean_stem(text):
    """Clean stem text, preserving paragraph structure."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', '\n')
    text = text.replace('\r', '')
    paragraphs = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        p = re.sub(r'\n', ' ', p)
        p = re.sub(r'  +', ' ', p)
        cleaned.append(p.strip())
    return '<br><br>'.join(cleaned)


def escape_json_string(s):
    """Ensure string is safe for JSON embedding."""
    if not s:
        return ""
    # json.dumps handles escaping; strip the outer quotes
    return json.dumps(s, ensure_ascii=False)[1:-1]


# ─── CSV Parsing ─────────────────────────────────────────────────────

def parse_csv():
    """Parse the CSV into a list of CQ objects."""
    cqs = []
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"  CSV Header columns: {len(header)}")
        
        cq_id = 0
        skipped = 0
        
        for row_num, row in enumerate(reader, start=2):
            if len(row) < 14:
                skipped += 1
                continue
            
            year = row[0].strip()
            subject = row[1].strip()
            chapter = row[2].strip()
            level = row[3].strip()
            category = row[4].strip()
            stem_raw = row[5].strip()
            qa_raw = row[6].strip()
            qb_raw = row[7].strip()
            qc_raw = row[8].strip()
            qd_raw = row[9].strip()
            aa_raw = row[10].strip()
            ab_raw = row[11].strip()
            ac_raw = row[12].strip()
            ad_raw = row[13].strip()
            
            # Skip empty rows
            if not stem_raw and not qa_raw:
                skipped += 1
                continue
            
            cq_id += 1
            
            # Build meta: "Level Board · Year" or "Level · Year"
            if category.lower() == "board":
                meta = f"{level} Board \u00b7 {year}"
            elif category.lower() == "college":
                meta = f"{level} \u00b7 {year}"
            else:
                meta = f"{level} \u00b7 {year}"
            
            cq_type = category.lower() if category else "board"
            
            # Clean all fields
            stem_clean = clean_stem(stem_raw)
            qa_clean = clean_question(qa_raw)
            qb_clean = clean_question(qb_raw)
            qc_clean = clean_question(qc_raw)
            qd_clean = clean_question(qd_raw)
            aa_clean = clean_answer(aa_raw)
            ab_clean = clean_answer(ab_raw)
            ac_clean = clean_answer(ac_raw)
            ad_clean = clean_answer(ad_raw)
            
            # Build questions array
            questions = []
            questions.append({"label": "a", "text": qa_clean, "answer": aa_clean})
            questions.append({"label": "b", "text": qb_clean, "answer": ab_clean})
            
            # Only add c and d if they have content
            if qc_clean or ac_clean:
                questions.append({"label": "c", "text": qc_clean, "answer": ac_clean})
            if qd_clean or ad_clean:
                questions.append({"label": "d", "text": qd_clean, "answer": ad_clean})
            
            cq_obj = {
                "id": str(cq_id).zfill(2),
                "stem": stem_clean,
                "meta": meta,
                "type": cq_type,
                "questions": questions
            }
            
            cqs.append(cq_obj)
        
        print(f"  Parsed: {len(cqs)} CQs, Skipped: {skipped} rows")
    
    return cqs


# ─── JSON Validation ─────────────────────────────────────────────────

def validate_cqs(cqs):
    """Validate the CQ array is structurally sound."""
    try:
        json_str = json.dumps(cqs, ensure_ascii=False, indent=2)
        parsed = json.loads(json_str)
        
        assert len(parsed) == len(cqs), f"Count mismatch: {len(parsed)} vs {len(cqs)}"
        
        for i, cq in enumerate(parsed):
            assert "id" in cq, f"CQ {i} missing 'id'"
            assert "stem" in cq, f"CQ {i} missing 'stem'"
            assert "meta" in cq, f"CQ {i} missing 'meta'"
            assert "type" in cq, f"CQ {i} missing 'type'"
            assert "questions" in cq, f"CQ {i} missing 'questions'"
            assert len(cq["questions"]) >= 2, f"CQ {i} has only {len(cq['questions'])} questions"
            
            for q in cq["questions"]:
                assert "label" in q, f"CQ {i} question missing 'label'"
                assert "text" in q, f"CQ {i} question missing 'text'"
                assert "answer" in q, f"CQ {i} question missing 'answer'"
        
        print(f"  [PASS] All {len(parsed)} CQs structurally valid")
        return True
    except Exception as e:
        print(f"  [FAIL] Validation error: {e}")
        return False


# ─── Injection ───────────────────────────────────────────────────────

def inject_into_database(cqs):
    """Inject chapter 3 CQ data into testDatabase.bus2."""
    
    # Create backup
    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"  Backup created: {BACKUP_PATH}")
    
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if bus2 chapter 3 already exists
    if '"3":' in content[content.find('"bus2"'):] and 'Chapter 3' in content[content.find('"bus2"'):]:
        # More precise check
        bus2_start = content.find('"bus2"')
        bus2_section = content[bus2_start:bus2_start + 5000]
        if '"3"' in bus2_section and 'Planning' in bus2_section:
            print("  [WARN] bus2 chapter 3 may already exist. Checking...")
    
    # Build chapter 3 data block
    chapter3_data = {
        "subjectName": "Business Organization & Management 2nd Paper",
        "chapterName": "Chapter 3 : Planning",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": cqs
    }
    
    ch3_json = json.dumps(chapter3_data, indent=8, ensure_ascii=False)
    # Fix indentation to match existing pattern (4-space base for chapter content)
    # The existing format uses 8-space indent for inner content
    
    # Find the injection point: after bus2's chapter "2" closes, before bus2 closes
    # Pattern: the closing of chapter 2 object "}" followed by closing of bus2 "}"
    # 
    # Current structure at end of data.js:
    #     ]          <- fullCQData close (line 82926)
    #     }          <- chapter "2" close (line 82927)  
    # }              <- bus2 close (line 82928)
    # };             <- testDatabase close (line 82929)
    
    # Find bus2 block
    bus2_idx = content.find('"bus2"')
    if bus2_idx == -1:
        print("  [FAIL] Could not find 'bus2' key in data.js")
        return False
    
    # Find the end of testDatabase: the final "};"
    final_close = content.rfind('};')
    if final_close == -1:
        print("  [FAIL] Could not find closing '};' of testDatabase")
        return False
    
    # Find the closing "}" of bus2 (the one just before "};")
    # Work backwards from "};" to find the bus2 closing brace
    bus2_close = content.rfind('}', 0, final_close)
    
    # The bus2 close should be preceded by the chapter "2" close
    # Let's find the pattern more precisely
    # Look for the last "}" before the bus2 closing "}" - that's the chapter 2 close
    ch2_close = content.rfind('}', 0, bus2_close)
    
    # Verify by checking what's around ch2_close
    context_around = content[ch2_close-20:ch2_close+20]
    print(f"  Injection context: ...{repr(context_around)}...")
    
    # Insert the new chapter after ch2_close
    # We need: comma after ch2 close, then new chapter 3
    insert_text = ',\n    "3": ' + ch3_json + '\n'
    
    new_content = content[:ch2_close+1] + insert_text + content[ch2_close+1:]
    
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  [OK] Injected {len(cqs)} CQs into testDatabase.bus2['3']")
    return True


# ─── Post-Validation ─────────────────────────────────────────────────

def post_validate():
    """Verify the output file integrity."""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    
    # 1. Balanced braces
    brace_count = 0
    bracket_count = 0
    in_string = False
    escape_next = False
    
    for ch in content:
        if escape_next:
            escape_next = False
            continue
        if ch == '\\':
            escape_next = True
            continue
        if ch == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == '{':
            brace_count += 1
        elif ch == '}':
            brace_count -= 1
        elif ch == '[':
            bracket_count += 1
        elif ch == ']':
            bracket_count -= 1
    
    if brace_count != 0:
        errors.append(f"Unbalanced braces: {brace_count}")
    if bracket_count != 0:
        errors.append(f"Unbalanced brackets: {bracket_count}")
    
    # 2. Check bus2 key present
    if '"bus2"' not in content:
        errors.append("bus2 key not found")
    
    # 3. Check chapter 3 present
    if '"Chapter 3 : Planning"' not in content:
        errors.append("Chapter 3 not found after injection")
    
    # 4. Check testDatabase closes properly
    if not content.rstrip().endswith('};'):
        errors.append("data.js does not end with '};'")
    
    # 5. Count CQs in chapter 3 section
    ch3_marker = '"Chapter 3 : Planning"'
    if ch3_marker in content:
        ch3_start = content.find(ch3_marker)
        # Count "id": patterns after this point until next chapter or end
        ch3_section = content[ch3_start:ch3_start + 500000]
        id_count = len(re.findall(r'"id"\s*:\s*"', ch3_section))
        print(f"  CQ count in chapter 3 section: {id_count}")
    
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        return False
    
    print("  [PASS] Post-injection validation: all checks passed")
    return True


# ─── Main ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("Bus2 Chapter 3 CQ Injection Pipeline")
    print("=" * 60)
    
    # Step 1: Parse CSV
    print("\n[1/4] Parsing CSV...")
    cqs = parse_csv()
    if not cqs:
        print("ABORTED: No CQs parsed")
        exit(1)
    
    # Step 2: Validate JSON
    print("\n[2/4] Validating JSON structure...")
    if not validate_cqs(cqs):
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
        print("\nWARNING: Post-validation issues detected!")
        print("Restoring from backup...")
        shutil.copy2(BACKUP_PATH, DB_PATH)
        print("Backup restored. Please fix issues and retry.")
        exit(1)
    
    print("\n" + "=" * 60)
    print(f"SUCCESS: {len(cqs)} CQs injected into testDatabase.bus2['3']")
    print("=" * 60)
