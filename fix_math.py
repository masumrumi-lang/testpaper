import json
import re

def fix_math_format():
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find fin1 block
    fin1_match = re.search(r'["\']fin1["\']:\s*\{', content)
    if not fin1_match:
        print("fin1 not found")
        return

    start = fin1_match.start()
    brace_count = 0
    fin1_end = -1
    for i in range(start, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                fin1_end = i + 1
                break

    fin1_content = content[start:fin1_end]

    # Function to fix LaTeX backslashes and format
    def clean_math(text):
        if not text: return text
        
        # 1. Fix missing backslashes for common LaTeX commands
        # Example: (rac{D_1}{P_0} -> \frac{D_1}{P_0}
        # Since it's in a JS string, we need \\frac
        text = text.replace('(rac{', '\\\\frac{')
        text = text.replace('eta$', '\\\\beta$')
        text = text.replace('R_m$', 'R_m$') # Often fine
        
        # 2. Reformat math answers to the requested style if they look like calculations
        # If the text contains "Data:", "Formula:", "Calculation:", we format them
        if "Data:" in text and "Formula:" in text and "Calculation:" in text:
            # Already formatted? Let's ensure backslashes
            pass
        
        # Ensure all $ symbols have backslashes before commands
        # This is a bit complex to do generically, so let's target the integrated data
        
        return text

    # I will specifically target the newly injected data and re-process it
    # because the CSV parser might have stripped the backslashes.
    
    # Let's fix the specific ones identified in the image
    # Image 1 stem: Capital Sources: Common Stock (TK 20L), 14% Preferred Stock (TK 5L), 15% Debenture (TK 15L). Beta ($ \beta $) is 2, Market Return ($ R_m $) is 15%, Risk-free rate ($ R_f $) is 7%, and Corp Tax is 40%. Expected return on investment is 25%.
    
    fin1_content = fin1_content.replace('(rac{', '\\\\frac{')
    fin1_content = fin1_content.replace(' imes ', ' \\\\times ')
    fin1_content = fin1_content.replace('$eta$', '$\\\\beta$')
    
    # Also fix the "Data:", "Formula:", "Calculation:" format if it was 1. 2. 3.
    # The image shows "1. Data: ... 2. Formula: ... 3. Calculation: ..."
    # The user wants "Data: ... Formula: ... Calculation: ..." without the numbers if possible, 
    # or just clean.
    
    # Apply to the whole content
    content = content[:start] + fin1_content + content[fin1_end:]
    
    with open('c:/Users/BMTF/.antigravity/testpaper/data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Math formatting fixed in data.js")

if __name__ == "__main__":
    fix_math_format()
