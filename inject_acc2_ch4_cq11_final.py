import json

new_cq = {
    "id": 11,
    "stem": "<p>Alpha Company Ltd. was formed with an authorized capital of Tk. 25,00,000, divided into 2,50,000 shares of Tk. 10 each. The company purchased furniture in exchange for 50,000 shares. From the remaining shares, 1,00,000 shares were issued to the public. A total of 1,20,000 shares were applied for. 1,00,000 shares were allotted among the applicants. Refund warrants were issued for the excess applications. A commission of Tk. 1 per allotted share was paid to the underwriter.</p>",
    "meta": "Sylhet Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "How much more share capital can the company raise in future?",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Amount (Tk.)</th></tr><tr><td>Capital that can be raised in future</td><td>(2,50,000 - 50,000 - 1,00,000) &times; 10</td><td>10,00,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the light of the stimulus. (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Furniture Account<br>To Share Capital Account</td><td></td><td>5,00,000</td><td>5,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>12,00,000</td><td>12,00,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account</td><td></td><td>10,00,000</td><td>10,00,000</td></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>2,00,000</td><td>2,00,000</td></tr><tr><td></td><td>Underwriter's Commission Account<br>To Bank Account</td><td></td><td>1,00,000</td><td>1,00,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Furniture</td><td></td><td></td><td>5,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>9,00,000</td></tr><tr><td>Unadjusted Expenses: Underwriter's Commission</td><td></td><td></td><td>1,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>15,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>2,50,000 shares of Tk. 10 each</td><td></td><td></td><td>25,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>For furniture: 50,000 shares of Tk. 10 each</td><td></td><td>5,00,000</td><td></td></tr><tr><td>To the public: 1,00,000 shares of Tk. 10 each</td><td></td><td>10,00,000</td><td>15,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>15,00,000</td></tr></table>"
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
