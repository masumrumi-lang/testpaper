import json

new_cq = {
    "id": 21,
    "stem": "<p>Mahadi Company Ltd. was registered with an authorized capital of Tk. 40,00,000, divided into 4,00,000 shares of Tk. 10 each. The company invited applications for 80% of the authorized shares at a 10% premium. Applications for 3,50,000 shares were received from the public. The company allotted all the issued shares duly. The excess application money was refunded to the respective applicants. The company paid a bank charge of Tk. 0.25 per share.</p>",
    "meta": "Rajshahi Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the number of issued shares and the amount of bank charge.",
            "answer": "<p>Issued Shares = Authorized shares &times; 80% = 4,00,000 &times; 80% = 3,20,000 shares</p><p>Bank Charge = Allotted shares &times; Bank charge per share = 3,20,000 &times; 0.25 = Tk. 80,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>38,50,000</td><td>38,50,000</td></tr></table><p><i>(Being application money received for 3,50,000 shares at Tk. 11 each including Tk. 1 premium per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Premium Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>38,50,000</td><td>3,20,000<br>32,00,000<br>3,30,000</td></tr></table><p><i>(Being application money for 3,20,000 shares transferred to capital account at Tk. 11 each including Tk. 1 premium and excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Charge Account<br>To Bank Account</td><td></td><td>80,000</td><td>80,000</td></tr></table><p><i>(Being bank charge paid)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>34,40,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Bank Charge</td><td></td><td></td><td>80,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>35,20,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>4,00,000 shares of Tk. 10 each</td><td></td><td></td><td>40,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>3,20,000 shares of Tk. 10 each</td><td></td><td></td><td>32,00,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>3,20,000 shares of Tk. 10 each</td><td></td><td></td><td>32,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>3,20,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>35,20,000</td></tr></table>"
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
