with open('data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Check for common JS string issues
# In the file, strings are wrapped in double quotes "..."
# Inside those strings, any literal " would break it
# The fix_quotes.py already fixed >" &ndash; patterns
# But let's check for other potential issues

# Check lines around where CQ1 and CQ3 answers are
import re

errors = []
for i, line in enumerate(lines):
    # Check for answer lines that might have broken strings
    if 'answer:' in line and 'answer: "' in line:
        # Extract the answer string content
        start_idx = line.find('answer: "') + len('answer: "')
        # Count unescaped quotes within
        in_string = True
        j = start_idx
        while j < len(line):
            ch = line[j]
            if ch == '\\' and j+1 < len(line):
                j += 2  # skip escaped char
                continue
            if ch == '"':
                # This closes the string - check if it's at the right place
                remaining = line[j+1:].strip()
                if remaining and not remaining.startswith(('\n', '\r', '}', ',')):
                    # Potential mid-string break
                    pass
                break
            j += 1

# Simpler check: look for lines with unbalanced quotes in answer strings
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('answer: "'):
        # Count double quotes (not inside HTML entities like &quot;)
        # Remove &quot; entities first
        cleaned = stripped.replace('&quot;', 'XXXX')
        # Remove escaped quotes
        cleaned = cleaned.replace('\\"', 'YY')
        quote_count = cleaned.count('"')
        if quote_count % 2 != 0:
            errors.append((i+1, stripped[:100]))

print(f"\nLines with odd number of quotes: {len(errors)}")
for line_num, preview in errors[:20]:
    print(f"  Line {line_num}: {preview}...")

# Also check: does the file have any null bytes or encoding issues?
with open('data.js', 'rb') as f:
    raw = f.read()
null_count = raw.count(b'\x00')
print(f"\nNull bytes: {null_count}")

# Check around the CQ1 update area for issues
cq1_line = None
for i, line in enumerate(lines):
    if 'Mr. Kawsar' in line:
        cq1_line = i + 1
        break
print(f"\nMr. Kawsar on line: {cq1_line}")
if cq1_line:
    # Show surrounding answer lines
    for j in range(cq1_line-1, min(cq1_line+30, len(lines))):
        if 'answer:' in lines[j]:
            stripped = lines[j].strip()
            cleaned = stripped.replace('&quot;', 'XXXX').replace('\\"', 'YY')
            qcount = cleaned.count('"')
            status = "OK" if qcount % 2 == 0 else "BROKEN"
            print(f"  Line {j+1} [{status}] quotes={qcount}: {stripped[:80]}...")
