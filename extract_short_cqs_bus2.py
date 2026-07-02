import re
import sys

def safe_process():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    for subj in ['"bus2":']:
        subj_idx = content.find(subj)
        if subj_idx == -1: continue

        bracket_count = 0
        subj_start = content.find('{', subj_idx)
        subj_end = -1
        for i in range(subj_start, len(content)):
            if content[i] == '{': bracket_count += 1
            elif content[i] == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    subj_end = i + 1
                    break
                    
        subj_block = content[subj_start:subj_end]
        
        new_subj_block = ""
        subj_last_idx = 0
        
        for ch_match in re.finditer(r'("\d+":\s*\{)', subj_block):
            ch_start = ch_match.start()
            new_subj_block += subj_block[subj_last_idx:ch_start]
            
            ch_bracket_count = 0
            ch_end = -1
            for i in range(ch_start, len(subj_block)):
                if subj_block[i] == '{': ch_bracket_count += 1
                elif subj_block[i] == '}':
                    ch_bracket_count -= 1
                    if ch_bracket_count == 0:
                        ch_end = i + 1
                        break
            
            ch_block = subj_block[ch_start:ch_end]
            
            full_match = re.search(r'fullCQData"?\s*:\s*\[', ch_block)
            if not full_match:
                new_subj_block += ch_block
                subj_last_idx = ch_end
                continue
                
            full_start = full_match.end() - 1
            arr_count = 0
            full_end = -1
            for i in range(full_start, len(ch_block)):
                if ch_block[i] == '[': arr_count += 1
                elif ch_block[i] == ']':
                    arr_count -= 1
                    if arr_count == 0:
                        full_end = i + 1
                        break
                        
            full_cq_str = ch_block[full_start:full_end]
            
            short_cqs = []
            short_id = 1
            
            cq_start = -1
            cq_depth = 0
            for i in range(len(full_cq_str)):
                if full_cq_str[i] == '{':
                    cq_depth += 1
                    if cq_depth == 1: cq_start = i
                elif full_cq_str[i] == '}':
                    cq_depth -= 1
                    if cq_depth == 0 and cq_start != -1:
                        cq_obj_str = full_cq_str[cq_start:i+1]
                        
                        meta_match = re.search(r'"meta"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"', cq_obj_str)
                        type_match = re.search(r'"type"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"', cq_obj_str)
                        
                        meta = meta_match.group(1) if meta_match else ""
                        cq_type = type_match.group(1) if type_match else "college"
                        
                        q_arr_match = re.search(r'"questions"\s*:\s*\[', cq_obj_str)
                        if q_arr_match:
                            q_start = q_arr_match.end() - 1
                            q_count = 0
                            q_end = -1
                            for j in range(q_start, len(cq_obj_str)):
                                if cq_obj_str[j] == '[': q_count += 1
                                elif cq_obj_str[j] == ']':
                                    q_count -= 1
                                    if q_count == 0:
                                        q_end = j + 1
                                        break
                            q_arr_str = cq_obj_str[q_start:q_end]
                            
                            label_matches = re.finditer(r'\{\s*"label"\s*:\s*"(a|b)"\s*,\s*"text"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*,\s*"answer"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*\}', q_arr_str, re.DOTALL)
                            for lm in label_matches:
                                label, text, answer = lm.groups()
                                short_cqs.append(f'''{{
            "id": {short_id},
            "text": "{text}",
            "meta": "{meta}",
            "type": "{cq_type}",
            "answer": "{answer}"
        }}''')
                                short_id += 1
                        
            short_match = re.search(r'shortCQData"?\s*:\s*\[', ch_block)
            if short_match:
                s_start = short_match.end() - 1
                s_count = 0
                s_end = -1
                for i in range(s_start, len(ch_block)):
                    if ch_block[i] == '[': s_count += 1
                    elif ch_block[i] == ']':
                        s_count -= 1
                        if s_count == 0:
                            s_end = i + 1
                            break
                
                short_arr_str = "[\n        " + ",\n        ".join(short_cqs) + "\n    ]"
                new_ch_block = ch_block[:s_start] + short_arr_str + ch_block[s_end:]
            else:
                short_arr_str = "\"shortCQData\": [\n        " + ",\n        ".join(short_cqs) + "\n    ],\n    "
                new_ch_block = ch_block[:full_match.start()] + short_arr_str + ch_block[full_match.start():]
                
            new_subj_block += new_ch_block
            subj_last_idx = ch_end
            
        new_subj_block += subj_block[subj_last_idx:]
        content = content[:subj_start] + new_subj_block + content[subj_end:]

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Extraction successful.")

if __name__ == '__main__':
    safe_process()
