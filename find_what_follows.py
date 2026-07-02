with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find "2" absolute start
start_pos = 5209330
bracket = 0
end_pos = -1
# Tracing braces
for i in range(start_pos, len(content)):
    if content[i] == '{': bracket += 1
    elif content[i] == '}':
        bracket -= 1
        if bracket == 0:
            end_pos = i+1
            break

print("Chapter 2 starting at 5209330 ends at:", end_pos)
print("Content after Chapter 2 (next 1000 chars):")
print(content[end_pos:end_pos+1000])
