import json

cq_data = {
    "id": 1,
    "stem": "<p>Heeran Company Ltd. was registered with an authorized capital of Tk. 5,00,000 divided into 50,000 shares of Tk. 10 each. The company issued a prospectus to sell 40,000 shares in the market at a 10% premium. Applications for 50,000 shares were received. The issued shares were duly allotted and the excess application money was refunded to the respective applicants. The company pays a bank charge of Tk. 0.60 per share.</p>",
    "meta": "Dhaka Board · 2025",
    "type": "board",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of share premium per share and total share premium.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th></tr><tr><td>Share premium per share (Tk. 10 &times; 10%)</td><td>1</td></tr><tr><td>Total share premium (40,000 &times; Tk. 1)</td><td>40,000</td></tr></table>"
        },
        {
            "label": "b",
            "text": "Give necessary journal entries (without explanation).",
            "answer": "<table><tr><th>Date</th><th>Particulars</th><th>L.F.</th><th>Debit (Tk.)</th><th>Credit (Tk.)</th></tr><tr><td></td><td>Bank Account<br>To Share Application Account</td><td></td><td>5,50,000</td><td>5,50,000</td></tr><tr><td></td><td>Share Application Account<br>To Share Capital Account<br>To Share Premium Account</td><td></td><td>4,40,000</td><td>4,00,000<br>40,000</td></tr><tr><td></td><td>Share Application Account<br>To Bank Account</td><td></td><td>1,10,000</td><td>1,10,000</td></tr><tr><td></td><td>Bank Charges Account<br>To Bank Account</td><td></td><td>24,000</td><td>24,000</td></tr></table>"
        },
        {
            "label": "c",
            "text": "Prepare the Statement of Financial Position of the company.",
            "answer": "<table><tr><th>Particulars</th><th>Amount (Tk.)</th><th>Amount (Tk.)</th></tr><tr><th>Assets:</th><td></td><td></td></tr><tr><td>Current Assets:</td><td></td><td></td></tr><tr><td>Bank Deposit (5,50,000 - 1,10,000 - 24,000)</td><td></td><td>4,16,000</td></tr><tr><th>Unadjusted Expenses:</th><td></td><td></td></tr><tr><td>Bank Charges</td><td></td><td>24,000</td></tr><tr><th>Total Assets</th><td></td><td>4,40,000</td></tr><tr><th>Shareholders' Equity and Liabilities:</th><td></td><td></td></tr><tr><th>Share Capital:</th><td></td><td></td></tr><tr><td>Authorized Capital:</td><td></td><td></td></tr><tr><td>50,000 shares of Tk. 10 each</td><td></td><td>5,00,000</td></tr><tr><td>Issued, Subscribed and Paid-up Capital:</td><td></td><td></td></tr><tr><td>40,000 shares of Tk. 10 each</td><td></td><td>4,00,000</td></tr><tr><th>Reserves and Surplus:</th><td></td><td></td></tr><tr><td>Share Premium</td><td></td><td>40,000</td></tr><tr><th>Total Equity and Liabilities</th><td></td><td>4,40,000</td></tr></table>"
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
        close_idx = content.find(']', cq_idx)
        inner_content = content[cq_idx + len('"fullCQData": ['):close_idx].strip()
        if inner_content == "":
            json_str = json.dumps(cq_data, indent=4, ensure_ascii=False)
            json_str = json_str.replace('\\n', '<br>') # Ensure multiline strings in JSON are handled if any, but we use strings directly
            # Actually, json.dumps will escape quotes. We want to preserve valid JS if possible, but JSON is safe.
            
            # Let's format it to look like lines in the file
            lines = json_str.split('\n')
            indented_lines = [lines[0]] + ['                ' + line for line in lines[1:]]
            formatted_json = '\n'.join(indented_lines)
            
            new_val = '"fullCQData": [\n                ' + formatted_json + '\n            ]'
            
            new_content = content[:cq_idx] + new_val + content[close_idx+1:]
            
            with open('data.js', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Success")
        else:
            print(f"Error: fullCQData is not empty: '{inner_content}'")
