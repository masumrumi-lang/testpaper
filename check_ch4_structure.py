with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '"chapterName": "Chapter 4: Capital of Joint Stock Companies",'
idx = content.find(target)
if idx != -1:
    # Print the next 1000 characters to see the structure
    print(content[idx:idx+1000])
else:
    print("Not found")
