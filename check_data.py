with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('"answer": "Data:')
if idx != -1:
    print(repr(content[idx:idx+200]))
else:
    print("Not found")
