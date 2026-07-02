import json

new_cq = {
    "id": 15,
    "stem": "<p>Rupali PLC is a joint stock company registered with 10,00,000 ordinary shares of Tk. 10 each. To meet preliminary expenses, the company issued 1,00,000 shares at par in cash to the sponsors at the beginning of the year. In the middle of the year, the company issued an IPO via prospectus to sell 40% of the total authorized shares at a 10% premium. The company received 20% more applications than the shares available for issue. Shares were allotted duly by lottery and excess application money was refunded.</p>",
    "meta": "Dinajpur Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the number of allotted shares and the amount of share premium.",
            "answer": "<p>Number of Allotted Shares = To sponsors + To public = 1,00,000 shares + 4,00,000 shares = 5,00,000 shares</p><p>Share Premium = 4,00,000 &times; 1 = Tk. 4,00,000</p>"
        },
        {
            "label": "b",
            "text": "Show necessary journal entries in the books of the company. (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Capital Account</td><td></td><td>10,00,000</td><td>10,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>52,80,000</td><td>52,80,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>44,00,000</td><td>40,00,000<br>4,00,000</td></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>8,80,000</td><td>8,80,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>54,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>54,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>10,00,000 shares of Tk. 10 each</td><td></td><td></td><td>1,00,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>For sponsors: 1,00,000 shares of Tk. 10 each</td><td></td><td>10,00,000</td><td></td></tr><tr><td>To the public: 4,00,000 shares of Tk. 10 each</td><td></td><td>40,00,000</td><td>50,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>4,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>54,00,000</td></tr></table>"
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
