"""
Bus2 Chapter 7 & 8 CQ Injection Pipeline
=========================================
Parses BUS2_CH7_CH8_CQ - Sheet1.csv and injects into testDatabase.bus2["7"] and testDatabase.bus2["8"]
"""
import csv
import json
import re
import shutil
import os
import sys

CSV_PATH = 'BUS2_CH7_CH8_CQ - Sheet1.csv'
DB_PATH = 'data.js'
BACKUP_PATH = 'data.js.bak_bus2_ch7_ch8'

# Ensure UTF-8 console output for Windows
sys.stdout.reconfigure(encoding='utf-8')

# ─── Text & Math Cleaning ────────────────────────────────────────────

def fix_math_errors(text):
    """Fix common typos and math formatting issues in the text."""
    if not text:
        return text
    # Fix the denominator typo in BEP units calculation
    text = text.replace('2,00,000 - 1,200', '2,000 - 1,200')
    
    # Fix potential LaTeX formatting mistakes
    text = text.replace('(rac{', '\\frac{')
    text = text.replace(' imes ', ' \\times ')
    text = text.replace('$eta$', '$\\beta$')
    
    return text


def clean_answer(text):
    """Convert multiline CSV answer text to HTML-safe format."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', '\n')
    text = text.replace('\r', '')
    text = fix_math_errors(text)
    
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
    text = fix_math_errors(text)
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
    text = fix_math_errors(text)
    
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
    """Parse the CSV into two lists of CQ objects for Ch7 and Ch8."""
    ch7_cqs = []
    ch8_cqs = []
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"  CSV Header columns: {len(header)}")
        
        ch7_id = 0
        ch8_id = 0
        skipped = 0
        
        for row_num, row in enumerate(reader, start=2):
            if len(row) < 14:
                skipped += 1
                continue
            
            year = row[0].strip()
            subject = row[1].strip()
            chapter_name = row[2].strip().lower()
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
            
            # Identify chapter
            is_ch7 = False
            is_ch8 = False
            if 'motivation' in chapter_name:
                is_ch7 = True
                ch7_id += 1
                cq_num = ch7_id
            elif 'communication' in chapter_name:
                is_ch8 = True
                ch8_id += 1
                cq_num = ch8_id
            else:
                print(f"  [WARN] Unknown chapter '{row[2]}' at row {row_num}. Skipping.")
                skipped += 1
                continue
            
            # Clean level name and build meta: "Level Board · Year" or "Level · Year"
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
                "id": str(cq_num).zfill(2),
                "stem": stem_clean,
                "meta": meta,
                "type": cq_type,
                "questions": questions
            }
            
            if is_ch7:
                ch7_cqs.append(cq_obj)
            else:
                ch8_cqs.append(cq_obj)
        
        print(f"  Parsed: Chapter 7: {len(ch7_cqs)} CQs, Chapter 8: {len(ch8_cqs)} CQs, Skipped: {skipped} rows")
    
    return ch7_cqs, ch8_cqs


# ─── JSON Validation ─────────────────────────────────────────────────

def validate_cqs(cqs, chapter_num):
    """Validate a CQ array is structurally sound."""
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
                
                # Check for the denominator typo in BEP calculations
                if "2,00,000 - 1,200" in q["answer"] or "2,00,000 - 1,200" in q["text"]:
                    raise ValueError(f"CQ {i} contains uncorrected BEP typo '2,00,000 - 1,200'!")
            
            # Verify no Board Board occurrences in new metadata
            assert "Board Board" not in cq["meta"], f"CQ {i} meta has duplicate 'Board Board': {cq['meta']}"
        
        print(f"  [PASS] Chapter {chapter_num}: All {len(parsed)} CQs structurally valid")
        return True
    except Exception as e:
        print(f"  [FAIL] Chapter {chapter_num} validation error: {e}")
        return False


# ─── Injection ───────────────────────────────────────────────────────

def inject_into_database(ch7_cqs, ch8_cqs):
    """Inject chapter 7 & 8 CQ data."""
    # Create backup
    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"  Backup created: {BACKUP_PATH}")
    
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Locate Chapter 6 closing brace
    ch6_idx = content.find('"Chapter 6 : Leadership"')
    if ch6_idx == -1:
        print("  [FAIL] Could not find Chapter 6 in data.js")
        return False
    
    ch6_block_start = content.rfind('{', 0, ch6_idx)
    bracket = 0
    ch6_block_end = -1
    for i in range(ch6_block_start, len(content)):
        if content[i] == '{':
            bracket += 1
        elif content[i] == '}':
            bracket -= 1
            if bracket == 0:
                ch6_block_end = i+1
                break
                
    if ch6_block_end == -1:
        print("  [FAIL] Could not trace Chapter 6 block end")
        return False
        
    print(f"  Chapter 6 block ends at index {ch6_block_end}")
    
    # Build Chapter 7 and 8 objects
    chapter7_data = {
        "subjectName": "Business Organization & Management 2nd Paper",
        "chapterName": "Chapter 7 : Motivation",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": ch7_cqs
    }
    
    chapter8_data = {
        "subjectName": "Business Organization & Management 2nd Paper",
        "chapterName": "Chapter 8 : Communication",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": ch8_cqs
    }
    
    ch7_json = json.dumps(chapter7_data, indent=8, ensure_ascii=False)
    ch8_json = json.dumps(chapter8_data, indent=8, ensure_ascii=False)
    
    # Insert new Chapter 7 and 8 at ch6_block_end
    insert_text = ',\n    "7": ' + ch7_json + ',\n    "8": ' + ch8_json
    new_content = content[:ch6_block_end] + insert_text + content[ch6_block_end:]
    
    # Clean up duplicate "Board Board" globally in case any slipped in
    count_bb = new_content.count("Board Board")
    if count_bb > 0:
        new_content = new_content.replace("Board Board \u00b7", "Board \u00b7")
        print(f"  [OK] Cleaned up {count_bb} duplicate 'Board Board' occurrences globally!")
            
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"  [OK] Injected Chapters 7 & 8 successfully")
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
    if '"Chapter 7 : Motivation"' not in content:
        errors.append("Chapter 7 Motivation key not found")
    if '"Chapter 8 : Communication"' not in content:
        errors.append("Chapter 8 Communication key not found")
        
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
        
    # 6. Verify no denominator typos remain
    if "2,00,000 - 1,200" in content:
        errors.append("Found persistent BEP denominator typo '2,00,000 - 1,200' in database!")
        
    # 7. Count CQs in Chapter 7 & 8
    for ch_num, ch_marker in [("7", '"Chapter 7 : Motivation"'), ("8", '"Chapter 8 : Communication"')]:
        if ch_marker in content:
            ch_start = content.find(ch_marker)
            ch_section = content[ch_start:ch_start + 700000]
            id_count = len(re.findall(r'"id"\s*:\s*"', ch_section))
            print(f"  CQ count in Chapter {ch_num} section: {id_count}")
        
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        return False
        
    print("  [PASS] Post-injection validation: all checks passed successfully!")
    return True


# ─── Main ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("Bus2 Chapter 7 & 8 CQ Injection Pipeline")
    print("=" * 60)
    
    # Step 1: Parse CSV
    print("\n[1/4] Parsing CSV...")
    ch7_cqs, ch8_cqs = parse_csv()
    if not ch7_cqs and not ch8_cqs:
        print("ABORTED: No CQs parsed")
        exit(1)
        
    # Step 2: Validate JSON
    print("\n[2/4] Validating JSON structure...")
    if not validate_cqs(ch7_cqs, 7) or not validate_cqs(ch8_cqs, 8):
        print("ABORTED: JSON validation failed")
        exit(1)
        
    # Step 3: Inject
    print("\n[3/4] Injecting into data.js...")
    if not inject_into_database(ch7_cqs, ch8_cqs):
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
    print(f"SUCCESS: Injected Chapter 7 ({len(ch7_cqs)} CQs) & Chapter 8 ({len(ch8_cqs)} CQs) into data.js")
    print("=" * 60)
