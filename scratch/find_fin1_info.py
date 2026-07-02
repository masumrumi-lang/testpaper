import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for "fin1" in data.js
matches = list(re.finditer(r'"fin1"\s*:\s*\{', content))
print(f"Matches for 'fin1': {len(matches)}")
for m in matches:
    start = m.start()
    print(f"Match found at char position {start}")
    # Print 500 characters around this position
    start_print = max(0, start - 100)
    end_print = min(len(content), start + 800)
    print("--- CONTEXT ---")
    print(content[start_print:end_print])
    print("----------------")
