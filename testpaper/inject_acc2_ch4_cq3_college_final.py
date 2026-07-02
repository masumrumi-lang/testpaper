import json

new_cq = {
    "id": 3,
    "stem": "<p>Mousumi Co. Limited was registered with a total capital of Tk. 50,00,000 divided into 5,00,000 shares of Tk. 10 each. The company issued 3,00,000 shares at a 20% premium for sale in the following manner:</p><p>I. The company purchased a machine in exchange for 20,000 shares.<br>II. The company received applications for 3,50,000 shares against the remaining issued shares.<br>III. Excess application money was refunded to the applicants and the remaining shares were allotted duly.<br>IV. Underwriter's commission was paid at Tk. 0.50 per share.</p>",
    "meta": "Rajuk Uttara Model College, Dhaka · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the value of the purchased machine.",
            "answer": "<p>Value of Purchased Machine = Issued shares &times; Issue price per share = 20,000 &times; 12 = Tk. 2,40,000</p><p><i>Calculation:</i><br>Issue price = Face value + Premium = 10 + (10 &times; 20%) = Tk. 12</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries for the above transactions.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>(i)</td><td>Machine Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>2,40,000</td><td>2,00,000<br>40,000</td></tr></table><p><i>(Being machine purchased in exchange for 20,000 shares at 20% premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>(ii)</td><td>Bank Account<br>To Share Application Account</td><td></td><td>42,00,000</td><td>42,00,000</td></tr></table><p><i>(Being application money received for 3,50,000 shares at Tk. 12 each including Tk. 2 premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>(iii)</td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account<br>To Bank Account</td><td></td><td>42,00,000</td><td>28,00,000<br>5,60,000<br>8,40,000</td></tr></table><p><i>(Being application money for 2,80,000 shares transferred to capital and premium, and excess application money for 70,000 shares refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>(iv)</td><td>Share Underwriter's Commission Account<br>To Bank Account</td><td></td><td>1,40,000</td><td>1,40,000</td></tr></table><p><i>(Being underwriter's commission paid at Tk. 0.50 per share on 2,80,000 shares)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Bank Account and Statement of Financial Position.",
            "answer": "<p><b>Bank Account:</b></p><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Application Account</td><td></td><td>42,00,000</td><td></td><td>42,00,000 (Dr)</td></tr><tr><td></td><td>Share Application Account (Refund)</td><td></td><td></td><td>8,40,000</td><td>33,60,000 (Dr)</td></tr><tr><td></td><td>Share Underwriter's Commission Account</td><td></td><td></td><td>1,40,000</td><td>32,20,000 (Dr)</td></tr></table><p><b>Statement of Financial Position:</b></p><table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Machine</td><td></td><td></td><td>2,40,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>32,20,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Share Underwriter's Commission</td><td></td><td></td><td>1,40,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>36,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>5,00,000 shares of Tk. 10 each</td><td></td><td></td><td>50,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>3,00,000 shares of Tk. 10 each</td><td></td><td></td><td>30,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>6,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>36,00,000</td></tr></table>"
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
