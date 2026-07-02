with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check CQ1 journal area for any remaining unescaped quotes
idx = content.find('Mr. Kawsar')
snippet = content[idx:idx+3000]

# Find all ditto mark patterns
import re

# Look for the pattern: >SOMETHING &ndash;31
for m in re.finditer(r">.{0,10}&ndash;31", snippet):
    start = m.start()
    print(f"Found at offset {start}: {repr(snippet[start:start+30])}")

print()
print("--- Checking for unescaped double quotes ---")
# Look for >" pattern (unescaped quote that would break JS)
for m in re.finditer(r'>".{0,5}&ndash;', snippet):
    start = m.start()
    print(f"BROKEN at offset {start}: {repr(snippet[start:start+30])}")

# Also check what's around the &quot; 
for m in re.finditer(r'&quot;.{0,5}&ndash;', snippet):
    start = m.start()
    print(f"OK at offset {start}: {repr(snippet[start:start+30])}")

print()
print("--- Check overall file for unescaped ditto marks ---")
# Global check: find >" &ndash; which would be broken
broken = [(m.start(), content[m.start()-20:m.start()+30]) for m in re.finditer(r'>"[\s]*&ndash;', content)]
print(f"Total broken ditto marks in file: {len(broken)}")
for pos, ctx in broken:
    print(f"  at {pos}: {repr(ctx)}")
