import csv
import re
import html

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_v3_EXPANDED.csv'

expansion_map = {
    r'\bA/R\b': 'Accounts Receivable',
    r'\bAR\b': 'Accounts Receivable',
    r'\bA/P\b': 'Accounts Payable',
    r'\bAP\b': 'Accounts Payable',
    r'\bBRS\b': 'Bank Reconciliation Statement',
    r'\bTB\b': 'Trial Balance',
    r'\bC/B\b': 'Cash Book',
    r'\bCB\b': 'Cash Book',
    r'\bCOGS\b': 'Cost of Goods Sold',
    r'\bP/L\b': 'Profit and Loss',
    r'\bPL\b': 'Profit and Loss',
    r'\bAFBD\b': 'Allowance for Bad Debt',
    r'\bBD Prov\b': 'Allowance for Bad Debt',
    r'\bDep\b': 'Depreciation',
    r'\bDep\.\b': 'Depreciation',
    r'\bAcc\. Dep\b': 'Accumulated Depreciation',
    r'\bAcc\. Dep\.\b': 'Accumulated Depreciation',
    r'\bCap\b': 'Capital',
    r'\bBal\b': 'Balance',
    r'\bO/S\b': 'Outstanding',
    r'\bOS\b': 'Outstanding',
    r'\bInc\b': 'Income',
    r'\bExp\b': 'Expense',
    r'\bRev\b': 'Revenue',
    r'\bLiab\b': 'Liability',
    r'\bLiabs\b': 'Liabilities',
    r'\bEq\b': 'Equity',
    r'\bDr\b': 'Debit',
    r'\bCr\b': 'Credit',
    r'\bDr\.\b': 'Debit',
    r'\bCr\.\b': 'Credit',
}

def expand_text(text):
    if not isinstance(text, str): return text, []
    found = []
    new_text = text
    for pattern, replacement in expansion_map.items():
        # Check for presence case-insensitively
        if re.search(pattern, new_text, re.IGNORECASE):
            # Record what was found
            matches = re.findall(pattern, new_text, re.IGNORECASE)
            found.extend(list(set(matches)))
            # Replace
            new_text = re.sub(pattern, replacement, new_text, flags=re.IGNORECASE)
    return new_text, found

def generate_html_table(text):
    if '|' not in text:
        return ""
    lines = [l.strip() for l in text.split('\n') if '|' in l]
    if not lines: return ""
    html_output = '<table border="1" style="border-collapse: collapse; width: 100%;">'
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.split('|')]
        row_style = ' style="background-color: #f2f2f2;"' if i == 0 else ""
        html_output += f'<tr{row_style}>'
        for cell in cells:
            is_numeric = re.search(r'\d', cell) and not re.search(r'[a-zA-Z]{3,}', cell.replace('TK', ''))
            align = 'right' if is_numeric else 'left'
            tag = 'th' if i == 0 else 'td'
            html_output += f'<{tag} style="text-align: {align}; padding: 5px;">{html.escape(cell)}</{tag}>'
        html_output += '</tr>'
    html_output += '</table>'
    return html_output

results = []
row_reports = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row_id, row in enumerate(reader, start=1):
        if 'Chapter 1' in row['Chapter'] or 'Chapter 8' in row['Chapter']:
            results.append(row)
            continue
        
        row_found = []
        # Expand Question
        row['Question'], q_found = expand_text(row['Question'])
        row_found.extend(q_found)
        
        # Expand Options
        row['Options'], o_found = expand_text(row['Options'])
        row_found.extend(o_found)
        
        # Expand Explanation
        row['Explanation'], e_found = expand_text(row['Explanation'])
        row_found.extend(e_found)
        
        if row_found:
            # Sync HTML
            if '|' in row['Question']:
                row['HTML_Code'] = generate_html_table(row['Question'])
            
            row_reports.append(f"Row {row_id}: {', '.join(set(row_found))}")
        
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Total rows processed: {len(results)}")
print(f"Total rows modified: {len(row_reports)}")
with open(r'c:\Users\BMTF\.antigravity\testpaper\expansion_report.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(row_reports))
print("Expansion report saved to expansion_report.txt")
