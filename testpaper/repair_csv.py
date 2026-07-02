import csv
import re
import html

input_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'
output_file = r'c:\Users\BMTF\.antigravity\testpaper\hsc_mcq_bank_WEB_READY.csv'

# Repairs mapping
repairs = {
    4: {
        'Options': "a) General Reserve\nb) Allowance for Debtors\nc) Provision for Discount on Creditors\nd) Provision for Discount on Debtors",
        'Answer': 'c'
    },
    8: {
        'Options': "a) Asset increase and Liability increase\nb) Asset decrease and Liability increase\nc) Asset decrease and Liability decrease\nd) Asset increase and Liability decrease",
        'Answer': 'b'
    },
    16: {
        'Options': "a) Cash Debit, Debenture Credit\nb) Jahir Debit, Loan Credit\nc) Cash Debit, Jahir Credit\nd) Debenture Debit, Cash Credit",
        'Answer': 'a'
    },
    21: {
        'Options': "a) Credit side Bank column\nb) Debit side Bank column\nc) Credit side Cash column\nd) Debit side Cash column",
        'Answer': 'a'
    },
    25: {
        'Options': "a) Income and Liability\nb) Asset and Expense\nc) Income and Expense\nd) Asset and Liability",
        'Answer': 'a'
    },
    27: {
        'Options': "a) Cash Discount\nb) Trade Discount\nc) Quantity Discount\nd) Purchase Discount",
        'Answer': 'a'
    },
    30: {
        'Options': "a) Drawings Debit, Purchase Credit\nb) Drawings Debit, Sales Credit\nc) Sales Debit, Drawings Credit\nd) Purchase Debit, Drawings Credit",
        'Answer': 'b'
    },
    32: {
        'Options': "a) Personal bank withdrawal\nb) Business bank withdrawal\nc) Check received from customer\nd) Payment by check",
        'Answer': 'b'
    },
    38: {
        'Options': "a) Determining Profit/Loss\nb) Checking arithmetical accuracy\nc) Preparing Balance Sheet\nd) Identifying transactions",
        'Answer': 'b'
    },
    42: {
        'Options': "a) 4,000 TK\nb) 5,000 TK\nc) 6,000 TK\nd) 1,000 TK",
        'Answer': 'c'
    },
    43: {
        'Options': "a) Expense\nb) Liability\nc) Asset\nd) Income",
        'Answer': 'c'
    },
    50: {
        'Options': "a) Asset increase, Equity increase\nb) Asset increase, Liability increase\nc) Asset decrease, Equity increase\nd) Asset decrease, Liability decrease",
        'Answer': 'a'
    },
    51: {
        'Options': "a) Debit Voucher\nb) Credit Voucher\nc) Journal Voucher\nd) Transfer Voucher",
        'Answer': 'b'
    },
    54: {
        'Options': "a) Capital Loss\nb) Revenue Loss\nc) Personal Loss\nd) Unusual Loss",
        'Answer': 'b'
    },
    56: {
        'Options': "a) Luca Pacioli\nb) Adam Smith\nc) Newton\nd) Aristotle",
        'Answer': 'a'
    },
    70: {
        'Options': "a) Single Column\nb) Double Column\nc) Triple Column\nd) Multi Column",
        'Answer': 'a'
    },
    84: {
        'Options': "a) Salary Debit, Cash Credit\nb) Salary Debit, Capital Credit\nc) Salary Debit, Drawings Credit\nd) Cash Debit, Salary Credit",
        'Answer': 'b'
    },
    93: {
        'Options': "a) Cash Debit, Commission Credit\nb) Accrued Commission Debit, Commission Income Credit\nc) Commission Income Debit, Accrued Commission Credit\nd) Cash Debit, Accrued Commission Credit",
        'Answer': 'b'
    },
    102: {
        'Options': "a) Drawings Debit, Cash Credit\nb) Income Tax Debit, Capital Credit\nc) Cash Debit, Income Tax Credit\nd) Income Tax Debit, Cash Credit",
        'Answer': 'a'
    },
    106: {
        'Options': "a) Sales Return Debit, Cash Credit\nb) Sales Return Debit, Receivable Credit\nc) Purchase Return Debit, Cash Credit\nd) Purchase Return Debit, Payable Credit",
        'Answer': 'b'
    },
    125: {
        'Options': "a) Discount Expense Debit, Receivable Credit\nb) Discount Expense Debit, Cash Credit\nc) Receivable Debit, Discount Expense Credit\nd) Cash Debit, Discount Expense Credit",
        'Answer': 'a'
    },
    143: {
        'Options': "a) Giver-Taker\nb) Self-sufficiency\nc) Dual Entity\nd) Dual Aspect",
        'Answer': 'd'
    },
    147: {
        'Options': "a) Purchase discount and Payable\nb) Purchase discount and Receivable\nc) Sales discount and Payable\nd) None of the above",
        'Answer': 'a'
    },
    159: {
        'Options': "a) carried down\nb) Credit discount\nc) Carried discount\nd) Cash discount",
        'Answer': 'a'
    },
    163: {
        'Options': "a) Reversing entry\nb) Adjusted trial balance\nc) Special journal\nd) Final accounts",
        'Answer': 'a'
    },
    168: {
        'Options': "a) Salary Debit, Cash Credit\nb) Salary Debit, Capital Credit\nc) Salary Debit, Drawings Credit\nd) Cash Debit, Salary Credit",
        'Answer': 'b'
    },
    173: {
        'Options': "a) Discount Allowed\nb) Discount Received\nc) Trade Discount\nd) Quantity Discount",
        'Answer': 'a'
    },
    174: {
        'Options': "a) July 1, 1991\nb) July 1, 1992\nc) July 1, 1990\nd) July 1, 1993",
        'Answer': 'a'
    },
    185: {
        'Options': "a) Purchase Debit, Payable Credit\nb) Machinery Debit, Cash Credit\nc) Purchase Debit, Cash Credit\nd) Machinery Debit, Payable Credit",
        'Answer': 'c'
    },
    187: {
        'Options': "a) Trade Discount\nb) Cash Discount\nc) Allowed Discount\nd) Received Discount",
        'Answer': 'a'
    },
    189: {
        'Options': "a) Discount Debit, Cash Credit\nb) Payable Debit, Discount Credit\nc) Cash Debit, Discount Credit\nd) Discount Debit, Payable Credit",
        'Answer': 'b'
    },
    190: {
        'Options': "a) Debit side (Cash)\nb) Credit side (Cash)\nc) Credit side (Bank)\nd) Debit side (Bank)",
        'Answer': 'c'
    },
    192: {
        'Options': "a) Cash\nb) Bank Balance\nc) Receivable (Debtor)\nd) Liability",
        'Answer': 'c'
    },
    201: {
        'Options': "a) Expense increases, Assets decrease\nb) Income increases, Assets decrease\nc) Expense decreases, Assets increase\nd) Income decreases, Assets increase",
        'Answer': 'a'
    },
    202: {
        'Options': "a) Asset and Liability increase\nb) Asset and Liability decrease\nc) Asset increase and Liability decrease\nd) Asset decrease and Liability increase",
        'Answer': 'c'
    },
    213: {
        'Options': "a) Drawings Debit, Purchase Credit\nb) Drawings Debit, Inventory Credit\nc) Sales Debit, Drawings Credit\nd) Drawings Debit, Sales Credit",
        'Answer': 'd'
    },
    219: {
        'Options': "a) Expense decrease, Asset increase\nb) Expense increase, Asset decrease\nc) Expense increase, Asset increase\nd) Expense decrease, Asset decrease",
        'Answer': 'b'
    },
    223: {
        'Options': "a) Salary Debit, Cash Credit\nb) Salary Debit, Capital Credit\nc) Salary Debit, Drawings Credit\nd) Cash Debit, Salary Credit",
        'Answer': 'b'
    },
    233: {
        'Options': "a) Personal withdrawal\nb) Cash deposit to bank\nc) Debtor bank deposit\nd) Cash purchase",
        'Answer': 'b'
    },
    236: {
        'Options': "a) Total Assets = Total Liabilities + Equity\nb) Total Assets = Profit\nc) Total Liabilities = Total Assets\nd) Total Equity = Total Assets",
        'Answer': 'a'
    },
    245: {
        'Options': "a) Conditional purchase\nb) Credit purchase\nc) Conditional sale\nd) Credit sale",
        'Answer': 'b'
    },
    281: {
        'Options': "a) Cash Debit, Hasan's Loan Credit\nb) Hasan's Loan Debit, Cash Credit\nc) Hasan Debit, Cash Credit\nd) Cash Debit, Hasan Credit",
        'Answer': 'b'
    },
    303: {
        'Options': "a) Not Satisfying Fund\nb) National Fund\nc) Not Sufficient Funds\nd) New Saving Fund",
        'Answer': 'c'
    },
    304: {
        'Options': "a) Person depositing money\nb) Person opening and operating an account\nc) Person borrowing money\nd) Bank manager",
        'Answer': 'b'
    },
    306: {
        'Options': "a) 8,000 TK (Overdraft)\nb) 12,000 TK (Overdraft)\nc) 12,000 TK (Deposit)\nd) 15,000 TK (Overdraft)",
        'Answer': 'b'
    }
}

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

rows = []
with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row_id, row in enumerate(reader, start=1):
        # Preservation Rule: Do NOT touch any rows belonging to Chapter 1 or Chapter 8.
        if 'Chapter 1' in row['Chapter'] or 'Chapter 8' in row['Chapter']:
            rows.append(row)
            continue
            
        if row_id in repairs:
            # Apply repair
            repair = repairs[row_id]
            row['Options'] = repair['Options']
            row['Answer'] = repair['Answer']
            
            # HTML Update
            row['HTML_Code'] = generate_html_table(row['Question'])
            
            print(f"Repaired Row {row_id}")
            
        rows.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Total rows updated: {len(repairs)}")
