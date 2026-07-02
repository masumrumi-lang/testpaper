with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'"id":\s*31', content)
print(f"Found {len(matches)} matches for '\"id\": 31'")

matches2 = re.findall(r'id:\s*31', content)
print(f"Found {len(matches2)} matches for 'id: 31'")

# Let's also search for "Akash Company Ltd." again to see if it appears twice.
matches3 = re.findall(r'Akash Company Ltd\.', content)
print(f"Found {len(matches3)} matches for 'Akash Company Ltd.'")
