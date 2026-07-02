#!/usr/bin/env python3
"""
extract_datajs.py  (v2 - fast regex-based approach)
====================================================
Reads data.js, converts JS object syntax to valid JSON using
regex-based string-aware key quoting (no per-character Python loops),
then writes one JSON file per subject to static-data/.

Why v2: v1 used character-by-character append → MemoryError on 14 MB.
v2 uses re.finditer to split at string boundaries, applies re.sub
only to non-string segments. The C-level regex engine handles 14 MB fast.

Usage:  py -3 extract_datajs.py
Output: static-data/<subject>.json
        static-data/manifest.json
        extract_datajs.log
"""

import os
import re
import sys
import json
import traceback

DATA_FILE  = "data.js"
OUTPUT_DIR = "static-data"
LOG_FILE   = "extract_datajs.log"

log_lines = []

def log(msg):
    print(msg, flush=True)
    log_lines.append(msg)

def write_log():
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(log_lines) + "\n")
    except Exception as e:
        print(f"[WARN] Could not write log: {e}", flush=True)


# ─── Fast JS → JSON conversion ────────────────────────────────────────────────
# Strategy:
#   1. Split content into (non-string, string) alternating chunks using regex
#   2. In non-string chunks: quote unquoted identifier keys
#   3. String chunks: pass through untouched
#   4. After reassembly: strip trailing commas (valid JS, invalid JSON)

# Matches any double-quoted JS string including escape sequences
_STRING_RE = re.compile(r'"(?:[^"\\]|\\.)*"', re.DOTALL)

# Matches an unquoted JS identifier used as an object key:
#   word boundary + identifier chars + optional whitespace + colon (not ::)
_KEY_RE = re.compile(r'(?<!["\w])([a-zA-Z_$][a-zA-Z0-9_$]*)(\s*:)(?!:)')


def _quote_keys_in_chunk(chunk):
    """Quote all bare identifier keys in a non-string JS chunk."""
    return _KEY_RE.sub(lambda m: f'"{m.group(1)}"' + m.group(2), chunk)


def js_to_json(js_str):
    """
    Convert a JS object literal to valid JSON.
    - Quotes unquoted identifier keys (only in non-string regions)
    - Strips trailing commas before ] and }
    - Replaces `undefined` with `null` in non-string regions
    """
    parts = []
    prev_end = 0

    for m in _STRING_RE.finditer(js_str):
        start, end = m.span()
        # Non-string chunk before this string
        chunk = js_str[prev_end:start]
        chunk = _quote_keys_in_chunk(chunk)
        chunk = chunk.replace('undefined', 'null')
        parts.append(chunk)
        # String: pass through verbatim
        parts.append(m.group(0))
        prev_end = end

    # Final non-string tail
    tail = js_str[prev_end:]
    tail = _quote_keys_in_chunk(tail)
    tail = tail.replace('undefined', 'null')
    parts.append(tail)

    result = ''.join(parts)

    # Strip trailing commas  ,]  or  ,}  (valid JS, invalid JSON)
    result = re.sub(r',(\s*[}\]])', r'\1', result)

    return result


