#!/usr/bin/env python3
"""
FIN1 Chapters 1, 3, 4, 6, 8, 9 CQ Injection Script
=====================================================
Reads CSV, reconstructs tables/formulas, injects into data.js fin1 section.
"""

import csv
import json
import re
import os
import shutil
import sys

CSV_FILE = "Fin1_ch_1_3_4_6_8_9_cq - Sheet1.csv"
DATA_FILE = "data.js"
BACKUP_FILE = "data.js.bak_fin1_ch1_3_4_6_8_9"
TARGET_CHAPTERS = ["1", "3", "4", "6", "8", "9"]


# ============================================================
# CONTENT PROCESSING FUNCTIONS
# ============================================================

def escape_js_string(s):
    """Escape a string for safe embedding in a JS double-quoted string."""
    if not s:
        return ""
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    s = s.replace("\r\n", "\n")
    s = s.replace("\r", "\n")
    # We'll handle newlines in the content processing
    return s


def detect_pipe_table(text):
    """Detect if text contains pipe-separated table data."""
    lines = text.strip().split("\n")
    pipe_lines = [l for l in lines if "|" in l and l.strip()]
    return len(pipe_lines) >= 2


def parse_pipe_table(text):
    """Parse pipe-separated table text into rows of cells."""
    lines = text.strip().split("\n")
    table_rows = []
    non_table_lines = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if "|" in stripped and stripped:
            # Check it's a real table row (not just a stray pipe)
            cells = [c.strip() for c in stripped.split("|")]
            cells = [c for c in cells if c]  # remove empty edge cells
            if len(cells) >= 2:
                table_rows.append(cells)
                in_table = True
            else:
                non_table_lines.append(stripped)
        else:
            if stripped:
                non_table_lines.append(stripped)

    return table_rows, non_table_lines


def build_html_table(rows, first_row_header=True):
    """Build an HTML table from a list of rows (lists of cells)."""
    if not rows:
        return ""
    html = "<table>"
    for i, row in enumerate(rows):
        html += "<tr>"
        for cell in row:
            tag = "th" if (i == 0 and first_row_header) else "td"
            html += f"<{tag}>{cell}</{tag}>"
        html += "</tr>"
    html += "</table>"
    return html


def detect_key_value_pairs(text):
    """Detect if text contains multiple Key: Value pairs."""
    # Match patterns like "Label: Value" or "Label = Value"
    kv_pattern = re.compile(r'^([A-Za-z][A-Za-z0-9\s\'/\(\)%&,-]+?)\s*[:=]\s*(.+)$', re.MULTILINE)
    matches = kv_pattern.findall(text)
    return matches


def detect_project_comparison_data(text):
    """Detect project/bond/security comparison data with Year-wise cash flows."""
    # Pattern: "Project X:\nYear 1: BDT ...\nYear 2: BDT ..."
    project_pattern = re.compile(
        r'(Project|Bond|Security|Investment|Source|Option)\s+([A-Za-z0-9]+)\s*:\s*\n',
        re.IGNORECASE
    )
    return project_pattern.findall(text)


