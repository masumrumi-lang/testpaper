import json
import re

def process():
    with open('data.js', 'r', encoding='utf-8') as f:
        db_content = f.read()

    # 1. Isolate the "bus2" block
    bus2_match = re.search(r'("bus2":\s*\{)', db_content)
    if not bus2_match: return
    start_pos = bus2_match.start()

    bracket_count = 0
    end_pos = -1
    for i in range(start_pos, len(db_content)):
        if db_content[i] == '{':
            bracket_count += 1
        elif db_content[i] == '}':
            bracket_count -= 1
            if bracket_count == 0:
                end_pos = i + 1
                break

    bus2_content = db_content[start_pos:end_pos]

    # 2. Isolate the "1" block inside "bus2"
    ch_match = re.search(r'("1":\s*\{)', bus2_content)
    if not ch_match: return
    ch_start = ch_match.start()

    bracket_count = 0
    ch_end = -1
    for i in range(ch_start, len(bus2_content)):
        if bus2_content[i] == '{':
            bracket_count += 1
        elif bus2_content[i] == '}':
            bracket_count -= 1
            if bracket_count == 0:
                ch_end = i + 1
                break

    ch_content = bus2_content[ch_start:ch_end]

    # 3. Find fullCQData array
    array_start = ch_content.find('"fullCQData":')
    if array_start != -1:
        array_start = ch_content.find('[', array_start)
        array_bracket_count = 0
        array_end = -1
        for i in range(array_start, len(ch_content)):
            if ch_content[i] == '[':
                array_bracket_count += 1
            elif ch_content[i] == ']':
                array_bracket_count -= 1
                if array_bracket_count == 0:
                    array_end = i + 1
                    break
        
        cq_json_str = ch_content[array_start:array_end]
        cqs = json.loads(cq_json_str)
        
        questions_text = {
            "a": '(a) "Management is universal" - whose quote is this? (1)',
            "b": "(b) Why is 'unity is strength' (esprit de corps) important for achieving goals? (2)",
            "c": "(c) Explain the function of 'A' in the figure on the basis of management levels. (3)",
            "d": '(d) "There is no fundamental difference among the skills of \'A\', \'B\', and \'C\' in the figure" - give your opinion with logic. (4)'
        }
        
        # Update CQ "17"
        for cq in cqs:
            if cq.get("id") == "17":
                for q in cq.get("questions", []):
                    label = q.get("label")
                    if label in questions_text:
                        q["text"] = questions_text[label]

        new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
        
        # Reconstruct
        new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
        new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
        final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print("Successfully updated missing questions for CQ 17.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
