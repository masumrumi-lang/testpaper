import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.rfind('"bus2"')
print("Context around bus2:")
print(repr(c[idx-50:idx+20]))
