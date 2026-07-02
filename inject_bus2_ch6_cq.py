"""
Bus2 Chapter 6 CQ Injection Pipeline
=====================================
Parses BUS2_CH6_CQ - Sheet1.csv and injects into testDatabase.bus2["6"]
"""
import csv
import json
import re
import shutil
import os
import sys

CSV_PATH = 'BUS2_CH6_CQ - Sheet1.csv'
DB_PATH = 'data.js'
BACKUP_PATH = 'data.js.bak_bus2_ch6'

# Ensure UTF-8 console output for Windows
sys.stdout.reconfigure(encoding='utf-8')

# ─── Text Cleaning ───────────────────────────────────────────────────

def clean_answer(text):
    """Convert multiline CSV answer text to HTML-safe format."""
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


def clean_question(text):
    """Clean question text."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', ' ')
    text = text.replace('\r', '').replace('\n', ' ')
    text = re.sub(r'  +', ' ', text)
    return text.strip()


def clean_stem_text(text):
    """Clean standard stem paragraph text."""
    if not text or not text.strip():
        return ""
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


def clean_stem(text):
    """Clean stem text, keeping SVG blocks completely intact from HTML formatting."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', '\n')
    text = text.replace('\r', '')
    
    # Check if there is an SVG block
    svg_match = re.search(r'(<svg.*?</svg>)', text, re.DOTALL | re.IGNORECASE)
    if svg_match:
        svg_content = svg_match.group(1)
        # SVG clean: replace consecutive whitespaces with a single space
        svg_clean = re.sub(r'\s+', ' ', svg_content).strip()
        
        # Split text around the SVG block
        parts = text.split(svg_content)
        cleaned_parts = []
        for part in parts:
            part_cleaned = clean_stem_text(part)
            cleaned_parts.append(part_cleaned)
        
        # Combine back with <br><br> where appropriate
        non_empty = []
        if cleaned_parts[0]:
            non_empty.append(cleaned_parts[0])
        non_empty.append(svg_clean)
        if len(cleaned_parts) > 1 and cleaned_parts[1]:
            non_empty.append(cleaned_parts[1])
            
        return '<br><br>'.join(non_empty)
    else:
        return clean_stem_text(text)


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
            
            # Clean level name and build meta: "Level Board · Year" or "Level · Year"
            # Prevent "Board Board" duplicates
            level_clean = level
            if category.lower() == "board":
                if not level_clean.lower().endswith("board"):
                    meta = f"{level_clean} Board \u00b7 {year}"
                else:
                    meta = f"{level_clean} \u00b7 {year}"
            else:
                meta = f"{level_clean} \u00b7 {year}"
            
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
                
                # Verify that no SVGs got broken inside answer/text and no <br> tags are inside SVG
                if "<svg" in cq["stem"]:
                    assert "<br>" not in cq["stem"][cq["stem"].find("<svg"):cq["stem"].find("</svg>")], "Found <br> tag inside SVG!"
            
            # Verify no Board Board occurrences in new metadata
            assert "Board Board" not in cq["meta"], f"CQ {i} meta has duplicate 'Board Board': {cq['meta']}"
        
        print(f"  [PASS] All {len(parsed)} CQs structurally valid")
        return True
    except Exception as e:
        print(f"  [FAIL] Validation error: {e}")
        return False


# ─── Injection ───────────────────────────────────────────────────────

def inject_into_database(cqs):
    """Inject chapter 6 CQ data."""
    
    # Create backup
    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"  Backup created: {BACKUP_PATH}")
    
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Locate Chapter 5 closing brace
    ch5_idx = content.find('"Chapter 5 : Staffing"')
    if ch5_idx == -1:
        print("  [FAIL] Could not find Chapter 5 in data.js")
        return False
    
    ch5_block_start = content.rfind('{', 0, ch5_idx)
    bracket = 0
    ch5_block_end = -1
    for i in range(ch5_block_start, len(content)):
        if content[i] == '{':
            bracket += 1
        elif content[i] == '}':
            bracket -= 1
            if bracket == 0:
                ch5_block_end = i+1
                break
                
    if ch5_block_end == -1:
        print("  [FAIL] Could not trace Chapter 5 block end")
        return False
        
    print(f"  Chapter 5 block ends at index {ch5_block_end}")
    
    # Build Chapter 6 object
    chapter6_data = {
        "subjectName": "Business Organization & Management 2nd Paper",
        "chapterName": "Chapter 6 : Leadership",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": cqs
    }
    
    ch6_json = json.dumps(chapter6_data, indent=8, ensure_ascii=False)
    
    # Insert new Chapter 6 at ch5_block_end
    insert_text = ',\n    "6": ' + ch6_json
    new_content = content[:ch5_block_end] + insert_text + content[ch5_block_end:]
    
    # Clean up duplicate "Board Board" in case any slipped in
    count_bb = new_content.count("Board Board")
    if count_bb > 0:
        new_content = new_content.replace("Board Board \u00b7", "Board \u00b7")
        print(f"  [OK] Cleaned up {count_bb} duplicate 'Board Board' occurrences globally!")
            
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"  [OK] Injected Chapter 6 successfully")
    return True


# ─── Post-Validation ─────────────────────────────────────────────────

def post_validate():
    """Verify output file syntax and structural integrity."""
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    errors = []
    
    # 1. Balanced braces
    brace_count = 0
    bracket_count = 0
    in_string = False
    escape_next = False
    
    for idx, ch in enumerate(content):
        if escape_next:
            escape_next = False
            continue
        if ch == '\\':
            escape_next = True
            continue
        if ch == '"':
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
        
    # 2. Check keys
    if '"bus2"' not in content:
        errors.append("bus2 key not found")
    if '"Chapter 6 : Leadership"' not in content:
        errors.append("Chapter 6 Leadership key not found")
    if '"Chapter 5 : Staffing"' not in content:
        errors.append("Chapter 5 Staffing key not found")
        
    # 3. Check for unexpected duplicates outside
    matches = re.findall(r'^\s*"(\w+)":\s*\{', content, re.MULTILINE)
    for m in matches:
        if m in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            idx = content.find(f'"{m}":')
            line_start = content.rfind('\n', 0, idx)
            prefix = content[line_start+1:idx]
            if len(prefix) == 4:
                errors.append(f"Unexpected top-level chapter key '{m}' found outside subject!")
                
    # 4. Check database closes properly
    if not content.rstrip().endswith('};'):
        errors.append("data.js does not end with '};'")
        
    # 5. Verify no 'Board Board' in the entire file
    if "Board Board" in content:
        errors.append("Found persistent 'Board Board' string inside database!")
        
    # 6. Count CQs in Chapter 6
    ch6_marker = '"Chapter 6 : Leadership"'
    if ch6_marker in content:
        ch6_start = content.find(ch6_marker)
        ch6_section = content[ch6_start:ch6_start + 700000]
        id_count = len(re.findall(r'"id"\s*:\s*"', ch6_section))
        print(f"  CQ count in Chapter 6 section: {id_count}")
        
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        return False
        
    print("  [PASS] Post-injection validation: all checks passed successfully!")
    return True


# ─── Main ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("Bus2 Chapter 6 CQ Injection Pipeline")
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
    print(f"SUCCESS: {len(cqs)} CQs injected into testDatabase.bus2['6']")
    print("=" * 60)
