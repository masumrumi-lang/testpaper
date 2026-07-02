with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The issue: the replacement used literal " which breaks the JS string
# In the replacement, we have: '" &ndash;31' 
# The " terminates the JS string prematurely!

idx = content.find('Khan Ltd. &mdash; Journal')
print('Journal table found at:', idx)

if idx > 0:
    # Show the problem area
    start = max(0, idx - 50)
    end = min(len(content), idx + 2500)
    snippet = content[start:end]
    
    # Find the unescaped double quote
    pos = snippet.find('" &ndash;')
    while pos >= 0:
        print(f'Found unescaped quote at offset {pos}:')
        print(repr(snippet[pos-20:pos+30]))
        pos = snippet.find('" &ndash;', pos+1)
