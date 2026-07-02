import csv
import re
import html

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_v3_EXPANDED.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_FINAL_REPAIRED.csv'

def generate_html_table(text):
    if '|' not in text: return ""
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

# Board Year Mapping (Common knowledge for these MCQ banks)
year_map = {
    890: "Sylhet Board - 2017",
    891: "Barishal Board - 2019",
    892: "Barishal Board - 2019",
    1455: "Chattogram & Sylhet Board - 2017",
    1460: "Rajshahi & Barishal Board - 2017",
}

def fix_metadata(level, row_id):
    if row_id in year_map:
        return year_map[row_id]
    
    val = level.strip()
    # Expand board names
    val = val.replace('Ctg', 'Chattogram').replace('Syl', 'Sylhet').replace('Raj', 'Rajshahi')
    val = val.replace('Com', 'Cumilla').replace('Jes', 'Jashore').replace('Din', 'Dinajpur')
    val = val.replace('Barisal', 'Barishal')
    
    if 'Board' not in val and val != '-':
        if any(b in val for b in ['Dhaka', 'Cumilla', 'Rajshahi', 'Jashore', 'Sylhet', 'Barishal', 'Chattogram', 'Dinajpur']):
            val += " Board"
    
    # Handle '21 style years
    val = re.sub(r'\'(\d{2})', r'20\1', val)
    
    return val

rows = []
modified_years = []

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row_id, row in enumerate(reader, start=1):
        # Skip Ch 1 and 8
        if 'Chapter 1' in row['Chapter'] or 'Chapter 8' in row['Chapter']:
            rows.append(row)
            continue
            
        # 1. Global fix for A/C corruption
        # Revert "Asset/Cash Book" and "Asset/C" to "Account"
        for field in ['Question', 'Options', 'Explanation']:
            row[field] = row[field].replace('Asset/Cash Book', 'Account')
            row[field] = row[field].replace('Asset/C', 'Account')
            row[field] = row[field].replace('Asset/c', 'account')
        
        # 2. Specific Option Fixes
        if row_id == 309:
            row['Options'] = "a) Current Account\nb) Savings Account\nc) Fixed Account\nd) Monthly Savings Account"
        elif row_id == 403:
            row['Options'] = "a) Cash Account\nb) Bank Account\nc) Interest Expense Account\nd) Interest Income Account"
        elif row_id == 408:
            row['Options'] = "a) Cash Account\nb) Accounts Receivable\nc) Bank Account\nd) Dividend Account"
        elif row_id in [490, 507]:
            row['Options'] = "a) Temporary Account\nb) Current Account\nc) Permanent Account\nd) Nominal Account"
            if row_id == 507: row['Options'] = row['Options'].replace('Temporary', 'Real').replace('Nominal', 'Temporary')
        elif row_id == 627:
            row['Options'] = "a) Final Account\nb) Trial Balance\nc) Double Entry\nd) Single Entry"
        
        # 3. Metadata Fixes
        old_level = row['Level']
        row['Level'] = fix_metadata(row['Level'], row_id)
        if row['Level'] != old_level:
            modified_years.append(f"Row {row_id}: {old_level} -> {row['Level']}")
            
        # 4. Stimulus Fixes
        if row_id == 536:
            row['Question'] = row['Question'].replace('(Ref #95) ', '')
            # The text is sufficient, no table needed
        
        # 5. HTML Sync
        row['HTML_Code'] = generate_html_table(row['Question'])
        
        rows.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

with open(r'c:\Users\BMTF\.antigravity\testpaper\metadata_fix_report.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(modified_years))

print(f"Repair complete. Total rows: {len(rows)}")
print(f"Metadata fixes: {len(modified_years)}")
print(f"Final file: {output_file}")
