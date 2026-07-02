with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Ahnaf Traders
idx = content.find('Ahnaf Traders')
if idx != -1:
    print(content[idx:idx+800])
