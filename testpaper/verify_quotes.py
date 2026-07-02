with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for any remaining unescaped " inside answer strings that could break JS
# The pattern is: inside an answer: "..." string, a literal " that's not escaped
# Let's check all occurrences of '>" ' which might be ditto marks
import re

# Find all instances of >" followed by space (potential ditto marks inside strings)
matches = [(m.start(), content[max(0,m.start()-30):m.start()+40]) for m in re.finditer(r"'>\"\s", content)]
print(f'Found {len(matches)} potential unescaped ditto marks')
for i, (pos, ctx) in enumerate(matches):
    print(f'  #{i+1} at {pos}: ...{repr(ctx)}...')
