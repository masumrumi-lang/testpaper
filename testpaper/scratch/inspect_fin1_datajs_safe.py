import re
import json

try:
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'["\']fin1["\']:\s*\{', content)
    if not match:
        result = "fin1 block not found in data.js"
    else:
        start = match.start()
        # Parse braces to find end of fin1 block
        brace_count = 0
        end = -1
        for i in range(start, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break

        fin1_block = content[start:end]
        # Let's extract the keys and print what each chapter has (mcqData length, shortCQData length, fullCQData length)
        # We can find each chapter block "1": { ... }, "2": { ... }
        ch_matches = list(re.finditer(r'["\'](\d+)["\']:\s*\{', fin1_block))
        
        result_lines = []
        result_lines.append(f"Found {len(ch_matches)} chapters in fin1 block:")
        for idx, m in enumerate(ch_matches):
            ch_num = m.group(1)
            # Find the end of this chapter object
            ch_start = m.start()
            # find brace count from this point
            ch_brace_count = 0
            ch_end = -1
            for j in range(ch_start, len(fin1_block)):
                if fin1_block[j] == '{':
                    ch_brace_count += 1
                elif fin1_block[j] == '}':
                    ch_brace_count -= 1
                    if ch_brace_count == 0:
                        ch_end = j + 1
                        break
            
            ch_obj_str = fin1_block[ch_start:ch_end]
            # Let's parse it using JSON if possible, otherwise regex
            # Let's clean the keys to make it valid JSON if needed, or just search
            # Since it might have unquoted keys (e.g. subjectName: ...), let's use regex
            mcq_match = re.search(r'mcqData:\s*\[(.*?)\],?\s*(?:shortCQData|fullCQData|\})', ch_obj_str, re.DOTALL)
            short_match = re.search(r'shortCQData:\s*\[(.*?)\],?\s*(?:fullCQData|mcqData|\})', ch_obj_str, re.DOTALL)
            full_match = re.search(r'fullCQData:\s*\[(.*?)\],?\s*(?:shortCQData|mcqData|\})', ch_obj_str, re.DOTALL)
            
            mcq_len = "Present" if mcq_match and mcq_match.group(1).strip() else "Empty"
            short_len = "Present" if short_match and short_match.group(1).strip() else "Empty"
            full_len = "Present" if full_match and full_match.group(1).strip() else "Empty"
            
            result_lines.append(f"Chapter {ch_num}: mcqData={mcq_len}, shortCQData={short_len}, fullCQData={full_len}")
            # Snippet of first few chars of chapter:
            result_lines.append(f"  Snippet: {ch_obj_str[:150]}...")
            
        result = "\n".join(result_lines)
except Exception as e:
    result = f"Error: {e}"

with open('scratch/inspect_fin1_summary.txt', 'w', encoding='utf-8') as f:
    f.write(result)
print("Finished inspection.")
