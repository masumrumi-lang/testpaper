import json

new_cq = {
    "id": 17,
    "stem": "<p>Meghna Company Limited was registered with an authorized capital of Tk. 60,00,000, divided into 6,0,000 shares of Tk. 10 each. The company purchased a piece of land valued at Tk. 25,00,000 from Navana Housing Company and paid by issuing shares at par. From the remaining shares, the company issued 3,00,000 shares to the public at a 15% premium. Applications for 3,50,000 shares were received. 3,00,000 shares were allotted duly among the applicants. The excess application money was refunded to the respective applicants.</p>",
    "meta": "Mymensingh Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total number of issued shares and the amount of share premium.",
            "answer": "<p>Total Number of Issued Shares = For asset purchase + To public = 2,50,000 + 3,00,000 = 5,50,000 shares</p><p>Share Premium = 3,00,000 &times; 1.5 = Tk. 4,50,000</p><p>Premium per Share = 10 &times; 15% = Tk. 1.50</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company. (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Land Account<br>To Share Capital Account</td><td></td><td>25,00,000</td><td>25,00,000</td></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>40,25,000</td><td>40,25,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>34,50,000</td><td>30,00,000<br>4,50,000</td></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>5,75,000</td><td>5,75,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Fixed Assets: Land</td><td></td><td></td><td>25,00,000</td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>34,50,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>59,50,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>6,00,000 shares of Tk. 10 each</td><td></td><td></td><td>60,00,000</td></tr><tr><th>Issued, Subscribed and Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>For land: 2,50,000 shares of Tk. 10 each</td><td></td><td>25,00,000</td><td></td></tr><tr><td>To the public: 3,00,000 shares of Tk. 10 each</td><td></td><td>30,00,000</td><td>55,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td></td><td>4,50,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>59,50,000</td></tr></table>"
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
