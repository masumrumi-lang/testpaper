import csv
import re
import sys
from collections import Counter

input_file = sys.argv[1] if len(sys.argv) > 1 else r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_v3_EXPANDED.csv'
report_file = r'c:\Users\BMTF\.antigravity\testpaper\audit_discrepancy_report.txt'

def check_options_count(options_str):
    # Standard labels: a) b) c) d) or (a) (b) (c) (d)
    labels = re.findall(r'[a-d]\)', options_str.lower())
    if not labels:
        labels = re.findall(r'\([a-d]\)', options_str.lower())
    return len(set(labels))

def has_table_mention(text):
    keywords = ['table', 'stimulus', 'following data', 'information above', 'উদ্দীপক', 'ছক']
    return any(kw in text.lower() for kw in keywords)

perfect_count = 0
problematic_count = 0
discrepancies = []
seen_questions = {}

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row_id, row in enumerate(reader, start=1):
        # Safety Rule: Skip Chapter 1 and 8
        if 'Chapter 1' in row['Chapter'] or 'Chapter 8' in row['Chapter']:
            continue
            
        row_errors = []
        
        # 1. Option Count
        opt_count = check_options_count(row['Options'])
        if opt_count != 4:
            row_errors.append(f"Invalid option count: found {opt_count} options")
            
        # 2. Incomplete Stimulus
        if has_table_mention(row['Question']) and '|' not in row['Question']:
            row_errors.append("Stimulus/Table mentioned but no text table found")
            
        # 3. Missing Type Data
        # Level column should contain Board and Year or College Name
        is_board = 'board' in row['Level'].lower() or 'board' in row['Category'].lower()
        has_year = re.search(r'(\d{4}|\'\d{2})', row['Level'])
        
        if is_board and not has_year:
            row_errors.append(f"Missing Year in Board Question: '{row['Level']}'")
        elif not is_board and not has_year and row['Level'].strip() == '-':
            row_errors.append(f"Missing Source/Year: '{row['Level']}'")

        # 4. HTML Integrity
        if '|' in row['Question'] and not row['HTML_Code'].strip():
            row_errors.append("Pipe table present but HTML_Code is empty")
            
        # 5. Duplicate Check
        q_key = (row['Question'].strip().lower(), row['Options'].strip().lower())
        if q_key in seen_questions:
            row_errors.append(f"Duplicate of Row {seen_questions[q_key]}")
        else:
            seen_questions[q_key] = row_id
            
        # 6. Basic Math/Value Check (Heuristic)
        # If question asks for a numeric value but options are non-numeric or vice-versa
        is_numeric_q = any(word in row['Question'].lower() for word in ['how much', 'amount', 'balance', 'what is the', 'total'])
        has_numeric_opt = any(re.search(r'\d', opt) for opt in row['Options'].split())
        if is_numeric_q and not has_numeric_opt and '|' in row['Question']:
             # Might be a conceptual question about a table, but worth checking
             pass

        if row_errors:
            problematic_count += 1
            discrepancies.append(f"Row {row_id}: {' | '.join(row_errors)}")
        else:
            perfect_count += 1

with open(report_file, 'w', encoding='utf-8') as f:
    f.write("HSC MCQ Bank Audit Discrepancy Report\n")
    f.write("=====================================\n\n")
    f.write(f"Summary:\n")
    f.write(f"Total Rows Scanned (Excluding Ch 1/8): {perfect_count + problematic_count}\n")
    f.write(f"Perfect Rows: {perfect_count}\n")
    f.write(f"Problematic Rows: {problematic_count}\n\n")
    f.write("Detailed Discrepancies:\n")
    f.write("-" * 23 + "\n")
    f.write("\n".join(discrepancies))

print(f"Audit complete. Perfect: {perfect_count}, Problematic: {problematic_count}")
print(f"Report saved to {report_file}")
