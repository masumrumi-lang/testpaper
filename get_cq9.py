import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')
idx_cq9 = c.find('"id": "09"', idx_bus2)
start = c.rfind('{', 0, idx_cq9)
end = c.find('    }', idx_cq9) + 5

with open('cq9_out.txt', 'w', encoding='utf-8') as fout:
    fout.write(c[start:end])
