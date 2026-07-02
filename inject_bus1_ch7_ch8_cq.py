# Bus1 Chapter 7 & 8 CQ Injection Pipeline
# -------------------------------------------------
# This script parses 'BUS1_CH7_CH8_CQ - Sheet1.csv' and injects the
# processed Creative Question data into the existing 'data.js' database
# under the 'bus1' top‑level key, creating entries for chapters "7" and "8".
# It mirrors the successful logic used for Bus2 injections while
# targeting the Bus1 schema.

import csv
import json
import re
import shutil
import sys
import os

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------
CSV_PATH = 'BUS1_CH7_CH8_CQ - Sheet1.csv'
DB_PATH = 'data.js'
BACKUP_PATH = 'data.js.bak_bus1_ch7_ch8'

# Ensure UTF‑8 console output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# ---------------------------------------------------------------------
# Text & Math Cleaning Helpers (same as bus2 helpers for consistency)
# ---------------------------------------------------------------------
def fix_math_errors(text: str) -> str:
    """Fix common typos and LaTeX formatting issues in the text."""
    if not text:
        return text
    # Example correction – denominator typo (if any present in bus1 data)
    text = text.replace('2,00,000 - 1,200', '2,000 - 1,200')
    # LaTeX fixes
    text = text.replace('(rac{', '\\frac{')
    text = text.replace(' imes ', ' \\times ')
    text = text.replace('$eta$', '$\\beta$')
    return text

def clean_answer(text: str) -> str:
    """Convert multiline answer text to HTML‑safe format."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', '\n')
    text = text.replace('\\r', '')
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

def clean_question(text: str) -> str:
    """Clean question stem text."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\n', ' ')
    text = text.replace('\\r', '').replace('\\n', ' ')
    text = re.sub(r'  +', ' ', text)
    text = fix_math_errors(text)
    return text.strip()

def clean_stem_text(text: str) -> str:
    """Clean generic stem paragraphs (used when no SVG)."""
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

