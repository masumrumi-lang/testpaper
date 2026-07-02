with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

habib_idx = content.find("Mr. Habib's business")
if habib_idx != -1:
    print("Found Mr. Habib at index", habib_idx)
    # print context
    print(content[max(0, habib_idx-500):habib_idx+500])
else:
    print("Mr. Habib not found in data.js!")
