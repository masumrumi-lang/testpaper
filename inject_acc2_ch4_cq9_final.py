import json

new_cq = {
    "id": 9,
    "stem": "<p>Sujan Company Ltd.'s authorized capital is Tk. 10,00,000 and the value of each share is Tk. 10. The company issued an advertisement to sell 50% of the authorized shares at a 10% premium for raising capital. The company received 20% more applications than the issued shares. The issued shares were duly allotted and excess application money was refunded to the respective applicants.</p>",
    "meta": "Chittagong Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the number of authorized shares.",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Value</th></tr><tr><td>Authorized shares</td><td>Authorized Capital / Share Price<br>10,00,000 / 10</td><td>1,00,000 shares</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Prepare Bank Account and Share Premium Account in the books of the company.",
            "answer": "<h3>Bank Account</h3><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Application Account</td><td></td><td>6,60,000</td><td></td><td>6,60,000</td></tr><tr><td></td><td>Share Application Account</td><td></td><td></td><td>1,10,000</td><td>5,50,000</td></tr></table><h3>Share Premium Account</h3><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Application Account</td><td></td><td></td><td>50,000</td><td>50,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>5,50,000</td></tr><tr><th>Total Assets</th><td></td><td>5,50,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td>10,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>50,000 shares of Tk. 10 each</td><td></td><td>5,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td>50,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>5,50,000</td></tr></table>"
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
