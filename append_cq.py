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
        
        new_id = str(max([int(cq['id']) for cq in cqs if cq['id'].isdigit()]) + 1)
        
        new_cq = {
            "id": new_id,
            "stem": "<p>A woman named Jamila works as a maid in the house of a professor of the management department. One day, out of curiosity, he asked Jamila where her husband was and what he did. Jamila simply replied that her husband was a manager. At first, Jamila's answer did not seem believable to him. So he wanted to know the matter from Jamila with an explanation. Jamila simply explained that her husband worked in a bakery factory and 6 workers worked under him. Therefore, her husband can certainly be called a manager.</p>",
            "meta": "Dhaka Board · 2023",
            "type": "board",
            "questions": [
                {
                    "label": "a",
                    "text": "(a) Mention the period of the Industrial Revolution. (1)",
                    "answer": "<p>The Industrial Revolution roughly occurred from the mid-18th century (around 1760) to the mid-19th century (around 1840).</p>"
                },
                {
                    "label": "b",
                    "text": "(b) Why are the functions of management interdependent? Explain. (2)",
                    "answer": "<p>The functions of management (planning, organizing, staffing, directing, etc.) are interdependent because they operate sequentially and cohesively as a cycle. For example, organizing cannot happen without a plan, and directing is impossible without organizing the right people. Each function relies on the success of the previous one to achieve the ultimate organizational goal.</p>"
                },
                {
                    "label": "c",
                    "text": "(c) At which level of management is Jamila's husband described in the stem? Explain. (3)",
                    "answer": "<p>Jamila's husband works at the lower level of management. He directly supervises 6 workers on the factory floor, ensuring daily operational tasks are completed. Lower-level managers form the link between the operational workforce and middle management, engaging more in technical labor than conceptual planning.</p>"
                },
                {
                    "label": "d",
                    "text": "(d) Why will Jamila's husband described in the stem be termed as a manager? Give your opinion. (4)",
                    "answer": "<p>Even though he works in a bakery and manages a small team, he performs the core function of management—getting work done through others. He organizes the 6 workers, provides direction, and coordinates their efforts to produce baked goods. Therefore, regardless of the scale, his supervisory role qualifies him as a lower-level operational manager.</p>"
                }
            ]
        }
        
        cqs.append(new_cq)

        new_cq_json_str = json.dumps(cqs, indent=4, ensure_ascii=False)
        
        # Reconstruct
        new_ch_content = ch_content[:array_start] + new_cq_json_str + ch_content[array_end:]
        new_bus2_content = bus2_content[:ch_start] + new_ch_content + bus2_content[ch_end:]
        final_content = db_content[:start_pos] + new_bus2_content + db_content[end_pos:]
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"Successfully appended new CQ as ID {new_id}.")
    else:
        print("fullCQData not found")

if __name__ == "__main__":
    process()
