#!/usr/bin/env python3
"""
Inject Fin1 Ch1 CQ data from 'Fin1_ch1_cq - Sheet1.csv' into data.js
======================================================================
Strategy:
  - All rows have A,B,C,D  → go into fullCQData
  - shortCQData entries: one per A-question (Knowledge) + one per B-question (Comprehension)
  - Injection: use rfind('\n};') to locate the tail of testDatabase (FAST - no full scan)
  - Output log written to inject_fin1_ch1_cq.log
"""

import csv
import re
import shutil
import os
import sys
import traceback

LOG_FILE  = "inject_fin1_ch1_cq.log"
CSV_FILE  = "Fin1_ch1_cq - Sheet1.csv"
DATA_FILE = "data.js"
BACKUP    = "data.js.bak_fin1_ch1_cq"

log_lines = []

def log(msg):
    print(msg, flush=True)
    log_lines.append(msg)

def write_log():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")

# ─── string helpers ──────────────────────────────────────────────────────────

def esc(s):
    """Escape text for embedding in a JS double-quoted string."""
    if not s:
        return ""
    s = str(s)
    s = s.replace("\\", "\\\\")
    s = s.replace('"',  '\\"')
    s = s.replace("\r\n", "\n")
    s = s.replace("\r",   "\n")
    # Collapse 3+ blank lines → double break
    s = re.sub(r"\n{3,}", "\n\n", s)
    # paragraph breaks → HTML breaks
    s = re.sub(r"\n{2}", "<br><br>", s)
    s = s.replace("\n", "<br>")
    return s.strip()


def fix_math(text):
    """
    Light math formatting:
    - Wrap currency/equation lines with a formula span for readability.
    - Leave $...$ MathJax notation intact.
    """
    if not text:
        return text
    return text  # answers are plain English - no LaTeX needed in ch1


def make_meta(year, level):
    return f"{str(level).strip()} · {str(year).strip()}"


def make_type(level):
    level_lower = str(level).lower()
    board_kw = ["board", "dhaka", "rajshahi", "comilla", "chittagong",
                "sylhet", "barisal", "jessore", "dinajpur", "mymensingh",
                "madrasa", "technical"]
    return "board" if any(k in level_lower for k in board_kw) else "college"


# ─── CSV parsing ─────────────────────────────────────────────────────────────

def parse_csv():
    short_cqs = []
    full_cqs  = []

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row_num, row in enumerate(reader, start=2):
            year  = (row.get("Year")    or "").strip()
            level = (row.get("Level")   or "").strip()
            stem  = (row.get("Stem")    or "").strip()
            q_a   = (row.get("Question_A") or "").strip()
            q_b   = (row.get("Question_B") or "").strip()
            q_c   = (row.get("Question_C") or "").strip()
            q_d   = (row.get("Question_D") or "").strip()
            ans_a = (row.get("Ans_A")   or "").strip()
            ans_b = (row.get("Ans_B")   or "").strip()
            ans_c = (row.get("Ans_C")   or "").strip()
            ans_d = (row.get("Ans_D")   or "").strip()

            if not stem and not q_a:
                continue  # blank row

            meta  = make_meta(year, level)
            qtype = make_type(level)
            has_cd = bool(q_c and q_d and ans_c and ans_d)

            # ── Short CQ items (always from A and B) ─────────────────────────
            if q_a and ans_a:
                short_cqs.append({
                    "id": str(len(short_cqs) + 1),
                    "category": "Knowledge",
                    "text": q_a,
                    "answer": ans_a,
                    "meta": meta,
                    "type": qtype,
                })
            if q_b and ans_b:
                short_cqs.append({
                    "id": str(len(short_cqs) + 1),
                    "category": "Comprehension",
                    "text": q_b,
                    "answer": ans_b,
                    "meta": meta,
                    "type": qtype,
                })

            # ── Full CQ ──────────────────────────────────────────────────────
            qs = [
                {"label": "a", "text": q_a, "answer": ans_a},
                {"label": "b", "text": q_b, "answer": ans_b},
            ]
            if has_cd:
                qs.append({"label": "c", "text": q_c, "answer": ans_c})
                qs.append({"label": "d", "text": q_d, "answer": ans_d})

            full_cqs.append({
                "id": len(full_cqs) + 1,
                "stem": stem,
                "meta": meta,
                "type": qtype,
                "questions": qs,
            })

    return short_cqs, full_cqs


