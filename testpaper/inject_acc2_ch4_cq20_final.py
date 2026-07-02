import json

new_cq = {
    "id": 20,
    "stem": "<p>Sun Company Ltd. was registered with an authorized capital of Tk. 15,00,000, divided into 75,000 shares of Tk. 20 each. The company issued 20,000 shares at a 10% discount. Applications for 15,000 shares were received and distributed among the respective applicants. The company paid an underwriter's commission of Tk. 2 per share.</p>",
    "meta": "Dhaka Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of share discount.",
            "answer": "<p>Share Discount = Allotted shares &times; Discount per share = 20,000 &times; (20 &times; 10%) = Tk. 40,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account (15,000 &times; 18)<br>To Share Application Account</td><td></td><td>2,70,000</td><td>2,70,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account (2 &times; 15,000)<br>To Share Capital Account (20 &times; 15,000)</td><td></td><td>2,70,000<br>30,000</td><td>3,00,000</td></tr><tr><td></td><td>Bank Account (5,000 &times; 18)<br>Share Discount Account (5,000 &times; 2)<br>To Share Capital Account (5,000 &times; 20)</td><td></td><td>90,000<br>10,000</td><td>1,00,000</td></tr><tr><td></td><td>Underwriter's Commission Account (20,000 &times; 2)<br>To Bank Account</td><td></td><td>40,000</td><td>40,000</td></tr><tr><th></th><th>Total</th><th></th><th>9,10,000</th><th>9,10,000</th></tr></table><p><i>Note: If applications received are less than shares issued, the underwriter buys the unsubscribed shares. Here, as shares were issued at a discount, the underwriter also bought shares at a discount.</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>3,20,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td></td><td>40,000</td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td>40,000</td><td>80,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>4,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>75,000 shares of Tk. 20 each</td><td></td><td></td><td>15,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>20,000 shares of Tk. 20 each</td><td></td><td></td><td>4,00,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>20,000 shares of Tk. 20 each</td><td></td><td></td><td>4,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>4,00,000</td></tr></table>"
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
