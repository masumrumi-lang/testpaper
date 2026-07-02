import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
ch2_idx = content.find('"2":', start_idx)
full_cq_idx = content.find('fullCQData: [', ch2_idx)
bracket_start = content.find('[', full_cq_idx)
bracket_count = 1
end_bracket = -1
for i in range(bracket_start + 1, len(content)):
    if content[i] == '[':
        bracket_count += 1
    elif content[i] == ']':
        bracket_count -= 1
        if bracket_count == 0:
            end_bracket = i
            break

array_str = content[bracket_start:end_bracket+1]

# Try to make it valid JSON
# Replace keys without quotes with quoted keys
array_str = re.sub(r'([a-zA-Z0-9_]+)\s*:', r'"\1":', array_str)
# Remove single quotes for HTML and convert them? No, inside string literals single quotes are fine in JSON.
# Wait, let's just write this string to a test file and use node to parse it!

with open('test.json', 'w', encoding='utf-8') as f:
    f.write(array_str)
print("Saved to test.json")
