import json

new_cq = {
    "id": 9,
    "stem": "<p>The Trial Balance of Hridoy Ltd. as of 31st December 2023 was as follows:</p><table><tr><th>Account Name</th><th>Debit (Tk.)</th><th>Account Name</th><th>Credit (Tk.)</th></tr><tr><td>Bank Deposit</td><td>60,800</td><td>Share Capital (Tk. 100 each)</td><td>1,50,000</td></tr><tr><td>Accounts Receivable</td><td>44,500</td><td>Accounts Payable</td><td>12,000</td></tr><tr><td>Leasehold Property (10 years)</td><td>20,000</td><td>5% Loan (from 1.7.23)</td><td>50,000</td></tr><tr><td>Building</td><td>85,000</td><td>General Reserve</td><td>10,000</td></tr><tr><td>Machinery</td><td>60,000</td><td>Retained Earnings</td><td>10,800</td></tr><tr><td>Preliminary Expenses</td><td>2,600</td><td>Sales</td><td>1,25,000</td></tr><tr><td>Purchase</td><td>60,000</td><td>Share Transfer Fee</td><td>200</td></tr><tr><td>Wages & Salary</td><td>15,000</td><td></td><td></td></tr><tr><td>Rent</td><td>9,300</td><td></td><td></td></tr><tr><td>Opening Stock</td><td>17,000</td><td></td><td></td></tr><tr><td>Insurance Premium</td><td>7,800</td><td></td><td></td></tr><tr><td>Income Tax</td><td>6,000</td><td></td><td></td></tr><tr><td>Dividend Paid</td><td>10,000</td><td></td><td></td></tr><tr><th>Total</th><th>3,98,000</th><th>Total</th><th>3,98,000</th></tr></table><p><b>Adjustments:</b><br>(1) Cost price of closing stock is Tk. 40,000, market value is Tk. 32,000.<br>(2) Purchase of Tk. 5,000 not recorded in purchase book.<br>(3) Wages and Salary payable Tk. 1,500.<br>(4) 10% depreciation is to be charged on Building and Machinery.<br>(5) Tk. 5,000 is to be maintained as provision for Income Tax.<br>(6) Dividend is to be declared at Tk. 2 per share.</p>",
    "meta": "Ideal School and College, Motijheel · 2024",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "What will be the Cost of Goods Sold?",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Opening Stock</td><td></td><td>17,000</td></tr><tr><td>Purchase</td><td>60,000</td><td></td></tr><tr><td>(+) Unrecorded Purchase</td><td>5,000</td><td>65,000</td></tr><tr><td>Wages and Salary</td><td>15,000</td><td></td></tr><tr><td>(+) Payable</td><td>1,500</td><td>16,500</td></tr><tr><td></td><td></td><td>98,500</td></tr><tr><td>(-) Closing Stock</td><td></td><td>(32,000)</td></tr><tr><th>Cost of Goods Sold</th><td></td><td>66,500</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Prepare Retained Earnings Statement assuming Net Profit after tax is Tk. 22,850.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Opening Retained Earnings</td><td></td><td>10,800</td></tr><tr><td>(+) Net Profit</td><td></td><td>22,850</td></tr><tr><td></td><td></td><td>33,650</td></tr><tr><td>(-) Income Tax Paid</td><td></td><td>(6,000)</td></tr><tr><td>(-) Dividend Paid</td><td></td><td>(10,000)</td></tr><tr><td>(-) Proposed Dividend</td><td></td><td>(3,000)</td></tr><tr><th>Closing Balance</th><td></td><td>14,650</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Leasehold Property</td><td>20,000</td><td></td></tr><tr><td>(-) Written off</td><td>(2,000)</td><td>18,000</td></tr><tr><td>Building</td><td>85,000</td><td></td></tr><tr><td>(-) Depreciation</td><td>(8,500)</td><td>80,500</td></tr><tr><td>Machinery</td><td>60,000</td><td></td></tr><tr><td>(-) Depreciation</td><td>(6,000)</td><td>54,000</td></tr><tr><td></td><td></td><td>1,12,500</td></tr><tr><th>Current Assets:</th><td></td><td></td></tr><tr><td>Bank Deposit</td><td></td><td>60,800</td></tr><tr><td>Accounts Receivable</td><td></td><td>44,500</td></tr><tr><td>Closing Stock</td><td></td><td>32,000</td></tr><tr><td></td><td></td><td>1,37,300</td></tr><tr><th>Fictitious Assets:</th><td></td><td></td></tr><tr><td>Preliminary Expenses</td><td></td><td>2,600</td></tr><tr><th>Total Assets</th><td></td><td>2,52,400</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Share Capital:</th><td></td><td></td></tr><tr><td>Authorized, Issued, Subscribed and Paid-up Capital</td><td></td><td>1,50,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td></tr><tr><td>General Reserve</td><td>10,000</td><td></td></tr><tr><td>Provision for Tax</td><td>5,000</td><td></td></tr><tr><td>Retained Earnings</td><td>14,650</td><td>29,650</td></tr><tr><th>Long Term Loan:</th><td></td><td></td></tr><tr><td>5% Loan</td><td></td><td>50,000</td></tr><tr><th>Current Liabilities:</th><td></td><td></td></tr><tr><td>Accounts Payable</td><td>12,000</td><td></td></tr><tr><td>(+) Unrecorded Purchase</td><td>5,000</td><td>19,000</td></tr><tr><td>Loan Interest</td><td>1,250</td><td></td></tr><tr><td>Payable Wages</td><td>1,500</td><td></td></tr><tr><td>Proposed Dividend</td><td>3,000</td><td>22,750</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>2,52,400</td></tr></table><p><i>(Note: The solution in part (c) contains several mathematical errors in the source image, such as Building net value shown as 80,500 instead of 76,500, and the sum of Fixed Assets shown as 1,12,500 instead of 1,52,500. The table has been reproduced as shown in the source to match the final total.)</i></p>"
        }
    ]
}

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '"chapterName": "Chapter 4: Capital of Joint Stock Companies",'
idx = content.find(target)

if idx == -1:
    print("Error: Target not found")
else:
    cq_idx = content.find('"fullCQData": [', idx)
    if cq_idx == -1:
        print("Error: fullCQData not found")
    else:
        close_idx = content.find('\n            ]', cq_idx)
        if close_idx == -1:
            print("Error: Closing bracket not found")
        else:
            json_str = json.dumps(new_cq, indent=4, ensure_ascii=False)
            lines = json_str.split('\n')
            indented_lines = ['                    ' + line for line in lines]
            formatted_json = '\n'.join(indented_lines)
            
            new_val = ',\n' + formatted_json
            
            new_content = content[:close_idx] + new_val + content[close_idx:]
            
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Success")
