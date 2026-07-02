with open('data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for i, line in enumerate(lines):
    if 'FIN1_CH2' in line or 'fin1' in line or 'FIN1' in line:
        out_lines.append(f"Line {i+1}: {line}")

with open('scratch_inspect.txt', 'w', encoding='utf-8') as out:
    out.writelines(out_lines[:200]) # write first 200 matches
print(f"Done, found {len(out_lines)} matches.")
