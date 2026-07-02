def check_syntax():
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if braces are balanced
    stack = []
    for i, char in enumerate(content):
        if char == '{':
            stack.append(i)
        elif char == '}':
            if not stack:
                print(f"Extra closing brace at {i}")
                return
            stack.pop()
    
    if stack:
        print(f"Unclosed opening braces at: {stack}")
    else:
        print("Braces are balanced")

if __name__ == "__main__":
    check_syntax()
