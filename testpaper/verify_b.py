with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    idx = content.find('acc2_ch4_cq1')
    if idx != -1:
        start = content.find('"label": "b"', idx)
        if start != -1:
            print(content[start:start+2000])
