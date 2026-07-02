with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find the occurrences of "bus2"
bus2_indices = []
idx = -1
while True:
    idx = content.find('"bus2"', idx + 1)
    if idx == -1:
        break
    bus2_indices.append(idx)
print("All indices of 'bus2':", bus2_indices)

for b_idx in bus2_indices:
    print(f"\n--- OCCURRENCE OF 'bus2' AT {b_idx} ---")
    print(content[b_idx:b_idx+300])

# Let's write a parser that checks braces for the entire data.js
brace_stack = []
bracket_stack = []
in_string = False
escape_next = False

for pos, ch in enumerate(content):
    if escape_next:
        escape_next = False
        continue
    if ch == '\\':
        escape_next = True
        continue
    if ch == '"':
        in_string = not in_string
        continue
    if in_string:
        continue
    
    if ch == '{':
        brace_stack.append(pos)
    elif ch == '}':
        if brace_stack:
            brace_stack.pop()
        else:
            print(f"Extra closing brace at position {pos}: {repr(content[pos-50:pos+50])}")
    elif ch == '[':
        bracket_stack.append(pos)
    elif ch == ']':
        if bracket_stack:
            bracket_stack.pop()
        else:
            print(f"Extra closing bracket at position {pos}: {repr(content[pos-50:pos+50])}")

print(f"\nFinal brace stack size: {len(brace_stack)}")
print(f"Final bracket stack size: {len(bracket_stack)}")
if brace_stack:
    print("Unclosed braces starting at:", brace_stack[:10])
