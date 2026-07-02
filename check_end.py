with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('"acc1":')
ch2_idx = content.find('"2":', start_idx)
end_ch2 = content.find('"3": {', ch2_idx)

print(content[end_ch2-200:end_ch2+100])
