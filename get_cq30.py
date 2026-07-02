import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')

idx_cq = c.find(f'"id": "30"', idx_bus2)
if idx_cq != -1:
    start = c.rfind('{', 0, idx_cq)
    bracket_count = 0
    end = -1
    for i in range(start, len(c)):
        if c[i] == '{':
            bracket_count += 1
        elif c[i] == '}':
            bracket_count -= 1
            if bracket_count == 0:
                end = i + 1
                break

    with open(f'cq30_out.txt', 'w', encoding='utf-8') as fout:
        fout.write(c[start:end])
else:
    with open(f'cq30_out.txt', 'w', encoding='utf-8') as fout:
        fout.write(f"CQ 30 not found.")
