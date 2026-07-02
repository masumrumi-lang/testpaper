import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
if bus2_idx != -1:
    # Print 500 characters after "5": to see how chapter 5 is structured
    ch5_idx = content.find('"5":', bus2_idx)
    if ch5_idx != -1:
        print("Chapter 5 block start:")
        print(content[ch5_idx:ch5_idx+1000])
    else:
        print("Chapter 5 not found")
else:
    print("bus2 not found")
