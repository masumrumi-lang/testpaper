with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
subj_start = content.find('{', bus2_idx)
print("Content of bus2 block first 1500 chars:")
print(content[subj_start:subj_start+1500])
