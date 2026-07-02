import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find Finance Chapter 2
start_fin = content.find('"fin1":')
if start_fin == -1:
    # try looking for "Finance 1st Paper"
    start_fin = content.find('"Finance 1st Paper"')
    
ch2_fin = content.find('"2":', content.rfind('{', 0, start_fin)) # wait this is fragile
# Just search for Sonali Trading since it's the broken one
sonali_idx = content.find('Sonali Trading')
if sonali_idx != -1:
    # Find the start of the fullCQData array containing Sonali
    bracket_start = content.rfind('fullCQData: [', 0, sonali_idx)
    # find the opening [
    bracket_start = content.find('[', bracket_start)
    
    # count brackets
    bracket_count = 1
    end_bracket = -1
    for i in range(bracket_start + 1, len(content)):
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_bracket = i
                break
    
    if end_bracket != -1:
        new_content = content[:bracket_start] + "[]" + content[end_bracket+1:]
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Wiped broken Finance Chapter 2 array!")
    else:
        print("End bracket not found")
else:
    print("Sonali not found")
