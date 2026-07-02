with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for various possible chapter 8 accounting keys
patterns = ['acc1_ch8', 'acc1_8', 'chapter_8', 'ch_8', 'acc_1_8', 'acc1ch8']
for p in patterns:
    idx = content.find(p)
    if idx >= 0:
        print(f'Found "{p}" at {idx}')
        print(repr(content[idx-30:idx+50]))
    
# Also search around "Depreciation" which is ch8 topic
idx = content.find('Depreciation')
print(f'\n"Depreciation" at: {idx}')
if idx > 0:
    print(repr(content[max(0,idx-100):idx+50]))

# Search for how chapters are keyed
import re
keys = re.findall(r"'(acc1_ch\d+)'", content)
unique_keys = sorted(set(keys))
print(f'\nAll acc1 chapter keys found: {unique_keys}')
