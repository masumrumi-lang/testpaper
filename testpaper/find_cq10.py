with open('data.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

found = False
for i, line in enumerate(lines):
    if '"id": 10' in line and '"type": "college"' in lines[i+3]: # Assuming type is a few lines below
        print(f"Found at line {i+1}")
        # Print lines around it
        start = max(0, i - 10)
        end = min(len(lines), i + 50)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        found = True
        break
    # Or just search for Sumi
    if 'Sumi and Mimi' in line:
        print(f"Found Sumi at line {i+1}")
        start = max(0, i - 10)
        end = min(len(lines), i + 50)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        found = True
        break

if not found:
    print("Not found")
