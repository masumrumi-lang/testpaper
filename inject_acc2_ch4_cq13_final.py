import json

new_cq = {
    "id": 13,
    "stem": "<p>Soren Company Limited was formed with an authorized capital of Tk. 1,00,00,000, divided into 10,00,000 shares of Tk. 10 each. The company issued a prospectus to sell 50% of the authorized shares at a 10% premium. The company received 25% more applications than the issued shares. The excess application money was refunded. An underwriter's commission of Tk. 0.10 per share and bank charges of Tk. 0.06 per share were charged.</p>",
    "meta": "Barisal Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total amount of underwriter's commission and bank charges.",
            "answer": "<table><tr><th>Particulars</th><th>Details (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Underwriter's Commission (5,00,000 &times; 0.10)</td><td></td><td>50,000</td></tr><tr><td>Bank Charges (5,00,000 &times; 0.06)</td><td></td><td>30,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>68,75,000</td><td>68,75,000</td></tr></table><p><i>(Being application money received for 6,25,000 shares at Tk. 11 each including Tk. 1 premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>55,00,000</td><td>50,00,000<br>5,00,000</td></tr></table><p><i>(Being application money for 5,00,000 shares transferred to capital and premium accounts)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>13,75,000</td><td>13,75,000</td></tr></table><p><i>(Being excess application money refunded with premium)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Underwriter's Commission Account<br>Bank Charges Account<br>To Bank Account</td><td></td><td>50,000<br>30,000</td><td>80,000</td></tr></table><p><i>(Being underwriter's commission and bank charges paid)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>54,20,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td>50,000</td><td></td></tr><tr><td>Bank Charges</td><td></td><td>30,000</td><td>80,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>55,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>10,00,000 shares of Tk. 10 each</td><td></td><td></td><td>1,00,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>5,00,000 shares of Tk. 10 each</td><td></td><td></td><td>50,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>5,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>55,00,000</td></tr></table>"
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
