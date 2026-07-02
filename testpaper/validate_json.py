import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's extract exactly the array we replaced
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

# Now let's try to parse it as JSON by replacing all unquoted keys with double quotes
# and removing any trailing commas
def fix_json(s):
    # Quote keys
    s = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)\s*:', r'\1"\2":', s)
    # Remove trailing commas
    s = re.sub(r',\s*([}\]])', r'\1', s)
    return s

json_str = fix_json(array_str)

import json
try:
    data = json.loads(json_str)
    print("Parsed perfectly! Length:", len(data))
except Exception as e:
    print("JSON Error:", e)
    # Give context around the error
    import traceback
    err_str = str(e)
    # Usually says "char 1234"
    match = re.search(r'char (\d+)', err_str)
    if match:
        pos = int(match.group(1))
        print("Context around error:")
        print(json_str[max(0, pos-100):pos+100])
