import json

new_cq = {
    "id": 8,
    "stem": "<p>The Trial Balance of National Company Ltd. as of 31st December 2023 was as follows:</p><table><tr><th>Account Name</th><th>Debit (Tk.)</th><th>Account Name</th><th>Credit (Tk.)</th></tr><tr><td>Opening Stock</td><td>60,000</td><td>Ordinary Share Capital (Tk. 10 each)</td><td>100,000</td></tr><tr><td>Purchase</td><td>1,15,000</td><td>10% Preference Share Capital (Tk. 10 each)</td><td>50,000</td></tr><tr><td>Return</td><td>8,000</td><td>Retained Earnings</td><td>96,000</td></tr><tr><td>Import Duty</td><td>19,000</td><td>Accounts Payable</td><td>20,000</td></tr><tr><td>Wages</td><td>10,000</td><td>Sales</td><td>1,84,000</td></tr><tr><td>Salary</td><td>8,000</td><td>General Reserve</td><td>20,000</td></tr><tr><td>Bank Deposit</td><td>16,000</td><td>Return</td><td>6,000</td></tr><tr><td>Machinery</td><td>1,20,000</td><td>Share Premium</td><td>20,000</td></tr><tr><td>Fictitious Assets</td><td>40,000</td><td></td><td></td></tr><tr><td>Leasehold Property (10 years)</td><td>20,000</td><td></td><td></td></tr><tr><td>Commission Receivable</td><td>8,000</td><td></td><td></td></tr><tr><td>Accounts Receivable</td><td>72,000</td><td></td><td></td></tr><tr><th>Total</th><th>4,96,000</th><th>Total</th><th>4,96,000</th></tr></table><p><b>Adjustments:</b><br>(1) Closing stock is valued at Tk. 60,000.<br>(2) 15% VAT is included in both Purchase and Sales.<br>(3) Machinery installation cost of Tk. 4,000 is included in wages. Depreciation of 5% is to be charged on machinery.<br>(4) A check of Tk. 5,000 deposited for collection has been dishonored but not recorded.<br>(5) 5% Provision for Bad Debts is to be maintained on Accounts Receivable.<br>(6) Dividend is to be proposed at Tk. 2 per ordinary share and necessary rate on preference share capital.</p>",
    "meta": "Ideal School and College, Motijheel · 2024",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of proposed dividend.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Ordinary Share Dividend (10,000 &times; 2)</td><td>20,000</td><td></td></tr><tr><td>Preference Share Dividend (50,000 &times; 10%)</td><td>5,000</td><td></td></tr><tr><th>Total Proposed Dividend</th><td></td><td>25,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Determine Gross Profit at the end of the year.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Sales</td><td></td><td>1,84,000</td><td></td></tr><tr><td>(-) Return</td><td></td><td>(8,000)</td><td></td></tr><tr><td></td><td></td><td>1,76,000</td><td></td></tr><tr><td>(-) VAT (1,76,000 &times; 15/115)</td><td></td><td>(22,956)</td><td>1,53,044</td></tr><tr><th>(-) Cost of Goods Sold:</th><td></td><td></td><td></td></tr><tr><td>Opening Stock</td><td></td><td>60,000</td><td></td></tr><tr><td>Purchase</td><td>1,15,000</td><td></td><td></td></tr><tr><td>(-) Return</td><td>(6,000)</td><td></td><td></td></tr><tr><td></td><td>1,09,000</td><td></td><td></td></tr><tr><td>(-) VAT (1,09,000 &times; 15/115)</td><td>(14,218)</td><td>94,782</td><td></td></tr><tr><td>Wages</td><td></td><td>10,000</td><td></td></tr><tr><td>Import Duty</td><td></td><td>19,000</td><td></td></tr><tr><td></td><td></td><td>1,83,782</td><td></td></tr><tr><td>(-) Closing Stock</td><td></td><td>(60,000)</td><td>(1,23,782)</td></tr><tr><th>Gross Profit</th><td></td><td></td><td>29,262</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Determine the amount of Total Assets for the completed year.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Fixed Assets:</th><td></td><td></td></tr><tr><td>Machinery</td><td>1,20,000</td><td></td></tr><tr><td>(+) Installation Cost</td><td>4,000</td><td></td></tr><tr><td></td><td>1,24,000</td><td></td></tr><tr><td>(-) Depreciation (10% used in source solution instead of 5%)</td><td>(12,400)</td><td>1,11,600</td></tr><tr><td>Fictitious Assets</td><td></td><td>40,000</td></tr><tr><td>Leasehold Property (Value as per source solution)</td><td></td><td>2,000</td></tr><tr><th>Total Assets</th><td></td><td>1,53,600</td></tr></table><p><i>(Note: The solution for part (c) contains several inconsistencies with the question's adjustments and trial balance, but has been reproduced as shown in the source image.)</i></p>"
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
