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
        
        correct_cq18 = {
            "id": "18",
            "stem": "<p>Mr. Nahid and Mr. Asad work in the same organization. The success of the organization depends on the proper discharge of duties and performance of both of them. Mr. Nahid determines the important policies of the organization. He is also involved in formulating plans. On the other hand, Mr. Asad provides necessary directions and advice to the supervisors and foremen for the proper implementation of the plans. With the combined effort and skill of both, the reputation and success of the organization are increasing day by day.</p>",
            "meta": "Dhaka Board · 2023",
            "type": "board",
            "questions": [
                {
                    "label": "a",
                    "text": "(a) Who is the father of scientific management? (1)",
                    "answer": "<p>F.W. Taylor is the father of scientific management.</p>"
                },
                {
                    "label": "b",
                    "text": "(b) Why is management called a social process? Explain. (2)",
                    "answer": "<p>It is a social process because it involves managing, coordinating, and leading people within a community to achieve common welfare.</p>"
                },
                {
                    "label": "c",
                    "text": "(c) At which level of management did Mr. Asad perform his duties as a manager? Explain. (3)",
                    "answer": "<p>Mid-level Manager. He acts as a bridge by instructing lower-level staff (supervisors/foremen) to execute top-level plans.</p>"
                },
                {
                    "label": "d",
                    "text": "(d) \"The mentioned organization is moving forward due to the combination of managerial skills of Mr. Nahid and Mr. Asad\" - do you agree with this? Explain with logic. (4)",
                    "answer": "<p>Yes. 1. Nahid provides Conceptual Skill (Vision). 2. Asad provides Human Skill (Execution). 3. Success requires both policy and practice.</p>"
                }
            ]
        }
        
        # Update CQ "18"
        for i, cq in enumerate(cqs):
            if cq.get("id") == "18":
                cqs[i] = correct_cq18
                break

        new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
        
        # Reconstruct
        new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
        new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
        final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print("Successfully completely reconstructed CQ 18.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
