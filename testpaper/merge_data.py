import json
import os

js_path = 'c:/Users/BMTF/.antigravity/testpaper/data.js'
json_path = 'c:/Users/BMTF/.antigravity/testpaper/agr1_data.json'

with open(json_path, 'r', encoding='utf-8') as f:
    agr1_data = json.load(f)

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read().strip()

# Remove the trailing '};'
if js_content.endswith('};'):
    js_content = js_content[:-2].strip()

# The JSON from agr1_data needs to be inserted as "agr1": { ... }
# Ensure we add a comma if the previous entry exists
if not js_content.endswith('{'):
    js_content += ','

# Convert agr1_data to JS object string
agr1_js = '"agr1": ' + json.dumps(agr1_data, indent=4, ensure_ascii=False)

# Append and close the object
final_content = js_content + "\n    " + agr1_js + "\n};"

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Successfully merged agr1 data into data.js")
