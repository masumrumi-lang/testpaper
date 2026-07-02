import re

def verify_injection():
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'["\']fin1["\']:\s*\{', content)
    if not match:
        print("fin1 not found")
        return
    
    start = match.start()
    for ch in ['2', '5', '7']:
        ch_match = re.search(r'["\']' + ch + r'["\']:\s*\{', content[start:])
        if ch_match:
            ch_start = start + ch_match.start()
            # Find the end of this chapter block
            brace_count = 0
            ch_end = -1
            for i in range(ch_start, len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        ch_end = i + 1
                        break
            
            ch_content = content[ch_start:ch_end]
            print(f"--- Chapter {ch} ---")
            print(f"Has shortCQData: {'shortCQData' in ch_content}")
            print(f"Has fullCQData: {'fullCQData' in ch_content}")
            print(f"Length of content: {len(ch_content)}")
            # Print a snippet of fullCQData
            f_idx = ch_content.find('fullCQData')
            if f_idx != -1:
                print(ch_content[f_idx:f_idx+200])

if __name__ == "__main__":
    verify_injection()
