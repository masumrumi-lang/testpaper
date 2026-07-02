import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
end_idx = content.find('"fin1":', start_idx)

acc1_content = content[start_idx:end_idx]
chapters = re.findall(r'"(\d+)":\s*\{', acc1_content)
print("acc1 chapters:", chapters)
