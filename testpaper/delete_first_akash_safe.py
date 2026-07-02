with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find("Akash Company Ltd.")
if idx != -1:
    start_idx = content.rfind('{', 0, idx)
    
    next_idx = content.find("Akash Company Ltd.", idx + 1)
    if next_idx != -1:
        start_idx_2 = content.rfind('{', 0, next_idx)
        
        print(f"Deleting from {start_idx} to {start_idx_2}")
        print("Content to delete:")
        print(content[start_idx:start_idx_2])
        
        # Perform deletion
        new_content = content[:start_idx] + content[start_idx_2:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success")
    else:
        print("Second occurrence not found")
else:
    print("First occurrence not found")
