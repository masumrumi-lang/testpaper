import os

def balance():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    o = content.count('{')
    c = content.count('}')
    print(f"Open: {o}, Close: {c}")
    
    if c > o:
        diff = c - o
        print(f"Removing {diff} extra braces...")
        ict_pos = content.find('"ict": {')
        if ict_pos == -1:
            print("ICT not found")
            return
            
        for _ in range(diff):
            search_area = content[:ict_pos]
            last_brace = search_area.rfind('}')
            if last_brace != -1:
                content = content[:last_brace] + content[last_brace+1:]
                # Update ict_pos after removal
                ict_pos = content.find('"ict": {')
                
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Balanced.")

balance()
