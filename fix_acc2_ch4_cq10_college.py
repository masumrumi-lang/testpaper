with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the specific part for CQ10
target_drawings = '"Goods Drawings (shown as 8,000 in source)"'
target_val = '<td>8,000</td>'
target_totals = '<th>Total</th><th>84,000</th><th>Total</th><th>88,000</th>'

# New values
new_drawings = '"Goods Drawings"'
new_val = '<td>4,000</td>'
new_totals = '<th>Total</th><th>84,000</th><th>Total</th><th>84,000</th>'

# Perform replacements
content = content.replace('Goods Drawings (shown as 8,000 in source)', 'Goods Drawings')
content = content.replace('<td>8,000</td>', '<td>4,000</td>', 2) # There are two instances in the file (one in solutions, one in tables)
content = content.replace('<th>Total</th><th>84,000</th><th>Total</th><th>88,000</th>', '<th>Total</th><th>84,000</th><th>Total</th><th>84,000</th>', 2)

# Remove the note
note = '<p><i>(Note: The source image shows Goods Drawings as 8,000 and the credit total as 88,000, but the divisible profit of 44,600 was calculated using 4,000 as drawings. The table reproduces the visual numbers from the source.)</i></p>'
content = content.replace(note, '')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Success")
