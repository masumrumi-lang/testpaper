import json
from pathlib import Path

base = Path('c:/Users/BMTF/OneDrive/Documents/Rumi/testpaper')

data_js_path = base / 'data.js'
bus1_data_path = base / 'bus1_data.json'
bus1_cq_path = base / 'bus1_cq_data.json'
backup_path = base / 'data.js.bak'

# Load JSON files
with bus1_data_path.open('r', encoding='utf-8') as f:
    bus1_data = json.load(f)

with bus1_cq_path.open('r', encoding='utf-8') as f:
    bus1_cq = json.load(f)

# Merge chapter data
merged = {}
for ch_id, ch_obj in bus1_data.items():
    merged[ch_id] = {
        'subjectName': ch_obj.get('subjectName', 'Business Organization 1st Paper'),
        'chapterName': ch_obj.get('chapterName', f'Chapter {ch_id}'),
        'mcqData': ch_obj.get('mcqData', [])
    }

for ch_id, cq_obj in bus1_cq.items():
    if ch_id not in merged:
        merged[ch_id] = {
            'subjectName': 'Business Organization 1st Paper',
            'chapterName': f'Chapter {ch_id}',
            'mcqData': []
        }
    merged[ch_id]['shortCQData'] = cq_obj.get('shortCQData', [])
    merged[ch_id]['fullCQData'] = cq_obj.get('fullCQData', [])

# Prepare insertion text
new_entry = json.dumps({'bus1': merged}, indent=4, ensure_ascii=False)
# Remove outer braces from new_entry to get inside content
new_entry = new_entry[1:-1].strip()

# Load data.js
text = data_js_path.read_text(encoding='utf-8')
if '"bus1"' in text:
    raise SystemExit('bus1 already present in data.js; aborting to avoid overwrite.')

# Backup
data_js_path.write_text(text, encoding='utf-8')
backup_path.write_text(text, encoding='utf-8')
print(f'Backup created: {backup_path}')

# Insert before final closing of testDatabase
end_idx = text.rfind('\n};')
if end_idx == -1:
    end_idx = text.rfind('};')
if end_idx == -1:
    raise SystemExit('Could not find closing testDatabase brace in data.js')

# Determine if we need a comma before insert
insert_text = text[:end_idx].rstrip()
if insert_text.endswith(','):
    prefix = '\n'
else:
    prefix = ',\n'

new_text = text[:end_idx] + prefix + new_entry + '\n' + text[end_idx:]

# Write result
data_js_path.write_text(new_text, encoding='utf-8')
print('Injected bus1 into data.js')
print('bus1 present count:', new_text.count('"bus1"'))
