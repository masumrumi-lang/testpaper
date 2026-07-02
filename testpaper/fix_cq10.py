with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Target line content
target = "<td><b>Sumi's Current A/c:</b> Goods Drawings</td><td>8,000</td>"
replacement = "<td><b>Sumi's Current A/c:</b> Goods Drawings</td><td>4,000</td>"

if target in content:
    content = content.replace(target, replacement)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success: Replaced 8,000 with 4,000")
else:
    print("Error: Target not found")
