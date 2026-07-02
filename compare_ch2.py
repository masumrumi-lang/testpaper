with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Chapter 2 (inside bus2) starts at 4782371
start_1 = 4782371
bracket = 0
end_1 = -1
for i in range(start_1, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            end_1 = i+1
            break

block_1 = content[start_1:end_1]
print("Block 1 length:", len(block_1))

# Chapter 2 (outside bus2) starts at 5209330
start_2 = 5209330
bracket = 0
end_2 = -1
for i in range(start_2, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            end_2 = i+1
            break

block_2 = content[start_2:end_2]
print("Block 2 length:", len(block_2))

# Check if they are identical or different
if block_1 == block_2:
    print("They are absolutely IDENTICAL!")
else:
    print("They are DIFFERENT!")
    # print first 500 chars of each
    print("\n--- Block 1 First 500 Chars ---")
    print(block_1[:500])
    print("\n--- Block 2 First 500 Chars ---")
    print(block_2[:500])
