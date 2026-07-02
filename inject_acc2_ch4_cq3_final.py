import json

new_cq = {
    "id": 3,
    "stem": "<p>Sonali Public Limited Company's authorized capital is Tk. 10,00,000 divided into 1,00,000 shares. The company published an advertisement in the newspaper on January 1, 2024, to sell 60,000 shares at face value for the purpose of raising capital. The following transactions were completed in the month of January:</p><p>2024<br>Jan 10: Applications received for a total of 70,000 shares.<br>Jan 20: 60,000 shares were duly allotted.<br>Jan 30: Excess application money was refunded to the respective applicants.<br>Jan 31: 5% commission was paid to the share underwriter.</p>",
    "meta": "Rajshahi Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the face value of each share.",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th></tr><tr><td>Face value of each share</td><td>Authorized Capital / Number of Shares<br>10,00,000 / 1,00,000 = Tk. 10</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Show necessary journal entries in the books of Sonali Public Limited.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>2024 Jan 10</td><td>Bank Account<br>To Share Application Account</td><td></td><td>7,00,000</td><td>7,00,000</td></tr></table><p><i>(Being share application money received for 70,000 shares at Tk. 10 each)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>Jan 20</td><td>Share Application Account<br>To Share Capital Account</td><td></td><td>6,00,000</td><td>6,00,000</td></tr></table><p><i>(Being application money for 60,000 shares at Tk. 10 each transferred to capital account)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>Jan 30</td><td>Share Application Account<br>To Bank Account</td><td></td><td>1,00,000</td><td>1,00,000</td></tr></table><p><i>(Being excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>Jan 31</td><td>Underwriter's Commission Account<br>To Bank Account</td><td></td><td>30,000</td><td>30,000</td></tr></table><p><i>(Being commission paid to underwriter)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company assuming the bank balance is Tk. 5,70,000.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td>5,70,000</td></tr><tr><td>Unadjusted Expenses: Underwriter's Commission</td><td></td><td>30,000</td></tr><tr><th>Total Assets</th><td></td><td>6,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td></tr><tr><td>1,00,000 shares of Tk. 10 each</td><td></td><td>10,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td></tr><tr><td>60,000 shares of Tk. 10 each</td><td></td><td>6,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>6,00,000</td></tr></table>"
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