def reconstruct_project_cash_flow_table(text):
    """Reconstruct project comparison data into HTML tables."""
    lines = text.strip().split("\n")
    result_parts = []
    current_intro = []
    projects = {}
    current_project = None
    current_project_data = []
    project_order = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Check if this is a project header
        proj_match = re.match(
            r'^(Project|Bond|Security|Investment|Source|Option)\s+([A-Za-z0-9]+)\s*:?\s*$',
            stripped, re.IGNORECASE
        )
        if proj_match:
            if current_project:
                projects[current_project] = current_project_data
            current_project = f"{proj_match.group(1)} {proj_match.group(2)}"
            project_order.append(current_project)
            current_project_data = []
            continue

        if current_project:
            # Parse "Year N: BDT X" or "Key: Value" lines
            kv_match = re.match(r'^(.+?)\s*:\s*(.+)$', stripped)
            if kv_match:
                current_project_data.append((kv_match.group(1).strip(), kv_match.group(2).strip()))
            else:
                current_project_data.append(("", stripped))
        else:
            current_intro.append(stripped)

    if current_project:
        projects[current_project] = current_project_data

    if not projects:
        return None

    html = ""

    # Add intro
    if current_intro:
        html += "<p>" + "<br>".join(current_intro) + "</p>"

    # Check if projects share the same keys (can make comparison table)
    # First check if all have Year-based data
    all_year_based = True
    all_keys = set()
    for proj_name in project_order:
        data = projects[proj_name]
        for k, v in data:
            if not re.match(r'^Year\s+\d+', k, re.IGNORECASE):
                all_year_based = False
            all_keys.add(k)

    if all_year_based and len(project_order) >= 2:
        # Build comparison table
        # Collect all years
        years = []
        for proj_name in project_order:
            for k, v in projects[proj_name]:
                if k not in years:
                    years.append(k)

        html += "<table>"
        # Header
        html += "<tr><th>Description</th>"
        for proj_name in project_order:
            html += f"<th>{proj_name}</th>"
        html += "</tr>"

        for year in years:
            html += f"<tr><td>{year}</td>"
            for proj_name in project_order:
                val = ""
                for k, v in projects[proj_name]:
                    if k == year:
                        val = v
                        break
                html += f"<td>{val}</td>"
            html += "</tr>"
        html += "</table>"
    else:
        # Render each project as its own table
        for proj_name in project_order:
            data = projects[proj_name]
            html += f"<p><strong>{proj_name}:</strong></p>"
            if data:
                html += "<table>"
                html += "<tr><th>Particulars</th><th>Amount/Value</th></tr>"
                for k, v in data:
                    if k:
                        html += f"<tr><td>{k}</td><td>{v}</td></tr>"
                    else:
                        html += f"<tr><td colspan='2'>{v}</td></tr>"
                html += "</table>"

    return html


def reconstruct_stimulus_kv_table(text):
    """If stimulus has 3+ key:value pairs, reconstruct into HTML table."""
    lines = text.strip().split("\n")
    intro_lines = []
    kv_pairs = []
    kv_started = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        kv_match = re.match(r'^([A-Za-z][A-Za-z0-9\s\'/\(\)%&,.-]+?)\s*:\s*(.+)$', stripped)
        if kv_match:
            kv_pairs.append((kv_match.group(1).strip(), kv_match.group(2).strip()))
            kv_started = True
        else:
            if not kv_started:
                intro_lines.append(stripped)
            else:
                # Mixed content after kv started - just add to intro
                intro_lines.append(stripped)

    if len(kv_pairs) >= 3:
        html = ""
        if intro_lines:
            html += "<p>" + "<br>".join(intro_lines) + "</p>"
        html += "<table>"
        html += "<tr><th>Particulars</th><th>Amount/Value</th></tr>"
        for k, v in kv_pairs:
            html += f"<tr><td>{k}</td><td>{v}</td></tr>"
        html += "</table>"
        return html

    return None


def reconstruct_pipe_table_content(text):
    """Reconstruct pipe-separated table content."""
    lines = text.strip().split("\n")
    intro_lines = []
    table_started = False
    table_rows = []
    post_table_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if "|" in stripped:
            cells = [c.strip() for c in stripped.split("|")]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                table_rows.append(cells)
                table_started = True
                continue
        if not table_started:
            intro_lines.append(stripped)
        else:
            post_table_lines.append(stripped)

    if not table_rows:
        return None

    html = ""
    if intro_lines:
        html += "<p>" + "<br>".join(intro_lines) + "</p>"

    html += build_html_table(table_rows, first_row_header=True)

    if post_table_lines:
        html += "<p>" + "<br>".join(post_table_lines) + "</p>"

    return html


