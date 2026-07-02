import json

new_cq = {
    "id": 23,
    "stem": "<p>Nadi Limited was registered with an authorized capital of Tk. 12,00,000, divided into 1,20,000 shares of Tk. 10 each. The company issued 1,00,000 shares at a premium of Tk. 2. Applications for 1,20,000 shares were received. The issued shares were allotted in due time and the excess application money was refunded.</p>",
    "meta": "Jessore Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total amount of share premium.",
            "answer": "<p>Total Share Premium = Allotted shares &times; Premium per share = 1,00,000 &times; 2 = Tk. 2,00,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>14,40,000</td><td>14,40,000</td></tr></table><p><i>(Being application money received for 1,20,000 shares at Tk. 12 each including Tk. 2 premium per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Premium Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>14,40,000</td><td>2,00,000<br>10,00,000<br>2,40,000</td></tr></table><p><i>(Being application money for 1,00,000 shares transferred to capital account at Tk. 12 each including Tk. 2 premium and excess application money refunded)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>12,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>12,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>1,20,000 shares of Tk. 10 each</td><td></td><td></td><td>12,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td></td><td>10,00,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td></td><td>10,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>2,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>12,00,000</td></tr></table>"
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
