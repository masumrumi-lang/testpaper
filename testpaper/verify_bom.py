import re

def verify_data(data_js_path):
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for the key
    key = "Business Organization and Management"
    if f'"{key}":' in content:
        print(f"PASS: Key '{key}' found in data.js")
    else:
        print(f"FAIL: Key '{key}' NOT found in data.js")
        return

    # Check for a specific management term being bolded
    # Plan, Organize, Lead, Control
    if "<strong>Plan</strong>" in content or "<strong>Organize</strong>" in content:
         print("PASS: Management terms are bolded.")
    else:
         print("FAIL: Management terms NOT bolded (or not found in the injected snippet).")

    # Check for Practice Question mapping
    if "Practice Question" in content:
         print("PASS: 'Practice Question' label found.")
    else:
         print("FAIL: 'Practice Question' label NOT found.")

if __name__ == "__main__":
    verify_data("data.js")
