import csv
import re
import html
import os

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_COMPLETE_FINAL.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\acc1_mcq_IMPORT_READY.csv'

# Chapter mapping based on website naming convention
chapter_names = {
    "1": "Chapter 1 : Introduction to Accounting",
    "2": "Chapter 2 : Books of Accounts",
    "3": "Chapter 3 : Bank Reconciliation Statement",
    "4": "Chapter 4 : Trial Balance",
    "5": "Chapter 5 : Accounting Principles (Out of Short Syllabus)",
    "6": "Chapter 6 : Accounting for Receivables (Out of Short Syllabus)",
    "7": "Chapter 7 : Work Sheet",
    "8": "Chapter 8 : Accounting for Tangible and Intangible Assets",
    "9": "Chapter 9 : Financial Statements",
    "10": "Chapter 10 : Single Entry System (Out of Short Syllabus)"
}

def get_chapter_num(chapter_str):
    if not chapter_str: return None
    match = re.search(r'Chapter\s*(\d+)', str(chapter_str), re.IGNORECASE)
    if match:
        # Convert to int then string to strip leading zeros (e.g., "03" -> "3")
        return str(int(match.group(1)))
    return None

def standardize_chapter(chapter_val):
    num = get_chapter_num(chapter_val)
    if num in chapter_names:
        return chapter_names[num]
    return chapter_val

def standardize_type(level, category):
    # Format: "Source - Year" e.g., "Dhaka Board - 2024"
    # Find year
    year_match = re.search(r'(\d{4})', str(level))
    year = year_match.group(1) if year_match else ""
    
    # Clean source
    source = str(level).replace(year, "").replace("-", "").strip()
    if not source or source == "":
        source = category
    
    if year:
        return f"{source} - {year}"
    return source

def split_options(options_str):
    if not options_str: return ["", "", "", ""]
    # Pattern to match a), b), c), d) or (a), (b), (c), (d)
    parts = re.split(r'\s*[a-d][\)\.]\s*', str(options_str))
    # Filter out empty strings and strip
    opts = [p.strip() for p in parts if p.strip()]
    
    # If we don't have 4 options, try a more aggressive split
    if len(opts) != 4:
        # Fallback: look for a) b) c) d) specifically
        opts = []
        for label in ['a', 'b', 'c', 'd']:
            start_pattern = rf'{label}[\)\.]'
            # Find start
            start_match = re.search(start_pattern, options_str, re.IGNORECASE)
            if start_match:
                start_idx = start_match.end()
                # Find next label or end of string
                next_labels = [l for l in ['a', 'b', 'c', 'd'] if l > label]
                end_idx = len(options_str)
                for nl in next_labels:
                    nl_match = re.search(rf'{nl}[\)\.]', options_str[start_idx:], re.IGNORECASE)
                    if nl_match:
                        end_idx = start_idx + nl_match.start()
                        break
                opts.append(options_str[start_idx:end_idx].strip())
    
    # Fill with empty strings if still not 4
    while len(opts) < 4:
        opts.append("")
    return opts[:4]

def ensure_tk(text):
    if not isinstance(text, str): return text
    
    # 1. Fix existing variations: Taka, taka, Tk, tk. -> TK
    text = re.sub(r'\b(Taka|taka|Tk|tk)\b\.?', 'TK', text)
    
    # 2. Add TK to numbers followed by nothing or non-TK words
    # Pattern: Digit(s) followed by comma/dot, but NOT followed by TK
    text = re.sub(r'(\d{1,3}(?:,\d{3})+(?:\.\d+)?)(?!\s*TK)', r'\1 TK', text)
    
    # 3. Clean up double TK
    text = text.replace('TK TK', 'TK').replace('TKTK', 'TK')
    return text

def generate_web_table(text):
    if '|' not in text:
        return ""
    
    lines = [l.strip() for l in text.split('\n') if '|' in l]
    if not lines:
        return ""
    
    # Use Tailwind-compatible classes if possible, or clean inline styles
    html_output = '<div class="overflow-x-auto my-4"><table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700 border border-gray-200 dark:border-gray-700">'
    
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.split('|')]
        bg_class = 'class="bg-gray-50 dark:bg-gray-800"' if i == 0 else 'class="bg-white dark:bg-gray-900"'
        html_output += f'<tr {bg_class}>'
        
        for cell in cells:
            is_numeric = re.search(r'\d', cell) and not re.search(r'[a-zA-Z]{3,}', cell.replace('TK', ''))
            align = 'text-right' if is_numeric else 'text-left'
            padding = 'px-4 py-2'
            tag = 'th' if i == 0 else 'td'
            text_class = 'text-xs font-semibold uppercase tracking-wider text-gray-500 dark:text-gray-400' if i == 0 else 'text-sm text-gray-700 dark:text-gray-300'
            
            html_output += f'<{tag} class="{padding} {align} {text_class} border-r border-gray-200 dark:border-gray-700 last:border-r-0">{html.escape(cell)}</{tag}>'
        
        html_output += '</tr>'
    
    html_output += '</table></div>'
    return html_output

# Process Data
rows = []
chapter_counts = {}

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit(1)

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 1. Filter Rule: Remove Chapter 1 and 8
        ch_num = get_chapter_num(row['Chapter'])
        if ch_num in ['1', '8']:
            continue
            
        # 2. Split Options
        opt_a, opt_b, opt_c, opt_d = split_options(row['Options'])
        
        # 3. Currency Consistency
        row['Question'] = ensure_tk(row['Question'])
        row['Explanation'] = ensure_tk(row['Explanation'])
        opt_a = ensure_tk(opt_a)
        opt_b = ensure_tk(opt_b)
        opt_c = ensure_tk(opt_c)
        opt_d = ensure_tk(opt_d)
        
        # 4. Standardize Naming
        new_row = {
            'Subject': row['Subject'],
            'Chapter': standardize_chapter(row['Chapter']),
            'Type': standardize_type(row['Level'], row['Category']),
            'Category': row['Category'].lower(),
            'q_text': row['Question'],
            'opt_a': opt_a,
            'opt_b': opt_b,
            'opt_c': opt_c,
            'opt_d': opt_d,
            'Answer': row['Answer'].lower().strip(),
            'Explanation': row['Explanation'],
            'HTML_Code': generate_web_table(row['Question'])
        }
        
        # 5. Tracking for Summary
        ch_display = new_row['Chapter']
        chapter_counts[ch_display] = chapter_counts.get(ch_display, 0) + 1
        
        rows.append(new_row)

# 6. Organizing & Sorting
# Sort by Chapter Number (extracted) and then Year (extracted from Type)
def sort_key(r):
    ch_match = re.search(r'Chapter\s*(\d+)', r['Chapter'])
    ch_n = int(ch_match.group(1)) if ch_match else 999
    
    yr_match = re.search(r'(\d{4})', r['Type'])
    yr = int(yr_match.group(1)) if yr_match else 0
    
    return (ch_n, -yr) # Negative year for newest first

rows.sort(key=sort_key)

# 7. Export
fieldnames = ['Subject', 'Chapter', 'Type', 'Category', 'q_text', 'opt_a', 'opt_b', 'opt_c', 'opt_d', 'Answer', 'Explanation', 'HTML_Code']
with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Successfully processed {len(rows)} questions.")
print(f"Output saved to: {output_file}")
print("\nChapter Summary:")
for ch, count in sorted(chapter_counts.items(), key=lambda x: int(re.search(r'Chapter\s*(\d+)', x[0]).group(1))):
    print(f"{ch}: {count} questions")