def process_content(text):
    """Process text content: reconstruct tables, format formulas, convert newlines to <br>."""
    if not text or not text.strip():
        return ""

    text = text.strip()

    # Check if text already has HTML tags - if so, preserve
    if re.search(r'<table|<tr|<td|<th', text, re.IGNORECASE):
        # Already has HTML, just clean up newlines
        text = text.replace("\n\n", "<br><br>")
        text = text.replace("\n", "<br>")
        return text

    # 1. Check for project/bond comparison data
    if re.search(r'(Project|Bond|Security|Investment|Source|Option)\s+[A-Za-z0-9]+\s*:', text, re.IGNORECASE):
        has_newline_kv = bool(re.search(r'\n\s*(Year|Initial|Cash|Expected|Return|Standard|Face|Coupon|Maturity|Required|Current|Dividend|Growth|Flotation|Market|Interest|BDT)\s', text, re.IGNORECASE))
        if has_newline_kv:
            result = reconstruct_project_cash_flow_table(text)
            if result:
                return result

    # 2. Check for pipe-separated tables
    if detect_pipe_table(text):
        result = reconstruct_pipe_table_content(text)
        if result:
            return result

    # 3. Check for key-value pairs (3+)
    result = reconstruct_stimulus_kv_table(text)
    if result:
        return result

    # 4. Default: convert newlines to <br>
    # But handle double-newlines as paragraph breaks
    text = text.replace("\n\n\n", "<br><br>")
    text = text.replace("\n\n", "<br><br>")
    text = text.replace("\n", "<br>")

    return text


def process_answer(text):
    """Process answer text: handle formulas, tables, key-value pairs."""
    if not text or not text.strip():
        return ""

    text = text.strip()

    # Check if text already has HTML tags
    if re.search(r'<table|<tr|<td|<th', text, re.IGNORECASE):
        text = text.replace("\n\n", "<br><br>")
        text = text.replace("\n", "<br>")
        return text

    # Check for pipe-separated tables in answers
    if detect_pipe_table(text):
        result = reconstruct_pipe_table_content(text)
        if result:
            return result

    # Check for key-value pairs (3+) in answers
    result = reconstruct_stimulus_kv_table(text)
    if result:
        return result

    # Default: convert newlines to <br>
    text = text.replace("\n\n\n", "<br><br>")
    text = text.replace("\n\n", "<br><br>")
    text = text.replace("\n", "<br>")

    return text


# ============================================================
# CSV PARSING
# ============================================================

def parse_csv():
    """Parse the CSV file and return rows grouped by chapter."""
    chapters = {}

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"[INFO] Total CSV rows: {len(rows)}")

    for i, r in enumerate(rows):
        chapter = r["Chapter"].strip()
        if chapter not in TARGET_CHAPTERS:
            print(f"[WARN] Row {i} has unexpected chapter '{chapter}', skipping.")
            continue

        # Process content
        stimulus = process_content(r["Stem"])
        q_a = process_content(r["Question_A"])
        q_b = process_content(r["Question_B"])
        q_c = process_content(r["Question_C"])
        q_d = process_content(r["Question_D"])
        ans_a = process_answer(r["Ans_A"])
        ans_b = process_answer(r["Ans_B"])
        ans_c = process_answer(r["Ans_C"])
        ans_d = process_answer(r["Ans_D"])

        # Determine toggle type
        has_cd = bool(q_c.strip() and q_d.strip() and ans_c.strip() and ans_d.strip())

        # Build CQ object
        cq = {
            "stimulus": stimulus,
            "q_a": q_a,
            "q_b": q_b,
            "ans_a": ans_a,
            "ans_b": ans_b,
        }

        if has_cd:
            cq["q_c"] = q_c
            cq["q_d"] = q_d
            cq["ans_c"] = ans_c
            cq["ans_d"] = ans_d

        if chapter not in chapters:
            chapters[chapter] = []
        chapters[chapter].append(cq)

    for ch in sorted(chapters.keys(), key=int):
        full = sum(1 for cq in chapters[ch] if "q_c" in cq)
        ab_only = len(chapters[ch]) - full
        print(f"[INFO] Chapter {ch}: {len(chapters[ch])} CQs ({full} full, {ab_only} a,b only)")

    return chapters


