import json

new_cq = {
    "id": 2,
    "stem": "<p>ACI Company Ltd.'s authorized capital is Tk. 4,00,000, divided into 40,000 shares of Tk. 10 each. 5,000 shares were issued for purchasing a piece of land. 30,000 shares were issued to the public at a 10% discount. The company received applications for 32,000 shares. The excess application money was refunded. The company paid Tk. 30,000 in cash as underwriter's commission.</p>",
    "meta": "Dhaka Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of share discount per share and total share discount.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th></tr><tr><td>Share discount per share (Tk. 10 &times; 10%)</td><td>1</td></tr><tr><td>Total share discount (30,000 &times; Tk. 1)</td><td>30,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (without explanation).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Land Account<br>To Share Capital Account</td><td></td><td>50,000</td><td>50,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>2,88,000</td><td>2,88,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>2,70,000<br>30,000</td><td>3,00,000</td></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>18,000</td><td>18,000</td></tr><tr><td></td><td>Underwriter's Commission Account<br>To Bank Account</td><td></td><td>30,000</td><td>30,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Land</td><td></td><td></td><td>50,000</td></tr><tr><td>Current Assets:</td><td></td><td></td><td></td></tr><tr><td>Bank Deposit (2,88,000 - 18,000 - 30,000)</td><td></td><td></td><td>2,40,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td></td><td>30,000</td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td>30,000</td><td>60,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>3,50,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>40,000 shares of Tk. 10 each</td><td></td><td></td><td>4,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>30,000 shares of Tk. 10 each to the public</td><td></td><td>3,00,000</td><td></td></tr><tr><td>5,000 shares of Tk. 10 each for land</td><td></td><td>50,000</td><td>3,50,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>3,50,000</td></tr></table>"
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
