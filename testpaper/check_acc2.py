import os

file_path = 'data.js'
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # Read first 100k chars to check structure
        content = f.read(100000)
        print(f"File size: {os.path.getsize(file_path)} bytes")
        print(f"acc1 in first 100k: {'acc1' in content}")
        print(f"acc2 in first 100k: {'acc2' in content}")
        
        # Check for acc2 anywhere
        if 'acc2' not in content:
            f.seek(0)
            full_content = f.read()
            print(f"acc2 in full file: {'acc2' in full_content}")
else:
    print("data.js not found")
