with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check the structure around acc1_ch8
idx = content.find('acc1_ch8')
print(f'acc1_ch8 found at: {idx}')
if idx > 0:
    print(repr(content[idx-50:idx+200]))

# Try to validate JS syntax by checking balanced braces/brackets around ch8
# Find fullCQData near ch8
idx2 = content.find('fullCQData', idx)
print(f'\nfullCQData after ch8 at: {idx2}')
if idx2 > 0:
    print(repr(content[idx2-20:idx2+100]))

# Check if the file can be parsed as JS at all
# Quick check: count opening vs closing braces in the first part
total_open = content.count('{')
total_close = content.count('}')
print(f'\nTotal {{ : {total_open}')
print(f'Total }} : {total_close}')
print(f'Balanced: {total_open == total_close}')

total_open_sq = content.count('[')
total_close_sq = content.count(']')
print(f'Total [ : {total_open_sq}')
print(f'Total ] : {total_close_sq}')
print(f'Balanced: {total_open_sq == total_close_sq}')
