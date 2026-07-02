import json

new_cq = {
    "id": 28,
    "stem": "<p>Zarif Company Limited was registered with an authorized capital of Tk. 2,00,000, divided into 20,000 shares of Tk. 10 each. The company issued a prospectus to sell 10,000 shares to the public at a 10% discount. Applications for 12,000 shares were received. The company allotted the issued shares duly and the excess application money was refunded. The company purchased a land worth Tk. 18,000 from Meghna Developer Company in exchange for 2,000 shares.</p>",
    "meta": "Chittagong Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the discount per share and total amount of fictitious assets.",
            "answer": "<p>Discount per Share = 10 &times; 10% = Tk. 1</p><p>Total Fictitious Assets = Total Share Discount = (10,000 &times; 1) + (2,000 &times; 1) = Tk. 12,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>1,08,000</td><td>1,08,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>1,08,000<br>10,000</td><td>1,00,000<br>18,000</td></tr><tr><td></td><td>Land Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>18,000<br>2,000</td><td>20,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Land</td><td></td><td></td><td>18,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>90,000</td></tr><tr><th>Fictitious Assets:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td></td><td></td><td>12,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>1,20,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>20,000 shares of Tk. 10 each</td><td></td><td></td><td>2,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>10,000 shares of Tk. 10 each</td><td></td><td></td><td>1,00,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>To the public: 10,000 shares of Tk. 10 each</td><td></td><td>1,00,000</td><td></td></tr><tr><td>For land: 2,000 shares of Tk. 10 each</td><td></td><td>20,000</td><td>1,20,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>1,20,000</td></tr></table>"
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
