with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '"answer": "<table><tr><th>Particulars</th><th>Calculation</th><th>Amount (Tk.)</th></tr><tr><td>Premium amount</td><td>1,60,000 &times; 1</td><td>1,60,000</td></tr></table>"'
replacement = '"answer": "<p>Premium amount = Allotted shares &times; Premium per share = 1,60,000 &times; 1 = Tk. 1,60,000</p>"'

if target in content:
    new_content = content.replace(target, replacement)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Error: Target not found")
