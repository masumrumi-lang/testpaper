import csv
import re
import html

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'

abbreviations = {
    r'\bGP\b': 'Gross Profit',
    r'\bSR\b': 'Service Revenue',
    r'\bA/R\b': 'Accounts Receivable',
    r'\bA/P\b': 'Accounts Payable',
    r'\bAFBD\b': 'Allowance for Bad Debt',
    r'\bProv\. for Bad Debt\b': 'Allowance for Bad Debt',
    r'\bProv\. for Debtors\b': 'Allowance for Debtors',
    r'\bA/C\b': 'Account',
    r'\bDr\b': 'Debit',
    r'\bCr\b': 'Credit',
    r'\bDr\.\b': 'Debit',
    r'\bCr\.\b': 'Credit',
    r'\bExp\b': 'Expense',
    r'\bInc\b': 'Income',
    r'\bRec\b': 'Receivable',
    r'\bPay\b': 'Payable',
    r'\bRet\b': 'Return',
    r'\bBal\b': 'Balance',
    r'\bOD\b': 'Overdraft',
    r'\bComm\b': 'Commission',
    r'\bInt\b': 'Interest',
    r'\bc/d\b': 'carried down',
    r'\bb/d\b': 'brought down',
    r'\ba/c\b': 'account',
    r'\bA up\b': 'Asset increase',
    r'\bA down\b': 'Asset decrease',
    r'\bL up\b': 'Liability increase',
    r'\bL down\b': 'Liability decrease',
    r'\bE up\b': 'Equity increase',
    r'\bE down\b': 'Equity decrease',
    r'\bTB\b': 'Trial Balance',
    r'\bBRS\b': 'Bank Reconciliation Statement',
    r'\bNSF\b': 'Not Sufficient Funds',
    r'\bOp\b': 'Opening',
    r'\bCl\b': 'Closing',
    r'\bCap\b': 'Capital',
    r'\bA & L\b': 'Assets and Liabilities',
    r'\bA\b': 'Asset',
    r'\bL\b': 'Liability',
    r'\bE\b': 'Equity',
}

def localize_and_expand(text):
    if not isinstance(text, str):
        return text
    
    # Currency localization: $5,000 -> 5,000 TK
    text = re.sub(r'\$(\d+(?:,\d+)*(?:\.\d+)?)', r'\1 TK', text)
    text = re.sub(r'(\d+(?:,\d+)*(?:\.\d+)?)\s*\$', r'\1 TK', text)
    text = text.replace('$', 'TK')

    # Specific replacements with context awareness
    # Assets, Liabilities, Equity (A, L, E) - only if they are standalone and NOT option labels
    text = re.sub(r'\bA\b(?!\s*[\)\.])', 'Asset', text)
    text = re.sub(r'\bL\b(?!\s*[\)\.])', 'Liability', text)
    text = re.sub(r'\bE\b(?!\s*[\)\.])', 'Equity', text)

    # Standard abbreviations
    for pattern, replacement in abbreviations.items():
        # Skip A, L, E as they are handled above
        if pattern in [r'\ba\b', r'\bl\b', r'\be\b', r'\bA\b', r'\bL\b', r'\bE\b']:
            continue
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # Clean up any "Asset increase" etc if they were doubled (unlikely with \b)
    return text

def standardize_table_headers(text):
    if '|' in text:
        lines = text.split('\n')
        new_lines = []
        for line in lines:
            if '|' in line:
                parts = [p.strip() for p in line.split('|')]
                header_terms = ['particulars', 'debit', 'credit', 'taka', 'amount', 'tk', 'assets', 'liabilities']
                match_count = sum(1 for p in parts if any(term in p.lower() for term in header_terms))
                
                if match_count >= 1:
                    new_parts = []
                    for p in parts:
                        p_low = p.lower()
                        if 'particular' in p_low: new_parts.append('Particulars')
                        elif 'debit' in p_low: 
                            if 'tk' not in p_low: new_parts.append('Debit (TK)')
                            else: new_parts.append(p.replace('Taka', 'TK').replace('taka', 'TK'))
                        elif 'credit' in p_low: 
                            if 'tk' not in p_low: new_parts.append('Credit (TK)')
                            else: new_parts.append(p.replace('Taka', 'TK').replace('taka', 'TK'))
                        elif 'taka' in p_low: new_parts.append(p.replace('Taka', 'TK').replace('taka', 'TK'))
                        else: new_parts.append(p)
                    line = " | ".join(new_parts)
            new_lines.append(line)
        return "\n".join(new_lines)
    return text

