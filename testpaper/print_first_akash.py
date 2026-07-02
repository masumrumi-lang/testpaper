with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("Akash Company Ltd.")
if idx != -1:
    # Find the start of the object
    start_idx = content.rfind('{', 0, idx)
    # Find the end of the object
    # This is tricky because of nested objects (solutions, questions).
    # Let's just find the next `"id": 30` or the end of the file to see where the next one starts.
    next_idx = content.find("Akash Company Ltd.", idx + 1)
    
    print(f"First block starts at {start_idx}")
    print(f"Next block starts at {next_idx}")
    
    # Let's print the content between them to see where the first block ends.
    print(content[start_idx:next_idx])
else:
    print("Not found")
