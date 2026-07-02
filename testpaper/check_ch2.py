with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
if start_idx == -1:
    print('acc1 not found')
else:
    ch2_idx = content.find('"2":', start_idx)
    if ch2_idx != -1:
        full_cq_idx = content.find('fullCQData: [', ch2_idx)
        end_ch2 = content.find('"3":', ch2_idx)
        if full_cq_idx != -1 and (end_ch2 == -1 or full_cq_idx < end_ch2):
            snippet = content[full_cq_idx:full_cq_idx+2000]
            print('fullCQData snippet:')
            print(snippet)
        else:
            print('No fullCQData found in Chapter 2')
    else:
        print('Chapter 2 not found')