def clean_stem(text: str) -> str:
    """Clean stem text while preserving any embedded SVG block untouched."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    text = text.replace('\\\\n', '\n')
    text = text.replace('\\r', '')
    text = fix_math_errors(text)
    # Preserve SVG block if present
    svg_match = re.search(r'(<svg.*?</svg>)', text, re.DOTALL | re.IGNORECASE)
    if svg_match:
        svg_content = svg_match.group(1)
        svg_clean = re.sub(r'\s+', ' ', svg_content).strip()
        parts = text.split(svg_content)
        cleaned_parts = [clean_stem_text(parts[0]), clean_stem_text(parts[1]) if len(parts) > 1 else ""]
        # Re‑assemble keeping the SVG as‑is
        result = '<br><br>'.join([p for p in cleaned_parts if p])
        if result:
            return f"{result}<br><br>{svg_clean}"
        else:
            return svg_clean
    else:
        return clean_stem_text(text)

# ---------------------------------------------------------------------
# CSV Parsing – identical chapter detection to bus2 script
# ---------------------------------------------------------------------
def parse_csv():
    """Parse the CSV into two CQ lists for Chapter 7 (Motivation) and Chapter 8 (Communication)."""
    ch7_cqs = []
    ch8_cqs = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        ch7_id = 0
        ch8_id = 0
        skipped = 0
        for row_num, row in enumerate(reader, start=2):
            if len(row) < 14:
                skipped += 1
                continue
            year, subject, chapter_name, level, category = row[0:5]
            stem_raw, qa_raw, qb_raw, qc_raw, qd_raw = row[5:10]
            aa_raw, ab_raw, ac_raw, ad_raw = row[10:14]
            if not stem_raw and not qa_raw:
                skipped += 1
                continue
            # Chapter identification – case‑insensitive match
            chapter_name_lc = chapter_name.strip().lower()
            # Map CSV chapter names to Bus1 chapters
            if 'state owned business' in chapter_name_lc:
                is_ch7 = True
                is_ch8 = False
            elif 'legal aspects of business' in chapter_name_lc:
                is_ch7 = False
                is_ch8 = True
            else:
                is_ch7 = False
                is_ch8 = False
            if not (is_ch7 or is_ch8):
                print(f"[WARN] Unknown chapter '{chapter_name}' at row {row_num}. Skipping.")
                skipped += 1
                continue
            # Build meta string
            level_clean = level.strip()
            if category.lower() == 'board' and not level_clean.lower().endswith('board'):
                meta = f"{level_clean} Board · {year}"
            else:
                meta = f"{level_clean} · {year}"
            cq_type = category.lower() if category else 'board'
            # Clean fields
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
            questions = [
                {"label": "a", "text": qa_clean, "answer": aa_clean},
                {"label": "b", "text": qb_clean, "answer": ab_clean},
            ]
            if qc_clean or ac_clean:
                questions.append({"label": "c", "text": qc_clean, "answer": ac_clean})
            if qd_clean or ad_clean:
                questions.append({"label": "d", "text": qd_clean, "answer": ad_clean})
            cq_obj = {
                "id": str(ch7_id + ch8_id + 1).zfill(2),
                "stem": stem_clean,
                "meta": meta,
                "type": cq_type,
                "questions": questions,
            }
            if is_ch7:
                ch7_id += 1
                cq_obj["id"] = str(ch7_id).zfill(2)
                ch7_cqs.append(cq_obj)
            else:
                ch8_id += 1
                cq_obj["id"] = str(ch8_id).zfill(2)
                ch8_cqs.append(cq_obj)
        print(f"Parsed: Chapter 7 – {len(ch7_cqs)} CQs, Chapter 8 – {len(ch8_cqs)} CQs, skipped {skipped} rows")
    return ch7_cqs, ch8_cqs

# ---------------------------------------------------------------------
# Validation – ensure generated JSON is well‑formed
# ---------------------------------------------------------------------
def validate_cqs(cqs, chapter_num):
    try:
        json_str = json.dumps(cqs, ensure_ascii=False, indent=2)
        parsed = json.loads(json_str)
        assert len(parsed) == len(cqs)
        for i, cq in enumerate(parsed):
            for field in ("id", "stem", "meta", "type", "questions"):
                assert field in cq, f"CQ {i} missing '{field}'"
            assert len(cq["questions"]) >= 2, f"CQ {i} has insufficient questions"
            for q in cq["questions"]:
                for sub in ("label", "text", "answer"):
                    assert sub in q
            # No leftover denominator typo
            if "2,00,000 - 1,200" in json.dumps(cq):
                raise ValueError(f"CQ {i} contains uncorrected denominator typo")
        print(f"[PASS] Chapter {chapter_num}: {len(parsed)} CQs validated")
        return True
    except Exception as e:
        print(f"[FAIL] Chapter {chapter_num} validation error: {e}")
        return False

# ---------------------------------------------------------------------
# Injection into data.js under bus1 → "7" / "8"
# ---------------------------------------------------------------------
def inject_into_database(ch7_cqs, ch8_cqs):
    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"Backup created: {BACKUP_PATH}")
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    # Load root dictionary
    # Assumes data.js starts with 'var data = {...}' or similar
    match = re.search(r'(=)\s*(\{.*?\})', content, re.DOTALL)
    if not match:
        print("[FAIL] Could not locate main object in data.js")
        return False
    
    data_str = match.group(2)
    data = json.loads(data_str)
    
    if "bus1" not in data:
        data["bus1"] = {}
        
    def build_chapter_obj(ch_num, cqs):
        return {
            "subjectName": "Business Organization & Management 1st Paper",
            "chapterName": f"Chapter {ch_num} : " + ("Motivation" if ch_num == 7 else "Communication"),
            "mcqData": [],
            "shortCQData": [],
            "fullCQData": cqs,
        }
    
    data["bus1"]["7"] = build_chapter_obj(7, ch7_cqs)
    data["bus1"]["8"] = build_chapter_obj(8, ch8_cqs)
    
    new_data_str = json.dumps(data, indent=4, ensure_ascii=False)
    # Reconstruct the file content: keep everything before the JSON assignment, 
    # insert the new JSON, and keep everything after.
    new_content = content[:match.start(2)] + new_data_str + content[match.end(2):]
    
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("[OK] Injected Bus1 Chapter 7 & 8 CQ data into data.js")
    return True

# ---------------------------------------------------------------------
# Post‑validation – basic brace balance and key presence checks
# ---------------------------------------------------------------------
def post_validate():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    errors = []
    brace = 0
    bracket = 0
    in_str = False
    esc = False
    for ch in content:
        if esc:
            esc = False
            continue
        if ch == '\\':
            esc = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch == '{':
            brace += 1
        elif ch == '}':
            brace -= 1
        elif ch == '[':
            bracket += 1
        elif ch == ']':
            bracket -= 1
    if brace != 0:
        errors.append(f"Unbalanced braces: {brace}")
    if bracket != 0:
        errors.append(f"Unbalanced brackets: {bracket}")
    # Required keys
    for key in ['"bus1"', '"Chapter 7 : Motivation"', '"Chapter 8 : Communication"']:
        if key not in content:
            errors.append(f"Missing key {key}")
    if errors:
        for e in errors:
            print(f"[FAIL] {e}")
        return False
    print("[PASS] Post‑injection validation successful")
    return True

# ---------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------
if __name__ == '__main__':
    print("=" * 60)
    print("Bus1 Chapter 7 & 8 CQ Injection Pipeline")
    print("=" * 60)
    print("\n[1/4] Parsing CSV...")
    ch7_cqs, ch8_cqs = parse_csv()
    if not ch7_cqs and not ch8_cqs:
        print("ABORTED: No CQs parsed")
        sys.exit(1)
    print("\n[2/4] Validating JSON structure...")
    if not validate_cqs(ch7_cqs, 7) or not validate_cqs(ch8_cqs, 8):
        print("ABORTED: Validation failed")
        sys.exit(1)
    print("\n[3/4] Injecting into data.js...")
    if not inject_into_database(ch7_cqs, ch8_cqs):
        print("ABORTED: Injection failed")
        sys.exit(1)
    print("\n[4/4] Post‑validation...")
    if not post_validate():
        print("WARNING: Post‑validation issues detected! Restoring backup...")
        shutil.copy2(BACKUP_PATH, DB_PATH)
        sys.exit(1)
    print("\n" + "=" * 60)
    print(f"SUCCESS: Injected Chapter 7 ({len(ch7_cqs)} CQs) & Chapter 8 ({len(ch8_cqs)} CQs) into data.js under bus1")
    print("=" * 60)
