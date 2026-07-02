import json

new_cq = {
    "id": 27,
    "stem": "<p>Jamuna Company Ltd. was formed with an authorized capital of Tk. 1,00,000, divided into 10,000 shares of Tk. 10 each. The company issued a prospectus to sell 7,000 shares at a 10% premium. Applications for 8,000 shares were received. The company allotted the issued shares duly and refunded the excess application money to the respective applicants. The company paid Tk. 0.30 per share as underwriter's commission.</p>",
    "meta": "Chittagong Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of share premium of Jamuna Company Ltd.",
            "answer": "<p>Share Premium = Allotted shares &times; Premium per share = 7,000 &times; (10 &times; 10%) = Tk. 7,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>88,000</td><td>88,000</td></tr></table><p><i>(Being application money received for 8,000 shares at Tk. 11 each including Tk. 1 premium per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Share Premium Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>88,000</td><td>7,000<br>70,000<br>11,000</td></tr></table><p><i>(Being application money for 7,000 shares transferred to capital account at Tk. 11 each including Tk. 1 premium and excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Underwriter's Commission Account<br>To Bank Account</td><td></td><td>2,100</td><td>2,100</td></tr></table><p><i>(Being underwriter's commission paid)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>74,900</td></tr><tr><th>Fictitious Assets:</th><td></td><td></td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td></td><td>2,100</td></tr><tr><th>Total Assets</th><td></td><td></td><td>77,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>10,000 shares of Tk. 10 each</td><td></td><td></td><td>1,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>7,000 shares of Tk. 10 each</td><td></td><td></td><td>70,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>7,000 shares of Tk. 10 each</td><td></td><td></td><td>70,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>7,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>77,000</td></tr></table>"
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
