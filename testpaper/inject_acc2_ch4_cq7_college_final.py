import json

new_cq = {
    "id": 7,
    "stem": "<p>Topten Company Ltd. was formed with 2,40,000 shares of Tk. 10 each. The company decided to sell 2,00,000 shares at a 10% discount.</p><ol><li>A machine was purchased in exchange for 20,000 shares.</li><li>Prospectus was issued for 1,00,000 shares, applications for 1,20,000 shares were received and issued shares were allotted.</li><li>Contracted with an underwriter for share sale work.</li><li>Issued 10,000 shares as underwriter's remuneration/commission.</li><li>Shares were allotted to applicants in exchange for previously received excess application money.</li><li>The remaining of the issued shares were issued and allotted.</li></ol>",
    "meta": "Holy Cross College · 2025",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total amount of discount.",
            "answer": "<p>Total Discount = (20,000 + 1,00,000 + 20,000 + 10,000 + 50,000) &times; 1 = 2,00,000 &times; 1 = Tk. 2,00,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries for Topten Company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Machine Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>1,80,000<br>20,000</td><td>2,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>10,80,000</td><td>10,80,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>10,80,000<br>1,20,000</td><td>12,00,000</td></tr><tr><td></td><td>Underwriter's Commission Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>90,000<br>10,000</td><td>1,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>4,50,000</td><td>4,50,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>4,50,000<br>50,000</td><td>5,00,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of Topten Company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Machine</td><td></td><td></td><td>1,80,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>15,30,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td>2,00,000</td><td></td><td></td></tr><tr><td>Underwriter's Fee</td><td>90,000</td><td>2,90,000</td><td></td></tr><tr><th>Total Assets</th><td></td><td></td><td>20,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>2,40,000 shares of Tk. 10 each</td><td></td><td></td><td>24,00,000</td></tr><tr><th>Issued Capital:</th><td></td><td></td><td></td></tr><tr><td>2,00,000 shares of Tk. 10 each</td><td></td><td></td><td>20,00,000</td></tr><tr><th>Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>For Machine: 20,000 shares of Tk. 10 each</td><td></td><td>2,00,000</td><td></td></tr><tr><td>To Public: 1,50,000 shares of Tk. 10 each</td><td></td><td>15,00,000</td><td></td></tr><tr><td>For Excess Application: 20,000 shares of Tk. 10 each</td><td></td><td>2,00,000</td><td></td></tr><tr><td>For Underwriter: 10,000 shares of Tk. 10 each</td><td></td><td>1,00,000</td><td>20,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>20,00,000</td></tr></table>"
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
