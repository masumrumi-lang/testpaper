import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

acc1_start = content.find('"acc1": {')
fin1_start = content.find('"fin1": {')

if acc1_start != -1 and fin1_start != -1:
    acc1_content = content[acc1_start:fin1_start]
    for ch in range(1, 11):
        ch_str = f'"{ch}": {{'
        ch_pos = acc1_content.find(ch_str)
        if ch_pos != -1:
            fullcq_pos = acc1_content.find('fullCQData: [', ch_pos)
            if fullcq_pos != -1:
                end_pos = acc1_content.find(']', fullcq_pos)
                if end_pos - fullcq_pos > 20:
                    print(f'Chapter {ch} fullCQData length roughly: {end_pos - fullcq_pos} chars')
                else:
                    print(f'Chapter {ch} fullCQData is EMPTY []')
