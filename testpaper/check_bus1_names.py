with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus1_idx = content.find('"bus1"')
start_brace = content.find('{', bus1_idx)

# Find first few chapterNames inside bus1
import re
ch_names = re.findall(r'"chapterName"\s*:\s*"([^"]+)"', content[start_brace:start_brace+100000])
print("Chapter names in bus1:", ch_names)
