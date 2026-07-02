"""
Bus1 Chapter 7 & 8 CQ Injection Pipeline (Fresh)
==================================================
Parses BUS1_CH7_CH8_CQ - Sheet1.csv and creates a NEW "bus1" key
inside testDatabase with chapters "7" and "8".

Chapter mapping:
  - "State Owned Business"     → Chapter 7
  - "Legal Aspects of Business" → Chapter 8
"""
import csv
import json
import re
import shutil
import sys

CSV_PATH  = 'BUS1_CH7_CH8_CQ - Sheet1.csv'
DB_PATH   = 'data.js'
BACKUP    = 'data.js.bak_bus1_fresh'

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


# ── Injection ───────────────────────────────────────────────────────

def inject_into_database(ch7_cqs, ch8_cqs):
    """Create a new 'bus1' top-level key inside testDatabase."""
    shutil.copy2(DB_PATH, BACKUP)
    print(f"  Backup: {BACKUP}")

    with open(DB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify bus1 doesn't already exist
    if '"bus1"' in content:
        print("  [WARN] bus1 already exists in data.js! Will append chapters.")
        # Find the bus1 block end to append chapters inside it
        bus1_idx = content.find('"bus1"')
        bus1_open = content.index('{', bus1_idx)
        brace = 1
        i = bus1_open + 1
        while i < len(content) and brace > 0:
            if content[i] == '{': brace += 1
            elif content[i] == '}': brace -= 1
            i += 1
        bus1_end = i  # position after the closing brace

        # Build chapter JSON
        ch7_data = {
            "subjectName": "Business Organization & Management 1st Paper",
            "chapterName": "Chapter 7 : State Owned Business",
            "mcqData": [],
            "shortCQData": [],
            "fullCQData": ch7_cqs,
        }
        ch8_data = {
            "subjectName": "Business Organization & Management 1st Paper",
            "chapterName": "Chapter 8 : Legal Aspects of Business",
            "mcqData": [],
            "shortCQData": [],
            "fullCQData": ch8_cqs,
        }
        ch7_json = json.dumps(ch7_data, indent=8, ensure_ascii=False)
        ch8_json = json.dumps(ch8_data, indent=8, ensure_ascii=False)

        # Insert before the closing brace of bus1
        insert_pos = bus1_end - 1  # just before '}'
        insert_text = ',\n        "7": ' + ch7_json + ',\n        "8": ' + ch8_json
        content = content[:insert_pos] + insert_text + '\n    ' + content[insert_pos:]
    else:
        # bus1 doesn't exist — create it as a new top-level key
        # Strategy: find the last closing brace before "};" (the end of testDatabase)
        # and insert bus1 after it with a comma

        # Find the end of testDatabase: the last "};" in the file
        end_marker = content.rstrip().rfind('};')
        if end_marker == -1:
            print("  [FAIL] Cannot find testDatabase closing '};'")
            return False

        # Build full bus1 object
        ch7_data = {
            "subjectName": "Business Organization & Management 1st Paper",
            "chapterName": "Chapter 7 : State Owned Business",
            "mcqData": [],
            "shortCQData": [],
            "fullCQData": ch7_cqs,
        }
        ch8_data = {
            "subjectName": "Business Organization & Management 1st Paper",
            "chapterName": "Chapter 8 : Legal Aspects of Business",
            "mcqData": [],
            "shortCQData": [],
            "fullCQData": ch8_cqs,
        }
        ch7_json = json.dumps(ch7_data, indent=8, ensure_ascii=False)
        ch8_json = json.dumps(ch8_data, indent=8, ensure_ascii=False)

        bus1_block = (
            ',\n'
            '    "bus1": {\n'
            '        "7": ' + ch7_json + ',\n'
            '        "8": ' + ch8_json + '\n'
            '    }\n'
        )

        # Insert just before the final "};"
        content = content[:end_marker] + bus1_block + content[end_marker:]

    with open(DB_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  [OK] Injected bus1 with chapters 7 & 8")
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
    if '"Chapter 7 : State Owned Business"' not in content:
        errors.append("Chapter 7 name not found")
    if '"Chapter 8 : Legal Aspects of Business"' not in content:
        errors.append("Chapter 8 name not found")

    # 3. File ends with };
    if not content.rstrip().endswith('};'):
        errors.append("data.js does not end with '};'")

    # 4. No Board Board
    if 'Board Board' in content:
        errors.append("Found 'Board Board' in database")

    # 5. Count CQs
    for ch, marker in [("7", '"Chapter 7 : State Owned Business"'),
                        ("8", '"Chapter 8 : Legal Aspects of Business"')]:
        if marker in content:
            start = content.find(marker)
            section = content[start:start+500000]
            count = len(re.findall(r'"id"\s*:\s*"', section))
            print(f"  CQ count in Ch{ch}: {count}")

    if errors:
        for e in errors:
            print(f"  [FAIL] {e}")
        return False

    print("  [PASS] All post-injection checks passed!")
    return True


# ── Main ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("Bus1 Chapter 7 & 8 CQ Injection (Fresh)")
    print("=" * 60)

    print("\n[1/4] Parsing CSV...")
    ch7, ch8 = parse_csv()
    if not ch7 and not ch8:
        print("ABORTED: No CQs parsed.")
        sys.exit(1)

    print("\n[2/4] Validating...")
    if not validate_cqs(ch7, 7) or not validate_cqs(ch8, 8):
        print("ABORTED: Validation failed.")
        sys.exit(1)

    print("\n[3/4] Injecting into data.js...")
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
    print(f"SUCCESS: bus1 injected — Ch7 ({len(ch7)} CQs) + Ch8 ({len(ch8)} CQs)")
    print("=" * 60)
