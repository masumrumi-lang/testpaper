with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find the database structure keys
keys = re.findall(r"['\"]([a-zA-Z0-9_]+)['\"]:\s*\{", content[:5000])
print("Top-level keys (first 5000 chars):", keys[:20])

# Search for subject/chapter patterns
patterns_found = re.findall(r"subject.*?['\"]([^'\"]+)['\"]", content[:5000])
print("Subject patterns:", patterns_found[:10])

# Just show the first 2000 chars of the file
print("\n=== First 2000 chars ===")
print(content[:2000])
