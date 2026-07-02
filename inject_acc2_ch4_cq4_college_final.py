import json

new_cq = {
    "id": 4,
    "stem": "<p>Maria Company Limited was registered with 50,000 shares of Tk. 10 each. The company issued a prospectus to sell 30,000 shares to the public at a 10% discount. The company received applications for 33,000 shares. The fixed number of shares were allotted and the excess application money was refunded to the respective applicants.</p>",
    "meta": "Dhaka Commerce College · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Show journal entries related to share issue (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>2,97,000</td><td>2,97,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>2,97,000<br>30,000</td><td>3,00,000<br>27,000</td></tr><tr><th>Total</th><td></td><td></td><td>6,24,000</td><td>6,24,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Prepare Bank Account and Share Discount Account.",
            "answer": "<p><b>Bank Account:</b></p><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Application Account</td><td></td><td>2,97,000</td><td></td><td>2,97,000 (Dr)</td></tr><tr><td></td><td>Share Application Account (Refund)</td><td></td><td></td><td>27,000</td><td>2,70,000 (Dr)</td></tr></table><p><b>Share Discount Account:</b></p><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Capital Account</td><td></td><td>30,000</td><td></td><td>30,000 (Dr)</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>2,70,000</td></tr><tr><td>Fictitious Assets: Share Discount</td><td></td><td></td><td>30,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>3,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>50,000 shares of Tk. 10 each</td><td></td><td></td><td>5,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>30,000 shares of Tk. 10 each</td><td></td><td></td><td>3,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>3,00,000</td></tr></table>"
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