# ============================================================
# JAVASCRIPT GENERATION
# ============================================================

def generate_cq_js(cq_list, chapter_num):
    """Generate JavaScript array content for a chapter's CQs."""
    items = []
    for idx, cq in enumerate(cq_list, 1):
        parts = []
        parts.append(f'        "id": {idx}')
        parts.append(f'        "stimulus": "{escape_js_string(cq["stimulus"])}"')
        parts.append(f'        "q_a": "{escape_js_string(cq["q_a"])}"')
        parts.append(f'        "q_b": "{escape_js_string(cq["q_b"])}"')

        if "q_c" in cq:
            parts.append(f'        "q_c": "{escape_js_string(cq["q_c"])}"')
            parts.append(f'        "q_d": "{escape_js_string(cq["q_d"])}"')

        parts.append(f'        "ans_a": "{escape_js_string(cq["ans_a"])}"')
        parts.append(f'        "ans_b": "{escape_js_string(cq["ans_b"])}"')

        if "q_c" in cq:
            parts.append(f'        "ans_c": "{escape_js_string(cq["ans_c"])}"')
            parts.append(f'        "ans_d": "{escape_js_string(cq["ans_d"])}"')

        item = "      {\n" + ",\n".join(parts) + "\n      }"
        items.append(item)

    return "[\n" + ",\n".join(items) + "\n    ]"


# ============================================================
# DATA.JS INJECTION
# ============================================================

def find_fin1_block(content):
    """Find the start and end positions of the fin1 block in data.js."""
    match = re.search(r'"fin1"\s*:\s*\{', content)
    if not match:
        return None, None, None

    key_start = match.start()  # Start of "fin1"
    brace_start = content.index("{", match.start() + 5)  # The opening brace of fin1's value

    brace_count = 0
    in_str = False
    escape = False
    end_idx = None

    for idx in range(brace_start, len(content)):
        char = content[idx]
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_str = not in_str
            continue
        if not in_str:
            if char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0:
                    end_idx = idx + 1
                    break

    return key_start, brace_start, end_idx


def parse_existing_fin1(content, brace_start, brace_end):
    """Parse the existing fin1 JSON object."""
    fin1_str = content[brace_start:brace_end]
    try:
        fin1_obj = json.loads(fin1_str)
        return fin1_obj
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse existing fin1 JSON: {e}")
        return None


def build_new_fin1_block(existing_fin1, new_chapters):
    """Build the new fin1 block combining existing and new chapters."""
    # Merge: existing chapters (2, 5, 7) + new chapters (1, 3, 4, 6, 8, 9)
    all_chapter_keys = set()
    if existing_fin1:
        all_chapter_keys.update(existing_fin1.keys())
    all_chapter_keys.update(new_chapters.keys())

    # Sort by chapter number
    sorted_keys = sorted(all_chapter_keys, key=int)

    parts = []
    for ch_key in sorted_keys:
        if ch_key in new_chapters:
            # Use newly generated content
            js_array = generate_cq_js(new_chapters[ch_key], ch_key)
            parts.append(f'    "{ch_key}": {js_array}')
        elif existing_fin1 and ch_key in existing_fin1:
            # Preserve existing content
            existing_json = json.dumps(existing_fin1[ch_key], ensure_ascii=False, indent=6)
            # Fix indentation to match
            lines = existing_json.split("\n")
            reindented = []
            for line in lines:
                reindented.append("    " + line)
            existing_str = "\n".join(reindented)
            # Remove leading extra indent from first line
            existing_str = existing_str.lstrip()
            parts.append(f'    "{ch_key}": {existing_str}')

    fin1_block = "{\n" + ",\n".join(parts) + "\n  }"
    return fin1_block


