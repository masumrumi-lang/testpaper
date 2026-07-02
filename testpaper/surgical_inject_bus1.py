"""
Surgical Injection Script for Bus1 Chapters 7 and 8 Creative Questions (CQs)
=============================================================================
Parses the CQ CSV file, cleans the text, and inserts shortCQData and fullCQData
into the existing chapters 7 and 8 under the 'bus1' key in data.js,
preserving the existing MCQ data for those chapters.
"""
import csv
import json
import re
import shutil
import sys

CSV_PATH  = 'BUS1_CH7_CH8_CQ - Sheet1.csv'
DB_PATH   = 'data.js'
BACKUP    = 'data.js.bak_bus1_surgical'

sys.stdout.reconfigure(encoding='utf-8')

# ── Chapter name mapping ────────────────────────────────────────────
CHAPTER_MAP = {
    'state owned business': 7,
    'legal aspects of business': 8,
}

# ── Text cleaning helpers ───────────────────────────────────────────

def clean_stem(text):
    if not text or not text.strip():
        return ""
    text = text.strip().replace('\\n', '\n').replace('\r', '')
    paragraphs = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        p = re.sub(r'\n', ' ', p)
        p = re.sub(r'  +', ' ', p)
        cleaned.append(p)
    return '<br><br>'.join(cleaned)


def clean_question(text):
    if not text or not text.strip():
        return ""
    text = text.strip().replace('\\n', ' ').replace('\r', '').replace('\n', ' ')
    return re.sub(r'  +', ' ', text).strip()


def clean_answer(text):
    if not text or not text.strip():
        return ""
    text = text.strip().replace('\\n', '\n').replace('\r', '')
    paragraphs = re.split(r'\n\s*\n', text)
    cleaned = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        p = re.sub(r'\n', ' ', p)
        p = re.sub(r'  +', ' ', p)
        cleaned.append(p)
    return '<br><br>'.join(cleaned)


# ── CSV Parsing ─────────────────────────────────────────────────────

def parse_csv():
    ch7_cqs, ch8_cqs = [], []
    ch7_id = ch8_id = skipped = 0

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"  CSV columns: {len(header)}")

        for row_num, row in enumerate(reader, start=2):
            if len(row) < 14:
                skipped += 1
                continue

            year      = row[0].strip()
            chapter   = row[2].strip()
            level     = row[3].strip()
            category  = row[4].strip()
            stem_raw  = row[5].strip()
            qa_raw, qb_raw, qc_raw, qd_raw = row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip()
            aa_raw, ab_raw, ac_raw, ad_raw = row[10].strip(), row[11].strip(), row[12].strip(), row[13].strip()

            if not stem_raw and not qa_raw:
                skipped += 1
                continue

            ch_num = CHAPTER_MAP.get(chapter.lower())
            if ch_num is None:
                if chapter.lower() != 'cooperative society':
                    print(f"  [WARN] Unknown chapter '{chapter}' at row {row_num}. Skipping.")
                skipped += 1
                continue

            if ch_num == 7:
                ch7_id += 1
                cq_num = ch7_id
            else:
                ch8_id += 1
                cq_num = ch8_id

            # Build meta string
            cq_type = category.lower() if category else "board"
            if cq_type == "board":
                meta = f"{level} · {year}" if level.lower().endswith("board") else f"{level} Board · {year}"
            else:
                meta = f"{level} · {year}"
            # Fix duplicate "Board Board"
            meta = meta.replace("Board Board", "Board")

            # Build questions array
            questions = []
            questions.append({"label": "a", "text": clean_question(qa_raw), "answer": clean_answer(aa_raw)})
            questions.append({"label": "b", "text": clean_question(qb_raw), "answer": clean_answer(ab_raw)})
            if qc_raw or ac_raw:
                questions.append({"label": "c", "text": clean_question(qc_raw), "answer": clean_answer(ac_raw)})
            if qd_raw or ad_raw:
                questions.append({"label": "d", "text": clean_question(qd_raw), "answer": clean_answer(ad_raw)})

            cq_obj = {
                "id": str(cq_num).zfill(2),
                "stem": clean_stem(stem_raw),
                "meta": meta,
                "type": cq_type,
                "questions": questions,
            }

            if ch_num == 7:
                ch7_cqs.append(cq_obj)
            else:
                ch8_cqs.append(cq_obj)

    print(f"  Parsed: Ch7 = {len(ch7_cqs)} CQs, Ch8 = {len(ch8_cqs)} CQs, skipped = {skipped}")
    return ch7_cqs, ch8_cqs


