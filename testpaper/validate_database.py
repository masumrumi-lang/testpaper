import json
import re

def main():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the object from the JS file
    match = re.search(r'const testDatabase = (\{.*\});', content, re.DOTALL)
    if not match:
        # Try without semicolon
        match = re.search(r'const testDatabase = (\{.*\})', content, re.DOTALL)
        
    if not match:
        print("Error: Could not find testDatabase object in data.js")
        # Let's try a simpler way - just check for keywords
        if 'undefined' in content:
            print("Found 'undefined' in data.js!")
        if 'null' in content:
             print("Found 'null' in data.js!")
        return

    # Note: The data.js is NOT strict JSON (unquoted keys), so we can't easily parse with json.loads
    # We'll use string checks for common failure patterns
    
    issues = []
    
    # Check for literal "undefined" or "null" (not as part of other words)
    # Using regex to find word boundaries
    if re.search(r'\bundefined\b', content):
        issues.append("Literal 'undefined' found in database.")
    
    if re.search(r'\bnull\b', content):
        # We need to be careful as null might be a value for shortCQData: [] or similar
        # But in our script we used [] or ""
        issues.append("Literal 'null' found in database.")

    # Check for empty questions or options
    # Pattern for empty text: text: "" or text: ''
    if re.search(r'text:\s*["\']\s*["\']', content):
        issues.append("Empty question text found.")
        
    if re.search(r'options:\s*\[\s*["\']\s*["\']', content):
        issues.append("Empty option found.")

    if not issues:
        print("Post-import check PASSED: No null, undefined, or empty values found in key fields.")
    else:
        for issue in issues:
            print(f"ISSUE: {issue}")

if __name__ == "__main__":
    main()