def inject_into_datajs(new_chapters):
    """Inject the new chapters into data.js."""
    print("[INFO] Reading data.js...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[INFO] data.js size: {len(content)} bytes")

    # Find fin1 block
    key_start, brace_start, brace_end = find_fin1_block(content)
    if key_start is None:
        print("[ERROR] Could not find fin1 block in data.js!")
        return False

    print(f"[INFO] Found fin1 block: key_start={key_start}, brace_start={brace_start}, brace_end={brace_end}")
    print(f"[INFO] Existing fin1 block size: {brace_end - brace_start} bytes")

    # Parse existing fin1
    existing_fin1 = parse_existing_fin1(content, brace_start, brace_end)
    if existing_fin1 is None:
        return False

    print(f"[INFO] Existing fin1 chapters: {list(existing_fin1.keys())}")

    # Verify no overlap with target chapters (they should be new)
    for ch in TARGET_CHAPTERS:
        if ch in existing_fin1:
            print(f"[WARN] Chapter {ch} already exists in fin1! It will be replaced.")

    # Build new fin1 block
    new_fin1_block = build_new_fin1_block(existing_fin1, new_chapters)

    # Replace in content
    new_content = content[:brace_start] + new_fin1_block + content[brace_end:]

    print(f"[INFO] New data.js size: {len(new_content)} bytes")
    print(f"[INFO] Size change: +{len(new_content) - len(content)} bytes")

    return new_content


# ============================================================
# VALIDATION
# ============================================================

def validate_js_syntax(content):
    """Validate the JavaScript syntax by checking balanced braces/brackets and quote escaping."""
    errors = []

    # Check balanced braces
    brace_count = 0
    bracket_count = 0
    in_str = False
    escape = False
    line_num = 1

    for i, char in enumerate(content):
        if char == "\n":
            line_num += 1

        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_str = not in_str
            continue
        if not in_str:
            if char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count < 0:
                    errors.append(f"Unmatched closing brace at line {line_num}")
            elif char == "[":
                bracket_count += 1
            elif char == "]":
                bracket_count -= 1
                if bracket_count < 0:
                    errors.append(f"Unmatched closing bracket at line {line_num}")

    if brace_count != 0:
        errors.append(f"Unbalanced braces: {brace_count} unclosed")
    if bracket_count != 0:
        errors.append(f"Unbalanced brackets: {bracket_count} unclosed")
    if in_str:
        errors.append("Unterminated string at end of file")

    return errors


def validate_fin1_structure(content):
    """Validate the fin1 block can be re-parsed."""
    key_start, brace_start, brace_end = find_fin1_block(content)
    if key_start is None:
        return ["Cannot find fin1 block in modified content"]

    fin1_str = content[brace_start:brace_end]
    try:
        obj = json.loads(fin1_str)
        chapters = list(obj.keys())
        print(f"[INFO] Validated fin1 chapters: {chapters}")

        # Verify all target chapters exist
        for ch in TARGET_CHAPTERS:
            if ch not in obj:
                return [f"Chapter {ch} missing from fin1 after injection"]
            if not isinstance(obj[ch], list):
                return [f"Chapter {ch} is not an array"]
            if len(obj[ch]) == 0:
                return [f"Chapter {ch} is empty"]

        # Verify existing chapters preserved
        for ch in ["2", "5", "7"]:
            if ch not in obj:
                return [f"Existing chapter {ch} was lost during injection!"]

        # Count items
        total = 0
        for ch in sorted(obj.keys(), key=int):
            count = len(obj[ch])
            total += count
            print(f"[INFO]   Chapter {ch}: {count} CQs")
        print(f"[INFO]   Total: {total} CQs")

        return []
    except json.JSONDecodeError as e:
        return [f"JSON parse error in fin1 block: {e}"]


