#!/usr/bin/env python3
"""
inject_fin1_ch1.py
==================
Reads Fin1_ch1_cq - Sheet1.csv and injects Chapter 1 CQ data
into static-data/fin1.json.

Rules:
  - Rows with Q_C + Q_D → fullCQData  (4-part full CQ)
  - Rows without Q_C/Q_D → shortCQData (2 items per stem: Knowledge + Comprehension)
  - Rows with all 4 parts also contribute to shortCQData (a + b items)
  - Math: plain English finance — no LaTeX conversion needed for ch1

Usage:  py -3 inject_fin1_ch1.py
Output: static-data/fin1.json  (chapter "1" added/updated)
        inject_fin1_ch1.log
"""

import csv
import json
import os
import re
import shutil
import sys
import traceback

CSV_FILE    = "Fin1_ch1_cq - Sheet1.csv"
FIN1_JSON   = os.path.join("static-data", "fin1.json")
BACKUP_FILE = FIN1_JSON + ".bak_ch1_inject"
LOG_FILE    = "inject_fin1_ch1.log"

log_lines = []

def log(msg):
    print(msg, flush=True)
    log_lines.append(msg)

def write_log():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")


# ─── Text helpers ─────────────────────────────────────────────────────────────

def clean(text):
    """Normalize a CSV cell: strip whitespace, normalize line endings."""
    if not text:
        return ""
    text = str(text).strip()
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def to_html(text):
    """
    Convert plain text with paragraph breaks to HTML-friendly format.
    Used for stem/question/answer display in the browser.
    """
    if not text:
        return ""
    # Double newline → paragraph break
    text = re.sub(r"\n{2,}", "<br><br>", text)
    # Single newline → line break
    text = text.replace("\n", "<br>")
    return text.strip()


def make_meta(year, level):
    return f"{str(level).strip()} · {str(year).strip()}"


def make_type(level):
    level_lower = str(level).lower()
    board_kw = [
        "board", "dhaka", "rajshahi", "comilla", "chittagong",
        "sylhet", "barisal", "jessore", "dinajpur", "mymensingh",
        "madrasa", "technical",
    ]
    return "board" if any(k in level_lower for k in board_kw) else "college"


# ─── CSV parsing ─────────────────────────────────────────────────────────────

