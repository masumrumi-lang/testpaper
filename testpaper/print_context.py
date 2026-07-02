with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = 5209250
end = 5210000
print(f"Content from {start} to {end}:")
print(content[start:end])
