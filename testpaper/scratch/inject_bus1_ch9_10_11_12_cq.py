import csv
import json
import re
import shutil
import sys
import os

CSV_PATH = 'BUS1_CH9_10_11_12_CQ - Sheet1.csv'
DB_PATH = 'data.js'
BACKUP_PATH = 'data.js.bak_bus1_ch9_10_11_12'

sys.stdout.reconfigure(encoding='utf-8')

# ---------------------------------------------------------------------
# Text & Math Cleaning Helpers
# ---------------------------------------------------------------------
def fix_math_errors(text: str) -> str:
    """Fix common typos and LaTeX formatting issues in the text."""
    if not text:
        return text
    text = text.replace('2,00,000 - 1,200', '2,000 - 1,200')
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
    """Clean question text."""
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
        result = '<br><br>'.join([p for p in cleaned_parts if p])
        if result:
            return f"{result}<br><br>{svg_clean}"
        else:
            return svg_clean
    else:
        return clean_stem_text(text)

# ---------------------------------------------------------------------
# CSV Parsing
# ---------------------------------------------------------------------
def parse_csv():
    """Parse target CSV file grouping CQs by Chapter."""
    chapters_cq = {"9": [], "10": [], "11": [], "12": []}
    skipped = 0
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        for row_num, row in enumerate(reader, start=2):
            if len(row) < 14:
                skipped += 1
                continue
            
            year      = row[0].strip()
            chapter   = row[2].strip()
            level     = row[3].strip()
            category  = row[4].strip()
            stem_raw  = row[5].strip()
            qa_raw    = row[6].strip()
            qb_raw    = row[7].strip()
            qc_raw    = row[8].strip()
            qd_raw    = row[9].strip()
            aa_raw    = row[10].strip()
            ab_raw    = row[11].strip()
            ac_raw    = row[12].strip()
            ad_raw    = row[13].strip()
            
            if not stem_raw and not qa_raw:
                skipped += 1
                continue
            
            ch_key = chapter.strip()
            if ch_key not in chapters_cq:
                print(f"[WARN] Unknown chapter '{chapter}' at row {row_num}. Skipping.")
                skipped += 1
                continue
                
            # Build meta string
            cq_type = category.lower() if category else "board"
            if cq_type == "board":
                meta = f"{level} · {year}" if level.lower().endswith("board") else f"{level} Board · {year}"
            else:
                meta = f"{level} · {year}"
            meta = meta.replace("Board Board", "Board")
            
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
                "id": None, # will be populated sequentially per chapter
                "stem": stem_clean,
                "meta": meta,
                "type": cq_type,
                "questions": questions,
            }
            
            chapters_cq[ch_key].append(cq_obj)
            
    # Set sequential IDs
    for ch_key, cq_list in chapters_cq.items():
        for idx, cq in enumerate(cq_list, start=1):
            cq["id"] = str(idx).zfill(2)
            
    print(f"Parsed CQs from CSV:")
    for ch, cqs in chapters_cq.items():
        print(f"  Chapter {ch}: {len(cqs)} CQs")
    print(f"Skipped rows: {skipped}")
    
    return chapters_cq

