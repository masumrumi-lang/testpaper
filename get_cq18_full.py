import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')
idx_cq18 = c.find('"id": "18"', idx_bus2)
start = c.rfind('{', 0, idx_cq18)
# Better way to extract the full object
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

with open('cq18_full.txt', 'w', encoding='utf-8') as fout:
    fout.write(c[start:end])
