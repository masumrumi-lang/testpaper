import json

new_cq = {
    "id": 10,
    "stem": "<p>Sumi and Mimi are two partners in a partnership business. They run the business on the basis of sharing profits and losses in the ratio of 3:2. On 1st January 2020, the balances of their business capital and current accounts were as follows:</p><table><tr><th>Account Name</th><th>Taka</th><th>Account Name</th><th>Taka</th></tr><tr><td>Sumi's Capital</td><td>100,000</td><td>Sumi's Current Account (Credit)</td><td>10,000</td></tr><tr><td>Mimi's Capital</td><td>80,000</td><td>Mimi's Current Account (Credit)</td><td>6,000</td></tr></table><p>On 1st July, Sumi brought Tk. 10,000 as additional capital. Mimi will receive an annual salary of Tk. 20,000 for performing full-time duties. Sumi brought Tk. 30,000 as a loan into the business in the middle of the year. In anticipation of profit in that year, the partners withdrew Tk. 25,000 and Tk. 15,000 in cash respectively. Besides cash drawings, Sumi withdrew goods worth Tk. 4,000 which was not recorded. Interest is to be charged at 10% on capital. Before making the above adjustments, the net profit of the business for the year ended 31st December 2020 arrived at Tk. 80,000.</p>",
    "meta": "Viqarunnisa Noon School and College · 2024",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Prepare Sumi's Capital Account under fixed capital method.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>Sumi (Tk.)</th><th>Mimi (Tk.)</th><th>Date</th><th>Particulars</th><th>Sumi (Tk.)</th><th>Mimi (Tk.)</th></tr><tr><td>2020 Dec 31</td><td>Balance c/d</td><td>1,10,000</td><td>80,000</td><td>2020 Jan 1<br>July 1</td><td>Balance b/d<br>Cash Account</td><td>1,00,000<br>10,000</td><td>80,000<br>-</td></tr><tr><th></th><th>Total</th><th>1,10,000</th><th>80,000</th><th></th><th>Total</th><th>1,10,000</th><th>80,000</th></tr></table>"
        },
        {
            "label": "b",
            "text": "Prepare Profit and Loss Appropriation Account of the partners.",
            "answer": "<table><tr><th>Particulars</th><th>Taka</th><th>Particulars</th><th>Taka</th></tr><tr><td><b>Partners' Current A/c (Int. on Capital):</b><br>Sumi: 10,500<br>Mimi: 8,000</td><td>18,500</td><td><b>Profit and Loss A/c:</b><br>Net Profit</td><td>80,000</td></tr><tr><td><b>Mimi's Current A/c:</b> Salary</td><td>20,000</td><td><b>Sumi's Current A/c:</b> Goods Drawings (shown as 8,000 in source)</td><td>8,000</td></tr><tr><td><b>Sumi's Current A/c:</b> Interest on Loan</td><td>900</td><td></td><td></td></tr><tr><td><b>Partners' Current A/c (Profit Share):</b><br>Sumi: 26,760<br>Mimi: 17,840</td><td>44,600</td><td></td><td></td></tr><tr><th>Total</th><th>84,000</th><th>Total</th><th>88,000</th></tr></table><p><i>(Note: The source image shows Goods Drawings as 8,000 and the credit total as 88,000, but the divisible profit of 44,600 was calculated using 4,000 as drawings. The table reproduces the visual numbers from the source.)</i></p>"
        },
        {
            "label": "c",
            "text": "Prepare Mimi's Current Account.",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>Taka</th><th>Date</th><th>Particulars</th><th>Taka</th></tr><tr><td>2020 Dec 31</td><td>Drawings Account</td><td>15,000</td><td>2020 Jan 1</td><td>Balance b/d</td><td>6,000</td></tr><tr><td>2020 Dec 31</td><td>Balance c/d</td><td>36,840</td><td>2020 Dec 31</td><td><b>P&L Appropriation A/c:</b></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>Interest on Capital</td><td>8,000</td></tr><tr><td></td><td></td><td></td><td></td><td>Salary</td><td>20,000</td></tr><tr><td></td><td></td><td></td><td></td><td>Share of Profit</td><td>17,840</td></tr><tr><th></th><th>Total</th><th>51,840</th><th></th><th>Total</th><th>51,840</th></tr></table>"
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
