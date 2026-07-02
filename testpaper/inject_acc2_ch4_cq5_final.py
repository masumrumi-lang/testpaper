import json

new_cq = {
    "id": 5,
    "stem": "<p>Fatema Company Ltd. was registered with a capital of Tk. 2,50,00,000, divided into 25,00,000 shares of Tk. 10 each. The company issued a prospectus to sell 50% of the shares at a premium of Tk. 2. A total of 14,0,000 shares were applied for. The issued shares were duly allotted and excess application money was refunded.</p>",
    "meta": "Jessore Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of share premium and refunded money.",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Amount (Tk.)</th></tr><tr><td>(i) Share Premium</td><td>Allotted Shares &times; Premium per share<br>(25,00,000 &times; 50%) &times; 2 = 12,50,000 &times; 2</td><td>25,00,000</td></tr><tr><td>(ii) Refunded Money</td><td>(Applied Shares - Allotted Shares) &times; 12<br>(14,00,000 - 12,50,000) &times; 12 = 1,50,000 &times; 12</td><td>18,00,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Prepare necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>1,68,00,000</td><td>1,68,00,000</td></tr></table><p><i>(Being application money received for 14,00,000 shares at Tk. 12 each including Tk. 2 premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>1,50,00,000</td><td>1,25,00,000<br>25,00,000</td></tr></table><p><i>(Being application money for 12,50,000 shares transferred to capital and premium accounts)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>18,00,000</td><td>18,00,000</td></tr></table><p><i>(Being excess application money refunded with premium)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>1,50,00,000</td></tr><tr><th>Total Assets</th><td></td><td>1,50,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>25,00,000 shares of Tk. 10 each</td><td></td><td>2,50,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>12,50,000 shares of Tk. 10 each</td><td></td><td>1,25,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td>25,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>1,50,00,000</td></tr></table>"
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
