with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of "Akash Company Ltd."
idx = 0
while True:
    idx = content.find("Akash Company Ltd.", idx)
    if idx == -1:
        break
    print(f"\nFound 'Akash Company Ltd.' at index {idx}")
    # Print the surrounding lines
    start = max(0, idx - 500)
    end = min(len(content), idx + 500)
    print(content[start:end])
    idx += 1