# ── Validation ──────────────────────────────────────────────────────

def validate_cqs(cqs, ch_num):
    try:
        s = json.dumps(cqs, ensure_ascii=False, indent=2)
        parsed = json.loads(s)
        assert len(parsed) == len(cqs)
        for i, cq in enumerate(parsed):
            for key in ("id", "stem", "meta", "type", "questions"):
                assert key in cq, f"CQ {i} missing '{key}'"
            assert len(cq["questions"]) >= 2, f"CQ {i} has < 2 questions"
            for q in cq["questions"]:
                for k in ("label", "text", "answer"):
                    assert k in q, f"CQ {i} sub-question missing '{k}'"
            assert "Board Board" not in cq["meta"], f"CQ {i} meta has 'Board Board'"
        print(f"  [PASS] Chapter {ch_num}: {len(parsed)} CQs valid")
        return True
    except Exception as e:
        print(f"  [FAIL] Chapter {ch_num}: {e}")
        return False


# ── Indentation formatting helper ───────────────────────────────────

def indent_json_string(json_str, num_spaces):
    lines = json_str.splitlines()
    indented_lines = []
    indented_lines.append(lines[0])
    for line in lines[1:]:
        indented_lines.append(" " * num_spaces + line)
    return "\n".join(indented_lines)


# ── Clean previous injection ────────────────────────────────────────

def clean_previous_injection(ch_text):
    short_idx = ch_text.find('"shortCQData"')
    if short_idx == -1:
        return ch_text
    
    # Find the last ']' before "shortCQData"
    last_mcq_bracket = ch_text.rfind(']', 0, short_idx)
    if last_mcq_bracket == -1:
        return ch_text
    
    # Reconstruct clean text up to the closing bracket of mcqData, and add closing brace
    clean_text = ch_text[:last_mcq_bracket + 1] + "\n        }"
    return clean_text


# ── Surgical Injection ──────────────────────────────────────────────

def inject_into_database(ch7_cqs, ch8_cqs):
    # Backup original file
    shutil.copy2(DB_PATH, BACKUP)
    print(f"  Backup created: {BACKUP}")

    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    bus1_idx = content.find('"bus1"')
    if bus1_idx == -1:
        print("  [FAIL] Could not locate 'bus1' in data.js")
        return False

    bus1_start_brace = content.find('{', bus1_idx)
    brace_cnt = 1
    idx = bus1_start_brace + 1
    while idx < len(content) and brace_cnt > 0:
        c = content[idx]
        if c == '{': brace_cnt += 1
        elif c == '}': brace_cnt -= 1
        idx += 1
    bus1_end = idx
    bus1_block = content[bus1_start_brace:bus1_end]

    def get_chapter_span(ch_key):
        pattern = r'"' + ch_key + r'"\s*:\s*\{'
        match = re.search(pattern, bus1_block)
        if not match:
            return None
        
        ch_start_in_bus1 = match.start()
        ch_open_brace = bus1_block.find('{', ch_start_in_bus1)
        
        brace_cnt = 1
        idx = ch_open_brace + 1
        while idx < len(bus1_block) and brace_cnt > 0:
            c = bus1_block[idx]
            if c == '{': brace_cnt += 1
            elif c == '}': brace_cnt -= 1
            idx += 1
        
        span_start = bus1_start_brace + match.start()
        span_end = bus1_start_brace + idx
        return span_start, span_end

    # Process both chapters 7 and 8
    new_content = content
    cqs_map = {7: ch7_cqs, 8: ch8_cqs}

    # We process in reverse order (Chapter 8 first, then Chapter 7) so that span indices
    # for earlier parts of the file remain valid even if we modify the text.
    for ch_num in [8, 7]:
        span = get_chapter_span(str(ch_num))
        if not span:
            print(f"  [FAIL] Chapter {ch_num} not found under 'bus1'")
            return False
        
        ch_text = new_content[span[0]:span[1]]
        
        # 1. Revert any previous injection
        ch_text_cleaned = clean_previous_injection(ch_text)
        
        # 2. Find the last ']' closing mcqData
        last_bracket_idx = ch_text_cleaned.rfind(']')
        if last_bracket_idx == -1:
            print(f"  [FAIL] Could not find closing bracket of mcqData in Chapter {ch_num}")
            return False
        
        # 3. Format the CQ json to match indentation
        cq_json_str = json.dumps(cqs_map[ch_num], indent=4, ensure_ascii=False)
        cq_json_formatted = indent_json_string(cq_json_str, 24)
        
        # 4. Insert the new keys
        injection = (
            ',\n'
            '            "shortCQData": [],\n'
            '            "fullCQData": ' + cq_json_formatted
        )
        
        new_ch_text = ch_text_cleaned[:last_bracket_idx + 1] + injection + ch_text_cleaned[last_bracket_idx + 1:]
        
        # Replace the span in new_content
        new_content = new_content[:span[0]] + new_ch_text + new_content[span[1]:]
        print(f"  [OK] Surgically injected Chapter {ch_num} CQs")

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


