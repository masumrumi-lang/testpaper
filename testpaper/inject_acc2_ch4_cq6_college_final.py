import json

new_cq = {
    "id": 6,
    "stem": "<p>Keya Company Limited was formed with an authorized capital of Tk. 10,00,000 divided into 12,500 shares of Tk. 80 each. The company purchased a machine worth Tk. 2,64,000 in exchange for 3,000 shares at a 10% premium. The board of directors issued 5,000 shares from the remaining shares at a 10% premium. Applications for 6,500 shares were received in total. The company allotted 5,000 shares duly to the applicants and excess application money was refunded. The company pays bank charges at Tk. 0.50 per share.</p>",
    "meta": "Adamjee Cantonment College, Dhaka · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine premium per share and total premium.",
            "answer": "<p>Premium per Share = Face value &times; Premium rate = 80 &times; 10% = Tk. 8</p><p>Total Premium = Total allotted shares &times; Premium per share = (3,000 + 5,000) &times; 8 = 8,000 &times; 8 = Tk. 64,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Machine Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>2,64,000</td><td>2,40,000<br>24,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>5,72,000</td><td>5,72,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account<br>To Bank Account</td><td></td><td>5,72,000</td><td>4,00,000<br>40,000<br>1,32,000</td></tr><tr><td></td><td>Bank Charge Account<br>To Bank Account</td><td></td><td>2,500</td><td>2,500</td></tr><tr><th>Total</th><td></td><td></td><td>14,10,500</td><td>14,10,500</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position assuming bank deposit is Tk. 4,37,500.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Machine</td><td></td><td></td><td>2,64,000</td></tr><tr><td>Current Assets: Bank Deposit (given)</td><td></td><td></td><td>4,37,500</td></tr><tr><td>Fictitious Assets: Bank Charge</td><td></td><td></td><td>2,500</td></tr><tr><th>Total Assets</th><td></td><td></td><td>7,04,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>12,500 shares of Tk. 80 each</td><td></td><td></td><td>10,00,000</td></tr><tr><th>Issued and Allotted Capital:</th><td></td><td></td><td></td></tr><tr><td>8,000 shares of Tk. 80 each</td><td></td><td></td><td>6,40,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>64,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>7,04,000</td></tr></table>"
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
