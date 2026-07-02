with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The pattern we want to fix:
#             },
#             },
#             {
#                 label: "b",
#                 text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",

bad_snippet = '''            },
            },
            {
                label: "b",
                text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",'''

good_snippet = '''            },
            {
                label: "b",
                text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",'''

if bad_snippet in content:
    content = content.replace(bad_snippet, good_snippet)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed the double '},' syntax error!")
else:
    print("Could not find the exact snippet. Let me search more flexibly.")
    
    # Let's try with regex just in case spaces differ
    import re
    pattern = r'\}\,\s*\}\,\s*\{\s*label:\s*"b",\s*text:\s*"Prepare Dep A/C and Accum Dep A/C for 2023-2024\.",'
    match = re.search(pattern, content)
    if match:
        good = match.group(0).replace('},\n            },', '},', 1)
        # Handle different spacing
        good = re.sub(r'\}\,\s*\}\,', '},', match.group(0), 1)
        content = content[:match.start()] + good + content[match.end():]
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed via regex!")
    else:
        print("Regex also failed to find it.")