# ---------------------------------------------------------------------
# Database Injection
# ---------------------------------------------------------------------
def inject_cqs(chapters_cq):
    # Backup original file
    shutil.copy2(DB_PATH, BACKUP_PATH)
    print(f"Backup created: {BACKUP_PATH}")
    
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    bus1_idx = content.find('"bus1"')
    if bus1_idx == -1:
        print("[FAIL] 'bus1' key not found in data.js")
        return False
        
    # Find the bounds of the bus1 block
    brace = 1
    i = content.index('{', bus1_idx)
    bus1_start_brace = i
    i += 1
    while i < len(content) and brace > 0:
        if content[i] == '{': brace += 1
        elif content[i] == '}': brace -= 1
        i += 1
    bus1_end_brace = i
    
    bus1_block = content[bus1_start_brace:bus1_end_brace]
    
    new_bus1_block = bus1_block
    
    for ch in ["9", "10", "11", "12"]:
        ch_key = f'"{ch}":'
        idx = new_bus1_block.find(ch_key)
        if idx == -1:
            print(f"[FAIL] Chapter {ch} key not found inside bus1 block")
            return False
            
        # Find chapter bounds within the bus1 block string
        c_brace = 1
        ch_start = new_bus1_block.index('{', idx)
        j = ch_start + 1
        while j < len(new_bus1_block) and c_brace > 0:
            if new_bus1_block[j] == '{': c_brace += 1
            elif new_bus1_block[j] == '}': c_brace -= 1
            j += 1
        ch_end = j
        
        ch_block = new_bus1_block[ch_start:ch_end]
        
        # Extract existing mcqData
        mcq_match = re.search(r'"mcqData"\s*:\s*\[', ch_block)
        if not mcq_match:
            mcq_match = re.search(r'mcqData\s*:\s*\[', ch_block)
            
        if not mcq_match:
            print(f"[FAIL] Could not find mcqData in chapter {ch}")
            return False
            
        mcq_start = mcq_match.end() - 1  # starts at '['
        brac = 1
        k = mcq_start + 1
        while k < len(ch_block) and brac > 0:
            if ch_block[k] == '[': brac += 1
            elif ch_block[k] == ']': brac -= 1
            k += 1
        mcq_raw_str = ch_block[mcq_start:k]
        
        # Build new chapter block string
        new_cqs = chapters_cq[ch]
        new_cqs_json = json.dumps(new_cqs, indent=16, ensure_ascii=False)
        
        new_ch_block = f"""{{
            "subjectName": "Business Organization and Management",
            "chapterName": "Chapter {ch}",
            "mcqData": {mcq_raw_str},
            "shortCQData": [],
            "fullCQData": {new_cqs_json}
        }}"""
        
        # Replace the old chapter block in new_bus1_block
        new_bus1_block = new_bus1_block[:ch_start] + new_ch_block + new_bus1_block[ch_end:]
        
    # Reassemble the file
    new_content = content[:bus1_start_brace] + new_bus1_block + content[bus1_end_brace:]
    
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("[OK] Chapters 9, 10, 11, and 12 successfully modified in data.js")
    return True

# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------
def validate_db():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    errors = []
    
    # 1. Brace / bracket balance (string-aware)
    brace = bracket = 0
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
        if ch == '{':   brace += 1
        elif ch == '}': brace -= 1
        elif ch == '[': bracket += 1
        elif ch == ']': bracket -= 1
        
    if brace != 0:
        errors.append(f"Unbalanced braces: {brace}")
    if bracket != 0:
        errors.append(f"Unbalanced brackets: {bracket}")
        
    # 2. Key presence and structure
    if '"bus1"' not in content:
        errors.append("bus1 key not found")
        
    for ch in ["9", "10", "11", "12"]:
        if f'"{ch}":' not in content:
            errors.append(f"Chapter {ch} key not found")
            
    if 'Board Board' in content:
        errors.append("Found duplicate 'Board Board' in metadata")
        
    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        return False
        
    print("[PASS] Post‑injection validation successful!")
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("Bus1 Chapter 9, 10, 11, 12 CQ Injection Pipeline")
    print("=" * 60)
    
    print("\n[1/3] Parsing CSV...")
    cqs = parse_csv()
    
    print("\n[2/3] Injecting into data.js...")
    if not inject_cqs(cqs):
        print("ABORTED: Injection failed")
        sys.exit(1)
        
    print("\n[3/3] Post-injection validation...")
    if not validate_db():
        print("\n[ROLLBACK] Restoring backup...")
        shutil.copy2(BACKUP_PATH, DB_PATH)
        print("Restored successfully. Please fix issues and retry.")
        sys.exit(1)
        
    print("\n" + "=" * 60)
    print("SUCCESS: Injected CQ data for chapters 9, 10, 11, and 12 into data.js under bus1!")
    print("=" * 60)
