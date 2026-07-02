with open('data.js', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'Chapter 4: Capital of Joint Stock Companies' in line:
            print(f"Found at line {i}: {line.strip()}")
            break
    else:
        print("Not found")
