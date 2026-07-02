import json

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

gen_count = content.count('"status": "generated"')
pen_count = content.count('"status": "pending"')

print(f"Generated images: {gen_count}")
print(f"Pending images: {pen_count}")
print(f"Total images: {gen_count + pen_count}")
