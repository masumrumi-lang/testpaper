with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

ch3_idx = content.find('"Chapter 3 : Planning"')
ch3_block_start = content.rfind('{', 0, ch3_idx)
bracket = 0
ch3_block_end = -1
for i in range(ch3_block_start, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            ch3_block_end = i+1
            break

print("--- END OF CHAPTER 3 CONTEXT ---")
print(content[ch3_block_end-100:ch3_block_end+1500])
