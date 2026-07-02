with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find "acc2" in the file
idx = content.find('"acc2":')
if idx != -1:
    print("Found acc2")
    # Let's find the keys (chapters) in acc2
    # We can search for '"chapterName":' after "acc2"
    ch_idx = idx
    while True:
        ch_idx = content.find('"chapterName":', ch_idx + 1)
        if ch_idx == -1:
            break
        # Print the chapter name
        end_idx = content.find('\n', ch_idx)
        print(content[ch_idx:end_idx])
else:
    print("acc2 not found")
