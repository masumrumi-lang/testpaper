import json

new_cq = {
    "id": 29,
    "stem": "<p>Meghna Ltd. was registered with an authorized capital of Tk. 25,00,000, divided into 2,50,000 shares of Tk. 10 each. The company decided to issue 2,00,000 shares.<br>2023:<br>Jan 10: Land purchased in exchange for 50,000 shares at a premium of Tk. 2.<br>Jan 15: Advertisement published in newspaper to sell remaining shares at a premium of Tk. 2.<br>Jan 20: Applications for 1,70,000 shares were received.<br>Jan 25: Excess application money was refunded and the issued shares were allotted duly.</p>",
    "meta": "Sylhet Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total amount of share premium.",
            "answer": "<p>Total Share Premium = Issued shares &times; Premium per share = (2,00,000 &times; 2) = Tk. 8,00,000<br><i>(Note: The source solution contains this mathematical inconsistency)</i></p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>2023<br>Jan 10</td><td>Land Account<br>To Share Premium Account<br>To Share Capital Account</td><td></td><td>6,00,000</td><td>1,00,000<br>5,00,000</td></tr></table><p><i>(Being land purchased in exchange for 50,000 shares of Tk. 10 each with Tk. 2 premium per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>Jan 20</td><td>Bank Account<br>To Share Application Account</td><td></td><td>20,80,000</td><td>20,80,000</td></tr></table><p><i>(Being application money received for 1,70,000 shares at Tk. 12 each including Tk. 2 premium per share)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>Jan 25</td><td>Share Application Account<br>To Share Premium Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>20,80,000</td><td>3,00,000<br>15,00,000<br>2,80,000</td></tr></table><p><i>(Being application money for 1,50,000 shares transferred to capital account at Tk. 12 each including Tk. 2 premium and excess application money refunded)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position as at 31st January, 2023.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Land</td><td></td><td></td><td>6,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>18,00,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>24,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>2,50,000 shares of Tk. 10 each</td><td></td><td></td><td>25,00,000</td></tr><tr><th>Issued Capital:</th><td></td><td></td><td></td></tr><tr><td>2,00,000 shares of Tk. 10 each</td><td></td><td></td><td>20,00,000</td></tr><tr><th>Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>To the public: 1,50,000 shares of Tk. 10 each</td><td></td><td>15,00,000</td><td></td></tr><tr><td>For land: 50,000 shares of Tk. 10 each</td><td></td><td>5,00,000</td><td>20,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>8,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>28,00,000</td></tr></table><p><i>(Note: Total assets is Tk. 24,00,000 and total liabilities is Tk. 28,00,000 in the source solution due to inconsistency in the problem)</i></p>"
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
