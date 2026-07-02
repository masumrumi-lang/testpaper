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
            import re
            # Simpler regex to find ID and Type
            matches = re.findall(r'"id":\s*(\d+)', chapter_content)
            print(f"Found {len(matches)} IDs")
            for m in matches:
                # Find the type for this ID
                id_idx = chapter_content.find(f'"id": {m}')
                type_idx = chapter_content.find('"type":', id_idx)
                end_type = chapter_content.find('"', type_idx + 9)
                type_val = chapter_content[type_idx+9:end_type]
                print(f"ID: {m}, Type: {type_val}")
        else:
            print("Closing bracket not found")
    else:
        print("fullCQData not found")
else:
    print("Chapter 4 not found")
