with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
ch2_idx = content.find('"2":', start_idx)

print("ch2_idx context:")
print(content[ch2_idx-50:ch2_idx+50])