def parse_csv():
    short_cqs = []   # for shortCQData
    full_cqs  = []   # for fullCQData

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row_num, row in enumerate(reader, start=2):
            year  = (row.get("Year")    or "").strip()
            level = (row.get("Level")   or "").strip()
            stem  = clean(row.get("Stem")       or "")
            q_a   = clean(row.get("Question_A") or "")
            q_b   = clean(row.get("Question_B") or "")
            q_c   = clean(row.get("Question_C") or "")
            q_d   = clean(row.get("Question_D") or "")
            ans_a = clean(row.get("Ans_A") or "")
            ans_b = clean(row.get("Ans_B") or "")
            ans_c = clean(row.get("Ans_C") or "")
            ans_d = clean(row.get("Ans_D") or "")

            # Skip blank rows
            if not stem and not q_a:
                continue

            meta  = make_meta(year, level)
            qtype = make_type(level)
            has_cd = bool(q_c and q_d and ans_c and ans_d)

            # ── Short CQ items (always: a = Knowledge, b = Comprehension) ────
            if q_a and ans_a:
                short_cqs.append({
                    "id":       str(len(short_cqs) + 1),
                    "category": "Knowledge",
                    "text":     to_html(q_a),
                    "answer":   to_html(ans_a),
                    "meta":     meta,
                    "type":     qtype,
                })
            if q_b and ans_b:
                short_cqs.append({
                    "id":       str(len(short_cqs) + 1),
                    "category": "Comprehension",
                    "text":     to_html(q_b),
                    "answer":   to_html(ans_b),
                    "meta":     meta,
                    "type":     qtype,
                })

            # ── Full CQ ───────────────────────────────────────────────────────
            questions = [
                {"label": "a", "text": to_html(q_a), "answer": to_html(ans_a)},
                {"label": "b", "text": to_html(q_b), "answer": to_html(ans_b)},
            ]
            if has_cd:
                questions.append({"label": "c", "text": to_html(q_c), "answer": to_html(ans_c)})
                questions.append({"label": "d", "text": to_html(q_d), "answer": to_html(ans_d)})

            full_cqs.append({
                "id":        len(full_cqs) + 1,
                "stem":      to_html(stem),
                "meta":      meta,
                "type":      qtype,
                "stemImage": "",
                "questions": questions,
            })

    return short_cqs, full_cqs


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    log("=" * 65)
    log("  FIN1 CH1 CQ → static-data/fin1.json")
    log("=" * 65)

    # Checks
    if not os.path.exists(CSV_FILE):
        log(f"[FATAL] CSV not found: {CSV_FILE}"); write_log(); sys.exit(1)
    if not os.path.exists(FIN1_JSON):
        log(f"[FATAL] {FIN1_JSON} not found.")
        log("        Run extract_datajs.py first to generate static-data/fin1.json.")
        write_log(); sys.exit(1)

    # Step 1 — Backup
    log(f"\n[STEP 1] Backing up {FIN1_JSON} → {BACKUP_FILE}")
    shutil.copy2(FIN1_JSON, BACKUP_FILE)
    log(f"         Backup: {os.path.getsize(BACKUP_FILE):,} bytes  ✓")

    # Step 2 — Load existing fin1.json
    log(f"\n[STEP 2] Loading {FIN1_JSON} ...")
    with open(FIN1_JSON, "r", encoding="utf-8") as f:
        fin1_data = json.load(f)

    existing_chapters = sorted(fin1_data.keys())
    log(f"         Existing chapters: {existing_chapters}")

    if "1" in fin1_data:
        existing_ch1 = fin1_data["1"]
        log(f"         Chapter 1 already has:")
        log(f"           MCQ     : {len((existing_ch1.get('mcqData')     or []))}")
        log(f"           shortCQ : {len((existing_ch1.get('shortCQData') or []))}")
        log(f"           fullCQ  : {len((existing_ch1.get('fullCQData')  or []))}")
    else:
        log("         Chapter 1 does not exist yet — will be created.")

    # Step 3 — Parse CSV
    log(f"\n[STEP 3] Parsing {CSV_FILE} ...")
    short_cqs, full_cqs = parse_csv()
    log(f"         Full CQ entries : {len(full_cqs)}")
    log(f"         Short CQ items  : {len(short_cqs)}")
    if not full_cqs and not short_cqs:
        log("[FATAL] No data parsed from CSV!"); write_log(); sys.exit(1)

    # Step 4 — Build chapter 1 entry
    log(f"\n[STEP 4] Building chapter 1 data object ...")
    ch1_obj = fin1_data.get("1") or {}

    # Preserve subjectName, chapterName, mcqData if already present
    if not ch1_obj.get("subjectName"):
        ch1_obj["subjectName"] = "Finance 1st Paper"
    if not ch1_obj.get("chapterName"):
        ch1_obj["chapterName"] = "Chapter 1: Introduction to Finance"

    ch1_obj["shortCQData"] = short_cqs
    ch1_obj["fullCQData"]  = full_cqs

    fin1_data["1"] = ch1_obj
    log(f"         shortCQData : {len(short_cqs)} items")
    log(f"         fullCQData  : {len(full_cqs)} items  ✓")

    # Step 5 — Write back
    log(f"\n[STEP 5] Writing {FIN1_JSON} ...")
    with open(FIN1_JSON, "w", encoding="utf-8") as f:
        json.dump(fin1_data, f, ensure_ascii=False, indent=2)
    new_size = os.path.getsize(FIN1_JSON)
    log(f"         Written: {new_size:,} bytes  ✓")

    # Step 6 — Verify re-read
    log(f"\n[STEP 6] Re-read verification ...")
    with open(FIN1_JSON, "r", encoding="utf-8") as f:
        verify = json.load(f)
    v_ch1 = verify.get("1", {})
    assert len(v_ch1.get("fullCQData", [])) == len(full_cqs),   "fullCQData count mismatch"
    assert len(v_ch1.get("shortCQData", [])) == len(short_cqs), "shortCQData count mismatch"
    log(f"  ✓ Chapter 1 verified: {len(full_cqs)} full CQs, {len(short_cqs)} short CQ items")

    # Also update manifest to include chapter "1" if missing
    manifest_path = os.path.join("static-data", "manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        fin1_manifest = manifest.get("subjects", {}).get("fin1", {})
        if fin1_manifest and "1" not in fin1_manifest.get("chapters", []):
            chapters = fin1_manifest["chapters"]
            chapters.insert(0, "1")
            chapters.sort(key=lambda x: int(x) if x.isdigit() else x)
            fin1_manifest["chapters"] = chapters
            with open(manifest_path, "w", encoding="utf-8") as f:
                json.dump(manifest, f, ensure_ascii=False, indent=2)
            log(f"  ✓ manifest.json updated: fin1 chapters = {chapters}")

    log("\n" + "=" * 65)
    log("  FIN1 CH1 INJECTION COMPLETE")
    log(f"  Full CQs   : {len(full_cqs)}")
    log(f"  Short items: {len(short_cqs)}")
    log(f"  Output     : {FIN1_JSON}")
    log(f"  Backup     : {BACKUP_FILE}")
    log("=" * 65)
    write_log()


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        log(f"[EXCEPTION] {ex}")
        log(traceback.format_exc())
        write_log()
        sys.exit(1)
