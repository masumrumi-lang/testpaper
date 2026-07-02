with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('"acc1":')
ch2_idx = content.find('"2":', start_idx)
full_cq_idx = content.find('fullCQData: [', ch2_idx)
print(content[full_cq_idx:full_cq_idx+100])
