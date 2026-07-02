import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_bus2 = c.find('"bus2":')
idx_cq16 = c.find('"id": "16"', idx_bus2)
start = c.rfind('{', 0, idx_cq16)
end = c.find('    }', idx_cq16) + 5

with open('cq16_out.txt', 'w', encoding='utf-8') as fout:
    fout.write(c[start:end])
