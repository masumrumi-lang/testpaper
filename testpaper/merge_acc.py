import re

with open('acc1_ch1_part1.js', 'r', encoding='utf-8') as f:
    part1 = f.read()
with open('acc1_ch1_part2.js', 'r', encoding='utf-8') as f:
    part2 = f.read()
with open('acc1_ch1_part3.js', 'r', encoding='utf-8') as f:
    part3 = f.read()

# Extract just the arrays from the files
def get_array_content(js_code):
    start = js_code.find('[')
    end = js_code.rfind(']')
    return js_code[start+1:end].strip()

arr1 = get_array_content(part1)
arr2 = get_array_content(part2)
arr3 = get_array_content(part3)

combined = '[\n' + arr1 + ',\n' + arr2 + ',\n' + arr3 + '\n            ]'

with open('data.js', 'r', encoding='utf-8') as f:
    data = f.read()

pattern = re.compile(r'(chapterName:\s*"Chapter 1 : Introduction to Accounting",\s*mcqData:\s*)\[[\s\S]*?\],\s*(shortCQData:)', re.MULTILINE)
data = pattern.sub(r'\1' + combined.replace('\\', '\\\\') + r',\n            \2', data)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(data)

print("Merged successfully.")
