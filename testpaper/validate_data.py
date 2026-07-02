import json

def validate_injection():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Chapter 2 block
    # It should look like "2": { ... }
    # We find it between Chapter 1 end and Chapter 2 end marker
    start_key = '"2": {'
    end_marker = '/* AGRI1_CHAPTER2_CQ_END */'
    
    start_pos = content.find(start_key)
    end_pos = content.find(end_marker)
    
    if start_pos == -1 or end_pos == -1:
        print(f"Markers not found: start_pos={start_pos}, end_pos={end_pos}")
        return

    # Extract the object string
    # We need to find the closing brace that matches the start_key's brace
    # But for a quick check, we'll just take everything up to the marker and clean it.
    
    block_str = content[start_pos:end_pos].strip()
    if block_str.endswith(','):
        block_str = block_str[:-1]
        
    # Wrap in {} to make a valid JSON object
    test_json = "{" + block_str + "}"
    
    try:
        # data.js uses double quotes for keys in my injection, so json.loads should work
        # If it used single quotes or no quotes, it would fail, but I used json.dumps
        data = json.loads(test_json)
        ch2_data = data["2"]
        questions = ch2_data["fullCQData"]
        
        print(f"✓ JSON Validation: Passed")
        print(f"✓ Question Count: {len(questions)} (Target: 26)")
        
        # Schema validation for first and last question
        for idx in [0, 25]:
            q = questions[idx]
            required = ["chapter", "question_id", "stem", "knowledge_comprehension", "full_cq", "images"]
            missing = [f for f in required if f not in q]
            if missing:
                print(f"✗ Schema Validation FAILED for Q{idx+1}: Missing {missing}")
            else:
                print(f"✓ Schema Validation: Passed for Q{idx+1}")
                
    except Exception as e:
        print(f"✗ JSON Validation FAILED: {e}")
        # Show where it failed
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    validate_injection()
