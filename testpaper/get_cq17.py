import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')
idx_cq17 = c.find('"id": "17"', idx_bus2)
start = c.rfind('{', 0, idx_cq17)
end = c.find('    }', idx_cq17) + 5

with open('cq17_out.txt', 'w', encoding='utf-8') as fout:
    fout.write(c[start:end])
