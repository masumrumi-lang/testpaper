with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check CQ1 area
idx = content.find('Mr. Kawsar')
print('CQ1 found at:', idx)
if idx > 0:
    snippet = content[idx:idx+3000]
    good = snippet.count('&quot; &ndash;')
    print(f'Properly escaped ditto marks in CQ1: {good}')

# Check CQ3 area
idx2 = content.find('Khan Ltd. &mdash;')
print('CQ3 found at:', idx2)
if idx2 > 0:
    snippet2 = content[idx2:idx2+3000]
    good2 = snippet2.count('&quot; &ndash;')
    print(f'Properly escaped ditto marks in CQ3: {good2}')

# Overall check - any JS parse issues around fullCQData
# Check chapter 8 fullCQData loads
ch8_start = content.find('fullCQData:', content.find("'acc1_ch8'"))
if ch8_start > 0:
    print(f'Chapter 8 fullCQData found at position {ch8_start}')
else:
    print('WARNING: Could not find ch8 fullCQData')
