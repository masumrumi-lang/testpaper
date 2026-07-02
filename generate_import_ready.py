import csv
import json
import re
import os

def format_content(text):
    if not text: return ""
    formulas = ['PV', 'FV', 'WACC', 'NPV', 'IRR', 'EPS', 'EAT', 'EBT', 'ROI', 'ROE']
    for f in formulas:
        text = re.sub(rf'\$?{f}\$?', f'<code>{f}</code>', text)
    text = re.sub(r'(\d+(?:,\d+)*(?:\.\d+)?)\s*TK', r'TK \1', text, flags=re.IGNORECASE)
    text = re.sub(r'TK\s*(\d+(?:,\d+)*(?:\.\d+)?)', r'TK \1', text, flags=re.IGNORECASE)
    text = re.sub(r'(\d+(?:\.\d+)?)\s*%', r'\1%', text)
    if '|' in text or '\t' in text:
        lines = text.split('\n')
        table_html = '<div class="table-responsive my-3"><table class="w-full text-sm border-collapse border border-gray-200 dark:border-gray-700">'
        for line in lines:
            if not line.strip(): continue
            cells = [c.strip() for c in re.split(r'[|\t]', line) if c.strip()]
            if not cells: continue
            table_html += '<tr>'
            for cell in cells:
                table_html += f'<td class="border border-gray-200 dark:border-gray-700 p-2">{cell}</td>'
            table_html += '</tr>'
        table_html += '</table></div>'
        return table_html
    return text

def generate_import_ready_csv():
    source_csv = 'Finance1 MCQ Database.csv'
    target_csv = 'finance1_mcq_IMPORT_READY.csv'
    
    processed_rows = []
    
    with open(source_csv, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        processed_rows.append(header)
        
        for row in reader:
            if not row: continue
            new_row = list(row)
            # Apply formatting to Question and Explanation
            if len(new_row) > 5:
                new_row[5] = format_content(new_row[5])
            if len(new_row) > 11:
                new_row[11] = format_content(new_row[11])
            processed_rows.append(new_row)
            
    with open(target_csv, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(processed_rows)
    
    print(f"Generated {target_csv}")

if __name__ == "__main__":
    generate_import_ready_csv()
