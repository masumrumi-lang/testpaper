with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find chapter 8 key
import re

ch8_match = re.search(r'"8"\s*:\s*\{', content)
if ch8_match:
    print(f'Chapter 8 found at position {ch8_match.start()}')
    print(repr(content[ch8_match.start()-50:ch8_match.start()+200]))
else:
    print('Chapter 8 NOT FOUND')
    # Maybe it was broken - search for nearby content
    idx = content.find('Dhaka College')
    print(f'"Dhaka College" at: {idx}')
    if idx > 0:
        # Go backwards to find the chapter definition
        before = content[max(0,idx-2000):idx]
        ch_match = re.search(r'"(\d+)"\s*:\s*\{[^}]*?chapterName', before)
        if ch_match:
            print(f'Found chapter def: {repr(before[ch_match.start():ch_match.start()+200])}')

# Check for the Mr. Kawsar CQ1 - look for syntax errors nearby
idx_k = content.find('Mr. Kawsar')
print(f'\nMr. Kawsar at: {idx_k}')

# Check the answer string is properly terminated
# Find the answer for CQ1 part b
idx_b = content.find('Mr. Kawsar &mdash; Journal')
print(f'CQ1 journal at: {idx_b}')
if idx_b > 0:
    # Find the end of this answer string - look for closing quote + newline
    end_area = content[idx_b:idx_b+3000]
    # Find the pattern: </div>" which closes the answer
    close_idx = end_area.find("</div>\"")
    if close_idx > 0:
        print(f'Answer closes at offset {close_idx}')
        print(f'After close: {repr(end_area[close_idx:close_idx+100])}')
    else:
        print('WARNING: Could not find answer closing!')
        # Check what we have
        all_closes = [m.start() for m in re.finditer(r'</div>', end_area)]
        print(f'All </div> positions: {all_closes[:10]}')