# ── Post-validation ─────────────────────────────────────────────────

def post_validate():
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

    # 2. Key presence
    if '"bus1"' not in content:
        errors.append("bus1 key not found")

    # 3. Check MCQ and CQ presence & count
    bus1_idx = content.find('"bus1"')
    start_brace = content.find('{', bus1_idx)
    brace_cnt = 1
    idx = start_brace + 1
    while idx < len(content) and brace_cnt > 0:
        c = content[idx]
        if c == '{': brace_cnt += 1
        elif c == '}': brace_cnt -= 1
        idx += 1
    bus1_block = content[start_brace:idx]

    expected_mcqs = {7: 136, 8: 118}
    expected_cqs = {7: 30, 8: 28}

    for ch in [7, 8]:
        pattern = r'"' + str(ch) + r'"\s*:\s*\{'
        match = re.search(pattern, bus1_block)
        if not match:
            errors.append(f"Chapter {ch} key not found under bus1")
            continue
        
        # Extract chapter block
        ch_start = match.start()
        ch_open = bus1_block.find('{', ch_start)
        brace = 1
        i = ch_open + 1
        while i < len(bus1_block) and brace > 0:
            if bus1_block[i] == '{': brace += 1
            elif bus1_block[i] == '}': brace -= 1
            i += 1
        ch_block = bus1_block[ch_start:i]

        # Count MCQ ids
        mcq_start = ch_block.find('"mcqData"')
        shortcq_start = ch_block.find('"shortCQData"')
        fullcq_start = ch_block.find('"fullCQData"')

        if mcq_start == -1:
            errors.append(f"Chapter {ch} missing 'mcqData'")
        else:
            # slice up to shortCQData or end of block
            mcq_end = shortcq_start if shortcq_start != -1 else len(ch_block)
            mcq_ids = len(re.findall(r'"id"\s*:\s*\d+', ch_block[mcq_start:mcq_end]))
            if mcq_ids != expected_mcqs[ch]:
                errors.append(f"Chapter {ch} MCQ count mismatch! Found {mcq_ids}, expected {expected_mcqs[ch]}")
            else:
                print(f"  [PASS] Chapter {ch} preserves all {mcq_ids} MCQs")

        if fullcq_start == -1:
            errors.append(f"Chapter {ch} missing 'fullCQData'")
        else:
            cq_ids = len(re.findall(r'"id"\s*:\s*"', ch_block[fullcq_start:]))
            if cq_ids != expected_cqs[ch]:
                errors.append(f"Chapter {ch} CQ count mismatch! Found {cq_ids}, expected {expected_cqs[ch]}")
            else:
                print(f"  [PASS] Chapter {ch} correctly contains {cq_ids} CQs")

    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        return False

    print("  [PASS] All post-injection checks passed!")
    return True


# ── Main ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("Bus1 Chapter 7 & 8 CQ Surgical Injection Pipeline")
    print("=" * 60)

    print("\n[1/4] Parsing CSV...")
    ch7, ch8 = parse_csv()
    if not ch7 and not ch8:
        print("ABORTED: No CQs parsed.")
        sys.exit(1)

    print("\n[2/4] Validating parsed CQs...")
    if not validate_cqs(ch7, 7) or not validate_cqs(ch8, 8):
        print("ABORTED: Validation failed.")
        sys.exit(1)

    print("\n[3/4] Surgically injecting into data.js...")
    if not inject_into_database(ch7, ch8):
        print("ABORTED: Injection failed.")
        sys.exit(1)

    print("\n[4/4] Post-injection validation...")
    if not post_validate():
        print("\n[ROLLBACK] Restoring backup...")
        shutil.copy2(BACKUP, DB_PATH)
        print("Restored. Fix issues and retry.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print(f"SUCCESS: bus1 chapters 7 & 8 CQs injected, keeping MCQ data safe!")
    print("=" * 60)
