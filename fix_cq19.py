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
        
        correct_cq19 = {
            "id": "19",
            "stem": "<p>Mr. Maruf worked as a supervisor in a garment factory for a long time. He gained a lot of expertise in this field. Since there was no such factory in his residential area, he considered it a profitable business. He set up a garment factory with his own savings and some loan from the bank. He showed foresight in selecting and implementing the project. Besides, he adopted the principle of economy in this regard. As a result, his organization became profitable within a short time.</p>",
            "meta": "Dhaka Board · 2023",
            "type": "board",
            "questions": [
                {
                    "label": "a",
                    "text": "(a) What is unity of command? (1)",
                    "answer": "<p>It means an employee should receive orders from only one superior to avoid confusion and conflict.</p>"
                },
                {
                    "label": "b",
                    "text": "(b) Why are principles of management necessary? Explain. (2)",
                    "answer": "<p>Principles provide a standardized guide for managers to make decisions, solve problems, and ensure consistency in organizational behavior.</p>"
                },
                {
                    "label": "c",
                    "text": "(c) Which function of management is present in Mr. Maruf's activities? Explain. (3)",
                    "answer": "<p>Planning. His foresight in \"project selection\" and deciding the nature of the business beforehand is the core of planning.</p>"
                },
                {
                    "label": "d",
                    "text": "(d) Evaluate the logic of Mr. Maruf's decision described in the stem. (4)",
                    "answer": "<p>Logical. 1. He used his prior technical experience as a supervisor. 2. He identified a market gap in his area. 3. He balanced risk with loans and savings.</p>"
                }
            ]
        }
        
        # Update CQ "19"
        for i, cq in enumerate(cqs):
            if cq.get("id") == "19":
                cqs[i] = correct_cq19
                break

        new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
        
        # Reconstruct
        new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
        new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
        final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print("Successfully completely reconstructed CQ 19.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
