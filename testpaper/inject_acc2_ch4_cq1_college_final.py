import json

new_cq = {
    "id": 1,
    "stem": "<p>A. B. S. Ltd. was registered with an authorized capital of Tk. 30,00,000, divided into 3,00,000 shares of Tk. 10 each. The company purchased a machinery from James Ltd. in exchange for 50,000 shares at par. Out of the remaining shares, the company issued a prospectus to sell 1,00,000 shares at a 10% discount. Applications for 80,000 shares were received from the public and all the applied shares were allotted duly.</p>",
    "meta": "Notre Dame College · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of discount per share and total amount of discount.",
            "answer": "<p>Discount per Share = Face value &times; Discount rate = 10 &times; 10% = Tk. 1</p><p>Total Discount = Allotted shares &times; Discount per share = 80,000 &times; 1 = Tk. 80,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Machinery Account<br>To Share Capital Account</td><td></td><td>5,00,000</td><td>5,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>7,20,000</td><td>7,20,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>7,20,000<br>80,000</td><td>8,00,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Fixed Assets: Machinery</td><td></td><td>5,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>7,20,000</td></tr><tr><td>Fictitious Assets: Share Discount</td><td></td><td>80,000</td></tr><tr><th>Total Assets</th><td></td><td>13,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>3,00,000 shares of Tk. 10 each</td><td></td><td>30,00,000</td></tr><tr><th>Issued Capital:</th><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td>10,00,000</td></tr><tr><th>Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>80,000 shares of Tk. 10 each</td><td>8,00,000</td><td></td></tr><tr><td>50,000 shares of Tk. 10 each (for machinery)</td><td>5,00,000</td><td>13,00,000</td></tr><tr><th>Total Liabilities</th><td></td><td>13,00,000</td></tr></table><p><i>(Note: Subscribed capital is greater than issued capital in the source solution due to inconsistency in the problem)</i></p>"
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
