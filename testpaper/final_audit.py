import csv
import re

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'

def check_options(options_str):
    if not options_str: return False
    options_str = options_str.lower()
    patterns = [
        [r'a\)', r'b\)', r'c\)', r'd\)'],
        [r'\(a\)', r'\(b\)', r'\(c\)', r'\(d\)'],
        [r'a\.\s', r'b\.\s', r'c\.\s', r'd\.\s']
    ]
    for p_set in patterns:
        if all(re.search(p, options_str) for p in p_set):
            return True
    return False

def check_trial_balance(question_text):
    if '|' not in question_text: return True, 0, 0
    lines = [l.strip() for l in question_text.split('\n') if '|' in l]
    if len(lines) < 2: return True, 0, 0
    total_row = next((l for l in lines if 'total' in l.lower()), None)
    if not total_row: return True, 0, 0
    
    header = [c.strip().lower() for c in lines[0].split('|')]
    debit_idx = next((i for i, h in enumerate(header) if 'debit' in h), -1)
    credit_idx = next((i for i, h in enumerate(header) if 'credit' in h), -1)
    if debit_idx == -1 or credit_idx == -1: return True, 0, 0
    
    cells = [c.strip() for c in total_row.split('|')]
    def parse_val(v):
        v = re.sub(r'[^0-9.LkK]', '', v)
        if not v: return 0
        factor = 1
        if v.upper().endswith('L'): factor = 100000; v = v[:-1]
        elif v.upper().endswith('K'): factor = 1000; v = v[:-1]
        try: return float(v) * factor
        except: return 0
    
    if len(cells) > max(debit_idx, credit_idx):
        d = parse_val(cells[debit_idx])
        c = parse_val(cells[credit_idx])
        if d > 0 and c > 0 and abs(d - c) > 1.0: return False, d, c
    return True, 0, 0

qc_flags = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        if not check_options(row['Options']):
            qc_flags.append(f"Row {row_id}: Missing options (a-d)")
        
        ok, d, c = check_trial_balance(row['Question'])
        if not ok:
            qc_flags.append(f"Row {row_id}: Trial Balance mismatch (Dr: {d}, Cr: {c})")

print(f"Total rows scanned: {row_id}")
print(f"Total remaining errors: {len(qc_flags)}")
if qc_flags:
    for flag in qc_flags[:20]: print(flag)