def strip_const_decl(content):
    """
    Strip  'const testDatabase = '  from start and trailing ';' from end.
    data.js is a single constant declaration so this is safe.
    """
    content = content.strip()
    m = re.match(r'const\s+testDatabase\s*=\s*', content)
    if not m:
        raise ValueError("Cannot find 'const testDatabase =' declaration")
    content = content[m.end():]
    content = content.rstrip()
    if content.endswith(';'):
        content = content[:-1].rstrip()
    return content


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    log('=' * 65)
    log('  EXTRACT data.js → per-subject JSON  (v2 fast)')
    log('=' * 65)

    if not os.path.exists(DATA_FILE):
        log(f"[FATAL] {DATA_FILE} not found"); write_log(); sys.exit(1)

    # Step 1: Read
    log(f"\n[STEP 1] Reading {DATA_FILE} ...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    log(f"         Size: {len(content)/1024/1024:.2f} MB ({len(content):,} chars)")

    # Step 2: Strip const declaration
    log(f"\n[STEP 2] Stripping const declaration ...")
    try:
        js_obj = strip_const_decl(content)
        log(f"         JS object: {len(js_obj)/1024/1024:.2f} MB")
    except Exception as e:
        log(f"[FATAL] {e}"); write_log(); sys.exit(1)

    # Step 3: Convert JS → JSON (regex, fast)
    log(f"\n[STEP 3] Converting JS → JSON (regex-based) ...")
    try:
        json_str = js_to_json(js_obj)
        log(f"         JSON string: {len(json_str)/1024/1024:.2f} MB")
    except Exception as e:
        log(f"[FATAL] Conversion error: {e}")
        log(traceback.format_exc())
        write_log(); sys.exit(1)

    # Step 4: Parse JSON
    log(f"\n[STEP 4] Parsing JSON ...")
    try:
        testDatabase = json.loads(json_str)
    except json.JSONDecodeError as e:
        log(f"[FATAL] JSON parse error — line {e.lineno}, col {e.colno}: {e.msg}")
        ctx_start = max(0, e.pos - 150)
        ctx_end   = min(len(json_str), e.pos + 150)
        log(f"         Context: ...{repr(json_str[ctx_start:ctx_end])}...")
        # Write the bad JSON to a temp file for inspection
        bad_path = "extract_bad_json.tmp"
        with open(bad_path, "w", encoding="utf-8") as f:
            f.write(json_str[max(0, e.pos-2000):min(len(json_str), e.pos+2000)])
        log(f"         Context written to: {bad_path}")
        write_log(); sys.exit(1)

    subject_ids = list(testDatabase.keys())
    log(f"         Subjects found: {', '.join(subject_ids)}")
    log(f"         Total: {len(subject_ids)} subjects")

    # Step 5: Create output directory
    log(f"\n[STEP 5] Creating {OUTPUT_DIR}/ ...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log(f"         OK: {os.path.abspath(OUTPUT_DIR)}")

    # Step 6: Write per-subject JSON files
    log(f"\n[STEP 6] Writing subject files ...\n")
    manifest = {"subjects": {}}
    total_chapters = 0

    for subject_id in subject_ids:
        subject_data = testDatabase[subject_id]
        chapters = sorted(
            subject_data.keys(),
            key=lambda x: int(x) if x.isdigit() else x
        )

        # Get subject name
        subject_name = subject_id
        for ch in chapters:
            d = subject_data.get(ch)
            if isinstance(d, dict) and d.get("subjectName"):
                subject_name = d["subjectName"]
                break

        # Counts
        mcq_count   = sum(len((subject_data.get(ch) or {}).get("mcqData",     [])) for ch in chapters)
        short_count = sum(len((subject_data.get(ch) or {}).get("shortCQData", [])) for ch in chapters)
        full_count  = sum(len((subject_data.get(ch) or {}).get("fullCQData",  [])) for ch in chapters)

        out_path = os.path.join(OUTPUT_DIR, f"{subject_id}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(subject_data, f, ensure_ascii=False, indent=2)

        size_kb  = os.path.getsize(out_path) / 1024
        rel_path = f"{OUTPUT_DIR}/{subject_id}.json"

        log(
            f"  ✓ {subject_id:<8}  {len(chapters):>2} ch  "
            f"MCQ:{mcq_count:<5}  sCQ:{short_count:<5}  fCQ:{full_count:<5}"
            f"  {rel_path} ({size_kb:.0f} KB)"
        )

        manifest["subjects"][subject_id] = {
            "name":     subject_name,
            "chapters": chapters,
            "file":     rel_path,
        }
        total_chapters += len(chapters)

    # Step 7: Write manifest.json
    log(f"\n[STEP 7] Writing manifest.json ...")
    manifest_path = os.path.join(OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    log(f"         Subjects: {len(subject_ids)},  Chapters: {total_chapters}")

    # Step 8: Validate
    log(f"\n[STEP 8] Validating ...")
    errors = 0
    for sid in subject_ids:
        try:
            with open(os.path.join(OUTPUT_DIR, f"{sid}.json"), "r", encoding="utf-8") as f:
                parsed = json.load(f)
            if not parsed:
                log(f"  ✗ {sid}: empty"); errors += 1
        except Exception as e:
            log(f"  ✗ {sid}: {e}"); errors += 1

    if errors == 0:
        log(f"  ✓ All {len(subject_ids)} files valid")

    # Done
    log("\n" + "=" * 65)
    log(f"  DONE — Subjects: {len(subject_ids)},  Chapters: {total_chapters}")
    log(f"  Output : {os.path.abspath(OUTPUT_DIR)}/")
    log(f"  data.js: UNTOUCHED  ({os.path.getsize(DATA_FILE):,} bytes)")
    log("=" * 65)
    write_log()
    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        log(f"[EXCEPTION] {ex}")
        log(traceback.format_exc())
        write_log()
        sys.exit(1)
