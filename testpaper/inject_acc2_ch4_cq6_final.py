import json

new_cq = {
    "id": 6,
    "stem": "<p>Taharat Limited's authorized capital is Tk. 20,00,000, divided into 20,000 shares of Tk. 100 each. The company issued a prospectus to sell 4,000 shares at a 2% discount. The company received applications for a total of 5,000 shares. The company decided to allot 4,000 shares among the applicants.</p>",
    "meta": "Jessore Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of share discount per share and total fictitious assets.",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Amount (Tk.)</th></tr><tr><td>(i) Share discount per share</td><td>100 &times; 2%</td><td>2</td></tr><tr><td>(ii) Fictitious Assets (Total Discount)</td><td>4,000 &times; 2</td><td>8,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Show necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>4,90,000</td><td>4,90,000</td></tr></table><p><i>(Being application money received for 5,000 shares at Tk. 98 each after Tk. 2 discount)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>3,92,000<br>8,000</td><td>4,00,000</td></tr></table><p><i>(Being application money for 4,000 shares at Tk. 98 each transferred to capital account)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>98,000</td><td>98,000</td></tr></table><p><i>(Being excess application money refunded)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position in the books of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>3,92,000</td></tr><tr><td>Unadjusted Expenses: Share Discount</td><td></td><td>8,000</td></tr><tr><th>Total Assets</th><td></td><td>4,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>20,000 shares of Tk. 100 each</td><td></td><td>20,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>4,00,000 shares of Tk. 100 each</td><td></td><td>4,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>4,00,000</td></tr></table>"
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
