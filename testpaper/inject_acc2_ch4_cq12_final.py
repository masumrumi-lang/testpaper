import json

new_cq = {
    "id": 12,
    "stem": "<p>Manik and Brothers Company Ltd. was registered with 1,80,000 shares of Tk. 10 each. The company decided to issue 1,60,000 of its shares at a premium of Tk. 1 each and allotted the shares accordingly.<br>2024<br>March 1: 25,000 shares were issued as payment for purchasing machinery.<br>March 20: 50,000 shares were distributed among the directors.<br>March 30: Applications for 95,000 shares were received for the remaining issued shares and shares were allotted duly. Excess application money was refunded.</p>",
    "meta": "Sylhet Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of premium received.",
            "answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Amount (Tk.)</th></tr><tr><td>Premium amount</td><td>1,60,000 &times; 1</td><td>1,60,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries. (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td>2024 March 1</td><td>Machinery Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>2,75,000</td><td>2,50,000<br>25,000</td></tr><tr><td>March 20</td><td>Goodwill Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>5,50,000</td><td>5,00,000<br>50,000</td></tr><tr><td>March 30</td><td>Bank Account<br>To Share Application Account</td><td></td><td>10,45,000</td><td>10,45,000</td></tr><tr><td>March 30</td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>9,35,000</td><td>8,50,000<br>85,000</td></tr><tr><td>March 30</td><td>Share Application Account<br>To Bank Account</td><td></td><td>1,10,000</td><td>1,10,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare Bank Account and Share Capital Account.",
            "answer": "<h3>Bank Account</h3><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td>2024 March 30</td><td>Share Application Account</td><td></td><td>10,45,000</td><td></td><td>10,45,000</td></tr><tr><td>March 30</td><td>Share Application Account</td><td></td><td></td><td>1,10,000</td><td>9,35,000</td></tr></table><h3>Share Capital Account</h3><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td>2024 March 1</td><td>Machinery Account</td><td></td><td></td><td>2,50,000</td><td>2,50,000 (Cr)</td></tr><tr><td>March 20</td><td>Goodwill Account</td><td></td><td></td><td>5,00,000</td><td>7,50,000 (Cr)</td></tr><tr><td>March 30</td><td>Share Application Account</td><td></td><td></td><td>8,50,000</td><td>16,00,000 (Cr)</td></tr></table>"
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
