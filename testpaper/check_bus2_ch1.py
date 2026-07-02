import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
print(f"bus2_idx: {bus2_idx}")

if bus2_idx != -1:
    ch1_match = re.search(r'"1":\s*\{', content[bus2_idx:])
    if ch1_match:
        ch1_start = bus2_idx + ch1_match.start()
        print(f"ch1_start: {ch1_start}")
        
        bracket_count = 0
        ch1_end = -1
        for i in range(ch1_start, len(content)):
            if content[i] == '{': bracket_count += 1
            elif content[i] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    ch1_end = i + 1
                    break
                    
        ch1_block = content[ch1_start:ch1_end]
        
        short_match = re.search(r'shortCQData\s*:\s*\[', ch1_block)
        if short_match:
            print("shortCQData found in bus2 chapter 1")
        else:
            print("shortCQData not found in bus2 chapter 1")
            
        full_match = re.search(r'fullCQData\s*:\s*\[', ch1_block)
        if full_match:
            print("fullCQData found in bus2 chapter 1")
        else:
            print("fullCQData NOT found in bus2 chapter 1")
    else:
        print("bus2 chapter 1 not found")
