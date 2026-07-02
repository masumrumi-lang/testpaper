import json

new_cq = {
    "id": 7,
    "stem": "<p>Shovon Company Ltd. was registered with a capital of Tk. 40,00,000, divided into 4,0,000 shares of Tk. 10 each. The company issued an advertisement to sell 50% of the shares from the authorized capital at a 10% premium. A total of 2,30,000 shares were applied for. The issued shares were duly allotted and excess application money was refunded.</p>",
    "meta": "Comilla Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the number of refunded shares.",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Value</th></tr><tr><td>Refunded shares</td><td>Applied shares - Allotted shares<br>2,30,000 - (4,00,000 &times; 50%)</td><td>30,000 shares</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>25,30,000</td><td>25,30,000</td></tr></table><p><i>(Being application money received for 2,30,000 shares at Tk. 11 each including Tk. 1 premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>22,00,000</td><td>20,00,000<br>2,00,000</td></tr></table><p><i>(Being application money for 2,00,000 shares transferred to capital and premium accounts)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>3,30,000</td><td>3,30,000</td></tr></table><p><i>(Being excess application money refunded with premium)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>22,00,000</td></tr><tr><th>Total Assets</th><td></td><td>22,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>4,00,000 shares of Tk. 10 each</td><td></td><td>40,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>2,00,000 shares of Tk. 10 each</td><td></td><td>20,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td>2,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>22,00,000</td></tr></table>"
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
