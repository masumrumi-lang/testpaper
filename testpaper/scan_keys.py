import re

with open("data.js", "r", encoding="utf-8") as f:
    for line in f:
        # Check if line looks like a top-level key
        match = re.match(r'^\s*["\']?([^"\':]+)["\']?:\s*\{', line)
        if match:
            print(match.group(1))
