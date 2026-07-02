with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
subj_start = content.find('{', bus2_idx)
bracket = 0
subj_end = -1
for i in range(subj_start, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            subj_end = i+1
            break

print("Ending of bus2 block:")
print(content[subj_end-200:subj_end+200])
