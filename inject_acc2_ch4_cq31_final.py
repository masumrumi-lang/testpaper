import json

new_cq = {
    "id": 31,
    "stem": "<p>The Balance Sheet of Sagar Bilas Limited as of 31st December, 2022 is given below:</p><table><tr><th>Liabilities</th><th>Amount (Tk.)</th><th>Assets</th><th>Amount (Tk.)</th></tr><tr><td>Share Capital</td><td>3,70,000</td><td>Fixed Assets</td><td>2,00,000</td></tr><tr><td>General Reserve</td><td>80,000</td><td>Inventory</td><td>27,500</td></tr><tr><td>12% Debenture</td><td>30,000</td><td>Accounts Receivable</td><td>1,50,000</td></tr><tr><td>Share Premium</td><td>10,000</td><td>Cash</td><td>30,000</td></tr><tr><td>Outstanding Expense</td><td>2,500</td><td>Bank Deposit</td><td>90,000</td></tr><tr><td>Accounts Payable</td><td>50,000</td><td>Notes Receivable</td><td>45,000</td></tr><tr><th>Total</th><th>5,42,500</th><th>Total</th><th>5,42,500</th></tr></table><p>The company sells goods at a profit of 25% on cost of goods sold. The amount of sales in 2022 was Tk. 7,50,000.</p>",
    "meta": "Chittagong Board · 2023",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the cost of goods sold.",
            "answer": "<p>Profit is 25% on Cost of Goods Sold. So, if Cost = 100, Sales Price = 100 + 25 = 125.</p><p>Cost of Goods Sold = (7,50,000 / 125) &times; 100 = Tk. 6,00,000</p>"
        },
        {
            "label": "b",
            "text": "Determine Current Ratio and Gross Profit Ratio.",
            "answer": "<p><b>Current Ratio:</b></p><p>Current Ratio = Current Assets / Current Liabilities = 3,42,500 / 52,500 = 6.52 : 1</p><p><i>Calculations:</i><br>Current Assets = Inventory + Accounts Receivable + Cash + Bank Deposit + Notes Receivable<br>= 27,500 + 1,50,000 + 30,000 + 90,000 + 45,000 = Tk. 3,42,500<br>Current Liabilities = Outstanding Expense + Accounts Payable<br>= 2,500 + 50,000 = Tk. 52,500</p><p><b>Gross Profit Ratio:</b></p><p>Gross Profit Ratio = (Gross Profit / Net Sales) &times; 100 = (1,50,000 / 7,50,000) &times; 100 = 20%</p><p><i>Calculation:</i><br>Gross Profit = Sales - Cost of Goods Sold = 7,50,000 - 6,00,000 = Tk. 1,50,000</p>"
        },
        {
            "label": "c",
            "text": "Determine Working Capital Ratio and Inventory Turnover Ratio.",
            "answer": "<p><b>Working Capital Ratio:</b></p><p>Working Capital Ratio = (Current Assets - Current Liabilities) / Current Liabilities<br>= (3,42,500 - 52,500) / 52,500 = 2,90,000 / 52,500 = 5.52 : 1</p><p><b>Inventory Turnover Ratio:</b></p><p>Inventory Turnover Ratio = Cost of Goods Sold / Average Inventory = 6,00,000 / 27,500 = 21.82 times</p><p><i>(Note: Closing inventory is used as average inventory since opening inventory is not provided.)</i></p>"
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
