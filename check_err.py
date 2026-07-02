with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

id2_idx = content.find('id: 2,')
b_label = content.find('label: "b"', id2_idx)
ans_start = content.find('answer:', b_label)

print(content[ans_start:ans_start+100])
