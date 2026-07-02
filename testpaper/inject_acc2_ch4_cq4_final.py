import json

new_cq = {
    "id": 4,
    "stem": "<p>Rupali Limited was registered with an authorized capital of Tk. 50,00,000 divided into 5,00,000 shares of Tk. 10 each. The company issued a prospectus to sell 3,00,000 shares to the public at a 10% discount for raising capital. A total of 3,20,000 shares were applied for. The issued shares were duly allotted and excess application money was refunded to the respective applicants. Rupali Limited allotted 1,00,000 shares to Fahim Motors for purchasing a machine worth Tk. 9,00,000.</p>",
    "meta": "Rajshahi Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Prepare the Bank Account of Rupali Limited.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Application Account</td><td></td><td>28,80,000</td><td></td><td>28,80,000</td></tr><tr><td></td><td>Share Application Account</td><td></td><td></td><td>1,80,000</td><td>27,00,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of Rupali Limited.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>28,80,000</td><td>28,80,000</td></tr></table><p><i>(Being application money received for 3,20,000 shares at Tk. 9 each after discount)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>27,00,000<br>3,00,000</td><td>30,00,000</td></tr></table><p><i>(Being application money for 3,00,000 shares at Tk. 10 each with Tk. 1 discount transferred to capital account)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>1,80,000</td><td>1,80,000</td></tr></table><p><i>(Being excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Machine Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>9,00,000<br>1,00,000</td><td>10,00,000</td></tr></table><p><i>(Being machine purchased by issuing 1,00,000 shares)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Machine</td><td></td><td></td><td>9,00,000</td></tr><tr><td>Current Assets: Bank Deposit (from a)</td><td></td><td></td><td>27,00,000</td></tr><tr><td>Unadjusted Expenses: Share Discount</td><td></td><td></td><td>4,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>40,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>5,00,000 shares of Tk. 10 each</td><td></td><td></td><td>50,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each for machine</td><td></td><td>10,00,000</td><td></td></tr><tr><td>3,00,000 shares of Tk. 10 each to the public</td><td></td><td>30,00,000</td><td>40,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>40,00,000</td></tr></table>"
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
