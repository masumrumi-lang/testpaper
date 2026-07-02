import re

def inspect_original():
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'["\']fin1["\']:\s*\{', content)
    if not match:
        print("fin1 not found")
        return
    
    start = match.start()
    ch2_match = re.search(r'["\']2["\']:\s*\{', content[start:])
    if ch2_match:
        ch2_start = start + ch2_match.start()
        # Find the end of this chapter block
        brace_count = 0
        ch2_end = -1
        for i in range(ch2_start, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    ch2_end = i + 1
                    break
        
        ch2_content = content[ch2_start:ch2_end]
        print(f"Chapter 2 keys: {re.findall(r'\"(\w+)\":', ch2_content)}")
        print(f"Chapter 2 snippet (end): {ch2_content[-200:]}")

if __name__ == "__main__":
    inspect_original()
