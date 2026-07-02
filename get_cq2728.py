import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')

for q_id in ["27", "28"]:
    idx_cq = c.find(f'"id": "{q_id}"', idx_bus2)
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

        with open(f'cq{q_id}_out.txt', 'w', encoding='utf-8') as fout:
            fout.write(c[start:end])
    else:
        with open(f'cq{q_id}_out.txt', 'w', encoding='utf-8') as fout:
            fout.write(f"CQ {q_id} not found.")
