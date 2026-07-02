with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The problem: literal " in '>" &ndash;31<' breaks the JS string
# Fix: replace the unescaped " with &quot; entity
old_bad = "'>\" &ndash;31<"
new_fix = "'>&quot; &ndash;31<"

count = content.count(old_bad)
print(f'Found {count} occurrences of unescaped quote in ditto mark')

if count > 0:
    content = content.replace(old_bad, new_fix)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {count} occurrences!')
    
    # Verify no more issues
    remaining = content.count(old_bad)
    print(f'Remaining after fix: {remaining}')
else:
    print('Nothing to fix')
