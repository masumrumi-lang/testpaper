import csv
import json
import re
import os
import shutil
import sys
import subprocess

CSV_FILE = "Fin1_ch_1_3_4_6_8_9_cq - Sheet1.csv"
DATA_FILE = "data.js"
BACKUP_FILE = "data.js.bak_fin1_surgical"
TARGET_CHAPTERS = ["1", "3", "4", "6", "8", "9"]

# ============================================================
# CONTENT PROCESSING FUNCTIONS (FROM ORIGINAL SCRIPT)
# ============================================================

def sanitize(text):
    if not text:
        return ""
    return text.replace('\r\n', '\n').strip()

def detect_pipe_table(text):
    lines = text.strip().split("\n")
    pipe_lines = [l for l in lines if "|" in l and l.strip()]
    return len(pipe_lines) >= 2

def build_html_table(rows, first_row_header=True):
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

def reconstruct_project_cash_flow_table(text):
    lines = text.strip().split("\n")
    current_intro = []
    projects = {}
    current_project = None
    current_project_data = []
    project_order = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

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
    if current_intro:
        html += "<p>" + "<br>".join(current_intro) + "</p>"

    all_year_based = True
    for proj_name in project_order:
        data = projects[proj_name]
        for k, v in data:
            if not re.match(r'^Year\s+\d+', k, re.IGNORECASE):
                all_year_based = False

    if all_year_based and len(project_order) >= 2:
        years = []
        for proj_name in project_order:
            for k, v in projects[proj_name]:
                if k not in years:
                    years.append(k)

        html += "<table>"
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
    if not text or not text.strip():
        return ""
    text = text.strip()

    if re.search(r'<table|<tr|<td|<th', text, re.IGNORECASE):
        text = text.replace("\n\n", "<br><br>")
        text = text.replace("\n", "<br>")
        return text

    if re.search(r'(Project|Bond|Security|Investment|Source|Option)\s+[A-Za-z0-9]+\s*:', text, re.IGNORECASE):
        has_newline_kv = bool(re.search(r'\n\s*(Year|Initial|Cash|Expected|Return|Standard|Face|Coupon|Maturity|Required|Current|Dividend|Growth|Flotation|Market|Interest|BDT)\s', text, re.IGNORECASE))
        if has_newline_kv:
            result = reconstruct_project_cash_flow_table(text)
            if result:
                return result

    if detect_pipe_table(text):
        result = reconstruct_pipe_table_content(text)
        if result:
            return result

    result = reconstruct_stimulus_kv_table(text)
    if result:
        return result

    text = text.replace("\n\n\n", "<br><br>")
    text = text.replace("\n\n", "<br><br>")
    text = text.replace("\n", "<br>")
    return text

# ============================================================
# CSV PARSING
# ============================================================

def parse_csv():
    chapter_data = {ch: {"full": [], "short": []} for ch in TARGET_CHAPTERS}
    
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            ch = row.get("Chapter", "").strip()
            if ch not in TARGET_CHAPTERS:
                continue

            stem = process_content(row.get("Stem", ""))
            meta = f"{row.get('Level', '-')} · {row.get('Year', '-')}"
            q_type = row.get('Category', 'board').strip().lower()

            questions = []
            if row.get("Question_A"):
                questions.append({"label": "a", "text": process_content(row["Question_A"]), "answer": process_content(row.get("Ans_A", ""))})
            if row.get("Question_B"):
                questions.append({"label": "b", "text": process_content(row["Question_B"]), "answer": process_content(row.get("Ans_B", ""))})
            if row.get("Question_C"):
                questions.append({"label": "c", "text": process_content(row["Question_C"]), "answer": process_content(row.get("Ans_C", ""))})
            if row.get("Question_D"):
                questions.append({"label": "d", "text": process_content(row["Question_D"]), "answer": process_content(row.get("Ans_D", ""))})

            idx = len(chapter_data[ch]["full"]) + 1
            full_item = {
                "id": f"fin1-ch{ch}-cq-{idx:03d}",
                "stem": stem,
                "meta": meta,
                "type": q_type,
                "questions": questions
            }
            chapter_data[ch]["full"].append(full_item)

            if row.get("Question_A"):
                chapter_data[ch]["short"].append({
                    "id": f"fin1-ch{ch}-short-a-{idx:03d}",
                    "text": process_content(row["Question_A"]),
                    "answer": process_content(row.get("Ans_A", "")),
                    "meta": meta,
                    "type": q_type
                })
            if row.get("Question_B"):
                chapter_data[ch]["short"].append({
                    "id": f"fin1-ch{ch}-short-b-{idx:03d}",
                    "text": process_content(row["Question_B"]),
                    "answer": process_content(row.get("Ans_B", "")),
                    "meta": meta,
                    "type": q_type
                })
                
    return chapter_data

