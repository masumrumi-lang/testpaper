import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('fin2_block_extracted.json', 'r', encoding='utf-8') as f:
    block_content = f.read()

json_str = block_content.split(':', 1)[1].strip()
fin2_data = json.loads(json_str)

for ch_num in sorted(fin2_data.keys(), key=int):
    ch_data = fin2_data[ch_num]
    print(f"Chapter {ch_num}: {ch_data.get('chapterName')}")
