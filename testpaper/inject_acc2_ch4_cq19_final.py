import json

new_cq = {
    "id": 19,
    "stem": "<p>Padma Company Ltd. was registered with an authorized capital of Tk. 60,00,000, divided into 60,000 shares of Tk. 100 each. The company issued 10,000 shares at a 10% premium. Applications for a total of 11,000 shares were received. The company allotted 10,000 shares among the applicants. The excess application money was refunded to the respective applicants.</p>",
    "meta": "Dhaka Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the premium per share and total premium.",
            "answer": "<p>Premium per Share = 100 &times; 10% = Tk. 10</p><p>Total Premium = 10,000 &times; 10 = Tk. 1,00,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>12,10,000</td><td>12,10,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Premium Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>12,10,000</td><td>1,00,000<br>10,00,000<br>1,10,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>11,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>11,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>60,000 shares of Tk. 100 each</td><td></td><td></td><td>60,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>10,000 shares of Tk. 100 each</td><td></td><td></td><td>10,00,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>10,000 shares of Tk. 100 each</td><td></td><td></td><td>10,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>1,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>11,00,000</td></tr></table>"
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
