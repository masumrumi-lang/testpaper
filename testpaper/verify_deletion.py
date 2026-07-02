with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f'acc2_ch4_cq1 found: {"acc2_ch4_cq1" in content}')
    idx = content.find('"acc2":')
    if idx != -1:
        print("acc2 section start:")
        print(content[idx:idx+500])