def generate_html_table(text):
    if '|' not in text:
        return ""
    
    lines = [l.strip() for l in text.split('\n') if '|' in l]
    if not lines:
        return ""
    
    html_output = '<table border="1" style="border-collapse: collapse; width: 100%;">'
    
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.split('|')]
        row_style = ' style="background-color: #f2f2f2;"' if i == 0 else ""
        html_output += f'<tr{row_style}>'
        
        for cell in cells:
            # Determine alignment
            # Numeric if it contains digits and not much else (allowing commas, dots, TK)
            is_numeric = re.search(r'\d', cell) and not re.search(r'[a-zA-Z]{3,}', cell.replace('TK', ''))
            align = 'right' if is_numeric else 'left'
            
            tag = 'th' if i == 0 else 'td'
            html_output += f'<{tag} style="text-align: {align}; padding: 5px;">{html.escape(cell)}</{tag}>'
        
        html_output += '</tr>'
    
    html_output += '</table>'
    return html_output

def check_options(options_str):
    if not options_str: return False
    options_str = options_str.lower()
    # Check for various formats: a) (a) a.
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
    if '|' not in question_text:
        return True, 0, 0
    
    lines = [l.strip() for l in question_text.split('\n') if '|' in l]
    if len(lines) < 2:
        return True, 0, 0

    # Only check if there is a "Total" row
    total_row = None
    for line in lines:
        if 'total' in line.lower():
            total_row = line
            break
    
    if not total_row:
        return True, 0, 0 # Not a complete TB or can't verify

    debit_total = 0
    credit_total = 0
    
    # Try to find columns for Debit and Credit
    header = [c.strip().lower() for c in lines[0].split('|')]
    debit_idx = -1
    credit_idx = -1
    for idx, h in enumerate(header):
        if 'debit' in h: debit_idx = idx
        if 'credit' in h: credit_idx = idx
        
    if debit_idx == -1 or credit_idx == -1:
        return True, 0, 0
    
    cells = [c.strip() for c in total_row.split('|')]
    if len(cells) > max(debit_idx, credit_idx):
        d_val = cells[debit_idx].replace(',', '').replace('TK', '').strip()
        c_val = cells[credit_idx].replace(',', '').replace('TK', '').strip()
        
        def parse_val(v):
            if not v: return 0
            v = re.sub(r'[^0-9.LkK]', '', v)
            if not v: return 0
            factor = 1
            if v.upper().endswith('L'): factor = 100000; v = v[:-1]
            elif v.upper().endswith('K'): factor = 1000; v = v[:-1]
            try: return float(v) * factor
            except: return 0
        
        debit_total = parse_val(d_val)
        credit_total = parse_val(c_val)
            
    if debit_total > 0 and credit_total > 0 and abs(debit_total - credit_total) > 1.0:
        return False, debit_total, credit_total
    
    return True, debit_total, credit_total

results = []
qc_flags = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ['HTML_Code']
    
    for row_id, row in enumerate(reader, start=1):
        if row_id == 1:
            print(f"DEBUG Row 1 fields: {row.keys()}")
            print(f"DEBUG Row 1 values: {row}")
        
        # 1. Localization & Terminology
        for field in ['Question', 'Options', 'Explanation']:
            row[field] = localize_and_expand(row[field])
            
        # 2. Structural Standardization (Question Column)
        row['Question'] = standardize_table_headers(row['Question'])
        
        # 3. HTML Generation
        row['HTML_Code'] = generate_html_table(row['Question'])
        
        # 4. Quality Control
        # Trial Balance check
        tb_ok, d_sum, c_sum = check_trial_balance(row['Question'])
        if not tb_ok:
            qc_flags.append(f"Row {row_id}: Trial Balance mismatch (Debit: {d_sum}, Credit: {c_sum})")
            
        # Options check
        if not check_options(row['Options']):
            qc_flags.append(f"Row {row_id}: Missing one or more options (a-d)")
            
        results.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Processed {len(results)} rows.")
print(f"Saved to {output_file}")

# Summarize QC flags
if qc_flags:
    print("\nQC Flags (First 20):")
    for flag in qc_flags[:20]:
        print(flag)
    print(f"... and {len(qc_flags) - 20} more flags.")
else:
    print("\nNo QC issues found.")

# Write QC flags to a separate file for the user
qc_file = r'c:\Users\BMTF\.antigravity\testpaper\qc_report.txt'
with open(qc_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(qc_flags))
print(f"Full QC report saved to {qc_file}")
