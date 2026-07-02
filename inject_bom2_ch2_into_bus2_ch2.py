import csv
import json
import re
import shutil


def clean_text(text):
    if not text:
        return ""
    text = text.strip().replace('\r', '')
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


def parse_bom2_ch2(csv_path='BOM2_Ch2_CQ - Sheet1.csv'):
    cqs = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        cq_id = 0
        for row in reader:
            if len(row) < 14:
                continue
            year = row[0].strip()
            subj = row[1].strip()
            chapter = row[2].strip()
            level = row[3].strip()
            category = row[4].strip()
            stem = row[5].strip()
            qa = row[6].strip() if len(row) > 6 else ''
            qb = row[7].strip() if len(row) > 7 else ''
            qc = row[8].strip() if len(row) > 8 else ''
            qd = row[9].strip() if len(row) > 9 else ''
            aa = row[10].strip() if len(row) > 10 else ''
            ab = row[11].strip() if len(row) > 11 else ''
            ac = row[12].strip() if len(row) > 12 else ''
            ad = row[13].strip() if len(row) > 13 else ''

            if not stem and not qa:
                continue

            cq_id += 1
            stem_c = clean_text(stem)
            aa_c = clean_text(aa)
            ab_c = clean_text(ab)
            ac_c = clean_text(ac)
            ad_c = clean_text(ad)

            meta = f"{level} · {year}"
            cq_type = category.lower() if category else 'board'

            cq = {
                "id": str(cq_id).zfill(2),
                "stem": stem_c,
                "meta": meta,
                "type": cq_type,
                "questions": [
                    {"label": "a", "text": qa, "answer": aa_c},
                    {"label": "b", "text": qb, "answer": ab_c},
                    {"label": "c", "text": qc, "answer": ac_c},
                    {"label": "d", "text": qd, "answer": ad_c}
                ]
            }
            cqs.append(cq)
    return cqs


def inject_to_bus2_ch2(cqs, db_path='data.js'):
    backup = db_path + '.bak_bom2_ch2_to_bus2'
    shutil.copy2(db_path, backup)
    print(f'Backup: {backup}')

    with open(db_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build chapter object
    ch_obj = {
        "subjectName": "Business Org & Mgmt 2nd Paper",
        "chapterName": "Chapter 2 : Principles of Management",
        "mcqData": [],
        "shortCQData": [],
        "fullCQData": cqs
    }

    # Find or create bus2
    if '"bus2"' in content:
        # Replace or insert chapter "2" under bus2
        # Locate bus2 block
        bus2_start = content.find('"bus2"')
        brace_open = content.find('{', bus2_start)
        # find matching closing brace for bus2 block
        idx = brace_open
        depth = 0
        end_idx = -1
        while idx < len(content):
            if content[idx] == '{':
                depth += 1
            elif content[idx] == '}':
                depth -= 1
                if depth == 0:
                    end_idx = idx + 1
                    break
            idx += 1
        bus2_block = content[bus2_start:end_idx]

        # Check if chapter "2" exists
        if '"2"' in bus2_block:
            # Replace existing "2" block's fullCQData
            new_bus2_block = re.sub(r'"2"\s*:\s*\{.*?\}', '"2": ' + json.dumps(ch_obj, indent=4, ensure_ascii=False), bus2_block, flags=re.DOTALL)
        else:
            # Insert new chapter before closing brace of bus2_block
            insert_at = bus2_block.rfind('}')
            prefix = bus2_block[:insert_at]
            suffix = bus2_block[insert_at:]
            addition = ',\n    "2": ' + json.dumps(ch_obj, indent=4, ensure_ascii=False) + '\n'
            new_bus2_block = prefix + addition + suffix

        new_content = content[:bus2_start] + new_bus2_block + content[end_idx:]
    else:
        # Create bus2 at end before final closing brace
        insert_at = content.rfind('};')
        if insert_at == -1:
            insert_at = content.rfind('}')
        bus2_str = '\n    "bus2": {\n' + '    "2": ' + json.dumps(ch_obj, indent=4, ensure_ascii=False) + '\n    }\n'
        # Ensure comma separation
        new_content = content[:insert_at].rstrip()
        if not new_content.endswith(','):
            new_content += ',\n'
        new_content += bus2_str + content[insert_at:]

    with open(db_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'Injected {len(cqs)} CQs into bus2["2"]')


if __name__ == '__main__':
    print('Parsing BOM2_Ch2 CSV...')
    cqs = parse_bom2_ch2()
    print(f'Parsed {len(cqs)} entries')
    print('Injecting into data.js -> bus2["2"] ...')
    inject_to_bus2_ch2(cqs)
    print('Done.')
