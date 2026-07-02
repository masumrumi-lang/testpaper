import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

bus2_idx = content.find('"bus2":')
print(f"bus2_idx: {bus2_idx}")

if bus2_idx != -1:
    ch2_match = re.search(r'"2":\s*\{', content[bus2_idx:])
    if ch2_match:
        ch2_start = bus2_idx + ch2_match.start()
        print(f"ch2_start: {ch2_start}")
        
        # let's extract chapter 2 block
        bracket_count = 0
        ch2_end = -1
        for i in range(ch2_start, len(content)):
            if content[i] == '{': bracket_count += 1
            elif content[i] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    ch2_end = i + 1
                    break
                    
        ch2_block = content[ch2_start:ch2_end]
        
        short_match = re.search(r'shortCQData\s*:\s*\[', ch2_block)
        if short_match:
            s_start = short_match.end() - 1
            s_count = 0
            s_end = -1
            for i in range(s_start, len(ch2_block)):
                if ch2_block[i] == '[': s_count += 1
                elif ch2_block[i] == ']':
                    s_count -= 1
                    if s_count == 0:
                        s_end = i + 1
                        break
            print("shortCQData found in bus2 chapter 2:")
            print(ch2_block[s_start:s_end][:500])
            print("Length of shortCQData array:", len(ch2_block[s_start:s_end]))
        else:
            print("shortCQData not found in bus2 chapter 2")
            
        full_match = re.search(r'fullCQData\s*:\s*\[', ch2_block)
        if full_match:
            print("fullCQData found in bus2 chapter 2")
        else:
            print("fullCQData NOT found in bus2 chapter 2")
    else:
        print("bus2 chapter 2 not found")
