import json

new_cq = {
    "id": 18,
    "stem": "<p>Surma Company Limited was formed with an authorized capital of Tk. 30,00,000, divided into 3,00,000 shares of Tk. 10 each. The company issued 2,00,000 shares to the public at a 10% discount. Applications for 2,50,000 shares were received. 2,00,000 shares were allotted duly. The excess application money was refunded to the respective applicants. An underwriter's commission of Tk. 0.50 per share was charged.</p>",
    "meta": "Mymensingh Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total amount of discount and underwriter's commission.",
            "answer": "<table><tr><th>Particulars</th><th>Details (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Total Discount (2,00,000 &times; 1)</td><td></td><td>2,00,000</td></tr><tr><td>Underwriter's Commission (2,00,000 &times; 0.50)</td><td></td><td>1,00,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>22,50,000</td><td>22,50,000</td></tr></table><p><i>(Being application money received for 2,50,000 shares at Tk. 9 each after discount)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>18,00,000<br>2,00,000</td><td>20,00,000</td></tr></table><p><i>(Being application money for 2,00,000 shares transferred to capital account with Tk. 1 discount per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>4,50,000</td><td>4,50,000</td></tr></table><p><i>(Being excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Underwriter's Commission Account<br>To Bank Account</td><td></td><td>1,00,000</td><td>1,00,000</td></tr></table><p><i>(Being underwriter's commission paid)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>17,00,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td></td><td>2,00,000</td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td>1,00,000</td><td>3,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>20,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>3,00,000 shares of Tk. 10 each</td><td></td><td></td><td>30,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>2,00,000 shares of Tk. 10 each</td><td></td><td></td><td>20,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>20,00,000</td></tr></table>"
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
