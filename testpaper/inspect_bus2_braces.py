with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
print("--- START OF BUS2 ---")
print(content[bus2_idx:bus2_idx+1000])

# Let's search for "Chapter 3 : Planning" and print around it
ch3_idx = content.find('"Chapter 3 : Planning"')
if ch3_idx != -1:
    print("\n--- AROUND CHAPTER 3 ---")
    print(content[ch3_idx-200:ch3_idx+500])
    
    # Also print near the end of Chapter 3 block
    # Chapter 3 starts with { at ch3_idx - 100 or so
    ch3_block_start = content.rfind('{', 0, ch3_idx)
    # let's find the closing brace
    bracket = 0
    ch3_block_end = -1
    for i in range(ch3_block_start, len(content)):
        if content[i] == '{': bracket += 1
        elif content[i] == '}':
            bracket -= 1
            if bracket == 0:
                ch3_block_end = i+1
                break
    print("\n--- END OF CHAPTER 3 ---")
    print(content[ch3_block_end-200:ch3_block_end+200])
