import json

new_cq = {
    "id": 2,
    "stem": "<p>Sabina PLC was registered with an authorized capital of Tk. 10,00,000, divided into 1,00,000 shares of Tk. 10 each. The company issued 50,000 shares for sale to the public at a 10% premium. Applications for 60,000 shares were received. The excess application money was refunded. Besides, the company issued 20,000 shares at par to purchase a machine. Underwriter's commission was charged at Tk. 1.00 per share and bank charge at Tk. 0.50 per share (on shares allotted to the public).</p>",
    "meta": "Dhaka College · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of underwriter's commission and bank charge.",
            "answer": "<p>Underwriter's Commission = Shares allotted to public &times; Commission per share = 50,000 &times; 1.00 = Tk. 50,000</p><p>Bank Charge = Shares allotted to public &times; Bank charge per share = 50,000 &times; 0.50 = Tk. 25,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>6,60,000</td><td>6,60,000</td></tr></table><p><i>(Being application money received for 60,000 shares at Tk. 11 each including Tk. 1 premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account<br>To Bank Account</td><td></td><td>6,60,000</td><td>5,00,000<br>50,000<br>1,10,000</td></tr></table><p><i>(Being application money for 50,000 shares transferred to capital and premium accounts, and excess money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Machine Account<br>To Share Capital Account</td><td></td><td>2,00,000</td><td>2,00,000</td></tr></table><p><i>(Being machine purchased in exchange for 20,000 shares of Tk. 10 each at par)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Underwriter's Commission Account<br>Bank Charge Account<br>To Bank Account</td><td></td><td>50,000<br>25,000</td><td>75,000</td></tr></table><p><i>(Being underwriter's commission and bank charge recorded)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Fixed Assets: Machine</td><td></td><td>2,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>4,75,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td></tr><tr><td>Underwriter's Commission</td><td>50,000</td><td></td></tr><tr><td>Bank Charge</td><td>25,000</td><td>75,000</td></tr><tr><th>Total Assets</th><td></td><td>7,50,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td>10,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>70,000 shares of Tk. 10 each</td><td></td><td>7,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td>50,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>7,50,000</td></tr></table>"
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