# ─── JS block builder ────────────────────────────────────────────────────────

def build_js(short_cqs, full_cqs):
    parts = []

    # shortCQData
    s_items = []
    for q in short_cqs:
        s_items.append(
            "        {\n"
            f'            id: {q["id"]},\n'
            f'            category: "{esc(q["category"])}",\n'
            f'            text: "{esc(q["text"])}",\n'
            f'            answer: "{esc(q["answer"])}",\n'
            f'            meta: "{esc(q["meta"])}",\n'
            f'            type: "{q["type"]}"\n'
            "        }"
        )
    short_js = "[\n" + ",\n".join(s_items) + "\n        ]" if s_items else "[]"

    # fullCQData
    f_items = []
    for q in full_cqs:
        sub_parts = []
        for sq in q["questions"]:
            sub_parts.append(
                "                {\n"
                f'                    label: "{sq["label"]}",\n'
                f'                    text: "{esc(sq["text"])}",\n'
                f'                    answer: "{esc(sq["answer"])}"\n'
                "                }"
            )
        questions_js = ",\n".join(sub_parts)
        f_items.append(
            "        {\n"
            f'            id: {q["id"]},\n'
            f'            stem: "{esc(q["stem"])}",\n'
            f'            meta: "{esc(q["meta"])}",\n'
            f'            type: "{q["type"]}",\n'
            '            stemImage: "",\n'
            "            questions: [\n"
            + questions_js + "\n"
            "            ]\n"
            "        }"
        )
    full_js = "[\n" + ",\n".join(f_items) + "\n        ]" if f_items else "[]"

    block = (
        '    "fin1": {\n'
        '        "1": {\n'
        '            subjectName: "Finance 1st Paper",\n'
        '            chapterName: "Chapter 1: Introduction to Finance",\n'
        f'            shortCQData: {short_js},\n'
        f'            fullCQData: {full_js}\n'
        '        }\n'
        '    }'
    )
    return block


# ─── Fast injection using rfind ───────────────────────────────────────────────

def inject(fin1_js):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    log(f"[INFO] data.js loaded: {len(content):,} bytes")

    # Guard: already injected?
    if '"fin1"' in content or "'fin1'" in content:
        log("[WARN] fin1 already exists — aborting to prevent duplicates.")
        return None

    # Use rfind to locate the closing `\n};` of testDatabase
    # This is the LAST occurrence in the file — always at the very end.
    end_marker = "\n};"
    last_pos = content.rfind(end_marker)
    if last_pos == -1:
        log("[ERROR] Could not find closing '};' of testDatabase.")
        return None

    log(f"[INFO] Closing '}}; found at position {last_pos:,}")

    # We need to insert before the final closing `}` of testDatabase.
    # content[last_pos] is '\n', content[last_pos+1] is '}'
    # We insert between content[:last_pos] and '\n};'
    # But we need a comma after the last item in testDatabase.
    # Look at what's just before last_pos (skip whitespace)
    before_tail = content[:last_pos].rstrip()
    needs_comma = before_tail and before_tail[-1] not in (",", "{")
    sep = ",\n" if needs_comma else "\n"

    new_content = (
        content[:last_pos]
        + sep
        + fin1_js
        + end_marker
        + "\n"
    )

    log(f"[INFO] New data.js size: {len(new_content):,} bytes (+{len(new_content)-len(content):,})")
    return new_content


# ─── Validation ──────────────────────────────────────────────────────────────

