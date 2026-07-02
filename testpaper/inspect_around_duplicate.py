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

print("=== TRANSITION REGION ===")
bus1_idx = content.find('"bus1"', ch3_block_end)
print("bus1 starts at:", bus1_idx)
text = content[ch3_block_end-100:bus1_idx+200]
safe_text = repr(text).encode('ascii', 'backslashreplace').decode('ascii')
print(safe_text)
