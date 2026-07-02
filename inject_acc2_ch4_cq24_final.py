import json

new_cq = {
    "id": 24,
    "stem": "<p>Modern Company Limited was registered with an authorized capital of Tk. 5,00,000, divided into 50,000 ordinary shares of Tk. 10 each. The company issued 80% of the authorized capital for sale at a 10% discount. 25% excess applications were received on the issued shares. The shares were allotted duly and the excess application money was refunded. The company issued 10,000 shares including discount to Square Company for the purchase of land.</p>",
    "meta": "Jessore Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the cost price of the land.",
            "answer": "<p>Cost Price of Land = 10,000 &times; 9 = Tk. 90,000</p>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries in the books of the company.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>4,50,000</td><td>4,50,000</td></tr></table><p><i>(Being application money received for 50,000 shares at Tk. 9 each after Tk. 1 discount)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>4,50,000<br>40,000</td><td>4,00,000<br>90,000</td></tr></table><p><i>(Being application money for 40,000 shares transferred to capital account at Tk. 9 each with Tk. 1 discount and excess application money refunded)</i></p><table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Land Account<br>Share Discount Account<br>To Share Capital Account</td><td></td><td>90,000<br>10,000</td><td>1,00,000</td></tr></table><p><i>(Being land purchased in exchange for 10,000 shares of Tk. 10 each with Tk. 1 discount per share)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare Bank Account and Share Discount Account.",
            "answer": "<p><b>Bank Account</b></p><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>To Share Application Account</td><td></td><td>4,50,000</td><td></td><td>4,50,000</td></tr><tr><td></td><td>By Share Application Account</td><td></td><td></td><td>90,000</td><td>3,60,000</td></tr></table><br><p><b>Share Discount Account</b></p><table><tr><th>Date</th><th>Particulars</th><th>J.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th><th>Balance (Tk.)</th></tr><tr><td></td><td>To Share Capital Account</td><td></td><td>40,000</td><td></td><td>40,000</td></tr><tr><td></td><td>To Share Capital Account</td><td></td><td>10,000</td><td></td><td>50,000</td></tr></table>"
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