def validate_no_duplicate_ids(content):
    """Check for duplicate IDs within each chapter."""
    key_start, brace_start, brace_end = find_fin1_block(content)
    if key_start is None:
        return ["Cannot find fin1 block"]

    fin1_str = content[brace_start:brace_end]
    obj = json.loads(fin1_str)

    errors = []
    for ch, items in obj.items():
        ids = [item.get("id") for item in items if "id" in item]
        if len(ids) != len(set(ids)):
            dupes = [x for x in ids if ids.count(x) > 1]
            errors.append(f"Chapter {ch} has duplicate IDs: {set(dupes)}")

    return errors


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("FIN1 CH 1,3,4,6,8,9 CQ INJECTION")
    print("=" * 60)

    # Step 1: Check files exist
    if not os.path.exists(CSV_FILE):
        print(f"[FATAL] CSV file not found: {CSV_FILE}")
        sys.exit(1)
    if not os.path.exists(DATA_FILE):
        print(f"[FATAL] data.js not found: {DATA_FILE}")
        sys.exit(1)

    # Step 2: Create backup
    print(f"\n[STEP 1] Creating backup: {BACKUP_FILE}")
    shutil.copy2(DATA_FILE, BACKUP_FILE)
    print(f"[INFO] Backup created: {os.path.getsize(BACKUP_FILE)} bytes")

    # Step 3: Parse CSV
    print(f"\n[STEP 2] Parsing CSV: {CSV_FILE}")
    new_chapters = parse_csv()

    if not new_chapters:
        print("[FATAL] No data parsed from CSV!")
        sys.exit(1)

    # Step 4: Inject into data.js
    print(f"\n[STEP 3] Injecting into data.js...")
    new_content = inject_into_datajs(new_chapters)

    if new_content is False:
        print("[FATAL] Injection failed!")
        sys.exit(1)

    # Step 5: Validate
    print(f"\n[STEP 4] Validating...")

    # 5a: JS syntax validation
    syntax_errors = validate_js_syntax(new_content)
    if syntax_errors:
        print("[FATAL] Syntax validation failed:")
        for err in syntax_errors:
            print(f"  - {err}")
        print("[ABORT] No changes written to data.js")
        sys.exit(1)
    print("[PASS] JS syntax validation passed")

    # 5b: fin1 structure validation
    struct_errors = validate_fin1_structure(new_content)
    if struct_errors:
        print("[FATAL] Structure validation failed:")
        for err in struct_errors:
            print(f"  - {err}")
        print("[ABORT] No changes written to data.js")
        sys.exit(1)
    print("[PASS] fin1 structure validation passed")

    # 5c: Duplicate ID check
    dup_errors = validate_no_duplicate_ids(new_content)
    if dup_errors:
        print("[WARN] Duplicate ID warnings:")
        for err in dup_errors:
            print(f"  - {err}")
    else:
        print("[PASS] No duplicate IDs found")

    # Step 6: Write
    print(f"\n[STEP 5] Writing modified data.js...")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[INFO] Written: {os.path.getsize(DATA_FILE)} bytes")

    # Step 7: Final validation - re-read and verify
    print(f"\n[STEP 6] Final re-read validation...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        final_content = f.read()

    final_syntax = validate_js_syntax(final_content)
    if final_syntax:
        print("[FATAL] Final syntax validation failed after write!")
        print("[ROLLBACK] Restoring from backup...")
        shutil.copy2(BACKUP_FILE, DATA_FILE)
        print("[ROLLBACK] Backup restored.")
        sys.exit(1)

    final_struct = validate_fin1_structure(final_content)
    if final_struct:
        print("[FATAL] Final structure validation failed after write!")
        print("[ROLLBACK] Restoring from backup...")
        shutil.copy2(BACKUP_FILE, DATA_FILE)
        print("[ROLLBACK] Backup restored.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("INJECTION COMPLETE - ALL VALIDATIONS PASSED")
    print("=" * 60)
    print(f"Backup: {BACKUP_FILE}")
    print(f"Modified: {DATA_FILE}")


if __name__ == "__main__":
    main()
