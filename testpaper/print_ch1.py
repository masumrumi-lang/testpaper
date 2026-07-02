with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

ch1_start = content.find('"1": {')
ch2_start = content.find('"2": {')

if ch1_start != -1 and ch2_start != -1:
    ch1_content = content[ch1_start:ch2_start]
    with open('ch1_out.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(ch1_content)
