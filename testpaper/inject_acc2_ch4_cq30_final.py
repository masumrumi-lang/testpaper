import json

new_cq = {
    "id": 30,
    "stem": "<p>Akash Company Ltd. was registered with an authorized capital of Tk. 80,00,000, divided into 8,00,000 shares of Tk. 10 each. The company issued 6,00,000 shares for sale at a 10% discount. Applications for 6,50,000 shares were received. The excess application money was refunded and the issued shares were allotted duly. Underwriter's commission was charged at Tk. 0.10 per share and bank charge at Tk. 0.06 per share.</p>",
    "meta": "Sylhet Board · 2024",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the total amount of underwriter's commission and bank charge.",
            "answer": "<table><tr><th>Particulars</th><th>Details (Tk.)</th><th>Amount (Tk.)</th></tr><tr><td>Underwriter's Commission (6,00,000 &times; 0.10)</td><td>60,000</td><td></td></tr><tr><td>Bank Charge (6,00,000 &times; 0.06)</td><td>36,000</td><td></td></tr><tr><th>Total</th><td></td><td>96,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (Explanation not required).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>58,50,000</td><td>58,50,000</td></tr><tr><td></td><td>Share Application Account<br>Share Discount Account<br>To Share Capital Account<br>To Bank Account</td><td></td><td>58,50,000<br>6,00,000</td><td>60,00,000<br>4,50,000</td></tr><tr><td></td><td>Underwriter's Commission Account<br>Bank Charge Account<br>To Bank Account</td><td></td><td>60,000<br>36,000</td><td>96,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td><td></td></tr><tr><td>Current Assets: Bank Deposit</td><td></td><td></td><td>53,04,000</td></tr><tr><th>Fictitious Assets:</th><td></td><td></td><td></td></tr><tr><td>Share Discount</td><td></td><td>6,00,000</td><td></td></tr><tr><td>Underwriter's Commission</td><td></td><td>60,000</td><td></td></tr><tr><td>Bank Charge</td><td></td><td>36,000</td><td>6,96,000</td></tr><tr><th>Total Assets</th><td></td><td></td><td>60,00,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td><td></td></tr><tr><th>Authorized Capital:</th><td></td><td></td><td></td></tr><tr><td>8,00,000 shares of Tk. 10 each</td><td></td><td></td><td>80,00,000</td></tr><tr><th>Issued and Subscribed Capital:</th><td></td><td></td><td></td></tr><tr><td>6,00,000 shares of Tk. 10 each</td><td></td><td></td><td>60,00,000</td></tr><tr><th>Paid-up Capital:</th><td></td><td></td><td></td></tr><tr><td>6,00,000 shares of Tk. 10 each</td><td></td><td></td><td>60,00,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td></td><td>60,00,000</td></tr></table>"
        }
    ]
}

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Since I am running this again, the file already has a CQ30.
# I need to find the existing CQ30 and replace it, or just append it again if I can't easily replace it.
# Actually, the previous run appended it. If I run it again, it will append ANOTHER CQ30.
# Let's write a script that replaces the existing CQ30 if found, or appends it.
# Or I can just read the file, find the last `}` before the closing bracket of `fullCQData`, and replace the content.
# Let's find `"id": 30` in the file.

idx = content.find('"id": 30')
if idx != -1:
    # Found existing CQ30. Let's find its start and end.
    # It should start with `{` some lines before.
    # Let's just find the start of the object.
    start_idx = content.rfind('{', 0, idx)
    # Let's find the end of the object.
    # It should end with `}` followed by `,` or `\n            ]`.
    end_idx = content.find('}', idx)
    
    # This might be tricky if there are nested objects.
    # Let's use a simpler approach: just find the target block and replace it.
    # Or I can just delete the last appended block if I know it was the last one.
    # Let's just look for the last `}` before the closing bracket of the array.
    
target = '"chapterName": "Chapter 4: Capital of Joint Stock Companies",'
ch_idx = content.find(target)
if ch_idx != -1:
    cq_idx = content.find('"fullCQData": [', ch_idx)
    if cq_idx != -1:
        close_idx = content.find('\n            ]', cq_idx)
        if close_idx != -1:
            # Let's find the start of the last object in the array.
            last_comma = content.rfind(',', cq_idx, close_idx)
            if last_comma != -1:
                # The last object starts after this comma (or it's the only object).
                # Let's check if the last object is indeed CQ30.
                if '"id": 30' in content[last_comma:close_idx]:
                    print("Found existing CQ30 at the end. Replacing it.")
                    json_str = json.dumps(new_cq, indent=4, ensure_ascii=False)
                    lines = json_str.split('\n')
                    indented_lines = ['                    ' + line for line in lines]
                    formatted_json = '\n'.join(indented_lines)
                    
                    new_content = content[:last_comma] + ',\n' + formatted_json + content[close_idx:]
                    with open('data.js', 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print("Success - Replaced")
                else:
                    print("Last object is not CQ30. Appending new one.")
                    # Fallback to append
                    json_str = json.dumps(new_cq, indent=4, ensure_ascii=False)
                    lines = json_str.split('\n')
                    indented_lines = ['                    ' + line for line in lines]
                    formatted_json = '\n'.join(indented_lines)
                    new_val = ',\n' + formatted_json
                    new_content = content[:close_idx] + new_val + content[close_idx:]
                    with open('data.js', 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print("Success - Appended")
            else:
                print("No comma found. Array might be empty or have one item.")
                # If it's the only item, we can just replace the whole content between brackets.
                # But let's assume it's not the case here.
                pass
else:
    print("Error: Target not found")
