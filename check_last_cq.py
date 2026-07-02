with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '"chapterName": "Chapter 4: Capital of Joint Stock Companies",'
idx = content.find(target)
if idx != -1:
    cq_idx = content.find('"fullCQData": [', idx)
    if cq_idx != -1:
        close_idx = content.find('\n            ]', cq_idx)
        if close_idx != -1:
            print("Found Chapter 4 fullCQData.")
            # Print the last 1000 characters before the closing bracket
            start = max(cq_idx, close_idx - 2000)
            print(content[start:close_idx + 100])
        else:
            print("Closing bracket not found")
    else:
        print("fullCQData not found")
else:
    print("Chapter 4 not found")