def fast_validate(content):
    """Quick brace/bracket balance check — skips string contents."""
    brace = bracket = 0
    in_str = esc_flag = False
    errors = []
    for c in content:
        if esc_flag:
            esc_flag = False
            continue
        if c == "\\":
            esc_flag = True
            continue
        if c == '"':
            in_str = not in_str
            continue
        if not in_str:
            if c == "{":   brace   += 1
            elif c == "}": brace   -= 1
            elif c == "[": bracket += 1
            elif c == "]": bracket -= 1
    if brace   != 0: errors.append(f"Unbalanced braces: {brace:+d}")
    if bracket != 0: errors.append(f"Unbalanced brackets: {bracket:+d}")
    if in_str:        errors.append("Unterminated string at EOF")
    return errors


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    log("=" * 65)
    log("  FIN1 CH1 CQ INJECTION  |  Fin1_ch1_cq - Sheet1.csv")
    log("=" * 65)

    if not os.path.exists(CSV_FILE):
        log(f"[FATAL] CSV not found: {CSV_FILE}")
        write_log(); sys.exit(1)
    if not os.path.exists(DATA_FILE):
        log(f"[FATAL] data.js not found")
        write_log(); sys.exit(1)

    # Step 1 — Backup
    log(f"\n[STEP 1] Creating backup → {BACKUP}")
    shutil.copy2(DATA_FILE, BACKUP)
    log(f"         Backup size: {os.path.getsize(BACKUP):,} bytes  ✓")

    # Step 2 — Parse CSV
    log(f"\n[STEP 2] Parsing {CSV_FILE} ...")
    short_cqs, full_cqs = parse_csv()
    log(f"         Full CQs     : {len(full_cqs)}")
    log(f"         Short CQ items: {len(short_cqs)}")
    if not full_cqs and not short_cqs:
        log("[FATAL] No data parsed!"); write_log(); sys.exit(1)

    # Step 3 — Build JS
    log(f"\n[STEP 3] Building JavaScript block ...")
    fin1_js = build_js(short_cqs, full_cqs)
    log(f"         Block size: {len(fin1_js):,} chars  ✓")

    # Step 4 — Inject
    log(f"\n[STEP 4] Injecting into data.js ...")
    new_content = inject(fin1_js)
    if new_content is None:
        write_log(); sys.exit(1)

    # Step 5 — Validate
    log(f"\n[STEP 5] Validating JS syntax ...")
    errors = fast_validate(new_content)
    if errors:
        log("[FATAL] Syntax errors:")
        for e in errors: log(f"  ✗ {e}")
        log("[ABORT] data.js NOT modified.")
        write_log(); sys.exit(1)
    log("  ✓ Balanced braces and brackets")

    if '"fin1"' not in new_content:
        log("[FATAL] fin1 key not found in new content — something went wrong.")
        write_log(); sys.exit(1)
    log("  ✓ fin1 key present in new content")

    # Step 6 — Write
    log(f"\n[STEP 6] Writing data.js ...")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    log(f"         Written: {os.path.getsize(DATA_FILE):,} bytes  ✓")

    # Step 7 — Re-read verification
    log(f"\n[STEP 7] Re-read verification ...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        check = f.read()
    errs2 = fast_validate(check)
    if errs2:
        log("[FATAL] Post-write validation FAILED. Rolling back ...")
        shutil.copy2(BACKUP, DATA_FILE)
        log("         Rollback complete.")
        write_log(); sys.exit(1)
    log("  ✓ Post-write validation passed")

    log("\n" + "=" * 65)
    log("  DONE — fin1 ch1 CQ successfully injected!")
    log(f"  Full CQs   : {len(full_cqs)}")
    log(f"  Short items: {len(short_cqs)}")
    log(f"  Backup     : {BACKUP}")
    log("=" * 65)
    write_log()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        log(f"[EXCEPTION] {ex}")
        traceback.print_exc()
        log(traceback.format_exc())
        write_log()
        sys.exit(1)
