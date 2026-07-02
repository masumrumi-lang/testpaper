import json

new_cq = {
    "id": 22,
    "stem": "<p>Achia Ltd. was registered with an authorized capital of Tk. 10,00,000, divided into 1,00,000 shares of Tk. 10 each. The company issued a prospectus to sell 70,000 shares to the public at a 10% discount. Applications for 60,000 shares were received from the public and were allotted duly. The company purchased a computer from Sayma Ltd. in exchange for 10,000 shares at par.</p>",
    "meta": "Rajshahi Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the discount per share and total discount.",
            "answer": "<p>Discount per Share = 10 &times; 10% = Tk. 1</p><p>Total Discount = 60,000 &times; 1 = Tk. 60,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>5,40,000</td><td>5,40,000</td></tr></table><p><i>(Being application money received for 60,000 shares at Tk. 9 each after Tk. 1 discount)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>5,40,000<br>60,000</td><td>6,00,000</td></tr></table><p><i>(Being application money for 60,000 shares transferred to capital account at Tk. 9 each with Tk. 1 discount per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Office Equipment Account<br>To Share Capital Account</td><td></td><td>1,00,000</td><td>1,00,000</td></tr></table><p><i>(Being computer purchased in exchange for 10,000 shares of Tk. 10 each)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Office Equipment</td><td></td><td></td><td>1,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>5,40,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td></td><td></td><td>60,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>7,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td></td><td>10,00,000</td></tr><tr><th>Issued Capital:</th><td></td><td></td><td></td></tr><tr><td>70,000 shares of Tk. 10 each</td><td></td><td></td><td>7,00,000</td></tr><tr><th>Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>To the public: 60,000 shares of Tk. 10 each</td><td></td><td>6,00,000</td><td></td></tr><tr><td>For office equipment: 10,000 shares of Tk. 10 each</td><td></td><td>1,00,000</td><td>7,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>7,00,000</td></tr></table>"
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
