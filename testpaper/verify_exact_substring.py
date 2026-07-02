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

# Chapter 3 block ends at ch3_block_end
# Let's find the start of "bus1" key after ch3_block_end
bus1_idx = content.find('"bus1"', ch3_block_end)

print("ch3_block_end:", ch3_block_end)
print("bus1_idx:", bus1_idx)
substring = content[ch3_block_end:bus1_idx]
print("Length of substring between them:", len(substring))
print("Start of substring (first 50 chars):", repr(substring[:50]))
print("End of substring (last 50 chars):", repr(substring[-50:]))