# ============================================================
# SURGICAL INJECTION
# ============================================================

def find_fin1_block(content):
    match = re.search(r'"fin1"\s*:\s*\{', content)
    if not match:
        return None, None, None

    key_start = match.start()
    brace_start = content.index("{", match.start() + 5)

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

def surgical_inject():
    print("Parsing CSV...")
    chapter_data = parse_csv()
    for ch in TARGET_CHAPTERS:
        print(f"Chapter {ch}: {len(chapter_data[ch]['full'])} Full CQs, {len(chapter_data[ch]['short'])} Short CQs")

    print(f"Reading {DATA_FILE}...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    key_start, brace_start, brace_end = find_fin1_block(content)
    if key_start is None:
        print("Error: fin1 block not found!")
        return

    fin1_block_str = content[brace_start:brace_end]
    
    # We will modify fin1_block_str surgically for each target chapter.
    for ch in TARGET_CHAPTERS:
        # Find chapter entry inside fin1 block
        # For example, "1": { ... } or "1": { subjectName: "Finance 1st Paper", ... }
        ch_pattern = re.compile(rf'"{ch}"\s*:\s*\{')
        ch_match = ch_pattern.search(fin1_block_str)
        if not ch_match:
            print(f"Error: Chapter {ch} not found in fin1 block!")
            return

        ch_start = ch_match.start()
        # Find brace bounds for this chapter
        brace_count = 0
        ch_end = -1
        for i in range(ch_start, len(fin1_block_str)):
            if fin1_block_str[i] == '{':
                brace_count += 1
            elif fin1_block_str[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    ch_end = i + 1
                    break
        
        ch_obj_str = fin1_block_str[ch_start:ch_end]
        
        # In this chapter object, replace shortCQData: [] and fullCQData: []
        # We will add markers inside the brackets
        short_json = json.dumps(chapter_data[ch]["short"], ensure_ascii=False, indent=4)
        inner_short_json = short_json.strip().strip('[]').strip()
        short_lines = [" " * 16 + line for line in inner_short_json.split("\n")]
        short_replacement = (
            "[\n" +
            f"            // === FIN1_CH{ch}_SHORTCQ_START ===\n" +
            "\n".join(short_lines) + "\n" +
            f"            // === FIN1_CH{ch}_SHORTCQ_END ===\n" +
            "            ]"
        )

        full_json = json.dumps(chapter_data[ch]["full"], ensure_ascii=False, indent=4)
        inner_full_json = full_json.strip().strip('[]').strip()
        full_lines = [" " * 16 + line for line in inner_full_json.split("\n")]
        full_replacement = (
            "[\n" +
            f"            // === FIN1_CH{ch}_FULLCQ_START ===\n" +
            "\n".join(full_lines) + "\n" +
            f"            // === FIN1_CH{ch}_FULLCQ_END ===\n" +
            "            ]"
        )

        # Replace shortCQData: []
        new_ch_obj_str = re.sub(r'shortCQData:\s*\[\s*\]', f'shortCQData: {short_replacement}', ch_obj_str)
        # Replace fullCQData: []
        new_ch_obj_str = re.sub(r'fullCQData:\s*\[\s*\]', f'fullCQData: {full_replacement}', new_ch_obj_str)

        # Replace this chapter block in fin1_block_str
        fin1_block_str = fin1_block_str[:ch_start] + new_ch_obj_str + fin1_block_str[ch_end:]

    # Reconstruct new data.js content
    new_content = content[:brace_start] + fin1_block_str + content[brace_end:]

    # Backup and Write
    print(f"Creating backup to {BACKUP_FILE}...")
    shutil.copy2(DATA_FILE, BACKUP_FILE)

    print(f"Writing updated {DATA_FILE}...")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Surgical injection completed. Validating syntax...")
    # Validate using node
    result = subprocess.run(['node', '-c', DATA_FILE], capture_output=True, text=True)
    if result.returncode == 0:
        print("Syntax Validation: PASSED")
    else:
        print("Syntax Validation: FAILED")
        print(result.stderr)
        print("ROLLING BACK changes...")
        shutil.copy2(BACKUP_FILE, DATA_FILE)
        print("Rollback complete.")

if __name__ == "__main__":
    surgical_inject()
