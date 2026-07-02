with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

target = '"chapterName": "Chapter 4: Capital of Joint Stock Companies",'
idx = content.find(target)
if idx != -1:
    cq_idx = content.find('"fullCQData": [', idx)
    if cq_idx != -1:
        close_idx = content.find('\n            ]', cq_idx)
        if close_idx != -1:
            chapter_content = content[cq_idx:close_idx]
            if '"id": 31' in chapter_content:
                print("CQ31 found in Chapter 4.")
                # Let's find its index to see if we can delete it.
                id_idx = chapter_content.find('"id": 31')
                print(f"Index of id: 31 is {id_idx}")
            else:
                print("CQ31 not found in Chapter 4.")
        else:
            print("Closing bracket not found")
    else:
        print("fullCQData not found")
else:
    print("Chapter 4 not found")
