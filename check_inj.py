with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
ch2_idx = content.find('"2":', start_idx)
full_cq_idx = content.find('fullCQData: [', ch2_idx)

if full_cq_idx != -1:
    end_idx = content.find('"3": {', ch2_idx)
    snippet = content[full_cq_idx:full_cq_idx+20000] if end_idx == -1 else content[full_cq_idx:end_idx]
    
    id2_idx = snippet.find('id: 2,')
    if id2_idx != -1:
        print('Context around id: 2:')
        print(snippet[max(0, id2_idx-200):id2_idx+200])
    else:
        print('id: 2 not found in snippet')
