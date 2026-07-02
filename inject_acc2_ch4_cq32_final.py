import json

new_cq = {
    "id": 32,
    "stem": "<p>The following information of Nilima Ltd. is provided:</p><table><tr><th>Current Assets</th><th>Tk.</th><th>Current Liabilities</th><th>Tk.</th></tr><tr><td>Inventory</td><td>1,50,000</td><td>Sundry Creditors / Accounts Payable</td><td>40,000</td></tr><tr><td>Sundry Debtors / Accounts Receivable</td><td>50,000</td><td>Bank Overdraft</td><td>20,000</td></tr><tr><td>Bank Deposit</td><td>50,000</td><td></td><td></td></tr></table><p>Total sales during the year was Tk. 8,00,000. The company sells goods at a profit of 25% on cost of goods sold. The net profit of the company was Tk. 80,000.</p>",
    "meta": "Chittagong Board · 2023",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of gross profit.",
            "answer": "<p>Profit is 25% on Cost of Goods Sold. So, if Cost = 100, Sales Price = 100 + 25 = 125.</p><p>Gross Profit = (8,00,000 / 125) &times; 25 = Tk. 1,60,000</p>"
        },
        {
            "label": "b",
            "text": "Determine Current Ratio and Gross Profit Ratio.",
            "answer": "<p><b>Current Ratio:</b></p><p>Current Ratio = Current Assets / Current Liabilities = 2,50,000 / 60,000 = 4.17 : 1</p><p><i>Calculations:</i><br>Current Assets = Inventory + Debtors + Bank Deposit = 1,50,000 + 50,000 + 50,000 = Tk. 2,50,000<br>Current Liabilities = Creditors + Bank Overdraft = 40,000 + 20,000 = Tk. 60,000</p><p><b>Gross Profit Ratio:</b></p><p>Gross Profit Ratio = (Gross Profit / Net Sales) &times; 100 = (1,60,000 / 8,00,000) &times; 100 = 20%</p>"
        },
        {
            "label": "c",
            "text": "Determine Net Profit Ratio and Inventory Turnover Ratio.",
            "answer": "<p><b>Net Profit Ratio:</b></p><p>Net Profit Ratio = (Net Profit / Net Sales) &times; 100 = (80,000 / 8,00,000) &times; 100 = 10%</p><p><b>Inventory Turnover Ratio:</b></p><p>Inventory Turnover Ratio = Cost of Goods Sold / Average Inventory = 6,40,000 / 1,50,000 = 4.27 times</p><p><i>Calculation:</i><br>Cost of Goods Sold = Sales - Gross Profit = 8,00,000 - 1,60,000 = Tk. 6,40,000<br>(Note: Closing inventory is used as average inventory since opening inventory is not provided.)</p>"
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
