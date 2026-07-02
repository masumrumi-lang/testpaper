import json

new_cq = {
    "id": 33,
    "stem": "<p>The following information regarding production for the month of January 2022 is supplied from Pallabi Enterprise:</p><table><tr><th>Particulars</th><th>Tk.</th></tr><tr><td>Opening Inventory of Raw Materials</td><td>35,000</td></tr><tr><td>Purchase of Raw Materials</td><td>2,00,000</td></tr><tr><td>Closing Inventory of Raw Materials</td><td>25,000</td></tr><tr><td>Direct Labor</td><td>1,20,000</td></tr><tr><td>Factory Overhead</td><td>75,000</td></tr><tr><td>Office and Administrative Expense</td><td>35,000</td></tr><tr><td>Selling and Distribution Expense</td><td>1,10,000</td></tr><tr><td>Opening Inventory of Finished Goods (5,000 units)</td><td>50,000</td></tr><tr><td>Closing Inventory of Finished Goods (10,000 units)</td><td>?</td></tr><tr><td>Sales (40,000 units)</td><td>8,00,000</td></tr></table>",
    "meta": "Chittagong Board · 2023",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of production (in units).",
            "answer": "<p>Amount of Production = Sales units + Closing units - Opening units</p><p>= 40,000 + 10,000 - 5,000 = 45,000 units</p>"
        },
        {
            "label": "b",
            "text": "Prepare the Statement of Cost of Production.",
            "answer": "<table><tr><th>Particulars</th><th>Tk.</th><th>Tk.</th><th>Tk.</th></tr><tr><td>Opening Inventory of Raw Materials</td><td>35,000</td><td></td><td></td></tr><tr><td>(+) Purchase of Raw Materials</td><td>2,00,000</td><td></td><td></td></tr><tr><td></td><td>2,35,000</td><td></td><td></td></tr><tr><td>(-) Closing Inventory of Raw Materials</td><td>25,000</td><td></td><td></td></tr><tr><td>Cost of Raw Materials Consumed</td><td></td><td>2,10,000</td><td></td></tr><tr><td>Direct Labor</td><td></td><td>1,20,000</td><td></td></tr><tr><th>Prime Cost</th><td></td><td></td><td>3,30,000</td></tr><tr><td>(+) Factory Overhead</td><td></td><td></td><td>75,000</td></tr><tr><th>Cost of Production</th><td></td><td></td><td>4,05,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Income Statement.",
            "answer": "<table><tr><th>Particulars</th><th>Tk.</th><th>Tk.</th></tr><tr><td>Sales</td><td></td><td>8,00,000</td></tr><tr><th>(-) Cost of Goods Sold:</th><td></td><td></td></tr><tr><td>Cost of Production</td><td>4,05,000</td><td></td></tr><tr><td>(+) Opening Inventory of Finished Goods</td><td>50,000</td><td></td></tr><tr><td></td><td>4,55,000</td><td></td></tr><tr><td>(-) Closing Inventory of Finished Goods</td><td>90,000</td><td>3,65,000</td></tr><tr><th>Gross Profit</th><td></td><td>4,35,000</td></tr><tr><th>(-) Operating Expenses:</th><td></td><td></td></tr><tr><td>Administrative Overhead</td><td>35,000</td><td></td></tr><tr><td>Selling Overhead</td><td>1,10,000</td><td>1,45,000</td></tr><tr><th>Net Profit</th><td></td><td>2,90,000</td></tr></table><p><i>Calculation of Closing Finished Goods:</i><br>Value = (Cost of Production / Production Units) &times; Closing Units<br>= (4,05,000 / 45,000) &times; 10,000 = Tk. 90,000</p>"
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
