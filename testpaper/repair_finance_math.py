import json
import re
import os
import sys

def repair_math(text):
    if not text:
        return text
    
    # Replace * with \times in math context
    text = re.sub(r'(\d|\)|\]|\})\s*\*\s*(\d|\(|\[|\{)', r'\1 \\times \2', text)
    
    # Fix 'imes' typo
    text = re.sub(r'(?<!\\)imes', r'\\times', text)
    
    # Remove <code> tags from inside math
    text = re.sub(r'(?<=[\$])(.*?)(?=[\$])', lambda m: m.group(1).replace('<code>', '').replace('</code>', '').replace('<b>', '').replace('</b>', ''), text)
    
    return text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # split by objects to be safer, or just use re.sub on known fields
    # Let's use a simpler approach: process common fields
    
    # Process "text": "..."
    content = process_field(content, "text")
    # Process "options": [...]
    content = process_field(content, "options")
    # Process "explanation": "..."
    content = process_field(content, "explanation")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Repaired {filepath}")

def process_field(content, field_name):
    pattern = rf'("{field_name}":\s*)'
    parts = re.split(pattern, content)
    new_parts = [parts[0]]
    for i in range(1, len(parts), 2):
        prefix = parts[i]
        rest = parts[i+1]
        
        # Determine if it's a string or an array
        if rest.strip().startswith('['):
            # Array processing
            end_bracket_idx = find_matching_bracket(rest, '[', ']')
            array_val = rest[:end_bracket_idx+1]
            remainder = rest[end_bracket_idx+1:]
            
            repaired_array = repair_math(array_val)
            # Wrap $ in $$
            repaired_array = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', r'$$\1$$', repaired_array)
            new_parts.append(prefix + repaired_array + remainder)
        else:
            # String processing
            end_quote_idx = rest.find('"')
            if end_quote_idx == -1: # should not happen
                new_parts.append(prefix + rest)
                continue
            
            val = rest[:end_quote_idx]
            remainder = rest[end_quote_idx:]
            
            repaired = repair_math(val)
            repaired = re.sub(r'(?<!\$)\$([^\$]+)\$(?!\$)', r'$$\1$$', repaired)
            new_parts.append(prefix + repaired + remainder)
            
    return "".join(new_parts)

def find_matching_bracket(text, open_b, close_b):
    count = 0
    for i in range(len(text)):
        if text[i] == open_b:
            count += 1
        elif text[i] == close_b:
            count -= 1
            if count == 0:
                return i
    return -1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_file(sys.argv[1])
    else:
        print("Usage: python repair_finance_math.py <filepath>")
