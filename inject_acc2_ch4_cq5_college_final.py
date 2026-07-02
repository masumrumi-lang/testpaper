import json

new_cq = {
    "id": 5,
    "stem": "<p>Teesta Company Limited was formed with an authorized capital of Tk. 40,00,000 divided into 2,00,000 shares of Tk. 20 each. The company purchased a piece of land in exchange for 20,000 shares at par. Besides, the company issued a prospectus to sell 1,40,000 shares to the public at a 10% premium. Applications for 1,50,000 shares were received. The issued shares were allotted duly and excess application money was refunded to the respective applicants. The company pays Tk. 0.40 per share as underwriter's commission.</p>",
    "meta": "Milestone College, Dhaka · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of underwriter's commission.",
            "answer": "<p>Underwriter's Commission = Shares allotted to public &times; Commission per share = 1,40,000 &times; 0.40 = Tk. 56,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Land Account<br>To Share Capital Account</td><td></td><td>4,00,000</td><td>4,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>33,00,000</td><td>33,00,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account<br>To Bank Account</td><td></td><td>33,00,000</td><td>28,00,000<br>2,80,000<br>2,20,000</td></tr><tr><td></td><td>Underwriter's Commission Account<br>To Bank Account</td><td></td><td>56,000</td><td>56,000</td></tr><tr><th>Total</th><td></td><td></td><td>70,56,000</td><td>70,56,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Land</td><td></td><td></td><td>4,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>30,24,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td></td><td>56,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>34,80,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>2,00,000 shares of Tk. 20 each</td><td></td><td></td><td>40,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>1,60,000 shares of Tk. 20 each</td><td></td><td></td><td>32,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>2,80,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>34,80,000</td></tr></table>"
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
