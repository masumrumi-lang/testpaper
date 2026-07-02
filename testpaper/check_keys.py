with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read(200000)
    print(f"cqData in content: {'cqData' in content}")
    print(f"fullCQData in content: {'fullCQData' in content}")
    print(f"shortCQData in content: {'shortCQData' in content}")
    
    # Let's find where acc1 chapter 1 ends and see the keys
    start = content.find('"acc1":')
    if start != -1:
        chapter1 = content.find('"1":', start)
        if chapter1 != -1:
            end = content.find('"2":', chapter1)
            if end == -1: end = chapter1 + 5000
            print(f"Sample structure for acc1 ch 1:\n{content[chapter1:end]}")
