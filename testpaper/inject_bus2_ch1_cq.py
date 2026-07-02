import csv
import json
import re
from pathlib import Path

INPUT_CSV = Path('BUS_2_CH1_CQ - ch1.cleaned.csv')
OUTPUT_JSON = Path('bus2_cq_data.json')
DATA_JS = Path('data.js')

BUS2_KEY = 'bus2'
CHAPTER_ID = '1'


def diagram_html_from_stem(stem: str) -> str:
    if '[Conceptual Diagram' not in stem:
        return stem

    # Extract the bracketed conceptual diagram text and draw it as a pre block.
    match = re.search(r'(\[Conceptual Diagram[^\]]*\])', stem)
    if not match:
        return stem

    bracket_text = match.group(1)
    diagram_text = bracket_text
    diagram_text = diagram_text.replace('概念', '')
    diagram_text = diagram_text.replace('$\\rightarrow$', '→')
    diagram_text = diagram_text.replace('\\rightarrow', '→')
    diagram_text = diagram_text.replace('$\rightarrow$', '→')
    diagram_text = diagram_text.replace('->', '→')
    diagram_text = diagram_text.replace('`', '')

    # Clean the bracketed text to isolate the diagram flow
    inner = diagram_text
    if inner.startswith('[') and inner.endswith(']'):
        inner = inner[1:-1].strip()

    # Use the bracket text as a caption and a simplified line diagram.
    return (
        f'<p>{bracket_text}</p>'
        f'<div style="background:#f8fafc;border:1px solid #d1d5db;border-radius:0.75rem;padding:0.9rem;margin-top:0.8rem;">'
        f'<pre style="margin:0;font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, \"Liberation Mono\", \"Courier New\", monospace; white-space:pre-wrap; font-size:0.95rem; line-height:1.5;">{inner}</pre>'
        f'</div>'
    )


def clean_html(text: str) -> str:
    if not text:
        return ''
    text = text.strip()
    if text.startswith('<') and text.endswith('>'):
        return text
    text = diagram_html_from_stem(text)
    if text.startswith('<') and text.endswith('>'):
        return text
    return text.replace('\n', '<br>')


def process_csv(file_path: Path):
    chapters = {}
    with file_path.open('r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            chapter_str = row['Chapter'].strip()
            chapter_num_match = re.search(r'\d+', chapter_str)
            chapter_id = str(int(chapter_num_match.group())) if chapter_num_match else '1'

            if chapter_id not in chapters:
                chapters[chapter_id] = {
                    'subjectName': 'Business Organization & Management 2nd Paper',
                    'chapterName': f'Chapter {chapter_id}',
                    'mcqData': [],
                    'shortCQData': [],
                    'fullCQData': []
                }

            year = row['Year'].strip()
            level = row['Level'].strip()
            category = row['Category'].strip().lower() or 'board'
            meta = f'{level} · {year}' if level else year
            q_type = category if category else 'board'

            cq_id = str(len(chapters[chapter_id]['fullCQData']) + 1).zfill(2)
            questions = []
            for label in ['A', 'B', 'C', 'D']:
                q_text = row.get(f'Question_{label}', '').strip()
                a_text = row.get(f'Ans_{label}', '').strip()
                if q_text:
                    questions.append({
                        'label': label.lower(),
                        'text': q_text,
                        'answer': a_text.replace('\n', '<br>')
                    })

            chapters[chapter_id]['fullCQData'].append({
                'id': cq_id,
                'stem': clean_html(row['Stem']),
                'meta': meta,
                'type': q_type,
                'questions': questions
            })

            if row.get('Question_A', '').strip():
                chapters[chapter_id]['shortCQData'].append({
                    'id': f'{cq_id}A',
                    'text': row['Question_A'].strip(),
                    'meta': f'Knowledge · {meta}',
                    'type': q_type,
                    'answer': row.get('Ans_A', '').strip().replace('\n', '<br>')
                })
            if row.get('Question_B', '').strip():
                chapters[chapter_id]['shortCQData'].append({
                    'id': f'{cq_id}B',
                    'text': row['Question_B'].strip(),
                    'meta': f'Comprehension · {meta}',
                    'type': q_type,
                    'answer': row.get('Ans_B', '').strip().replace('\n', '<br>')
                })

    return chapters


def format_json_for_datajs(obj):
    json_text = json.dumps(obj, indent=4, ensure_ascii=False)
    lines = json_text.splitlines()
    return '\n'.join('    ' + line for line in lines)


def replace_or_insert_chapter(data_js_text: str, chapter_id: str, chapter_obj: dict) -> str:
    bus2_idx = data_js_text.find(f'"{BUS2_KEY}":')
    if bus2_idx == -1:
        raise RuntimeError('bus2 section not found in data.js')

    # Find the opening brace of bus2 object
    brace_idx = data_js_text.find('{', bus2_idx)
    if brace_idx == -1:
        raise RuntimeError('bus2 object open brace not found')

    # Look for existing chapter block
    chapter_pattern = re.compile(rf'"{chapter_id}"\s*:\s*\{{', re.MULTILINE)
    chapter_match = chapter_pattern.search(data_js_text, brace_idx)
    if chapter_match and data_js_text.find('"2":', brace_idx) > chapter_match.start():
        # Replace existing chapter block
        start = chapter_match.start()
        depth = 0
        end = None
        for i in range(start, len(data_js_text)):
            if data_js_text[i] == '{':
                depth += 1
            elif data_js_text[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise RuntimeError('Could not locate end of existing chapter block')
        replacement = format_json_for_datajs({chapter_id: chapter_obj})
        replacement = replacement.strip()
        replacement = replacement[4:]  # remove outer indentation of json.dumps
        return data_js_text[:start] + replacement + data_js_text[end:]

    # Insert before chapter 2 or before closing brace
    insert_pattern = re.compile(r'\n(\s*)"2"\s*:\s*\{')
    insert_match = insert_pattern.search(data_js_text, brace_idx)
    insert_text = format_json_for_datajs({chapter_id: chapter_obj}).strip()
    if insert_match:
        insert_pos = insert_match.start(0)
        return data_js_text[:insert_pos] + insert_text + ',\n' + data_js_text[insert_pos:]

    # Fallback: insert before closing brace of bus2
    depth = 0
    end = None
    for i in range(brace_idx, len(data_js_text)):
        if data_js_text[i] == '{':
            depth += 1
        elif data_js_text[i] == '}':
            depth -= 1
            if depth == 0:
                end = i
                break
    if end is None:
        raise RuntimeError('Could not locate end of bus2 object')
    return data_js_text[:end] + ',\n' + insert_text + data_js_text[end:]


def main():
    chapters = process_csv(INPUT_CSV)
    if CHAPTER_ID not in chapters:
        raise RuntimeError(f'Chapter {CHAPTER_ID} not found in {INPUT_CSV}')

    # Write updated JSON file
    with OUTPUT_JSON.open('w', encoding='utf-8', newline='') as f:
        json.dump(chapters, f, indent=4, ensure_ascii=False)

    chapter_obj = chapters[CHAPTER_ID]

    data_js_text = DATA_JS.read_text(encoding='utf-8')
    new_text = replace_or_insert_chapter(data_js_text, CHAPTER_ID, chapter_obj)
    DATA_JS.write_text(new_text, encoding='utf-8')

    print(f'Injected bus2 chapter {CHAPTER_ID} CQ into {DATA_JS.name}.')
    print(f'Updated JSON written to {OUTPUT_JSON.name}.')


if __name__ == '__main__':
    main()
