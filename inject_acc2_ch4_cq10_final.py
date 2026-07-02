import json

new_cq = {
    "id": 10,
    "stem": "<p>Shreya Limited was registered with an authorized capital of Tk. 80,00,000, divided into 8,0,000 shares of Tk. 10 each. The company issued a prospectus to sell 2,00,000 shares at a 5% discount. The company received applications for a total of 2,50,000 shares. The issued shares were allotted and excess application money was refunded. The bank charged Tk. 0.05 per share as bank charges.</p>",
    "meta": "Chittagong Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of fictitious assets.",
            "answer": "<table><tr><th>Particulars</th><th>Details (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Share Discount {2,00,000 &times; (10 &times; 5%)}</td><td>1,00,000</td><td></td></tr><tr><td>Bank Charges (2,00,000 &times; 0.05)</td><td>10,000</td><td></td></tr><tr><th>Total Fictitious Assets</th><td></td><td>1,10,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Show necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>23,75,000</td><td>23,75,000</td></tr></table><p><i>(Being application money received for 2,50,000 shares at Tk. 9.50 each after Tk. 0.50 discount)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>19,00,000<br>1,00,000</td><td>20,00,000</td></tr></table><p><i>(Being application money for 2,00,000 shares at Tk. 9.50 each transferred to capital account)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>4,75,000</td><td>4,75,000</td></tr></table><p><i>(Being excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Charges Account<br>To Bank Account</td><td></td><td>10,000</td><td>10,000</td></tr></table><p><i>(Being bank charges recorded)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare Bank Account and Share Application Account in the books of the company.",
            "answer": "<h3>Bank Account</h3><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Share Application Account</td><td></td><td>23,75,000</td><td></td><td>23,75,000</td></tr><tr><td></td><td>Share Application Account</td><td></td><td></td><td>4,75,000</td><td>19,00,000</td></tr><tr><td></td><td>Bank Charges Account</td><td></td><td></td><td>10,000</td><td>18,90,000</td></tr></table><h3>Share Application Account</h3><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>Bank Account</td><td></td><td></td><td>23,75,000</td><td>23,75,000 (Cr)</td></tr><tr><td></td><td>Share Capital Account</td><td></td><td>19,00,000</td><td></td><td>4,75,000 (Cr)</td></tr><tr><td></td><td>Bank Account</td><td></td><td>4,75,000</td><td></td><td>Nil</td></tr></table>"
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
