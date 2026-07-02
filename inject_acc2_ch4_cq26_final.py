import json

new_cq = {
    "id": 26,
    "stem": "<p>Suman Limited was registered with an authorized capital of Tk. 15,00,000, divided into 1,50,000 shares of Tk. 10 each. The company issued 80,000 shares for sale. Applications for 75,000 shares were received. The excess application money was refunded. [Note: Solution shows underwriter took remaining shares]. Besides, the company purchased a machine by issuing 25,000 shares at par. Underwriter's commission was charged at Tk. 0.75 per share and bank charge at Tk. 0.45 per share.</p>",
    "meta": "Comilla Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of underwriter's commission and bank charge.",
            "answer": "<p>Underwriter's Commission = 80,000 &times; 0.75 = Tk. 60,000</p><p>Bank Charge = 80,000 &times; 0.45 = Tk. 36,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>7,50,000</td><td>7,50,000</td></tr></table><p><i>(Being application money received for 75,000 shares at Tk. 10 each)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account</td><td></td><td>7,50,000</td><td>7,50,000</td></tr></table><p><i>(Being application money for 75,000 shares transferred to capital account)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Machine Account<br>To Share Capital Account</td><td></td><td>2,50,000</td><td>2,50,000</td></tr></table><p><i>(Being machine purchased in exchange for 25,000 shares at Tk. 10 each)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Capital Account</td><td></td><td>50,000</td><td>50,000</td></tr></table><p><i>(Being underwriter purchased remaining 5,000 shares at Tk. 10 each)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Underwriter's Commission Account<br>Bank Charge Account<br>To Bank Account</td><td></td><td>60,000<br>36,000</td><td>96,000</td></tr></table><p><i>(Being underwriter's commission and bank charge paid)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Machine</td><td></td><td></td><td>2,50,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>7,04,000</td></tr><tr><th>Fictitious Assets:</th><td></td><td></td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td>60,000</td><td></td></tr><tr><td>Bank Charge</td><td></td><td>36,000</td><td>96,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>10,50,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>1,50,000 shares of Tk. 10 each</td><td></td><td></td><td>15,00,000</td></tr><tr><th>Issued Capital:</th><td></td><td></td><td></td></tr><tr><td>80,000 shares of Tk. 10 each</td><td></td><td></td><td>8,00,000</td></tr><tr><th>Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>To the public: 80,000 shares of Tk. 10 each</td><td></td><td></td><td>8,00,000</td></tr><tr><td>For machine: 25,000 shares of Tk. 10 each</td><td></td><td></td><td>2,50,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>10,50,000</td></tr></table>"
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
