import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find start of "agr1":
match = re.search(r'"agr1"\s*:\s*\{', content)
if not match:
    print("agr1 not found")
    exit()

start_pos = match.start()
print("agr1 starts at index:", start_pos)

# Find the closing brace of agr1 block
# We count matching braces starting from the opening brace
brace_start = content.find('{', start_pos)
brace_count = 0
end_pos = -1
for i in range(brace_start, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_pos = i + 1
            break

print("agr1 ends at index:", end_pos)
print("Snippet after agr1 ends:")
print(repr(content[end_pos:end_pos+200]))
